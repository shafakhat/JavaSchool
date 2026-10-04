#!/usr/bin/env python3
"""
build.py - static site builder for "JavaSchool", a W3Schools-style Java tutorial site.

Zero dependencies (Python 3.8+). Usage:

    python3 build.py

Reads markdown pages from  content/*.md  (and  content/imported/*.md  produced by
tools/wayback_fetch.py), renders them with a shared template, and writes a fully
static site to  docs/  which can be deployed directly to GitHub Pages.
"""

from __future__ import annotations

import csv
import html as html_mod
import json
import re
import shutil
import sys
import urllib.parse
from pathlib import Path

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

ROOT = Path(__file__).resolve().parent
CONTENT_DIR = ROOT / "content"
IMPORTED_DIR = CONTENT_DIR / "imported"
ASSETS_DIR = ROOT / "assets"
OUT_DIR = ROOT / "docs"
MANIFEST_PATH = ROOT / "tools" / "wayback_manifest.csv"
IMPORTED_SECTION = "Imported - java2s Archive"

SITE_NAME = "JavaSchool"
SITE_TAGLINE = "Learn Java Programming - Free and Easy"
SITE_DESCRIPTION = (
    "Complete Java tutorial with hundreds of runnable examples: syntax, object oriented "
    "programming, collections, threads, lambdas, streams, JDBC and more."
)

# Display order of sidebar sections. Any other section found in front matter is
# appended after these, in first-seen order.
SECTION_ORDER = [
    "Get Started",
    "Java Basics",
    "Object Oriented",
    "Core Java",
    "Collections",
    "Advanced Java",
    "Interview & Certification",
    "Reference",
    "Imported - java2s Archive",
]

# The "Java HOME" link pinned at the top of the sidebar.
HOME_NAV = {"label": "Java HOME", "href": "index.html"}

# Footer quick links (only those that exist are shown).
FOOTER_LINKS = [
    ("intro", "Java Introduction"),
    ("variables", "Variables"),
    ("strings", "Strings"),
    ("classes-objects", "Classes and Objects"),
    ("collections", "Collections"),
    ("exceptions", "Exceptions"),
    ("quiz", "Java Quiz"),
]

LANG_EXT = {
    "java": "java",
    "sql": "sql",
    "bash": "sh",
    "sh": "sh",
    "xml": "xml",
    "html": "html",
    "text": "txt",
    "": "txt",
}

# --------------------------------------------------------------------------- #
# Markdown -> HTML (small, purpose-built converter)
# --------------------------------------------------------------------------- #

_INLINE_CODE = re.compile(r"`[^`]+`")
_BOLD = re.compile(r"\*\*([^*]+)\*\*")
_ITALIC = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
_PLACEHOLDER = re.compile(r"\x00(\d+)\x00")


def esc(s: str) -> str:
    return html_mod.escape(s, quote=False)


def esc_q(s: str) -> str:
    return html_mod.escape(s, quote=True)


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]*>", "", text)
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-") or "section"


def inline(text: str) -> str:
    """Convert inline markdown (code, bold, italic, links) on escaped text.

    Code spans are stashed as placeholders first so that **bold** and *italic*
    markers can still span across them (e.g. **NIO (`java.nio.file`)**).
    """
    text = esc(text)

    code_spans: list[str] = []

    def stash(m: re.Match) -> str:
        code_spans.append(m.group(0))
        return f"\x00{len(code_spans) - 1}\x00"

    text = _INLINE_CODE.sub(stash, text)
    text = _BOLD.sub(r"<strong>\1</strong>", text)
    text = _ITALIC.sub(r"<em>\1</em>", text)
    text = _LINK.sub(r'<a href="\2">\1</a>', text)

    def restore(m: re.Match) -> str:
        span = code_spans[int(m.group(1))]
        return "<code>" + span[1:-1] + "</code>"

    return _PLACEHOLDER.sub(restore, text)


