#!/usr/bin/env python3
"""
clean_imported.py - deduplicate + de-junk content/imported/*.md

1. strips java2s boilerplate lines (nav menus, "HOME | Copyright © www.java2s.com 2016",
   "Next »" / "« Previous" markers, duplicated title lines)
2. removes duplicate pages: same normalized body -> keep the shortest/best slug,
   delete the rest and record the mapping in tools/dupes.csv

Safe to re-run: it is idempotent and can be run before every build.py.
"""
from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMP = ROOT / "content" / "imported"
DUPES = ROOT / "tools" / "dupes.csv"

JUNK_PATTERNS = [
    re.compile(r"^\s*\[HOME\]\([^)]*\)\s*\|\s*Copyright\s*©", re.I),
    re.compile(r"Copyright\s*©\s*www\.java2s\.com", re.I),
    re.compile(r"^\s*(-\s*)?(Next|Previous)\s*»", re.I),
    re.compile(r"^\s*«\s*(Prev|Back|Home)", re.I),
    re.compile(r"^\s*-\s*Java (Basic|Language|Data Types|Features|Algorithms)", re.I),
    re.compile(r"^\s*-\s*(OCA OCP Exam|Java Language Basics Java Language)"),
    re.compile(r"Source\s*and\s*Support", re.I),
    re.compile(r"^\s*www\.java2s\.com\s*$", re.I),
    re.compile(r"^\s*Copyright\s*©\s*$", re.I),
    # dead-end nav captured from the archived pages, e.g. "Back to Area  ↑"
    re.compile(r"^\s*-?\s*Back to .{0,70}[\u2191\ufffd]\s*$"),
]

# long nav-chain lines produced by the extractor, e.g.
# "Java Basic", "Java Language Basics Java Language Data Types Operator ... OCA OCP Exam 33"
NAV_CHAIN = re.compile(
    r"^(?:Java \w+|OCA OCP Exam\s*\d*|Java Language Basics|Data Types|Operator|Statement|"
    r"String|enum|Array|Autobox|class|Method|interface|Generics|Exception|Javadoc|Lambda|"
    r"package|import|Algorithms|Byte Array|Data Structures|Design Patterns|Directory|Network|"
    r"Regular Expression|Text File|\s)+$"
)


# ---------------------------------------------------------------------------
# java2s branding injected into the archived code samples, e.g.
#   //fromwww.java2s.com        /*from www.java2s.com*/
#   //from w w w . j a v a 2 s . c o m     (obfuscated: one <span> per character)
# Stripped from code blocks only; the code itself is left untouched.
# ---------------------------------------------------------------------------
_J2S_URL = r"(?:w\s*w\s*w\s*\.?\s*)?j\s*a\s*v\s*a\s*2\s*s\s*\.?\s*c\s*o\s*m"
CODE_COMMENT = re.compile(r"(?://|/\*)\s*(?:from\s*)?" + _J2S_URL + r"\s*(?:\*/)?", re.I)
CODE_URL_TEXT = re.compile(_J2S_URL, re.I)


def strip_code_branding(body: str) -> str:
    out: list[str] = []
    in_code = False
    for line in body.splitlines():
        st = line.lstrip()
        if st.startswith("```") or st.startswith("~~~"):
            in_code = not in_code
            out.append(line)
            continue
        if in_code:
            line = CODE_COMMENT.sub("", line)
            line = CODE_URL_TEXT.sub("JavaSchool", line)
            line = re.sub(r"[ \t]+$", "", line)
            if not line.strip():
                continue
        out.append(line)
    return "\n".join(out)


def strip_junk(body: str, title: str) -> str:
    body = strip_code_branding(body)
    out_lines = []
    title_norm = re.sub(r"\W+", "", title.lower())
    seen_titleish = 0
    for ln in body.splitlines():
        s = ln.strip()
        if not s:
            out_lines.append(ln)
            continue
        if any(p.search(s) for p in JUNK_PATTERNS):
            continue
        if NAV_CHAIN.match(s) and (s.count(" ") > 6 or s.startswith("Java Basic")):
            continue
        # duplicated title-ish line (plain echo of the title)
        norm = re.sub(r"\W+", "", s.lower())
        if norm == title_norm and seen_titleish < 2:
            seen_titleish += 1
            continue
        out_lines.append(ln)
    text = "\n".join(out_lines)
    # dead links pointing back into java2s (archive paths) -> keep the text only
    text = re.sub(r"\[([^\]]*)\]\((?:\.\./|/|https?://(?:www\.)?java2s\.com)[^)]*\)", r"\1", text)
    # a code fence left empty after stripping nav lines is just noise
    text = re.sub(r"^```[^\n]*\n\s*```\s*\n?", "", text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text + "\n"


def body_hash(body: str) -> str:
    norm = re.sub(r"\s+", " ", body).strip().lower()
    norm = re.sub(r"``````", "", norm)
    return hashlib.sha1(norm.encode("utf-8", "ignore")).hexdigest()


def main() -> int:
    files = sorted(IMP.glob("*.md"))
    by_hash: dict[str, Path] = {}
    dupes = []
    cleaned = 0
    removed = 0
    for f in files:
        raw = f.read_text(encoding="utf-8", errors="ignore")
        if raw.startswith("---"):
            end = raw.find("\n---", 3)
            fm, body = raw[: end + 4], raw[end + 4 :]
        else:
            fm, body = "", raw
        m = re.search(r"^title:\s*(.+)$", fm, re.M)
        title = m.group(1).strip() if m else f.stem
        new_body = strip_junk(body, title)
        if new_body != body.lstrip("\n"):
            f.write_text(fm + "\n" + new_body, encoding="utf-8")
            cleaned += 1
        h = body_hash(new_body)
        prev = by_hash.get(h)
        if prev is not None:
            # keep the shorter slug (less suffix noise), drop this one
            keep, drop = (prev, f) if len(prev.stem) <= len(f.stem) else (f, prev)
            if keep is not prev:
                by_hash[h] = keep
            drop.unlink()
            dupes.append((drop.stem, keep.stem))
            removed += 1
        else:
            by_hash[h] = f
    with DUPES.open("w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerows(dupes)
    print(f"cleaned={cleaned} duplicates_removed={removed} remaining={len(list(IMP.glob('*.md')))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
