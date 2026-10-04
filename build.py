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
    "Java Tutorial",
    "Certifications",
    "Interview Questions",
    "Java Examples",
]

# original lesson sections fold into Java Tutorial
ORIGINAL_SECTION_MAP = {
    "Get Started": "Java Tutorial",
    "Java Basics": "Java Tutorial",
    "Object Oriented": "Java Tutorial",
    "Core Java": "Java Tutorial",
    "Collections": "Java Tutorial",
    "Advanced Java": "Java Tutorial",
    "Reference": "Java Tutorial",
    "Interview Prep": "Interview Questions",
    "Interview & Certification": "Interview Questions",
}

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
        section = meta.get("section", "Java Examples")
        orig_section = section
        section = ORIGINAL_SECTION_MAP.get(section, section)
        pages.append(
            {
                "slug": slug,
                "title": title,
                "nav": clean_field(meta.get("nav", "")) or title,
                "description": clean_field(meta.get("description", "")),
                "section": section,
                "orig_section": orig_section,
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

def build_sidebar(sections: list[dict], active_slug: str, active_section: str = "") -> str:
    """Sidebar: HOME + the four top sections."""
    links = [("Java HOME", HOME_NAV["href"], "")]
    for s in sections:
        href = s.get("href") or "#"
        links.append((s["title"], href, s["title"]))
    parts = ['<nav id="sidebar" class="sidebar" aria-label="Tutorial menu">', '<div class="side-section">']
    for label, href, sec in links:
        act = ""
        if sec == "" and not active_slug:
            act = " active"
        elif sec and sec == active_section:
            act = " active"
        icon = '<span class="side-home-icon">&#127968;</span> ' if sec == "" else ""
        parts.append(f'<a class="side-link side-home{" top" if sec else ""}{act}" href="{href}">{icon}{esc(label)}</a>')
    parts += ["</div>", "</nav>"]
    return "\n".join(parts)


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
    sidebar = build_sidebar(sections, active_slug="", active_section="")
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
        if len(sec["pages"]) < 80:
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
    "Java Tutorial": "&#128218;",
    "Certification": "&#127891;",
    "Java Examples": "&#128230;",
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
        if groups:
            count = sum(len(g["pages"]) for g in groups)
        elif sec.get("chips"):
            count = sum(c.get("count") or 0 for c in sec["chips"])
        else:
            count = len(sec["pages"])
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
        if sec.get("chips"):
            for c in sec["chips"]:
                cls = "tchip tchip-all" if c.get("highlight") else "tchip"
                cnt = c.get("count") or 0
                badge = f' <b>{cnt}</b>' if cnt else ""
                out.append(f'<a class="{cls}" href="{c["href"]}">{esc(c["label"])}{badge}</a>')
        elif groups:
            out.append(
                f'<a class="tchip tchip-all" href="archive-index.html">'
                f'&#128218; All Java examples <b>{count}</b></a>'
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
            sidebar_html=build_sidebar(sections, active_slug=slug, active_section="Java Tutorial"),
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
        "Java Examples - All Categories",
        (
            f'    {build_crumb(("Java HOME", "index.html"), ("Java Examples", None))}\n'
            f'    <h1>Java Examples</h1>\n'
            f'    <p>Example pages restored from the java2s.com archive &mdash; <strong>{total} pages</strong> '
            f'across {len(groups)} categories. '
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
                f'    {build_crumb(("Java HOME", "index.html"), ("Java Examples", "archive-index.html"), (g["title"], None))}\n'
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


# --------------------------------------------------------------------------- #
# java2s-style Java Tutorial + Certification structure
# --------------------------------------------------------------------------- #

DATA_DIR = ROOT / "tools" / "data"
TUT_DIR_RE = re.compile(r"/Tutorial/Java/(\d{4}__[^/]+)/")
CERT_LABELS = {
    "ocaq": ("OCA OCP Practice Questions", "oca-questions.html"),
    "ocae": ("OCA Java SE 8 Modules", "oca-exams.html"),
    "ocal": ("OCA OCP Exam Papers 1-15", "oca-exams.html"),
    "scjp": ("SCJP Exam (SUN Certified Java Programmer)", "scjp.html"),
}


def load_json_data(name: str):
    path = DATA_DIR / name
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []


def partition_imported(pages: list[dict]) -> tuple[dict, dict, dict, list]:
    chapters: dict[str, list] = {}
    extra: dict[str, list] = {}
    cert = {"ocaq": [], "ocae": [], "ocal": [], "scjp": []}
    examples: list = []
    for p in pages:
        u = p.get("source") or ""
        ul = u.lower()
        m = TUT_DIR_RE.search(u)
        if m and "/Tutorial/Java/" in u:
            chapters.setdefault(m.group(1), []).append(p)
        elif "oca-ocp-practice-question" in ul:
            cert["ocaq"].append(p)
        elif "/tutorials/java/oca_" in ul:
            cert["ocae"].append(p)
        elif "/ref/java/java-oca-ocp-exam" in ul:
            cert["ocal"].append(p)
        elif "/tutorial/scjp/" in ul:
            cert["scjp"].append(p)
        elif "/tutorials/java/" in ul:
            key = u.split("/Tutorials/Java/", 1)[1].split("/", 1)[0]
            extra.setdefault(key, []).append(p)
        else:
            examples.append(p)
    return chapters, extra, cert, examples


def chapter_slug(idx: int, title: str) -> str:
    return f"tutorial-{idx + 1:02d}-{slugify(title)}"


def extra_group_href(key: str) -> str:
    return "archive-cat-" + slugify("New " + key.replace("_", " "))


def build_chips(section_entries: list[tuple[str, str, int]], all_href: str, all_label: str,
                total: int) -> list[dict]:
    chips = [{"label": all_label, "href": all_href, "count": total, "highlight": True}]
    for label, href, cnt in section_entries:
        chips.append({"label": label, "href": href, "count": cnt, "highlight": False})
    return chips


def render_tutorial_hub(tree: list[dict], chapters: dict, extra: dict, sections: list[dict],
                        chapters_pages_total: int, foundations: list[tuple]) -> None:
    rows = []
    for i, ch in enumerate(tree):
        pages_here = len(chapters.get(ch["dir"], []))
        total = sum(s["count"] for s in ch["subtopics"])
        rows.append(
            f'<a class="tut-chapter" href="tutorial-{i + 1:02d}-{slugify(ch["title"])}.html">'
            f'<span class="tut-num">{i + 1}</span>'
            f'<span class="tut-meta"><span class="tut-title">{esc(ch["title"])}</span>'
            f'<span class="tut-sub">{len(ch["subtopics"])} sub-topics &middot; {total} articles on java2s '
            f'&middot; <b>{pages_here}</b> imported</span></span></a>'
        )
    found_rows = "".join(
        f'<a class="tchip" href="{href}">{esc(label)} <b>{cnt}</b></a>' for label, href, cnt in foundations
    )
    extra_rows = []
    for key in sorted(extra, key=str.lower):
        pages_here = len(extra[key])
        label = key.replace("_", " ")
        extra_rows.append(
            f'<a class="tchip" href="{extra_group_href(key)}.html">{esc(label)} <b>{pages_here}</b></a>'
        )
    main = (
        f'    {build_crumb(("Java HOME", "index.html"), ("Java Tutorial", None))}\n'
        '    <h1>Java Tutorial</h1>\n'
        '    <p>The complete java2s.com Java tutorial, chapter by chapter - same structure as the original '
        f'site ({len(tree)} chapters, {sum(len(c["subtopics"]) for c in tree)} sub-topics, '
        f'{sum(sum(s["count"] for s in c["subtopics"]) for c in tree)} articles), rebuilt in this site\'s style. '
        'Pick a chapter; each chapter page lists its sub-topics and every article imported for it.</p>\n'
        + ('    <h2>Learn Java - written lessons</h2>\n    <div class="tchips">\n'
           + found_rows + '\n    </div>\n' if found_rows else "")
        + '    <h2>The java2s tutorial chapters</h2>\n'
        + '    <div class="tut-grid">\n' + "\n".join(rows) + '\n    </div>\n'
        + ('    <h2>Additional java2s tutorial sections</h2>\n    <div class="tchips">\n'
           + "\n".join(extra_rows) + '\n    </div>\n' if extra_rows else "")
        + f'    <p class="arc-crumb"><b>{chapters_pages_total}</b> tutorial articles imported so far. '
          'New articles keep being added from the archive - use the search box for the full index.</p>\n'
    )
    doc = page_document(
        meta_title="Java Tutorial - All Chapters",
        description="The complete java2s Java tutorial rebuilt chapter by chapter: language, data types, collections, threads, Swing, JDBC, JSP, Spring and more.",
        sidebar_html=build_sidebar(sections, active_slug="java-tutorial", active_section="Java Tutorial"),
        main_html=main,
        is_home=False,
        body_class="page-java-tutorial",
    )
    (OUT_DIR / "java-tutorial.html").write_text(doc, encoding="utf-8")


TAB_SCRIPT = """<script>
(function(){
  document.querySelectorAll('.tabs').forEach(function(box){
    var btns = box.querySelectorAll('.tab-btn');
    btns.forEach(function(b){
      b.addEventListener('click', function(){
        var id = b.getAttribute('data-tab');
        btns.forEach(function(x){ x.classList.remove('active'); x.setAttribute('aria-selected','false'); });
        b.classList.add('active'); b.setAttribute('aria-selected','true');
        box.querySelectorAll('.tab-panel').forEach(function(p){ p.style.display = (p.id === id) ? '' : 'none'; });
      });
    });
  });
})();
</script>"""


def _tokens(s: str) -> set:
    return {w for w in re.findall(r"[a-z0-9]{3,}", s.lower()) if w not in
            {"the", "and", "for", "with", "from", "java", "using", "how", "your", "example"}}


def assign_subtopics(subtopics: list[dict], pages: list[dict]) -> list[tuple]:
    """Return [(subtopic_dict, [pages])] in catalog order + a trailing 'Other examples'."""
    tok = [(_tokens(s["title"]), s) for s in subtopics]
    buckets: dict[int, list] = {i: [] for i in range(len(subtopics))}
    other: list = []
    for pg in sorted(pages, key=lambda x: x["title"].lower()):
        pt = _tokens(pg["title"])
        best, score = None, 0
        for i, (st, _s) in enumerate(tok):
            sc = len(pt & st)
            if sc > score:
                best, score = i, sc
        if best is not None and score >= 1:
            buckets[best].append(pg)
        else:
            other.append(pg)
    groups = [(subtopics[i], buckets[i]) for i in range(len(subtopics)) if buckets[i]]
    if other:
        groups.append(({"num": "", "title": "Other examples", "count": len(other)}, other))
    return groups


def render_chapter_pages(tree: list[dict], i: int, pages_here: list[dict], sections: list[dict],
                         budget: int = 170_000) -> str:
    """One topic page per chapter, sub-topics as tabs; auto-split into parts when huge."""
    ch = tree[i]
    base_slug = f"tutorial-{i + 1:02d}-{slugify(ch['title'])}"
    groups = assign_subtopics(ch["subtopics"], pages_here) if pages_here else []

    # split into parts by raw markdown size
    parts: list[list] = []
    cur: list = []
    size = 0
    for sub, plist in groups:
        chunk = sum(len(p["body_md"]) for p in plist) + 400
        if cur and size + chunk > budget:
            parts.append(cur)
            cur, size = [], 0
        cur.append((sub, plist))
        size += chunk
    if cur:
        parts.append(cur)
    if not parts:
        parts = [[]]

    n = len(parts)
    hub_href = f"{base_slug}.html"
    for pi, part in enumerate(parts):
        slug = base_slug if pi == 0 else f"{base_slug}-{pi + 1}"
        label = ch["title"] if n == 1 else f"{ch['title']} ({pi + 1}/{n})"
        tab_btns, tab_panels = [], []
        for ti, (sub, plist) in enumerate(part):
            tid = f"tab-{ti}"
            active = " active" if ti == 0 else ""
            tab_btns.append(
                f'<button type="button" class="tab-btn{active}" data-tab="{tid}" '
                f'aria-selected="{"true" if ti == 0 else "false"}">{esc(sub["title"])} '
                f'<span class="tab-count">{len(plist)}</span></button>'
            )
            md = []
            for pg in plist:
                md.append(f'### {pg["title"]}\n\n{pg["body_md"]}\n')
            html, _ = convert_markdown("\n".join(md))
            style = "" if ti == 0 else ' style="display:none"'
            tab_panels.append(f'<div class="tab-panel" id="{tid}"{style}>{html}</div>')
        subtotal = sum(len(p) for _s, p in part)
        sub_chips = "".join(
            f'<span class="sub-chip"><span class="sub-num">{esc(s["num"])}</span> {esc(s["title"])} '
            f'<b>{s["count"]}</b></span>' for s in ch["subtopics"]
        )
        pager_links = ""
        if n > 1:
            prev_l = f'<a class="btn btn-outline" href="{base_slug if pi == 0 else (base_slug if pi == 1 else f"{base_slug}-{pi}")}.html">&larr; Previous part</a>' if pi > 0 else ""
            next_l = f'<a class="btn btn-green" href="{base_slug}-{pi + 2}.html">Next part &rarr;</a>' if pi < n - 1 else ""
            pager_links = f'<p class="part-pager">{prev_l} {next_l}</p>'
        main = (
            f'    {build_crumb(("Java HOME", "index.html"), ("Java Tutorial", "java-tutorial.html"), (ch["title"], hub_href))}\n'
            f'    <h1>{i + 1}. {esc(label)}</h1>\n'
            f'    <p><strong>{len(ch["subtopics"])} sub-topics</strong> &middot; '
            f'<strong>{sum(s["count"] for s in ch["subtopics"])} articles</strong> on java2s &middot; '
            f'<strong>{len(pages_here)}</strong> imported here, grouped into tabs below'
            + (f' (part {pi + 1} of {n}, {subtotal} articles)' if n > 1 else "") + '.</p>\n'
            f'    {pager_links}\n'
            '    <div class="tabs">\n      <div class="tab-bar">' + "".join(tab_btns) + '</div>\n      '
            + "\n      ".join(tab_panels) + '\n    </div>\n'
            + TAB_SCRIPT
            + f'\n    <details class="sub-map"><summary>All sub-topics in this chapter ({len(ch["subtopics"])})</summary>'
              f'<div class="sub-chips">{sub_chips}</div></details>\n'
            + f'\n    <p class="arc-crumb"><a href="java-tutorial.html">&larr; All tutorial chapters</a></p>\n'
        )
        doc = page_document(
            meta_title=f'{label} - Java Tutorial',
            description=f'{ch["title"]}: java2s tutorial chapter with tabs per sub-topic, {len(pages_here)} archived articles imported.',
            sidebar_html=build_sidebar(sections, active_slug=slug, active_section="Java Tutorial"),
            main_html=main,
            is_home=False,
            body_class="page-chapter",
        )
        (OUT_DIR / f"{slug}.html").write_text(doc, encoding="utf-8")
    return hub_href


def render_certification(cert: dict, scjp_tree: list[dict], sections: list[dict]) -> None:
    def count(k):
        return len(cert.get(k, []))

    hub_cards = [
        ("oca-questions.html", "OCA / OCP Practice Questions", f'{count("ocaq")} archived question pages, each with a worked answer'),
        ("oca-exams.html", "OCA Java SE 8 + Exam Papers", f'{count("ocae")} OCA SE 8 modules and {count("ocal")} OCA/OCP exam paper indexes'),
        ("scjp.html", "SCJP Exam", f'{count("scjp")} SCJP tutorial articles on the classic exam topics'),
        ("ocjp-practice.html", "Our OCJP Practice Test 1", "50 original exam-style questions, instantly scored"),
        ("ocjp-practice-2.html", "Our Practice Test 2", "Threads, generics, exceptions, streams, memory"),
        ("ocjp-practice-3.html", "Our Practice Test 3", "OOP design, language corners, output puzzles"),
        ("interview.html", "Interview Question Banks", "205 topical Q&A across 8 banks + 115-question master list"),
    ]
    cards = "\n".join(
        f'<a class="arc-card" href="{href}"><span class="arc-card-name">{esc(name)}</span>'
        f'<span class="arc-card-count">{esc(sub)}</span></a>'
        for href, name, sub in hub_cards
    )
    main = (
        f'    {build_crumb(("Java HOME", "index.html"), ("Certification", None))}\n'
        '    <h1>Java Certification</h1>\n'
        '    <p>Everything for OCA (Oracle Certified Associate), OCP and the classic SCJP exam - '
        'restored java2s question banks plus original scored practice tests written for this site.</p>\n'
        f'    <div class="arc-cards">\n{cards}\n    </div>\n'
    )
    doc = page_document(
        meta_title="Java Certification - OCA, OCP, SCJP",
        description="OCA/OCP and SCJP certification material: 3,000+ archived practice questions, OCA Java SE 8 modules, exam papers and original scored practice tests.",
        sidebar_html=build_sidebar(sections, active_slug="certification", active_section="Certifications"),
        main_html=main,
        is_home=False,
        body_class="page-certification",
    )
    (OUT_DIR / "certification.html").write_text(doc, encoding="utf-8")

    # --- OCA questions page (grouped, filterable) ---
    q = sorted(cert.get("ocaq", []), key=lambda p: qnum(p))
    groups_items = []
    cur = None
    buf = []
    for p in q:
        n = qnum(p)
        band = ((n - 1) // 100) * 100 + 1 if n else 0
        if band != cur:
            if cur is not None:
                groups_items.append((cur, buf))
            cur, buf = band, []
        buf.append(p)
    if cur is not None:
        groups_items.append((cur, buf))
    parts = []
    for band, plist in groups_items:
        hi = band + 99 if band else "?"
        parts.append(f'    <h2 id="q{band}">Questions {band}-{hi}</h2>\n    <ul class="arc-list">')
        parts.append("\n".join(f'      <li><a href="{p["slug"]}.html">{esc(p["nav"])}</a></li>' for p in plist))
        parts.append("    </ul>")
    if not parts:
        parts.append('    <p>Question pages are being imported from the archive right now.</p>')
    main = (
        f'    {build_crumb(("Java HOME", "index.html"), ("Certifications", "certification.html"), ("OCA / OCP Practice Questions", None))}\n'
        f'    <h1>OCA / OCP Practice Questions</h1>\n'
        f'    <p><strong>{len(q)}</strong> archived question pages from java2s (the full bank is 3,284 questions). '
        'Each page shows the question with its answer and explanation. More are imported continuously.</p>\n'
        '    <div class="arc-filter-wrap"><input type="text" id="arcFilter" class="arc-filter" '
        'placeholder="Search questions..." autocomplete="off"></div>\n'
        + "\n".join(parts) + "\n"
        + ARC_FILTER_SCRIPT
    )
    doc = page_document(
        meta_title="OCA OCP Practice Questions",
        description="java2s OCA/OCP practice question bank restored from the archive - question, answer and explanation per page.",
        sidebar_html=build_sidebar(sections, active_slug="oca-questions", active_section="Certifications"),
        main_html=main,
        is_home=False,
        body_class="page-oca-questions",
    )
    (OUT_DIR / "oca-questions.html").write_text(doc, encoding="utf-8")

    # --- OCA exam papers page ---
    def ul(pages_):
        return "\n".join(f'      <li><a href="{p["slug"]}.html">{esc(p["nav"])}</a></li>'
                          for p in sorted(pages_, key=lambda x: x["title"].lower()))

    main = (
        f'    {build_crumb(("Java HOME", "index.html"), ("Certifications", "certification.html"), ("OCA Java SE 8 & Exam Papers", None))}\n'
        '    <h1>OCA Java SE 8 Modules &amp; Exam Papers</h1>\n'
        '    <h2>OCA Java SE 8 study modules</h2>\n'
        f'    <ul class="arc-list">\n{ul(cert.get("ocae", [])) or "      <li>Importing...</li>"}\n    </ul>\n'
        '    <h2>OCA OCP exam paper indexes</h2>\n'
        f'    <ul class="arc-list">\n{ul(cert.get("ocal", [])) or "      <li>Importing...</li>"}\n    </ul>\n'
        '    <h2>OCA mock exam question sets</h2>\n'
        '    <ul class="arc-list">\n'
        + ul([p for p in cert.get("ocae", []) if "mock" in (p.get("source") or "").lower()] or cert.get("ocaq", [])[:0])
        + ("\n      <li>Importing...</li>" if not [p for p in cert.get("ocae", []) if "mock" in (p.get("source") or "").lower()] else "")
        + '\n    </ul>\n'
    )
    doc = page_document(
        meta_title="OCA Java SE 8 & Exam Papers",
        description="OCA Java SE 8 modules and OCA/OCP exam paper indexes restored from java2s.",
        sidebar_html=build_sidebar(sections, active_slug="oca-exams", active_section="Certifications"),
        main_html=main,
        is_home=False,
        body_class="page-oca-exams",
    )
    (OUT_DIR / "oca-exams.html").write_text(doc, encoding="utf-8")

    # --- SCJP page ---
    tree_html = []
    for g in scjp_tree:
        subs = g.get("subtopics") or []
        tree_html.append(f'    <h2>{esc(g["title"])}</h2>\n    <div class="tchips">'
                         + "".join(f'<span class="tchip">{esc(s)}</span>' for s in subs) + "</div>")
    main = (
        f'    {build_crumb(("Java HOME", "index.html"), ("Certifications", "certification.html"), ("SCJP", None))}\n'
        '    <h1>SCJP - Sun Certified Java Programmer</h1>\n'
        '    <p>The classic pre-OCA certification. java2s kept a full SCJP tutorial organised in nine topics - '
        'restored below, with every imported article listed under it.</p>\n'
        + "\n".join(tree_html) + "\n"
        f'    <h2>SCJP articles imported ({len(cert.get("scjp", []))})</h2>\n'
        f'    <ul class="arc-list">\n{ul(cert.get("scjp", [])) or "      <li>Importing from the archive...</li>"}\n    </ul>\n'
    )
    doc = page_document(
        meta_title="SCJP - Sun Certified Java Programmer",
        description="SCJP certification tutorial restored from java2s: nine exam topics with archived articles.",
        sidebar_html=build_sidebar(sections, active_slug="scjp", active_section="Certifications"),
        main_html=main,
        is_home=False,
        body_class="page-scjp",
    )
    (OUT_DIR / "scjp.html").write_text(doc, encoding="utf-8")


def qnum(page: dict) -> int:
    m = re.search(r"question-(\d+)", page.get("source") or "")
    return int(m.group(1)) if m else 0


def render_extra_section(key: str, pages_: list[dict], sections: list[dict]) -> None:
    """List page for one of the additional java2s tutorial sections (new structure)."""
    label = key.replace("_", " ")
    items = "\n".join(
        f'      <li><a href="{p["slug"]}.html">{esc(p["nav"])}</a></li>'
        for p in sorted(pages_, key=lambda x: x["title"].lower())
    ) or '      <li class="arc-empty">Importing from the archive...</li>'
    main = (
        f'    {build_crumb(("Java HOME", "index.html"), ("Java Tutorial", "java-tutorial.html"), (label, None))}\n'
        f'    <h1>{esc(label)}</h1>\n'
        f'    <p><strong>{len(pages_)}</strong> pages imported from this java2s tutorial section.</p>\n'
        '    <div class="arc-filter-wrap"><input type="text" id="arcFilter" class="arc-filter" '
        f'placeholder="Filter {esc(label)}..." autocomplete="off"></div>\n'
        f'    <ul class="arc-list" id="arcList">\n{items}\n    </ul>\n'
        + ARC_FILTER_SCRIPT
        + f'\n    <p class="arc-crumb"><a href="java-tutorial.html">&larr; All tutorial chapters</a></p>\n'
    )
    doc = page_document(
        meta_title=f"{label} - Java Tutorial",
        description=f"{label}: java2s tutorial section restored with {len(pages_)} imported pages.",
        sidebar_html=build_sidebar(sections, active_slug=extra_group_href(key), active_section="Java Tutorial"),
        main_html=main,
        is_home=False,
        body_class="page-extra-section",
    )
    (OUT_DIR / f"{extra_group_href(key)}.html").write_text(doc, encoding="utf-8")


def main() -> int:
    sections_all, flat = load_pages()

    # split imported archive pages away from the original sections
    imported = [p for p in flat if p["section"] == IMPORTED_SECTION]
    sections = [s for s in sections_all if s["title"] != IMPORTED_SECTION]

    chapters, extra, cert, examples = partition_imported(imported)
    # relabel imported pages with their new home section (search index + crumbs)
    for v in chapters.values():
        for p in v:
            p["section"] = "Java Tutorial"
    for v in extra.values():
        for p in v:
            p["section"] = "Java Tutorial"
    for k in ("ocaq", "ocae", "ocal", "scjp"):
        for p in cert[k]:
            p["section"] = "Certification"
    for p in examples:
        p["section"] = "Java Examples"
    tree = load_json_data("catalog_tree.json")
    scjp_tree = load_json_data("scjp_tree.json")

    # example groups (Code/Java and friends) get category sub-pages
    example_sec = {"title": "Java Examples", "pages": examples}
    example_groups = attach_archive_groups([example_sec])
    example_groups = example_sec.get("groups", [])

    # ---- crumb routing for imported pages ----
    route: dict[str, list] = {}
    chapters_known = {ch["dir"] for ch in tree}
    for i, ch in enumerate(tree):
        href = chapter_slug(i, ch["title"]) + ".html"
        for p in chapters.get(ch["dir"], []):
            route[p["slug"]] = [("Java Tutorial", "java-tutorial.html"), (ch["title"], href)]
    for d, pages_ in chapters.items():
        if d not in chapters_known:
            for p in pages_:
                route[p["slug"]] = [("Java Tutorial", "java-tutorial.html"), (d.split("__")[-1].replace("-", " "), None)]
    for key, pages_ in extra.items():
        href = extra_group_href(key) + ".html"
        for p in pages_:
            route[p["slug"]] = [("Java Tutorial", "java-tutorial.html"), (key.replace("_", " "), href)]
    for p in cert["ocaq"]:
        route[p["slug"]] = [("Certifications", "certification.html"), ("OCA / OCP Practice Questions", "oca-questions.html")]
    for p in cert["ocae"] + cert["ocal"]:
        route[p["slug"]] = [("Certifications", "certification.html"), ("OCA Java SE 8 & Exam Papers", "oca-exams.html")]
    for p in cert["scjp"]:
        route[p["slug"]] = [("Certifications", "certification.html"), ("SCJP", "scjp.html")]
    for g in example_groups:
        for p in g["pages"]:
            route[p["slug"]] = [("Java Examples", "archive-index.html"), (g["title"], g["href"])]

    # ---- home / sidebar sections (four top sections only) ----
    tut_total = sum(len(v) for v in chapters.values()) + sum(len(v) for v in extra.values())
    foundations = []
    fsec_order = ["Get Started", "Java Basics", "Object Oriented", "Core Java", "Collections",
                  "Advanced Java", "Reference"]
    originals = [p for p in flat if not p.get("source")]
    for name in fsec_order:
        gp = [p for p in originals if p.get("orig_section") == name]
        if gp:
            foundations.append((name, gp[0]["slug"] + ".html", len(gp)))

    chips_tut = [{"label": "Start here - written lessons", "href": "java-tutorial.html",
                  "count": len(originals), "highlight": True}]
    for i, ch in enumerate(tree):
        chips_tut.append({"label": f'{i + 1}. {ch["title"]}',
                          "href": f"tutorial-{i + 1:02d}-{slugify(ch['title'])}.html",
                          "count": len(chapters.get(ch["dir"], [])), "highlight": False})
    for key in sorted(extra, key=str.lower):
        chips_tut.append({"label": key.replace("_", " "), "href": extra_group_href(key) + ".html",
                          "count": len(extra[key]), "highlight": False})
    tut_sec = {"title": "Java Tutorial", "pages": [], "chips": chips_tut, "href": "java-tutorial.html"}

    chips_cert = [
        {"label": "Certifications home", "href": "certification.html", "count": 0, "highlight": True},
        {"label": "OCA / OCP Practice Questions", "href": "oca-questions.html",
         "count": len(cert["ocaq"]), "highlight": False},
        {"label": "OCA Java SE 8 & Exam Papers", "href": "oca-exams.html",
         "count": len(cert["ocae"]) + len(cert["ocal"]), "highlight": False},
        {"label": "SCJP Exam", "href": "scjp.html", "count": len(cert["scjp"]), "highlight": False},
        {"label": "OCJP Practice Test 1 (50 Q)", "href": "ocjp-practice.html", "count": 50, "highlight": False},
        {"label": "OCJP Practice Test 2 (50 Q)", "href": "ocjp-practice-2.html", "count": 50, "highlight": False},
        {"label": "OCJP Practice Test 3 (50 Q)", "href": "ocjp-practice-3.html", "count": 50, "highlight": False},
    ]
    cert_sec = {"title": "Certifications", "pages": [], "chips": chips_cert, "href": "certification.html"}

    interview_slugs = [
        ("Interview Questions home", "interview.html", 0),
        ("Core Java & JVM", "interview-core.html", 35),
        ("Collections", "interview-collections.html", 30),
        ("Threads & Concurrency", "interview-threading.html", 28),
        ("Strings & Immutability", "interview-strings.html", 22),
        ("Java 8-21 Features", "interview-java8.html", 25),
        ("JDBC & Database", "interview-jdbc.html", 20),
        ("Web & Frameworks", "interview-web.html", 25),
        ("Coding & Puzzles", "interview-coding.html", 20),
        ("All 115 questions (master list)", "interview-master.html", 115),
        ("Java Quiz", "quiz.html", 10),
    ]
    chips_int = [{"label": lbl, "href": href, "count": c, "highlight": i == 0}
                 for i, (lbl, href, c) in enumerate(interview_slugs)]
    int_sec = {"title": "Interview Questions", "pages": [], "chips": chips_int, "href": "interview.html"}

    ex_total = sum(len(g["pages"]) for g in example_groups)
    chips_ex = [{"label": "All Java examples", "href": "archive-index.html", "count": ex_total, "highlight": True}]
    for g in example_groups:
        chips_ex.append({"label": g["title"], "href": g["href"], "count": len(g["pages"]), "highlight": False})
    example_sec = {"title": "Java Examples", "pages": [], "chips": chips_ex, "href": "archive-index.html"}

    sections = [tut_sec, cert_sec, int_sec, example_sec]

    home_path = CONTENT_DIR / "home.md"
    if not home_path.exists():
        print("ERROR: content/home.md is missing.", file=sys.stderr)
        return 1

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    (OUT_DIR / "assets").mkdir(parents=True)
    for name in ("style.css", "script.js", "favicon.svg"):
        src = ASSETS_DIR / name
        if src.exists():
            shutil.copy2(src, OUT_DIR / "assets" / name)

    # search index
    index = [{"t": p["title"], "s": p["section"], "u": p["slug"] + ".html", "d": p["description"]}
             for p in flat]
    (OUT_DIR / "assets" / "search-index.js").write_text(
        "window.JSCHOOL_INDEX=" + json.dumps(index, ensure_ascii=False) + ";\n", encoding="utf-8")

    # home
    (OUT_DIR / "index.html").write_text(render_home(home_path, sections, flat), encoding="utf-8")

    # pages
    for idx, page in enumerate(flat):
        body_html, headings = convert_markdown(page["body_md"])
        sidebar = build_sidebar(sections, active_slug=page["slug"], active_section=page["section"])
        if page["layout"] == "home":
            inner = body_html
        else:
            r = route.get(page["slug"])
            if r:
                crumb = build_crumb(("Java HOME", "index.html"), *r)
            elif page["section"] in ("Java Tutorial", "Certification", "Java Examples"):
                crumb = build_crumb(("Java HOME", "index.html"), (page["section"], None))
            else:
                crumb = build_crumb(("Java HOME", "index.html"), (page["section"], None))
            inner = f'    {crumb}\n    <h1>{esc(page["title"])}</h1>\n{body_html}'
        main_html = f"{inner}\n    {build_pager(flat, idx)}"
        doc = page_document(
            meta_title=page["title"],
            description=page["description"],
            sidebar_html=sidebar,
            main_html=main_html,
            is_home=False,
            body_class=f"page-{page['slug']}",
        )
        (OUT_DIR / f"{page['slug']}.html").write_text(doc, encoding="utf-8")

    # generated structure pages
    render_tutorial_hub(tree, chapters, extra, sections, tut_total, foundations)
    for i, ch in enumerate(tree):
        render_chapter_pages(tree, i, chapters.get(ch["dir"], []), sections)
    for key, pages_ in extra.items():
        render_extra_section(key, pages_, sections)
    render_certification(cert, scjp_tree, sections)
    if example_groups:
        render_archive_pages(example_groups, sections)

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
    (OUT_DIR / ".nojekyll").write_text("", encoding="utf-8")

    print(f"Built {len(flat)} pages + home + 404 -> {OUT_DIR}")
    for sec in sections:
        n = len(sec["pages"]) if sec["pages"] else len(sec.get("chips", []))
        print(f"  [{sec['title']}] {n} entries")
    print(f"  [Java Tutorial] {len(tree)} chapters, {tut_total} articles imported")
    print(f"  [Certification] {len(cert['ocaq'])} OCA questions, {len(cert['ocae'])} SE8, "
          f"{len(cert['ocal'])} exam papers, {len(cert['scjp'])} SCJP")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