# HTML elements that swallow everything until their explicit closing tag
_RAW_HOST = re.compile(r"<(script|style|pre|table|dl|details)\b[^>]*>", re.I)
_TAG_TOKEN = re.compile(r"<(/?)([A-Za-z][A-Za-z0-9]*)\b[^>]*?(/?)>")
_HTML_VOID = frozenset(
    {"br", "hr", "img", "input", "meta", "link", "area", "base",
     "col", "embed", "source", "track", "wbr"}
)


class MarkdownRenderer:
    def __init__(self) -> None:
        self.out: list[str] = []
        self.heading_ids: dict[str, int] = {}
        self.headings: list[tuple[int, str, str]] = []  # (level, text, id)

    # -- helpers ---------------------------------------------------------- #

    def _heading_id(self, text: str) -> str:
        base = slugify(text)
        count = self.heading_ids.get(base, 0)
        self.heading_ids[base] = count + 1
        hid = base if count == 0 else f"{base}-{count}"
        return hid

    @staticmethod
    def _is_block_start(line: str) -> bool:
        s = line.strip()
        if not s:
            return True
        if s.startswith(("```", "##", ">", "- ", "* ")):
            return True
        if re.match(r"^\d+\.\s", s):
            return True
        if s.startswith("|") and len(s) > 2:
            return True
        if s.startswith("<"):
            return True
        return False

    # -- block parsers ----------------------------------------------------- #

    def _code_fence(self, lines: list[str], i: int) -> int:
        info = lines[i].strip()[3:].strip()
        tokens = info.split()
        lang = tokens[0] if tokens and "=" not in tokens[0] else "text"
        title = None
        for t in tokens:
            if t.startswith("title="):
                title = t[6:]
        i += 1
        buf: list[str] = []
        while i < len(lines) and not lines[i].strip().startswith("```"):
            buf.append(lines[i])
            i += 1
        i += 1  # closing fence
        code = "\n".join(buf)

        if lang == "raw":
            self.out.append(code)
            return i

        ext = LANG_EXT.get(lang, lang or "txt")
        label = title or f"Example.{ext}"
        cls = f' class="lang-{esc_q(lang)}" data-lang="{esc_q(lang)}"'
        self.out.append(
            '<div class="code-box">'
            f'<div class="code-bar"><span class="code-file">{esc(label)}</span>'
            '<button type="button" class="copy-btn" title="Copy code">Copy</button></div>'
            f"<pre><code{cls}>{esc(code)}</code></pre>"
            "</div>"
        )
        return i

    def _heading(self, line: str) -> None:
        m = re.match(r"^(#{2,4})\s+(.*)$", line.strip())
        level = len(m.group(1))
        raw = m.group(2).strip()
        hid = self._heading_id(raw)
        self.headings.append((level, re.sub(r"[`*]", "", raw), hid))
        self.out.append(f'<h{level} id="{hid}">{inline(raw)}</h{level}>')

    def _blockquote(self, lines: list[str], i: int) -> int:
        buf: list[str] = []
        while i < len(lines) and lines[i].strip().startswith(">"):
            buf.append(lines[i].strip().lstrip(">").strip())
            i += 1
        text = " ".join(x for x in buf if x)
        style, label, icon = "note", "Note", "&#128161;"
        m = re.match(r"^\*\*(Note|Tip|Warning|Remember):\*\*\s*(.*)$", text, re.I)
        if m:
            key = m.group(1).lower()
            text = m.group(2)
            style = {"note": "note", "tip": "tip", "warning": "warn", "remember": "remember"}[key]
            label = key.capitalize()
            icon = {"note": "&#128161;", "tip": "&#128640;", "warning": "&#9888;", "remember": "&#128218;"}[key]
        self.out.append(
            f'<div class="callout callout-{style}">'
            f'<span class="callout-title">{icon} {label}</span> {inline(text)}</div>'
        )
        return i

    @staticmethod
    def _split_row(row: str) -> list[str]:
        row = row.strip()
        row = row.strip("|")
        return [c.strip() for c in row.split("|")]

    def _table(self, lines: list[str], i: int) -> int:
        header = self._split_row(lines[i])
        i += 2  # skip separator
        rows: list[list[str]] = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            rows.append(self._split_row(lines[i]))
            i += 1
        th = "".join(f"<th>{inline(c)}</th>" for c in header)
        body = "".join(
            "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>" for row in rows
        )
        self.out.append(f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead>'
                        f"<tbody>{body}</tbody></table></div>")
        return i

    def _list(self, lines: list[str], i: int) -> int:
        ordered = bool(re.match(r"^\s*\d+\.\s", lines[i]))
        tag = "ol" if ordered else "ul"
        items: list[str] = []
        while i < len(lines):
            s = lines[i].strip()
            if ordered:
                m = re.match(r"^\d+\.\s+(.*)$", s)
            else:
                m = re.match(r"^[-*]\s+(.*)$", s)
            if not m:
                break
            items.append(f"<li>{inline(m.group(1))}</li>")
            i += 1
        self.out.append(f"<{tag}>" + "".join(items) + f"</{tag}>")
        return i

    def _paragraph(self, lines: list[str], i: int) -> int:
        buf: list[str] = []
        while i < len(lines):
            s = lines[i]
            if buf and self._is_block_start(s):
                break
            if not s.strip() and (not buf or self._is_block_start(lines[i + 1]) if i + 1 < len(lines) else True):
                if buf:
                    break
            if not s.strip():
                break
            buf.append(s.strip())
            i += 1
        if buf:
            self.out.append("<p>" + inline(" ".join(buf)) + "</p>")
        return i

    def _raw_html(self, lines: list[str], i: int) -> int:
        """Emit an HTML block verbatim.

        Consumes consecutive ``<``-lines, blank lines followed by more HTML,
        and - crucially - plain text lines that sit *inside* an element that
        is still open (e.g. a ``<p>`` wrapped across multiple lines).
        """
        buf: list[str] = []
        depth = 0                      # net open tags of ordinary elements
        open_tag: str | None = None    # script/style/pre/... swallow-until-close
        close_re = None
        while i < len(lines):
            s = lines[i]
            st = s.strip()
            if open_tag:
                # inside script/style/pre/table/...: consume to closing tag
                buf.append(s)
                i += 1
                if close_re.search(st):
                    open_tag = None
                continue
            if st.startswith("<"):
                buf.append(s)
                i += 1
                m = _RAW_HOST.match(st)
                if m and not re.search(r"</" + m.group(1) + r"\s*>", st, re.I) \
                        and not st.endswith("/>"):
                    open_tag = m.group(1).lower()
                    close_re = re.compile(r"</" + re.escape(open_tag) + r"\s*>", re.I)
                    continue
                for closing, name, selfclose in _TAG_TOKEN.findall(st):
                    tag = name.lower()
                    if selfclose or tag in _HTML_VOID:
                        continue
                    depth += -1 if closing else 1
                continue
            if not st:
                # blank line: keep going only when another HTML line follows
                j = i + 1
                if j < len(lines) and lines[j].strip().startswith("<"):
                    buf.append(s)
                    i += 1
                    continue
                break
            if buf and depth > 0:
                # plain text inside an open element -> part of the block
                if st.startswith(("```", "##")) or st == "---":
                    break              # safety valve: never swallow structure
                buf.append(s)
                i += 1
                continue
            break
        self.out.append("\n".join(buf))
        return i

    # -- main -------------------------------------------------------------- #

    def render(self, md: str) -> tuple[str, list[tuple[int, str, str]]]:
        lines = md.split("\n")
        i = 0
        n = len(lines)
        while i < n:
            line = lines[i]
            s = line.strip()
            if not s:
                i += 1
                continue
            if s.startswith("```"):
                i = self._code_fence(lines, i)
            elif re.match(r"^#{2,4}\s", s):
                self._heading(line)
                i += 1
            elif s.startswith(">"):
                i = self._blockquote(lines, i)
            elif (
                "|" in s
                and i + 1 < n
                and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1])
                and "-" in lines[i + 1]
            ):
                i = self._table(lines, i)
            elif re.match(r"^[-*]\s", s) or re.match(r"^\d+\.\s", s):
                i = self._list(lines, i)
            elif s.startswith("<"):
                i = self._raw_html(lines, i)
            elif s == "---":
                self.out.append("<hr>")
                i += 1
            else:
                i = self._paragraph(lines, i)
        return "\n".join(self.out), self.headings


