#!/usr/bin/env python3
"""
live_fetch.py - crawl the LIVE java2s.com site into content/imported/.

Resumable, concurrent, allow-list based. Re-uses the HTML extraction code from
wayback_fetch.py so imported pages keep the exact same format.

Usage:
    python3 tools/live_fetch.py --prefix /Tutorials/Java --prefix /Tutorial/SCJP
    python3 tools/live_fetch.py --sitemap /tmp/sitemap_locs.txt --prefix /Tutorials/Java
    python3 tools/live_fetch.py --prefix /Tutorial/Java --limit 500

The manifest tools/live_manifest.csv records every URL attempted so re-runs
pick up exactly where they stopped. URLs already imported from the Wayback
archive (tools/wayback_manifest.csv) are skipped automatically.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import random
import re
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
MANIFEST = ROOT / "tools" / "live_manifest.csv"
WAYBACK_MANIFEST = ROOT / "tools" / "wayback_manifest.csv"

# wireframe: reuse the archive importer's extractor so formats match exactly
_spec = importlib.util.spec_from_file_location("wf", ROOT / "tools" / "wayback_fetch.py")
wf = importlib.util.module_from_spec(_spec)
sys.modules["wf"] = wf
_spec.loader.exec_module(wf)

BASE = "https://www.java2s.com"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36 JavaSchoolMirror/1.0 (+github.com/shafakhat/JavaSchool)")

SKIP_EXT = re.compile(r"\.(jpe?g|png|gif|css|js|ico|svg|zip|gz|jar|pdf|xml|txt|mp3|mp4|woff2?)$", re.I)

_print_lock = threading.Lock()


def log(*a):
    with _print_lock:
        print(*a, flush=True)


def norm_path(url: str) -> str:
    p = urllib.parse.urlsplit(url).path
    p = urllib.parse.unquote(p).lower()
    p = re.sub(r"\.html?$", "", p)
    p = p.rstrip("/")
    return p


def canon(url: str) -> str | None:
    """Absolute, cleaned java2s URL or None."""
    url = url.strip()
    if not url or url.startswith(("mailto:", "javascript:", "#", "data:")):
        return None
    u = urllib.parse.urljoin("https://www.java2s.com/", url)
    s = urllib.parse.urlsplit(u)
    if "java2s.com" not in s.netloc:
        return None
    path = s.path
    if SKIP_EXT.search(path):
        return None
    return "https://www.java2s.com" + path


def fetch(url: str, retries: int = 2, timeout: int = 25) -> tuple[str, str] | None:
    """Return (final_url, html) or None."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
                enc = r.headers.get_content_charset() or "utf-8"
                return r.geturl(), data.decode(enc, "replace")
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                return None
            if attempt >= retries:
                return None
            time.sleep(1.5 * (attempt + 1) + random.random())
        except Exception:
            if attempt >= retries:
                return None
            time.sleep(1.5 * (attempt + 1) + random.random())
    return None


def extract_links(html: str, base_url: str) -> list[str]:
    links = []
    for m in re.finditer(r'<a\s[^>]*href="([^"]+)"', html, re.I):
        u = canon(urllib.parse.urljoin(base_url, m.group(1)))
        if u:
            links.append(u)
    return links


def load_manifest() -> set[str]:
    done = set()
    if MANIFEST.exists():
        with MANIFEST.open(newline="", encoding="utf-8") as f:
            for row in csv.reader(f):
                if len(row) >= 2:
                    done.add(norm_path(row[1]))
    return done


def load_wayback_paths() -> set[str]:
    paths = set()
    if WAYBACK_MANIFEST.exists():
        with WAYBACK_MANIFEST.open(newline="", encoding="utf-8") as f:
            for row in csv.reader(f):
                if len(row) >= 2 and row[0] not in ("-", "(thin)"):
                    paths.add(norm_path(row[1]))
    return paths


_manifest_lock = threading.Lock()
_manifest_file = None


def append_manifest(slug: str, url: str) -> None:
    global _manifest_file
    with _manifest_lock:
        if _manifest_file is None:
            _manifest_file = MANIFEST.open("a", newline="", encoding="utf-8")
        csv.writer(_manifest_file).writerow([slug, url])
        _manifest_file.flush()


def write_page(slug: str, title: str, desc: str, body: str, url: str, order: int) -> Path:
    nav = title if len(title) <= 28 else title[:26] + "..."
    fm = [
        "---",
        f"title: {wf.yaml_escape(title)}",
        f"nav: {wf.yaml_escape(nav)}",
        f"description: {wf.yaml_escape(desc or ('Imported from java2s.com: ' + title))}",
        "section: Imported - java2s Archive",
        f"order: {order}",
        f"source: {url}",
        "---",
        "",
    ]
    body = re.sub(r"^# ", "## ", body, flags=re.M)
    path = OUT_DIR / f"{slug}.md"
    n = 2
    while path.exists():
        path = OUT_DIR / f"{slug}-{n}.md"
        n += 1
    path.write_text("\n".join(fm) + body, encoding="utf-8")
    return path


