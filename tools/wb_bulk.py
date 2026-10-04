#!/usr/bin/env python3
"""
wb_bulk.py - fast, resumable, concurrent Wayback Machine crawler.

Lists every archived URL under one or more java2s path prefixes (CDX API),
then downloads snapshots with N parallel workers, extracting pages with the
same extractor as wayback_fetch.py so output stays uniform.

Also records the parent/child link map for index pages into
tools/tree_map.json so the site builder can recreate the java2s tutorial
tree (chapter -> sub-topic -> article).

Usage:
    python3 tools/wb_bulk.py --prefix /Tutorial/Java/ --limit 0
    python3 tools/wb_bulk.py --prefix /ref/java/ --workers 8 --min-delay 0.05
    python3 tools/wb_bulk.py --prefix /Tutorial/Java/ --urls-only
"""
from __future__ import annotations

import argparse
import csv
import gzip
import importlib.util
import json
import random
import re
import signal
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "content" / "imported"
MANIFEST = ROOT / "tools" / "bulk_manifest.csv"
TREEMAP = ROOT / "tools" / "tree_map.json"
DATA_DIR = ROOT / "tools" / "data"

_spec = importlib.util.spec_from_file_location("wf", ROOT / "tools" / "wayback_fetch.py")
wf = importlib.util.module_from_spec(_spec)
sys.modules["wf"] = wf
_spec.loader.exec_module(wf)

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36 JavaSchoolMirror/1.0 (+github.com/shafakhat/JavaSchool)")
CDX = "http://web.archive.org/cdx/search/cdx"

log_lock = threading.Lock()


def log(*a):
    with log_lock:
        print(*a, flush=True)


def norm_path(url: str) -> str:
    p = urllib.parse.urlsplit(url).path
    return re.sub(r"\.html?$", "", p.lower()).rstrip("/")


# --------------------------------------------------------------------------- #
# CDX listing
# --------------------------------------------------------------------------- #

def cdx_list(prefix: str, resume_file: Path) -> list[tuple[str, str]]:
    if resume_file.exists():
        rows = [tuple(l.split(" ", 1)) for l in resume_file.read_text().splitlines() if l.strip()]
        log(f"[cdx] {prefix}: {len(rows)} urls (cached)")
        return rows
    rows: list[tuple[str, str]] = []
    page = 0
    while page < 40:
        params = urllib.parse.urlencode({
            "url": "www.java2s.com" + prefix + "*",
            "fl": "original,timestamp",
            "collapse": "urlkey",
            "limit": "40000",
            "page": str(page),
        })
        url = f"{CDX}?{params}"
        body = None
        for attempt in range(4):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=150) as r:
                    body = r.read().decode("utf-8", "replace")
                break
            except Exception as e:  # noqa: BLE001
                log(f"[cdx] {prefix} page {page} attempt {attempt}: {type(e).__name__}")
                time.sleep(8 * (attempt + 1))
        if not body or body.lstrip().startswith("<"):
            break
        lines = [l for l in body.splitlines() if l.strip()]
        if not lines:
            break
        for l in lines:
            parts = l.split()
            if len(parts) >= 2:
                rows.append((parts[0], parts[1]))
        log(f"[cdx] {prefix}: {len(rows)} urls so far (page {page})")
        if len(lines) < 40000:
            break
        page += 1
    resume_file.write_text("\n".join(f"{u} {t}" for u, t in rows))
    return rows


# --------------------------------------------------------------------------- #
# Fetch / extract
# --------------------------------------------------------------------------- #

def fetch_snapshot(url: str, ts: str, timeout: int = 40) -> str | None:
    fetch_url = f"https://web.archive.org/web/{ts}id_/{url}"
    req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
    except urllib.error.HTTPError as e:
        if e.code in (404, 410):
            return None
        raise
    if data[:2] == b"\x1f\x8b":
        try:
            data = gzip.decompress(data)
        except Exception:  # noqa: BLE001
            pass
    for enc in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", "replace")


INDEX_PAGE = re.compile(r"/(\d{4}__[^/]+)\.html?$|/Catalog[^/]*\.html?$", re.I)
LINK_RE = re.compile(r'<a\s[^>]*href="([^"]+\.(?:htm|html))"', re.I)


def article_links(raw: str, base: str) -> list[str]:
    out = []
    for m in LINK_RE.finditer(raw):
        u = urllib.parse.urljoin(base, m.group(1))
        if "java2s.com" in u and "/Tutorial/Java/" in u:
            out.append(u.split("?")[0])
    return out


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

_treemap_lock = threading.Lock()
_treemap: dict[str, list[str]] = {}
_manifest_lock = threading.Lock()
_manifest_fh = None
_counts = {"import": 0, "skip": 0, "fail": 0, "thin": 0}
_counts_lock = threading.Lock()


def bump(key: str, n: int = 1):
    with _counts_lock:
        _counts[key] += n


def manifest_append(slug: str, url: str):
    global _manifest_fh
    with _manifest_lock:
        if _manifest_fh is None:
            _manifest_fh = MANIFEST.open("a", newline="", encoding="utf-8")
        csv.writer(_manifest_fh).writerow([slug, url])
        _manifest_fh.flush()


def flush_treemap():
    with _treemap_lock:
        if not _treemap:
            return
        merged = {}
        if TREEMAP.exists():
            try:
                merged = json.loads(TREEMAP.read_text())
            except Exception:  # noqa: BLE001
                merged = {}
        for k, v in _treemap.items():
            cur = merged.setdefault(k, [])
            for u in v:
                if u not in cur:
                    cur.append(u)
        TREEMAP.write_text(json.dumps(merged, indent=1))