def convert_markdown(md: str) -> tuple[str, list[tuple[int, str, str]]]:
    return MarkdownRenderer().render(md)


# --------------------------------------------------------------------------- #
# Front matter & page loading
# --------------------------------------------------------------------------- #

def parse_front_matter(text: str) -> tuple[dict, str]:
    if text.startswith("---"):
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
        if m:
            meta: dict = {}
            for line in m.group(1).splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip().lower()] = v.strip()
            return meta, text[m.end():]
    return {}, text


def clean_field(value: str) -> str:
    """Strip leftover markup (java2s <em> highlight markers etc.) from metadata."""
    if not value:
        return value
    return re.sub(r"<[^>]+>", "", value).strip()


def load_pages() -> list[dict]:
    pages: list[dict] = []
    sources = []
    if CONTENT_DIR.is_dir():
        sources += sorted(p for p in CONTENT_DIR.glob("*.md"))
    if IMPORTED_DIR.is_dir():
        sources += sorted(p for p in IMPORTED_DIR.glob("*.md"))

    for path in sources:
        raw = path.read_text(encoding="utf-8")
        meta, body = parse_front_matter(raw)
        slug = path.stem
        if slug == "home":
            continue
        title = clean_field(meta.get("title", slug.replace("-", " ").title()))
        pages.append(
            {
                "slug": slug,
                "title": title,
                "nav": clean_field(meta.get("nav", "")) or title,
                "description": clean_field(meta.get("description", "")),
                "section": meta.get("section", "Imported - java2s Archive"),
                "order": int(meta.get("order", "100") or 100),
                "layout": meta.get("layout", ""),
                "body_md": body,
                "source": meta.get("source", ""),
            }
        )

    # group by section, preserving SECTION_ORDER then first-seen order
    section_index = {name: i for i, name in enumerate(SECTION_ORDER)}
    extra: list[str] = []
    for p in pages:
        if p["section"] not in section_index and p["section"] not in extra:
            extra.append(p["section"])
    ordered_names = SECTION_ORDER + extra

    flat: list[dict] = []
    sections = []
    for name in ordered_names:
        group = [p for p in pages if p["section"] == name]
        if not group:
            continue
        group.sort(key=lambda p: (p["order"], p["title"].lower()))
        sections.append({"title": name, "pages": group})
        flat.extend(group)
    return sections, flat


