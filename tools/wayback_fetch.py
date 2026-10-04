#!/usr/bin/env python3
"""
wayback_fetch.py - import archived java2s.com pages from the Internet Archive
into the JavaSchool static site.

The crawler:
  1. asks the Wayback CDX API for archived URLs matching your filters
  2. downloads each snapshot (raw original HTML via the `id_` suffix)
  3. extracts the article content (title, headings, prose, code blocks)
  4. writes a markdown page into  content/imported/  with proper front matter
  5. records progress in a manifest so the crawl can be resumed

Rebuild the site afterwards:

    python3 build.py

Examples:

    # dry run: list what would be fetched (no download of page bodies)
    python3 tools/wayback_fetch.py --list --limit 20

    # the Java TUTORIAL chapters (recommended starting point, ~10k pages)
    python3 tools/wayback_fetch.py --include /Tutorial/Java/ --limit 500

    # Java CODE example pages
    python3 tools/wayback_fetch.py --include /Code/Java/ --limit 500

    # everything Java-related, politely paced, resumable
    python3 tools/wayback_fetch.py --include /Tutorial/Java/ --include /Code/Java/ --delay 1.0

Notes
-----
* Be polite to the archive: keep --delay >= 1 second. The archive may return
  HTTP 429/503; the script backs off automatically and can be re-run to resume.
* Content scraped from java2s.com remains copyright of its original owners.
  Check the site's terms before redistributing imported pages publicly.
"""

from __future__ import annotations

import argparse
import csv
import os
import random
import html
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

CDX = "https://web.archive.org/cdx/search/cdx"
UA = "JavaSchoolImport/1.0 (static-site builder; polite crawler; +set-your-contact-here)"
ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = ROOT / "content" / "imported"
MANIFEST = Path(os.environ.get("JAVA2S_MANIFEST", ROOT / "tools" / "wayback_manifest.csv"))

# --------------------------------------------------------------------------- #
# Minimal tolerant DOM
# --------------------------------------------------------------------------- #

VOID = {"br", "img", "hr", "meta", "link", "input", "area", "base", "col",
        "embed", "param", "source", "track", "wbr"}


class Node:
    __slots__ = ("tag", "attrs", "children", "parent")

    def __init__(self, tag, attrs=None, parent=None):
        self.tag = tag
        self.attrs = dict(attrs or {})
        self.children = []   # Node or str
        self.parent = parent

    def get(self, name, default=""):
        return self.attrs.get(name, default)

    def classes(self):
        return (self.get("class") or "").lower()

    def text(self, sep=" "):
        parts = []

        def walk(n):
            for c in n.children:
                if isinstance(c, str):
                    parts.append(c)
                else:
                    walk(c)

        walk(self)
        return sep.join(p for p in (re.sub(r"\s+", " ", p).strip() for p in parts) if p)

    def iter(self):
        for c in self.children:
            if isinstance(c, Node):
                yield c
                yield from c.iter()


class DomParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#document")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        node = Node(tag, {k.lower(): (v if v is not None else "") for k, v in attrs},
                    parent=self.stack[-1])
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag.lower() not in VOID and len(self.stack) > 1:
            self.stack.pop()

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in VOID:
            return
        # tolerant: pop until matching tag found
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return
        # ignore stray closing tags

    def handle_data(self, data):
        if data:
            self.stack[-1].children.append(data)


def parse_html(raw: str) -> Node:
    p = DomParser()
    p.feed(raw)
    return p.root


# --------------------------------------------------------------------------- #
# Content extraction
# --------------------------------------------------------------------------- #

DROP_CLASS_TOKENS = [
    "script", "style", "advert", "banner", "leftbar", "left-bar", "googlebar",
    "menu", "navbar", "nav-", "sidebar", "footer", "breadcrumb", "related",
    "share", "social", "cookie", "popup", "pagination",
]
DROP_TAGS = {"script", "style", "noscript", "iframe", "head", "form", "select",
             "button", "svg", "canvas", "object", "embed", "map"}