def crawl(seed_urls: list[str], prefixes: list[str], limit: int, workers: int,
          delay: float, order_start: int) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    done = load_manifest()
    wb_paths = load_wayback_paths()
    log(f"[init] manifest has {len(done)} urls; wayback paths: {len(wb_paths)}")

    def allowed(u: str) -> bool:
        p = urllib.parse.urlsplit(u).path
        for pre in prefixes:
            if p.startswith(pre) and (len(p) == len(pre) or p[len(pre)] == "/"):
                return True
        return False

    queue: list[str] = []
    seen: set[str] = set()
    for u in seed_urls:
        u = canon(u)
        if u and allowed(u) and u not in seen:
            seen.add(u)
            queue.append(u)
    log(f"[init] {len(queue)} seed urls")

    imported = skipped = failed = 0
    order = order_start
    t0 = time.time()

    def work(url: str):
        time.sleep(delay * (0.5 + random.random()))
        got = fetch(url)
        if got is None:
            return url, None, None, []
        final_url, raw = got
        try:
            title, desc, md = wf.extract(raw, final_url)
        except Exception:
            return url, None, None, []
        links = extract_links(raw, final_url)
        return url, final_url, (title, desc, md), links

    with ThreadPoolExecutor(max_workers=workers) as pool:
        while queue and imported < limit:
            batch = queue[: workers * 6]
            del queue[: len(batch)]
            for url, final_url, parsed, links in pool.map(work, batch):
                for l in links:
                    if allowed(l) and l not in seen and norm_path(l) not in done:
                        seen.add(l)
                        queue.append(l)
                np_ = norm_path(final_url or url)
                if np_ in done:
                    skipped += 1
                    continue
                if parsed is None:
                    append_manifest("-", url)
                    done.add(np_)
                    failed += 1
                    continue
                title, desc, md = parsed
                md_stripped = re.sub(r"[\s`#*>|-]+", "", md)
                if len(md_stripped) < 60:
                    append_manifest("(thin)", final_url or url)
                    done.add(np_)
                    skipped += 1
                    continue
                if np_ in wb_paths:
                    append_manifest("(in-archive)", final_url or url)
                    done.add(np_)
                    skipped += 1
                    continue
                slug = wf.slug_from_url(final_url or url)
                title = wf.clean_title(title, final_url or url)
                write_page(slug, title, desc, md, final_url or url, order)
                append_manifest(slug, final_url or url)
                done.add(np_)
                order += 1
                imported += 1
            el = time.time() - t0
            rate = imported / el if el else 0
            log(f"[crawl] imported={imported} skipped={skipped} failed={failed} "
                f"queue={len(queue)} seen={len(seen)} {rate:.1f}/s")
    log(f"[done] imported={imported} skipped={skipped} failed={failed} "
        f"in {time.time()-t0:.0f}s")
    # emit next seeds hint: leftover queue saved for next run
    if queue:
        left = ROOT / "tools" / "live_queue.txt"
        left.write_text("\n".join(queue), encoding="utf-8")
        log(f"[done] {len(queue)} urls left in queue -> tools/live_queue.txt")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prefix", action="append", default=[],
                    help="path prefix to stay within (repeatable)")
    ap.add_argument("--sitemap", default=None,
                    help="file with one URL per line (e.g. dumped sitemap <loc> list)")
    ap.add_argument("--seed", action="append", default=[],
                    help="extra seed URL (repeatable)")
    ap.add_argument("--limit", type=int, default=0, help="max imports this run (0=all)")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--delay", type=float, default=0.08)
    ap.add_argument("--order-start", type=int, default=50000)
    args = ap.parse_args()

    if not args.prefix:
        print("need at least one --prefix", file=sys.stderr)
        return 2

    seeds: list[str] = []
    qf = ROOT / "tools" / "live_queue.txt"
    if qf.exists():
        seeds += [l.strip() for l in qf.read_text().splitlines() if l.strip()]
        qf.unlink()
    if args.sitemap:
        for line in Path(args.sitemap).read_text(encoding="utf-8").splitlines():
            if any(args.prefix[0] or True for _ in [0]):
                seeds.append(line.strip())
    seeds += args.seed

    def allowed_seed(u: str) -> bool:
        p = urllib.parse.urlsplit(u).path
        return any(p.startswith(pre) for pre in args.prefix)

    seeds = [u for u in (canon(s) for s in seeds) if u and allowed_seed(u)]
    if not seeds:
        seeds = ["https://www.java2s.com" + p + ("/index.html" if not p.endswith(".html") else "")
                 for p in args.prefix]

    crawl(seeds, args.prefix, args.limit, args.workers, args.delay, args.order_start)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