# --------------------------------------------------------------------------- #
# HTML template
# --------------------------------------------------------------------------- #

def build_sidebar(sections: list[dict], active_slug: str) -> str:
    """Minimal sidebar: just the link back to the Java HOME page."""
    active = "" if active_slug else " active"
    return (
        '<nav id="sidebar" class="sidebar" aria-label="Tutorial menu">\n'
        '  <div class="side-section">'
        f'<a class="side-link side-home{active}" href="{HOME_NAV["href"]}">'
        f'<span class="side-home-icon">&#127968;</span> {HOME_NAV["label"]}</a>'
        "</div>\n"
        "</nav>"
    )


def build_pager(flat: list[dict], idx: int) -> str:
    prev_p = flat[idx - 1] if idx > 0 else None
    next_p = flat[idx + 1] if idx + 1 < len(flat) else None
    left = right = ""
    if prev_p:
        left = (
            f'<a class="pager-btn" href="{prev_p["slug"]}.html">'
            f'<span class="pager-lbl">&#10094; Previous</span>'
            f'<span class="pager-title">{esc(prev_p["nav"])}</span></a>'
        )
    if next_p:
        right = (
            f'<a class="pager-btn pager-next" href="{next_p["slug"]}.html">'
            f'<span class="pager-lbl">Next &#10095;</span>'
            f'<span class="pager-title">{esc(next_p["nav"])}</span></a>'
        )
    return f'<div class="pager">{left}{right}</div>'