CODE_CLASS_TOKENS = ["codeshade", "coderesult", "codeblock", "code-block",
                     "highlight", "source", "java_code", "javacode", "pre"]
# link-only lines are almost always navigation leftovers
NAV_TEXT = {
    "home", "java", "java tutorial", "catalog", "more", "next", "previous",
    "print", "email", "copyright", "advertisement", "search", "sign in", "login",
}


def _has_code_class(node: Node) -> bool:
    cls = node.classes()
    style = (node.get("style") or "").lower()
    if any(t in cls for t in CODE_CLASS_TOKENS):
        return True
    # java2html converter wraps sources in <div class="java">
    words = cls.split()
    if words == ["java"] or "code" in words:
        return True
    if "pre" == cls.strip() or "monospace" in style:
        return True
    return False


def _is_nav_td(node: Node) -> bool:
    w = (node.get("width") or "").strip()
    if w.endswith("px"):
        w = w[:-2]
    try:
        if w and int(float(w)) <= 170:
            # nav columns are narrow; make sure it is link-heavy
            links = sum(1 for n in node.iter() if n.tag == "a")
            text = node.text()
            if links >= 3 or (text and len(text) < 400 and links >= 2):
                return True
    except ValueError:
        pass
    return False


def prune(node: Node) -> None:
    """Remove scripts, ads and navigation columns from the tree (in place)."""
    keep = []
    for c in node.children:
        if isinstance(c, Node):
            tag = c.tag
            cls = c.classes()
            id_ = (c.get("id") or "").lower()
            if tag in DROP_TAGS:
                continue
            if any(t in cls for t in DROP_CLASS_TOKENS) or any(
                t in id_ for t in ("header", "footer", "nav", "menu", "banner", "advert")
            ):
                continue
            if tag == "td" and _is_nav_td(c):
                continue
            if tag == "a" and (id_ == "top" or "javascript:" in (c.get("href") or "").lower()):
                continue
            prune(c)
            keep.append(c)
        else:
            keep.append(c)
    node.children = keep


def looks_like_nav_line(text: str, row: bool = False) -> bool:
    """Heuristic: is this text site chrome rather than content?

    row=True relaxes the rules for <tr> cells: table rows are where java2s
    keeps its numbered article index ("2.2.1. java.lang.Boolean") and its code
    listings (which can contain words like "trademark" in licence headers).
    """
    t = text.strip().lower()
    if not t:
        return False
    if t in NAV_TEXT:
        return True
    # "Java » JDK 7 » Asynchronous Channel" breadcrumbs etc.
    if len(t) < 80 and (" » " in t or " << " in t or " « " in t):
        return True
    limit = 400 if row else 160
    if t.startswith(("copyright", "©")) and len(t) < limit:
        return True
    if "all rights reserved" in t and len(t) < limit:
        return True
    if "contact us" in t and len(t) < 80:
        return True
    if ("trademark" in t or "demo source and support" in t) and len(t) < limit:
        return True
    # numbered table-of-contents entries: "1.3.2 Program Comments..." - these
    # are navigation in prose, but content when they are table rows.
    if not row and re.match(r"^(\d+\s*\.\s*)+\d", t) and len(t) < 120:
        return True
    return False


def has_code_descendant(n: Node) -> bool:
    if n.tag in ("pre", "code") or _has_code_class(n):
        return True
    for c in n.iter():
        if c.tag == "pre" or _has_code_class(c):
            return True
        # java2html (2005-2007 era) wraps whole sources in a single <code>
        # element split by <br/> - inline <code> in prose has no <br>
        if c.tag == "code" and sum(1 for b in c.iter() if b.tag == "br") >= 3:
            return True
    return False