def load_done_paths() -> set[str]:
    done = set()
    for name in ("bulk_manifest.csv", "wayback_manifest.csv", "live_manifest.csv"):
        p = ROOT / "tools" / name
        if not p.exists():
            continue
        with p.open(newline="", encoding="utf-8") as f:
            for row in csv.reader(f):
                if len(row) >= 2:
                    done.add(norm_path(row[1]))
    return done


def worker(item: tuple[str, str], done: set[str], min_delay: float, order_base: int,
           counter: list[int]) -> None:
    url, ts = item
    if norm_path(url) in done:
        bump("skip")
        return
    time.sleep(min_delay * (0.4 + random.random()))
    raw = None
    for attempt in range(4):
        try:
            raw = fetch_snapshot(url, ts)
            break
        except urllib.error.HTTPError as e:
            if e.code in (429, 503, 502, 500):
                time.sleep(10 * (attempt + 1) + random.random() * 5)
                continue
            raw = None
            break
        except Exception:  # noqa: BLE001
            time.sleep(4 * (attempt + 1))
            continue
    if raw is None:
        manifest_append("-", url)
        done.add(norm_path(url))
        bump("fail")
        return
    try:
        title, desc, md = wf.extract(raw, url)
    except Exception:  # noqa: BLE001
        title, desc, md = "", "", ""
    if INDEX_PAGE.search(urllib.parse.urlsplit(url).path):
        links = article_links(raw, url)
        if links:
            with _treemap_lock:
                _treemap[url] = links
            if len(_treemap) % 25 == 0:
                flush_treemap()
    stripped = re.sub(r"[\s`#*>|-]+", "", md)
    if len(stripped) < 60:
        manifest_append("(thin)", url)
        done.add(norm_path(url))
        bump("thin")
        return
    slug = wf.slug_from_url(url)
    title = wf.clean_title(title, url)
    path = OUT_DIR / f"{slug}.md"
    n = 2
    while path.exists():
        path = OUT_DIR / f"{slug}-{n}.md"
        n += 1
    if path.exists():
        bump("skip")
        return
    order = order_base + counter[0]
    counter[0] += 1
    nav = title if len(title) <= 28 else title[:26] + "..."
    fm = ["---", f"title: {wf.yaml_escape(title)}", f"nav: {wf.yaml_escape(nav)}",
          f"description: {wf.yaml_escape(desc or ('Imported from java2s.com: ' + title))}",
          "section: Imported", f"order: {order}", f"source: {url}", "---", ""]
    body = re.sub(r"^# ", "## ", md, flags=re.M)
    path.write_text("\n".join(fm) + body, encoding="utf-8")
    manifest_append(slug, url)
    done.add(norm_path(url))
    bump("import")
    with _counts_lock:
        total = sum(_counts.values())
    if total % 50 < 4:
        log(f"[bulk] import={_counts['import']} skip={_counts['skip']} "
            f"fail={_counts['fail']} thin={_counts['thin']}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prefix", action="append", required=True)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--min-delay", type=float, default=0.06)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--urls-only", action="store_true")
    ap.add_argument("--urls-file", action="append", default=[],
                    help="pre-listed url files ('url ts' per line) - skips CDX")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    done = load_done_paths()
    log(f"[init] already done: {len(done)} urls")

    items: list[tuple[str, str]] = []
    seen = set()
    if args.urls_file:
        for uf in args.urls_file:
            for line in Path(uf).read_text(encoding="utf-8", errors="replace").splitlines():
                parts = line.split()
                if len(parts) < 2:
                    continue
                url, ts = parts[0], parts[1]
                if url in seen:
                    continue
                seen.add(url)
                items.append((url, ts))
    else:
        for prefix in args.prefix:
            key = re.sub(r"\W+", "_", prefix.strip("/")) or "root"
            for url, ts in cdx_list(prefix, DATA_DIR / f"urls_{key}.txt"):
                if url in seen:
                    continue
                seen.add(url)
                items.append((url, ts))
    log(f"[init] {len(items)} candidate urls")
    if args.urls_only:
        return 0

    pending = [it for it in items if norm_path(it[0]) not in done]
    if args.limit:
        pending = pending[: args.limit]
    log(f"[init] {len(pending)} to fetch with {args.workers} workers")

    stop = threading.Event()

    def on_signal(signum, frame):  # noqa: ARG001
        log("[sig] stopping ...")
        stop.set()

    signal.signal(signal.SIGTERM, on_signal)
    signal.signal(signal.SIGINT, on_signal)

    counter = [0]
    t0 = time.time()
    try:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futs = []
            for it in pending:
                if stop.is_set():
                    break
                futs.append(pool.submit(worker, it, done, args.min_delay, 20000, counter))
                if len(futs) >= args.workers * 8:
                    for f in futs:
                        f.result()
                    futs = []
                    el = time.time() - t0
                    log(f"[bulk] imported={_counts['import']} skip={_counts['skip']} "
                        f"fail={_counts['fail']} thin={_counts['thin']} "
                        f"{_counts['import']/el:.2f}/s" if el else "")
            for f in futs:
                f.result()
    finally:
        flush_treemap()
    log(f"[done] {_counts} in {time.time()-t0:.0f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