def build_footer() -> str:
    links = []
    for slug, label in FOOTER_LINKS:
        links.append(f'<a href="{slug}.html">{esc(label)}</a>')
    links_html = "".join(links)
    return f"""<footer class="ws-footer">
  <div class="footer-inner">
    <div class="footer-col footer-brand">
      <div class="brand footer-logo"><span class="brand-mark">J</span><span class="brand-text">avaSchool</span></div>
      <p>{esc(SITE_DESCRIPTION)}</p>
    </div>
    <div class="footer-col">
      <h4>Tutorial</h4>
      {links_html}
    </div>
    <div class="footer-col">
      <h4>More</h4>
      <a href="keywords.html">Java Keywords</a>
      <a href="string-methods.html">String Methods</a>
      <a href="java-api.html">Useful Java Classes</a>
      <a href="how-java-works.html">How Java Works</a>
    </div>
  </div>
  <div class="footer-bottom">
    <span>&copy; <span id="site-year">2026</span> {SITE_NAME} &middot; Tutorial content is original, written for this site.</span>
    <span>Shafakhatullah Khan Mohammed</span>
  </div>
</footer>"""


def page_document(
    *,
    meta_title: str,
    description: str,
    sidebar_html: str,
    main_html: str,
    is_home: bool,
    body_class: str = "",
) -> str:
    title_tag = (
        f"{SITE_NAME} - {SITE_TAGLINE}" if is_home else f"{meta_title} - {SITE_NAME}"
    )
    desc = description or SITE_DESCRIPTION
    dark_init = """
<script>
(function(){try{var t=localStorage.getItem('jschool-theme');
if(t==='dark'||(!t&&window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches)){
document.documentElement.setAttribute('data-theme','dark');}}catch(e){}})();
</script>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title_tag)}</title>
<meta name="description" content="{esc_q(desc)}">
<meta name="generator" content="build.py (JavaSchool)">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/style.css">{dark_init}
</head>
<body class="{body_class}">
<header class="topnav">
  <button type="button" id="navToggle" class="icon-btn nav-toggle" aria-label="Open menu">&#9776;</button>
  <a class="brand" href="index.html" aria-label="JavaSchool home">
    <span class="brand-mark">J</span><span class="brand-text">avaSchool</span>
  </a>
  <div class="search-wrap">
    <input type="text" id="searchInput" placeholder="Search Tutorials..." autocomplete="off" spellcheck="false">
    <div id="searchResults" class="search-results" hidden></div>
  </div>
  <button type="button" id="themeToggle" class="icon-btn theme-toggle" title="Toggle dark mode" aria-label="Toggle dark mode">&#9680;</button>
</header>
{sidebar_html}
<main class="main">
  <article class="ws-content">
{main_html}
  </article>
</main>
{build_footer()}
<button type="button" id="topBtn" class="top-btn" title="Go to top" aria-label="Go to top">&#8679;</button>
<script src="assets/search-index.js"></script>
<script src="assets/script.js"></script>
</body>
</html>
"""


def render_home(home_path: Path, sections: list[dict], flat: list[dict]) -> str:
    raw = home_path.read_text(encoding="utf-8")
    meta, body = parse_front_matter(raw)
    body_html, _ = convert_markdown(body)
    # Expandable topic cards (links live inside the cards).
    body_html = body_html.replace(
        '<div id="topic-cards"></div>', build_topic_cards(sections)
    )
    # For the home layout, the hero is part of the markdown; no extra <h1>.
    sidebar = build_sidebar(sections, active_slug="")
    pager = build_pager(flat, 0) if flat else ""
    main = f'    <div class="home-wrap">\n{body_html}\n    </div>\n    {pager}'
    return page_document(
        meta_title=meta.get("title", SITE_NAME),
        description=meta.get("description", ""),
        sidebar_html=sidebar,
        main_html=main,
        is_home=True,
        body_class="page-home",
    )


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# Archive grouping (keeps the sidebar small: one link per category instead of
# one per imported page)
# --------------------------------------------------------------------------- #