def extract(raw: str, base_url: str) -> tuple[str, str, str]:
    """Return (title, description, markdown_body) from java2s-ish HTML."""
    # cut off head noise early
    m = re.search(r"<title[^>]*>(.*?)</title>", raw, re.I | re.S)
    raw_title = html.unescape(m.group(1)).strip() if m else ""

    root = parse_html(raw)
    body = None
    for n in root.iter():
        if n.tag == "body":
            body = n
            break
    if body is None:
        body = root
    prune(body)

    out: list[str] = []
    dbg = [0]
    code_buf: list[str] | None = None   # committed code lines
    code_line: list[str] = []            # current code line fragments
    buf: list[str] = []                  # current paragraph / inline run
    BLOCK_TAGS = {"table", "p", "div", "ul", "ol", "dl", "blockquote", "pre",
                  "form", "hr", "h1", "h2", "h3", "h4", "h5", "h6"}

    def flush_para():
        nonlocal buf
        text = re.sub(r"[ \t]+", " ", "".join(buf)).strip()
        buf = []
        if not text:
            return
        if looks_like_nav_line(text):
            return
        # numbered table-of-contents entry like "1.3.Comments" or "1. 12. 5. Title"
        if re.match(r"^(\d+\s*\.\s*)+\d*\.?\s*\S", text) and len(text) < 120:
            return
        out.append(text + "\n")

    def start_code():
        nonlocal code_buf, code_line, buf
        flush_para()
        code_buf = []
        code_line = []

    def commit_code_line():
        nonlocal code_line
        if code_buf is None:
            return
        if not code_line:
            return   # spacer <br/> with no content - don't create blank lines
        line = "".join(code_line).rstrip()
        code_line = []
        code_buf.append(line)

    def end_code():
        nonlocal code_buf, code_line
        if code_buf is None:
            return
        commit_code_line()
        lines = code_buf
        code_buf = None
        code_line = []
        # java2html inserts empty spacer lines between every source line;
        # drop blank lines so imported snippets stay compact
        lines = [l for l in lines if l.strip()]
        # collapse runs of whitespace-only content already handled above
        if any(l.strip() for l in lines):
            out.append("\n```java title=Example.java\n" + "\n".join(lines) + "\n```\n")

    def add_text(s: str, in_code: bool):
        if not s:
            return
        if in_code:
            # java2s wrapped every code token in a <span>; the separating spaces
            # are whitespace-only text nodes, so they must be kept as separators
            # (dropping them glues tokens together: "public class" -> "publicclass").
            if s.strip() == "":
                if "\xa0" in s:
                    s = s.replace("\xa0", " ")          # indentation
                elif " " in s:
                    s = " "                              # token separator
                else:
                    return                               # pure newline noise
            else:
                s = s.replace("\xa0", " ")
            code_line.append(s)
        else:
            s = s.replace("\xa0", " ")
            buf.append(s)

    def walk(n: Node):
        nonlocal code_buf
        tag = n.tag
        in_code = code_buf is not None
        if os.environ.get("J2S_DEBUG"):
            dbg[0] += 1
            if dbg[0] <= 40:
                print(f"[walk {dbg[0]:2d}] <{tag}> in_code={in_code} text={n.text()[:40]!r}",
                      file=sys.stderr)

        if _has_code_class(n) and not in_code:
            start_code()
            for c in n.children:
                if isinstance(c, str):
                    add_text(c, True)
                elif c.tag == "br":
                    commit_code_line()   # direct child: walk_inline() never sees it
                else:
                    walk_inline(c, code=True)
            end_code()
            return

        if tag in ("pre", "code") and not in_code:
            start_code()
            for c in n.children:
                if isinstance(c, str):
                    add_text(c, True)
                elif c.tag == "br":
                    commit_code_line()
                else:
                    walk_inline(c, code=True)
            end_code()
            return

        if tag in ("h1", "h2", "h3", "h4"):
            flush_para()
            level = int(tag[1])
            # Old java2s pages use unclosed <H1>, which makes the parser nest
            # the entire layout inside the heading. Collect only the leading
            # inline text, then keep walking the remaining children as content.
            parts: list[str] = []
            rest_start = len(n.children)
            for idx, c in enumerate(n.children):
                if isinstance(c, str):
                    parts.append(c)
                    rest_start = idx + 1
                elif c.tag in BLOCK_TAGS:
                    rest_start = idx
                    break
                else:
                    inline_txt = []
                    for cc in c.children:
                        if isinstance(cc, str):
                            inline_txt.append(cc)
                    parts.append("".join(inline_txt))
                    rest_start = idx + 1
            heading = re.sub(r"\s+", " ", "".join(parts)).strip()
            # Old java2s pages use unclosed <H1>, so the heading text is just
            # the page title - the site template renders its own <h1>, so we
            # consume it silently and keep walking the children as content.
            if tag == "h1":
                pass
            elif heading:
                out.append("\n" + "#" * level + " " + heading + "\n")
            for c in n.children[rest_start:]:
                if isinstance(c, str):
                    add_text(c, False)
                else:
                    walk(c)
            flush_para()
            return

        if tag == "p":
            flush_para()
            walk_inline(n, code=False)
            flush_para()
            out.append("")
            return

        if tag == "br":
            if code_buf is not None:
                commit_code_line()
            else:
                buf.append("\n")
            return

        if tag == "li":
            flush_para()
            item = n.text().strip()
            if item and not looks_like_nav_line(item):
                out.append("- " + item)
            return

        if tag == "tr":
            flush_para()
            row_links = sum(1 for c in n.iter() if c.tag == "a")
            row_text = n.text()
            code_row = any(has_code_descendant(c) for c in n.children if isinstance(c, Node))
            # link-heavy, short rows are navigation menus / breadcrumbs
            if row_links >= 3 and len(row_text) < 200 and not code_row:
                return
            if not code_row and looks_like_nav_line(row_text, row=True):
                return
            cell_nodes = [c for c in n.children
                          if isinstance(c, Node) and c.tag in ("td", "th")]
            # java2s puts <div class="codeShade"> inside table cells - walk the
            # cells so code blocks are detected instead of flattened to text
            if any(has_code_descendant(c) for c in cell_nodes):
                for c in cell_nodes:
                    walk(c)
                flush_para()
                return
            cells = [re.sub(r"\s+", " ", c.text()).strip() for c in cell_nodes]
            cells = [c for c in cells if c]
            if cells and not all(looks_like_nav_line(c) for c in cells):
                out.append("| " + " | ".join(cells) + " |")
            return

        if tag in ("ul", "ol"):
            flush_para()
            for c in n.children:
                if isinstance(c, Node):
                    walk(c)
            out.append("")
            return

        if tag == "a":
            add_text(n.text(), in_code)
            return

        # generic element
        for c in n.children:
            if isinstance(c, str):
                add_text(c, in_code)
            else:
                walk(c)

    def walk_inline(n: Node, code: bool):
        for c in n.children:
            if isinstance(c, str):
                add_text(c, code)
            else:
                if c.tag in DROP_TAGS:
                    continue
                if c.tag == "br":
                    if code:
                        commit_code_line()
                    else:
                        buf.append("\n")
                elif c.tag == "a" and not code:
                    href = c.get("href") or ""
                    text = c.text().strip()
                    if text and href and not href.lower().startswith("javascript"):
                        if href.startswith("/"):
                            parsed = urllib.parse.urlsplit(base_url)
                            href = f"{parsed.scheme}://{parsed.netloc}{href}"
                        buf.append(f"[{text}]({href})")
                    else:
                        buf.append(text)
                elif c.tag in ("b", "strong"):
                    t = c.text().strip()
                    if code:
                        # java2s wraps keywords like <b>public class </b>
                        # inside codeShade blocks - keep them on the current line
                        inner = []
                        for cc in c.children:
                            if isinstance(cc, str):
                                inner.append(cc)
                        code_line.append("".join(inner).replace("\xa0", " "))
                    elif t:
                        buf.append(f"**{t}**")
                elif c.tag in ("i", "em"):
                    t = c.text().strip()
                    if code:
                        inner = []
                        for cc in c.children:
                            if isinstance(cc, str):
                                inner.append(cc)
                        code_line.append("".join(inner).replace("\xa0", " "))
                    elif t:
                        buf.append(f"*{t}*")
                elif c.tag in ("h1", "h2", "h3", "h4") and not code:
                    flush_para()
                    walk(c)
                elif c.tag == "table" and not code:
                    flush_para()
                    walk(c)
                    out.append("")
                else:
                    walk_inline(c, code)

    # body-level walk, remembering separator rows
    if os.environ.get("J2S_DEBUG"):
        kids = [getattr(c, "tag", "#text") for c in body.children]
        print(f"[debug] body children: {kids}", file=sys.stderr)
        print(f"[debug] body text head: {body.text()[:120]!r}", file=sys.stderr)
    walk(body)
    flush_para()
    if os.environ.get("J2S_DEBUG"):
        print(f"[debug] out lines={len(out)}", file=sys.stderr)
        for line in out[:8]:
            print(f"[debug]   {line[:120]!r}", file=sys.stderr)

    # post-process: convert pipe-only runs into markdown tables, drop noise
    md = cleanup_markdown("\n".join(out))

    # description: first real paragraph
    desc = ""
    for line in md.splitlines():
        line = line.strip()
        if len(line) > 60 and not line.startswith(("#", "|", "-", "```")):
            desc = line[:170]
            break

    return raw_title, desc, md


