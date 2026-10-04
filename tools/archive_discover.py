#!/usr/bin/env python3
"""
archive_discover.py - walk every java2s sub-topic LISTING page in the Wayback
Machine (snapshots 2014-2020) and harvest the real article links.

Why: the numbers in round brackets on the catalog page are unreliable (the 2026
snapshot regenerated them), so the only trustworthy inventory is the listing
pages themselves. Each listing page links its own articles.

Output (resumable):
  tools/data/subtopic_articles.jsonl  - one JSON object per sub-topic:
    {"key","chapter","num","title","snap","articles":["/Tutorial/Java/.../X.htm", ...]}
  tools/data/article_inventory.txt    - unique article URLs (for the crawler)

Usage:
  python3 tools/archive_discover.py --workers 6 --limit 0
"""
from __future__ import annotations

import argparse
import json
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
DATA = ROOT / "tools" / "data"
OUT = DATA / "subtopic_articles.jsonl"
INV = DATA / "article_inventory.txt"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36 JavaSchoolMirror/1.0")

YEARS = [2016, 2018, 2020, 2014, 2017, 2019]
_lock = threading.Lock()


def log(*a):
    with _lock:
        print(*a, flush=True)


def fetch(url: str, timeout: int = 30, tries: int = 2) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for i in range(tries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except Exception:
            if i >= tries:
                return None
            time.sleep(2 * (i + 1) + random.random())
    return None


def snap_html(path: str, year: int) -> tuple[str, str] | None:
    base = "http://www.java2s.com" + path
    variants = [path, re.sub(r"\.htm$", ".html", path), re.sub(r"\.html$", ".htm", path)]
    years = [year] if year else [2016]
    years += [x for x in YEARS if x not in years][:1]
    for v in dict.fromkeys(variants):
        for y in list(years) + [None]:
            prefix = f"{y}" if y else ""
            url = f"https://web.archive.org/web/{prefix}id_/http://www.java2s.com{v}"
            html = fetch(url)
            if html and len(html) > 1500 and "Temporarily Offline" not in html:
                return html, f"{y}"
    return None


ART_RE = re.compile(r'<a\s+href=\\?"([^"]+?\.html?)\\?"[^>]*>(.*?)</a>', re.I | re.S)


def listing_articles(html: str, self_path: str) -> list[str]:
    """Article links on a listing page = same-directory .htm links (not catalogs)."""
    dirn = self_path.rsplit("/", 1)[0].lower()
    found, seen = [], set()
    for m in ART_RE.finditer(html):
        href = m.group(1)
        clean = href.split("?")[0].split("#")[0]
        if clean.startswith(("mailto:", "javascript:")):
            continue
        absu = urllib.parse.urljoin("http://www.java2s.com" + self_path, clean)
        p = urllib.parse.urlsplit(absu).path
        if not p.lower().startswith(dirn):
            continue
        if "catalog" in p.lower() or p.rstrip("/") == dirn:
            continue
        if p.lower().endswith((".css", ".js", ".ico", ".png", ".gif", ".jpg")):
            continue
        if urllib.parse.urlsplit(absu).netloc and "java2s.com" not in urllib.parse.urlsplit(absu).netloc:
            continue
        if p not in seen:
            seen.add(p)
            found.append(p)
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--year", type=int, default=0, help="prefer this snapshot year")
    args = ap.parse_args()

    tree = json.loads((DATA / "catalog_tree.json").read_text(encoding="utf-8"))
    subs = []
    for ch in tree:
        for st in ch["subtopics"]:
            p = st.get("href") or ""
            if p.endswith(".htm") or p.endswith(".html"):
                subs.append({
                    "key": f'{ch["dir"]}|{st["num"]}|{st["title"]}',
                    "chapter": ch["title"],
                    "dir": ch["dir"],
                    "num": st["num"], "title": st["title"], "path": p,
                })
    done: set[str] = set()
    if OUT.exists():
        for line in OUT.read_text(encoding="utf-8").splitlines():
            try:
                done.add(json.loads(line)["key"])
            except Exception:
                pass
    todo = [s for s in subs if s["key"] not in done]
    if args.limit:
        todo = todo[: args.limit]
    log(f"[discover] {len(subs)} sub-topics, {len(done)} done, {len(todo)} to do")

    out_f = OUT.open("a", encoding="utf-8")
    inv_seen: set[str] = set()
    for s in subs:
        if s["key"] in done:
            pass
    # inventory from previous runs
    if INV.exists():
        inv_seen = set(INV.read_text(encoding="utf-8").split())
    inv_f = INV.open("a", encoding="utf-8")

    n_ok = n_empty = n_fail = 0
    t0 = time.time()

    def work(s):
        got = snap_html(s["path"], args.year)
        if not got:
            return s, None, None
        html, snap = got
        arts = listing_articles(html, urllib.parse.urlsplit("http://x" + s["path"]).path)
        # drop self-listing page
        arts = [a for a in arts if a.lower() != s["path"].lower()]
        return s, snap, arts

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for s, snap, arts in pool.map(work, todo):
            if snap is None:
                n_fail += 1
                continue
            rec = {"key": s["key"], "chapter": s["chapter"], "dir": s["dir"], "num": s["num"],
                   "title": s["title"], "path": s["path"], "snap": snap, "articles": arts or []}
            out_f.write(json.dumps(rec) + "\n")
            out_f.flush()
            new = [a for a in (arts or []) if a not in inv_seen]
            for a in new:
                inv_seen.add(a)
                inv_f.write(a + "\n")
            inv_f.flush()
            if arts:
                n_ok += 1
            else:
                n_empty += 1
            if (n_ok + n_empty + n_fail) % 25 == 0:
                log(f"[discover] ok={n_ok} empty={n_empty} fail={n_fail} "
                    f"inventory={len(inv_seen)} {(time.time()-t0):.0f}s")
    log(f"[done] ok={n_ok} empty={n_empty} fail={n_fail} inventory={len(inv_seen)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