def category_from_url(url: str) -> str:
    path = urllib.parse.urlparse(url).path.strip("/")
    parts = [p for p in path.split("/") if p]
    cat = "Other examples"
    if len(parts) >= 3 and parts[0] in ("Code", "Tutorial") and parts[1] == "Java":
        cat = parts[2]
    elif len(parts) >= 3 and parts[0] == "Tutorials" and parts[1] == "Java":
        cat = "New " + parts[2]
    elif len(parts) >= 3 and parts[0] == "Article-Tutorial" and parts[1] == "Java":
        cat = parts[2]
    elif len(parts) >= 3 and parts[0] == "Tutorial" and parts[1] not in ("Java",):
        cat = parts[1]
    elif len(parts) >= 2 and parts[0] == "ref":
        cat = "OCA OCP Practice" if "oca" in parts[-1].lower() else "ref " + parts[1]
    elif len(parts) >= 2 and parts[0] == "example":
        cat = parts[1].replace("java-", "java ").replace("-", " ")
    elif parts:
        cat = parts[-1].rsplit(".", 1)[0] if parts[-1].endswith((".htm", ".html")) else parts[-1]
    name = cat.replace("__", " ").replace("_", " ").replace("-", " ").strip()
    m = re.match(r"^(\d{4})\s+(.*)$", name)
    if m:
        name = f"{m.group(2)} ({m.group(1)})"
    return name or "Other examples"


def archive_category_map() -> dict:
    mapping = {}
    for path in (MANIFEST_PATH, ROOT / "tools" / "live_manifest.csv"):
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as f:
            for row in csv.reader(f):
                if len(row) < 2:
                    continue
                slug, url = row[0], row[1]
                if slug in ("-", "(thin)", "(in-archive)"):
                    continue
                mapping.setdefault(slug, category_from_url(url))
    return mapping


def attach_archive_groups(sections: list[dict]) -> list[dict]:
    """Give the imported section category sub-pages instead of huge link lists."""
    cats = archive_category_map()
    for sec in sections:
        if sec["title"] != IMPORTED_SECTION or len(sec["pages"]) < 80:
            continue
        by_cat: dict[str, list] = {}
        for p in sec["pages"]:
            by_cat.setdefault(cats.get(p["slug"], "Other examples"), []).append(p)
        groups = []
        for name in sorted(by_cat, key=lambda s: s.lower()):
            pages = sorted(by_cat[name], key=lambda p: p["title"].lower())
            gslug = "archive-cat-" + slugify(name)
            groups.append({
                "title": name,
                "slug": gslug,
                "href": gslug + ".html",
                "pages": pages,
            })
        sec["groups"] = groups
        return groups
    return []


def build_crumb(*parts: tuple[str, str | None]) -> str:
    """Breadcrumb; first part is always the Home link. href=None renders plain text."""
    seg = []
    for text, href in parts:
        seg.append(f'<a href="{href}">{text}</a>' if href else f"<span>{text}</span>")
    joined = ' <span class="crumb-sep">&rsaquo;</span> '.join(seg)
    return f'<nav class="crumb">&#127968; {joined}</nav>'


SECTION_ICONS = {
    "Get Started": "&#128640;",
    "Java Basics": "&#128216;",
    "Object Oriented": "&#129513;",
    "Core Java": "&#9749;",
    "Collections": "&#128449;",
    "Advanced Java": "&#129514;",
    "Interview & Certification": "&#127919;",
    "Reference": "&#128218;",
    IMPORTED_SECTION: "&#128230;",
}