def cleanup_markdown(md: str) -> str:
    src = md.split("\n")
    lines: list[str] = []
    i = 0
    in_fence = False
    while i < len(src):
        line = src[i].rstrip()
        s = line.strip()

        # code fences are sacred: copy verbatim, never merge their lines
        if s.startswith("```"):
            in_fence = not in_fence
            lines.append(line)
            i += 1
            continue
        if in_fence:
            lines.append(line)
            i += 1
            continue

        # table detection: >=3 consecutive pipe rows
        if s.startswith("|") and i + 1 < len(src) and src[i + 1].strip().startswith("|"):
            j = i
            rows = []
            while j < len(src) and src[j].strip().startswith("|"):
                rows.append(src[j].strip())
                j += 1
            if len(rows) >= 3:
                ncols = rows[0].count("|") - 1
                if ncols >= 1 and all(r.count("|") - 1 == ncols for r in rows):
                    header = rows[0]
                    lines.append(header)
                    lines.append("|" + "---|" * ncols)
                    lines.extend(rows[1:])
                    lines.append("")
                    i = j
                    continue
            # inconsistent pipe rows: not a real table - keep the text plain
            for r in rows:
                text = re.sub(r"\s*\|\s*", "  ", r).strip("| ")
                if text and not looks_like_nav_line(text):
                    lines.append(text)
            lines.append("")
            i = j
            continue

        if s:
            if lines and lines[-1].strip() and not lines[-1].startswith("```") and not s.startswith(("#", "```")):
                # join wrapped prose lines
                if not lines[-1].strip().startswith("-") and not s.startswith("-"):
                    lines[-1] = lines[-1].rstrip() + " " + s
                    i += 1
                    continue
            lines.append(s)
        elif lines and lines[-1].strip() != "":
            lines.append("")
        i += 1

    # collapse blank runs
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # post-pass: flatten only genuinely lone pipe rows (broken table fragments).
    # Rows that belong to a table (adjacent to other pipe rows / a separator)
    # must stay intact, including narrow two-column index tables.
    fixed: list[str] = []
    src2 = text.split("\n")
    for idx, line in enumerate(src2):
        s = line.strip()
        prev = src2[idx - 1].strip() if idx else ""
        nxt = src2[idx + 1].strip() if idx + 1 < len(src2) else ""
        is_sep = bool(re.fullmatch(r"\|[\s:|-]*\|", s))
        in_table = is_sep or prev.startswith("|") or nxt.startswith("|")
        if s.startswith("|") and s.endswith("|") and s.count("|") <= 4 and not in_table:
            plain = re.sub(r"\s*\|\s*", "  ", s).strip("| ").strip()
            if plain and not looks_like_nav_line(plain, row=True):
                fixed.append(plain)
            continue
        fixed.append(line)
    text = "\n".join(fixed)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


