#!/usr/bin/env python3
"""
cdx_inventory.py - pull the COMPLETE java2s link inventory from the Wayback CDX
API, restricted to snapshots from 2014 to 2020 (as requested).

Writes:
  tools/data/cdx_inventory.txt     - unique URLs (sorted)
  tools/data/cdx_inventory.tsv     - url <tab> best-timestamp
  tools/data/cdx_report.txt        - per-prefix counts

Usage:  python3 tools/cdx_inventory.py [--from 2014] [--to 2020] [--delay 2]
"""
from __future__ import annotations

import argparse
import csv
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "tools" / "data"
UA = "Mozilla/5.0 (compatible; JavaSchoolMirror/1.0)"

PREFIXES = [
    "/Tutorial/Java/", "/Tutorial/SCJP/", "/Tutorials/Java/", "/Code/Java/",
    "/ref/java/", "/Article-Tutorial/Java/", "/example/java",
]


def cdx(prefix: str, y1: str, y2: str, tries: int = 4) -> list[tuple[str, str]]:
    q = urllib.parse.urlencode({
        "url": "java2s.com" + prefix + "*",
        "fl": "original,timestamp",
        "collapse": "urlkey",
        "from": y1, "to": y2,
        "limit": "200000",
    })
    url = "https://web.archive.org/cdx/search/cdx?" + q
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=180) as r:
                text = r.read().decode("utf-8", "replace")
            if "Temporarily Offline" in text or text.lstrip().startswith("<html"):
                time.sleep(5 * (i + 1))
                continue
            rows = []
            for line in text.splitlines():
                parts = line.split()
                if len(parts) >= 2:
                    rows.append((parts[0], parts[1]))
            return rows
        except Exception:
            time.sleep(5 * (i + 1))
    return []


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="y1", default="2014")
    ap.add_argument("--to", dest="y2", default="2020")
    ap.add_argument("--delay", type=float, default=3.0)
    args = ap.parse_args()

    DATA.mkdir(parents=True, exist_ok=True)
    seen: dict[str, str] = {}
    report = []
    for p in PREFIXES:
        rows = cdx(p, args.y1, args.y2)
        added = 0
        for url, ts in rows:
            u = url.replace("http://www.java2s.com:80", "http://www.java2s.com")
            if u not in seen:
                seen[u] = ts
                added += 1
        report.append((p, len(rows), added))
        print(f"[cdx] {p:26s} rows={len(rows):6d} new={added:6d} total={len(seen)}", flush=True)
        time.sleep(args.delay)

    urls = sorted(seen)
    (DATA / "cdx_inventory.txt").write_text("\n".join(urls) + "\n", encoding="utf-8")
    with (DATA / "cdx_inventory.tsv").open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, delimiter="\t").writerows((u, seen[u]) for u in urls)
    (DATA / "cdx_report.txt").write_text(
        "\n".join(f"{p}\t{rows}\t{new}" for p, rows, new in report), encoding="utf-8")
    art = [u for u in urls if re.search(r"\.html?$", u, re.I)]
    print(f"[done] total={len(urls)} pages={len(art)} -> tools/data/cdx_inventory.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