def build_topic_cards(sections: list[dict]) -> str:
    """Expandable topic cards for the home page - links live inside the cards."""
    out = ['<div class="topic-cards">']
    for i, sec in enumerate(sections):
        sid = "tc-" + slugify(sec["title"])
        groups = sec.get("groups")
        count = sum(len(g["pages"]) for g in groups) if groups else len(sec["pages"])
        opened = i == 0
        icon = SECTION_ICONS.get(sec["title"], "&#128196;")
        out.append(f'<div class="tcard{" open" if opened else ""}">')
        out.append(
            f'<button type="button" class="tcard-head" data-target="{sid}" '
            f'aria-expanded="{"true" if opened else "false"}">'
            f'<span class="tcard-icon">{icon}</span>'
            f'<span class="tcard-title">{esc(sec["title"])}</span>'
            f'<span class="tcard-count">{count} pages</span>'
            '<span class="tcard-caret">&#9662;</span></button>'
        )
        out.append(f'<div class="tcard-body" id="{sid}">')
        out.append('<div class="tchips">')
        if groups:
            out.append(
                f'<a class="tchip tchip-all" href="archive-index.html">'
                f'&#128218; All archive pages <b>{count}</b></a>'
            )
            for g in groups:
                out.append(
                    f'<a class="tchip" href="{g["href"]}">{esc(g["title"])} '
                    f'<b>{len(g["pages"])}</b></a>'
                )
        else:
            for p in sec["pages"]:
                out.append(f'<a class="tchip" href="{p["slug"]}.html">{esc(p["nav"])}</a>')
        out.append("</div>")
        out.append("</div></div>")
    out.append("</div>")
    out.append(TOPIC_TOGGLE_SCRIPT)
    return "\n".join(out)


TOPIC_TOGGLE_SCRIPT = """<script>
(function(){
  document.querySelectorAll('.tcard-head').forEach(function(btn){
    btn.addEventListener('click', function(){
      var card = btn.closest('.tcard');
      var open = card.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
})();
</script>"""


def render_archive_pages(groups: list[dict], sections: list[dict]) -> None:
    def shell(slug: str, title: str, main: str) -> None:
        doc = page_document(
            meta_title=title,
            description=f"Browse the java2s.com archive restored on JavaSchool: {title}.",
            sidebar_html=build_sidebar(sections, active_slug=slug),
            main_html=main,
            is_home=False,
            body_class="page-archive",
        )
        (OUT_DIR / f"{slug}.html").write_text(doc, encoding="utf-8")

    total = sum(len(g["pages"]) for g in groups)
    cards = "\n".join(
        f'<a class="arc-card" href="{g["href"]}"><span class="arc-card-name">{esc(g["title"])}</span>'
        f'<span class="arc-card-count">{len(g["pages"])} pages</span></a>'
        for g in groups
    )
    shell(
        "archive-index",
        "Imported java2s Archive - All Categories",
        (
            f'    {build_crumb(("Java HOME", "index.html"), (IMPORTED_SECTION, None))}\n'
            f'    <h1>Imported java2s Archive</h1>\n'
            f'    <p>Every page restored from the Internet Archive\'s snapshots of the now-dead '
            f'<strong>java2s.com</strong> &mdash; <strong>{total} pages</strong> across {len(groups)} categories. '
            f'Pick a category below, or use the search box at the top of the page (it searches all '
            f'{total} archive pages plus the whole tutorial).</p>\n'
            f'    <div class="arc-filter-wrap"><input type="text" id="arcFilter" class="arc-filter" '
            f'placeholder="Filter categories..." autocomplete="off"></div>\n'
            f'    <div class="arc-cards" id="arcCards">\n{cards}\n    </div>\n'
            + ARC_FILTER_SCRIPT
        ),
    )
    for g in groups:
        items = "\n".join(
            f'      <li><a href="{p["slug"]}.html">{esc(p["nav"])}</a></li>' for p in g["pages"]
        )
        shell(
            g["slug"],
            f"Archive: {g['title']}",
            (
                f'    {build_crumb(("Java HOME", "index.html"), (IMPORTED_SECTION, "archive-index.html"), (g["title"], None))}\n'
                f'    <h1>{esc(g["title"])}</h1>\n'
                f'    <p class="arc-crumb"><a href="archive-index.html">&larr; All archive categories</a></p>\n'
                f'    <p><strong>{len(g["pages"])} pages</strong> restored from java2s.com. '
                f'Use the filter box to narrow the list.</p>\n'
                f'    <div class="arc-filter-wrap"><input type="text" id="arcFilter" class="arc-filter" '
                f'placeholder="Filter {esc(g["title"])}..." autocomplete="off"></div>\n'
                f'    <ul class="arc-list" id="arcList">\n{items}\n    </ul>\n'
                + ARC_FILTER_SCRIPT
            ),
        )