# --------------------------------------------------------------------------- #
# CDX listing + fetching
# --------------------------------------------------------------------------- #

def cdx_query(url_pattern: str, from_year: str | None, to_year: str | None,
              limit: int) -> list[tuple[str, str]]:
    """One CDX query -> [(original_url, timestamp), ...]."""
    params = {
        "url": url_pattern,
        "filter": "statuscode:200",
        "collapse": "urlkey",
        "fl": "original,timestamp",
        "limit": str(limit if limit > 0 else 100000),
    }
    # Only pass matchType for wildcard-less patterns; a trailing * already
    # implies a prefix query and combining both yields zero results.
    if "*" not in url_pattern:
        params["matchType"] = "domain" if "/" not in url_pattern.split("://")[-1] else "prefix"
    if from_year:
        params["from"] = from_year
    if to_year:
        params["to"] = to_year
    q = urllib.parse.urlencode(params)
    url = f"{CDX}?{q}"
    print(f"[cdx] querying {url_pattern} ...", flush=True)
    raw = ""
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=180) as r:
                raw = r.read().decode("utf-8", "replace")
            break
        except Exception as e:  # noqa: BLE001
            wait = 10 * (attempt + 1)
            print(f"  [!] CDX failed ({e}); retry in {wait}s ...", flush=True)
            time.sleep(wait)
    if not raw:
        print("  [!] CDX query failed permanently", flush=True)
        return []
    out = []
    for line in raw.splitlines():
        parts = line.split()
        if len(parts) == 2:
            out.append((parts[0], parts[1]))
    print(f"[cdx]   {len(out)} raw snapshots", flush=True)
    return out


def cdx_list(url_pattern: str, host: str, include: list[str], exclude: str | None,
             from_year: str | None, to_year: str | None, limit: int) -> list[tuple[str, str]]:
    """Return filtered [(original_url, timestamp), ...].

    When --include path prefixes like /Tutorial/Java/ are given, a separate
    prefix query is issued per include so the archive only has to scan that
    subtree (fast) instead of the whole domain (slow, then discarded).
    """
    queries: list[str] = []
    path_includes = [s for s in include if s.startswith("/")]
    other_includes = [s for s in include if not s.startswith("/")]

    if path_includes:
        for inc in path_includes:
            queries.append(host + inc.rstrip("*").rstrip("/") + "/*")
    else:
        queries.append(url_pattern)

    seen: set[str] = set()
    rows: list[tuple[str, str]] = []
    for q in queries:
        for original, ts in cdx_query(q, from_year, to_year,
                                      limit=limit if limit > 0 else 100000):
            if original in seen:
                continue
            seen.add(original)
            if path_includes and not any(s in original for s in path_includes):
                continue
            if other_includes and not any(s in original for s in other_includes):
                continue
            rows.append((original, ts))

    excl = re.compile(exclude) if exclude else None
    out = []
    seen_paths: set[str] = set()
    for original, ts in rows:
        if excl and excl.search(original):
            continue
        if not re.search(r"\.html?$", original, re.I):
            continue
        # treat /Page.htm and /Page.html as the same article
        key = re.sub(r"\.html?$", "", original, flags=re.I)
        if key in seen_paths:
            continue
        seen_paths.add(key)
        out.append((original, ts))
    return out


def fetch(url: str, retries: int, delay: float) -> str | None:
    """Fetch a page with retries and an https -> http fallback."""
    candidates = [url]
    if url.startswith("https://web.archive.org"):
        candidates.append("http://" + url[len("https://"):])
    last_err = None
    for attempt in range(retries + 1):
        for u in candidates:
            try:
                req = urllib.request.Request(u, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
                with urllib.request.urlopen(req, timeout=45) as r:
                    data = r.read()
                    enc = r.headers.get_content_charset() or "utf-8"
                    return data.decode(enc, "replace")
            except urllib.error.HTTPError as e:
                last_err = e
            except Exception as e:
                last_err = e
        if attempt < retries:
            time.sleep(1.5 * (attempt + 1) + random.random())
    print(f"  [!] {type(last_err).__name__}: {last_err}", flush=True)
    return None


def slug_from_url(url: str) -> str:
    path = urllib.parse.urlsplit(url).path
    parts = [p for p in path.split("/") if p]
    # drop trailing filename extension
    if parts:
        parts[-1] = re.sub(r"\.html?$", "", parts[-1], flags=re.I)
    # remove ordering prefixes like 0020__Language
    cleaned = []
    for p in parts:
        p = re.sub(r"^\d+__", "", p)
        cleaned.append(p)
    # keep the last two meaningful segments
    keep = cleaned[-2:] if len(cleaned) >= 2 else cleaned
    slug = slugify("-".join(keep))
    return slug or slugify(parts[-1] if parts else "page")


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:80].strip("-")