ARC_FILTER_SCRIPT = """    <script>
(function(){
  var inp = document.getElementById('arcFilter');
  if (!inp) return;
  var items = Array.prototype.slice.call(document.querySelectorAll('#arcCards .arc-card, #arcList li'));
  inp.addEventListener('input', function(){
    var q = inp.value.toLowerCase().trim();
    items.forEach(function(el){
      var hit = !q || (el.textContent || '').toLowerCase().indexOf(q) !== -1;
      el.style.display = hit ? '' : 'none';
    });
  });
})();
</script>"""


def main() -> int:
    sections, flat = load_pages()
    archive_groups = attach_archive_groups(sections)

    home_path = CONTENT_DIR / "home.md"
    if not home_path.exists():
        print("ERROR: content/home.md is missing.", file=sys.stderr)
        return 1

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    (OUT_DIR / "assets").mkdir(parents=True)

    # assets
    for name in ("style.css", "script.js", "favicon.svg"):
        src = ASSETS_DIR / name
        if src.exists():
            shutil.copy2(src, OUT_DIR / "assets" / name)

    # search index (as JS so it also works over file://)
    index = [
        {
            "t": p["title"],
            "s": p["section"],
            "u": p["slug"] + ".html",
            "d": p["description"],
        }
        for p in flat
    ]
    index_js = "window.JSCHOOL_INDEX=" + json.dumps(index, ensure_ascii=False) + ";\n"
    (OUT_DIR / "assets" / "search-index.js").write_text(index_js, encoding="utf-8")

    # home
    (OUT_DIR / "index.html").write_text(
        render_home(home_path, sections, flat), encoding="utf-8"
    )

    # pages
    slug_to_group = {}
    for g in archive_groups:
        for p in g["pages"]:
            slug_to_group[p["slug"]] = g

    for idx, page in enumerate(flat):
        body_html, headings = convert_markdown(page["body_md"])
        sidebar = build_sidebar(sections, active_slug=page["slug"])
        if page["layout"] == "home":
            inner = body_html
        else:
            grp = slug_to_group.get(page["slug"])
            if grp:
                crumb = build_crumb(
                    ("Java HOME", "index.html"),
                    (IMPORTED_SECTION, "archive-index.html"),
                    (grp["title"], grp["href"]),
                )
            else:
                crumb = build_crumb(("Java HOME", "index.html"), (page["section"], None))
            inner = f'    {crumb}\n    <h1>{esc(page["title"])}</h1>\n{body_html}'
        main = f"{inner}\n    {build_pager(flat, idx)}"
        doc = page_document(
            meta_title=page["title"],
            description=page["description"],
            sidebar_html=sidebar,
            main_html=main,
            is_home=False,
            body_class=f"page-{page['slug']}",
        )
        (OUT_DIR / f"{page['slug']}.html").write_text(doc, encoding="utf-8")

    # archive category pages (compact sidebar)
    if archive_groups:
        render_archive_pages(archive_groups, sections)

    # 404
    not_found = page_document(
        meta_title="Page Not Found",
        description="The page you were looking for does not exist.",
        sidebar_html="",
        main_html=(
            f'    {build_crumb(("Java HOME", "index.html"), ("Page not found", None))}\n'
            '    <div class="nf-box"><div class="nf-code">404</div>'
            "<h1>Page not found</h1>"
            "<p>The tutorial page you are looking for does not exist or has moved.</p>"
            '<p><a class="btn btn-green" href="index.html">Go to Java HOME</a></p></div>'
        ),
        is_home=False,
        body_class="page-404",
    )
    (OUT_DIR / "404.html").write_text(not_found, encoding="utf-8")

    # GitHub Pages: don't run Jekyll
    (OUT_DIR / ".nojekyll").write_text("", encoding="utf-8")

    print(f"Built {len(flat)} pages + home + 404 -> {OUT_DIR}")
    for sec in sections:
        print(f"  [{sec['title']}] {len(sec['pages'])} pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