def clean_title(raw_title: str, url: str) -> str:
    t = re.sub(r"\s+", " ", raw_title).strip()
    # java2s titles look like " Comments : Language : Java Tutorial "
    # or " Introduction « Language « Java Tutorial "
    for sep in (":", "«", "»", "|"):
        if sep in t:
            first = t.split(sep)[0].strip()
            if first:
                t = first
                break
    if not t:
        t = slug_from_url(url).replace("-", " ").title()
    return t


def write_page(out_dir: Path, slug: str, title: str, desc: str, body: str,
               url: str, ts: str, order: int, overwrite: bool = False) -> Path:
    # if a table header survived as first line, fine; ensure body has content
    source = f"https://web.archive.org/web/{ts}/{url}"
    nav = title if len(title) <= 28 else title[:26] + "..."
    fm = [
        "---",
        f"title: {yaml_escape(title)}",
        f"nav: {yaml_escape(nav)}",
        f"description: {yaml_escape(desc or ('Imported from the java2s.com archive: ' + title))}",
        "section: Imported - java2s Archive",
        f"order: {order}",
        f"source: {source}",
        "---",
        "",
    ]
    # demote any H1 in body (template renders its own H1)
    body = re.sub(r"^# ", "## ", body, flags=re.M)
    text = "\n".join(fm) + body
    path = out_dir / f"{slug}.md"
    if not overwrite:
        n = 2
        while path.exists():
            path = out_dir / f"{slug}-{n}.md"
            n += 1
    path.write_text(text, encoding="utf-8")
    return path


def yaml_escape(s: str) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def load_manifest() -> dict[str, tuple[str, str]]:
    done = {}
    if MANIFEST.exists():
        with MANIFEST.open(newline="", encoding="utf-8") as f:
            for row in csv.reader(f):
                if len(row) >= 3:
                    done[row[1]] = (row[0], row[2])  # slug, original
    return done


def append_manifest(slug: str, original: str, ts: str) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST.open("a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([slug, original, ts])


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Import archived java2s.com pages from the Wayback Machine.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument("--url", default="java2s.com/*",
                    help="CDX url pattern (default: java2s.com/*)")
    ap.add_argument("--host", default="java2s.com",
                    help="host used to expand --include path prefixes (default java2s.com)")
    ap.add_argument("--include", action="append", default=[],
                    help="only URLs containing this substring (repeatable), "
                         "e.g. --include /Tutorial/Java/")
    ap.add_argument("--exclude", default=None,
                    help="regex of URLs to skip (e.g. 'Catalog.*\\\\.htm$')")
    ap.add_argument("--limit", type=int, default=0,
                    help="max pages to import this run (0 = no limit)")
    ap.add_argument("--delay", type=float, default=1.5,
                    help="seconds to sleep between page downloads (default 1.5)")
    ap.add_argument("--from", dest="from_year", default=None,
                    help="earliest snapshot year, e.g. 2016")
    ap.add_argument("--to", dest="to_year", default=None,
                    help="latest snapshot year, e.g. 2023")
    ap.add_argument("--out", default=str(DEFAULT_OUT),
                    help=f"output directory (default {DEFAULT_OUT})")
    ap.add_argument("--list", action="store_true",
                    help="dry run: list matching URLs and exit")
    ap.add_argument("--urls-file", default=None,
                    help="file of URLs (one per line) to fetch directly, skipping CDX")
    ap.add_argument("--stamp", default=None,
                    help="snapshot year/ts to request for --urls-file (e.g. 2016); "
                         "default = nearest to 2016")
    ap.add_argument("--retries", type=int, default=3)
    ap.add_argument("--overwrite", action="store_true",
                    help="replace existing pages instead of writing -2, -3 duplicates")
    ap.add_argument("--start-order", type=int, default=1000,
                    help="front-matter order of the first imported page")
    args = ap.parse_args(argv)

    if args.urls_file:
        lines = [l.strip() for l in Path(args.urls_file).read_text(encoding="utf-8").splitlines() if l.strip()]
        out_dir = Path(args.out)
        out_dir.mkdir(parents=True, exist_ok=True)
        done = load_manifest()
        imported = skipped = failed = 0
        order = args.start_order
        print(f"[urls-file] {len(lines)} urls, {len(done)} in manifest", flush=True)
        for original in lines:
            if original in done:
                skipped += 1
                continue
            if args.limit and imported >= args.limit:
                break
            stamp = args.stamp or "2016"
            print(f"[get] {original}", flush=True)
            raw = fetch(f"https://web.archive.org/web/{stamp}id_/{original}",
                        retries=args.retries, delay=args.delay)
            if raw is None:
                failed += 1
                append_manifest("-", original, stamp)
                continue
            try:
                raw_title, desc, md = extract(raw, original)
            except Exception:
                failed += 1
                append_manifest("-", original, stamp)
                continue
            if len(re.sub(r"[\s`#*>|-]+", "", md)) < 60:
                skipped += 1
                append_manifest("(thin)", original, stamp)
                continue
            slug = slug_from_url(original)
            title = clean_title(raw_title, original)
            write_page(out_dir, slug, title, desc, md, original, stamp, order,
                       overwrite=args.overwrite)
            append_manifest(slug, original, stamp)
            done[original] = (slug, stamp)
            order += 1
            imported += 1
            if imported % 20 == 0:
                print(f"[progress] imported={imported} skipped={skipped} failed={failed}", flush=True)
        print(f"\nDone. imported={imported} skipped={skipped} failed={failed}")
        return 0

    # List generously so that manifest-skip doesn't starve the run, but don't
    # scan the entire archive when the user only wants a handful of pages.
    cdx_limit = 0 if args.limit == 0 else min(100000, max(5000, args.limit * 50))
    urls = cdx_list(args.url, args.host, args.include, args.exclude,
                    args.from_year, args.to_year,
                    limit=cdx_limit)
    print(f"[cdx] {len(urls)} candidate URLs after filters")

    if args.list:
        for original, ts in urls[: args.limit or len(urls)]:
            print(f"  {ts}  {original}")
        if args.limit and len(urls) > args.limit:
            print(f"  ... and {len(urls) - args.limit} more")
        return 0

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    done = load_manifest()
    imported = skipped = failed = 0
    order = args.start_order

    for original, ts in urls:
        if original in done:
            skipped += 1
            continue
        if args.limit and imported >= args.limit:
            break

        print(f"[get] {original} @{ts}", flush=True)
        raw = fetch(f"https://web.archive.org/web/{ts}id_/{original}",
                    retries=args.retries, delay=args.delay)
        if raw is None:
            failed += 1
            append_manifest("-", original, ts)
            continue

        try:
            raw_title, desc, md = extract(raw, original)
        except Exception as e:  # noqa: BLE001
            print(f"  [!] parse error: {e}", flush=True)
            failed += 1
            continue

        # Chapter/menu pages in the archive are link stubs without prose or
        # code - skip them so only real articles are imported.
        if "```" not in md and len(md) < 900:
            print("  [i] looks like a listing/TOC page, skipping")
            skipped += 1
            append_manifest("(thin)", original, ts)
            continue

        title = clean_title(raw_title, original)
        slug = slug_from_url(original)
        path = write_page(out_dir, slug, title, desc, md, original, ts, order)
        append_manifest(path.stem, original, ts)
        imported += 1
        order += 1
        print(f"  [ok] {path.name}  ({len(md)} chars)")
        time.sleep(args.delay)

    print(f"\nDone. imported={imported} skipped={skipped} failed={failed}")
    print(f"Output: {out_dir}")
    print("Rebuild the site with:  python3 build.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
