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
    "Java Tutorial",
    "Certification",
    "Tutorials & How-To",
    "Java Examples",
    "Java Articles",
    "Reference",
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


def render_home(home_path: Path, sections: list[dict], flat: list[dict], nav_cards: str = "") -> str:
    raw = home_path.read_text(encoding="utf-8")
    meta, body = parse_front_matter(raw)
    body_html, _ = convert_markdown(body)
    # Expandable topic cards (links live inside the cards).
    body_html = body_html.replace('<div id="topic-cards"></div>', nav_cards)
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
# java2s tutorial tree: chapters -> sub-topics -> articles
# --------------------------------------------------------------------------- #

INDEX_HINT = re.compile(r"/Catalog[^/]*$", re.I)

TREE_DATA = ROOT / "tools" / "data" / "java_tutorial.json"
TREE_MAP_PATH = ROOT / "tools" / "tree_map.json"

SECTION_ICONS = {
    "Get Started": "&#128640;",
    "Java Basics": "&#128216;",
    "Object Oriented": "&#129513;",
    "Core Java": "&#9749;",
    "Collections": "&#128449;",
    "Advanced Java": "&#129514;",
    "Interview & Certification": "&#127919;",
    "Java Tutorial": "&#128218;",
    "Certification": "&#127891;",
    "Tutorials & How-To": "&#128161;",
    "Java Examples": "&#128187;",
    "Java Articles": "&#128240;",
    "Reference": "&#128220;",
}

FILTER_SCRIPT = """<script>
(function(){
  var inp = document.getElementById('arcFilter');
  if (!inp) return;
  var items = Array.prototype.slice.call(document.querySelectorAll('.filterable li'));
  inp.addEventListener('input', function(){
    var q = inp.value.toLowerCase().trim();
    items.forEach(function(el){
      el.style.display = (!q || (el.textContent || '').toLowerCase().indexOf(q) !== -1) ? '' : 'none';
    });
  });
})();
</script>"""


def build_crumb(*parts) -> str:
    seg = []
    for text, href in parts:
        seg.append(f'<a href="{href}">{text}</a>' if href else f"<span>{text}</span>")
    joined = ' <span class="crumb-sep">&rsaquo;</span> '.join(seg)
    return f'<nav class="crumb">&#127968; {joined}</nav>'


def norm_src(url: str) -> str:
    path = urllib.parse.urlparse(url).path.lower()
    return re.sub(r"\.html?$", "", path).rstrip("/")


def load_tree_map() -> dict:
    if not TREE_MAP_PATH.exists():
        return {}
    try:
        raw = json.loads(TREE_MAP_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return {norm_src(k): v for k, v in raw.items()}


def load_tutorial_chapters() -> list:
    if not TREE_DATA.exists():
        return []
    try:
        return json.loads(TREE_DATA.read_text(encoding="utf-8")).get("chapters", [])
    except Exception:
        return []


def classify_imported(pages: list) -> None:
    """Re-home imported pages into java2s-style sections (no flat archive dump)."""
    for p in pages:
        src = p.get("source") or ""
        if not src:
            continue
        path = urllib.parse.urlparse(src).path
        p["tgroup"] = ""
        m = re.search(r"/Tutorial/Java/([^/]+)/", path)
        if m:
            p["section"] = "Java Tutorial"
            p["tgroup"] = m.group(1)
            continue
        if "/Tutorials/Java/" in path:
            seg = path.split("/Tutorials/Java/", 1)[1].split("/")[0]
            p["section"] = "Tutorials & How-To"
            p["tgroup"] = seg
            continue
        if "/ref/java/" in path:
            name = path.rsplit("/", 1)[-1].lower()
            if "oca" in name or "ocp" in name:
                p["section"] = "Certification"
                p["tgroup"] = "OCA_OCP_PRACTICE"
            else:
                p["section"] = "Reference"
                p["tgroup"] = "Java Reference"
            continue
        if "/Tutorial/SCJP" in path or "/Tutorial/OCJP" in path:
            p["section"] = "Certification"
            p["tgroup"] = "SCJP"
            continue
        if "/Code/Java/" in path:
            segs = path.split("/Code/Java/", 1)[1].split("/")
            p["section"] = "Java Examples"
            p["tgroup"] = segs[0] if len(segs) > 1 else "Misc"
            continue
        if "/example/" in path:
            p["section"] = "Java Examples"
            p["tgroup"] = "Utility Methods"
            continue
        if "/Article-Tutorial/Java/" in path:
            segs = path.split("/Article-Tutorial/Java/", 1)[1].split("/")
            p["section"] = "Java Articles"
            p["tgroup"] = segs[0] if len(segs) > 1 else "Misc"
            continue
        p["section"] = "Java Examples"
        p["tgroup"] = "Other"


def pretty_group(name: str) -> str:
    return name.replace("__", " ").replace("_", " ").replace("-", " ").strip()


def article_list_html(items: list, placeholder: str) -> str:
    if not items:
        return f'<p class="arc-note">{esc(placeholder)}</p>'
    lis = "\n".join(
        f'      <li><a href="{p["slug"]}.html">{esc(p["title"])}</a></li>' for p in items
    )
    return (
        '    <div class="arc-filter-wrap"><input type="text" id="arcFilter" class="arc-filter" '
        f'placeholder="Filter {len(items)} pages..." autocomplete="off"></div>\n'
        f'    <ul class="arc-list filterable">\n{lis}\n    </ul>\n' + FILTER_SCRIPT
    )


def tutorial_tree_pages(pages: list, chapters: list, tree_map: dict):
    """Build the java2s-style tree. Returns (out_pages, placement, skip_slugs)."""
    by_src = {}
    for p in pages:
        if p.get("source"):
            by_src[norm_src(p["source"])] = p
    placement = {}
    skip = set()
    chunks = []  # chapter page data

    for ch in chapters:
        num = ch["num"]
        folder = ch["folder"]
        ch_slug = f"tut-{num}-{slugify(ch['title'])}"
        topics = []
        for i, t in enumerate(ch.get("topics", []), 1):
            t_slug = f"tut-{num}-{i}-{slugify(t['title'])}"
            key = norm_src(f"/Tutorial/Java/{folder}/{t['page']}")
            arts = []
            for u in tree_map.get(key, []):
                pg = by_src.get(norm_src(u))
                if pg and not pg.get("is_index"):
                    arts.append(pg)
                    placement[pg["slug"]] = (ch, t, t_slug)
            arts.sort(key=lambda x: x["title"].lower())
            topics.append({"i": i, "title": t["title"], "count": t.get("count", 0),
                           "slug": t_slug, "articles": arts})
        chunks.append({"ch": ch, "slug": ch_slug, "topics": topics})

    # pages that are index/catalog pages of the classic tutorial are not
    # rendered separately - the tree pages replace them
    for p in pages:
        if p["section"] != "Java Tutorial" or not p.get("source"):
            continue
        np_ = norm_src(p["source"])
        if np_ in tree_map or INDEX_HINT.search(np_) or p["slug"] in placement:
            if np_ in tree_map or INDEX_HINT.search(np_):
                skip.add(p["slug"])

    out = []
    # hub: tutorial.html
    rows = []
    for c in chunks:
        n_arts = sum(len(t["articles"]) for t in c["topics"])
        rows.append(
            f'<a class="tut-chapter" href="{c["slug"]}.html">'
            f'<span class="tut-chapter-num">{c["ch"]["num"]}</span>'
            f'<span class="tut-chapter-name">{esc(c["ch"]["title"])}</span>'
            f'<span class="tut-chapter-meta">{len(c["topics"])} topics &middot; '
            f'{c["ch"].get("count", 0)} articles</span></a>'
        )
    out.append(("tutorial", "Java Tutorial - All Chapters",
                build_crumb(("Java HOME", "index.html"), ("Java Tutorial", None))
                + '    <h1>Java Tutorial</h1>\n'
                + '    <p>The complete java2s.com Java tutorial, chapter by chapter &mdash; '
                + f'<strong>{len(chunks)} chapters</strong>, <strong>'
                + f'{sum(len(c["topics"]) for c in chunks)} sub-topics</strong>, '
                + f'<strong>{sum(c["ch"].get("count", 0) for c in chunks)} articles</strong>. '
                + 'Pick a chapter; each chapter lists its sub-topics, and each sub-topic lists its articles.</p>\n'
                + '    <div class="tut-chapters">\n' + "\n".join(rows) + '\n    </div>'))

    for c in chunks:
        ch = c["ch"]
        chips = []
        for t in c["topics"]:
            n = len(t["articles"]) or t["count"]
            chips.append(f'<a class="tchip" href="{t["slug"]}.html">{esc(t["title"])} <b>{n}</b></a>')
        # articles in the chapter that were not matched to a sub-topic
        matched = {a["slug"] for t in c["topics"] for a in t["articles"]}
        loose = [p for p in pages
                 if p["section"] == "Java Tutorial" and p.get("tgroup") == ch["folder"]
                 and p["slug"] not in matched and p["slug"] not in skip]
        loose.sort(key=lambda x: x["title"].lower())
        body = (
            build_crumb(("Java HOME", "index.html"), ("Java Tutorial", "tutorial.html"), (ch["title"], None))
            + f'    <h1>{ch["num"]}. {esc(ch["title"])}</h1>\n'
            + f'    <p><strong>{len(c["topics"])} sub-topics</strong> in this chapter. '
            + 'Choose a sub-topic to see its articles.</p>\n'
            + '    <div class="tchips">\n' + "\n".join(chips) + '\n    </div>\n'
            + ('    <h2>All articles in this chapter</h2>\n' + article_list_html(loose, "Articles are being imported - check back soon.")
               if loose else "")
        )
        out.append((c["slug"], f'{ch["num"]}. {ch["title"]} - Java Tutorial', body))

        for t in c["topics"]:
            t_slug = t["slug"]
            body = (
                build_crumb(("Java HOME", "index.html"), ("Java Tutorial", "tutorial.html"),
                            (ch["title"], c["slug"] + ".html"), (t["title"], None))
                + f'    <h1>{ch["num"]}.{t["i"]} {esc(t["title"])}</h1>\n'
                + f'    <p>{t["count"]} articles in this sub-topic.</p>\n'
                + article_list_html(t["articles"], "These articles are still being imported from the archive - check back soon.")
            )
            out.append((t_slug, f'{t["title"]} - {ch["title"]}', body))
    return out, placement, skip


def build_group_pages(pages: list, placement: dict):
    """Group hub + chunk pages for the non-tutorial sections. Returns (out_pages, nav)."""
    groups = {}
    for p in pages:
        sec = p["section"]
        if sec in ("Java Tutorial",) or not p.get("tgroup"):
            continue
        groups.setdefault((sec, p["tgroup"]), []).append(p)

    out = []
    nav = {}
    CHUNK = 400
    for (sec, grp), items in sorted(groups.items()):
        items = sorted(items, key=lambda p: x_title(p))
        label = pretty_group(grp)
        gslug = "grp-" + slugify(sec + "-" + grp)
        nav.setdefault(sec, []).append({"label": label, "count": len(items), "href": gslug + ".html"})
        if len(items) <= CHUNK:
            body = (build_crumb(("Java HOME", "index.html"), (sec, None), (label, None))
                    + f'    <h1>{esc(label)}</h1>\n'
                    + f'    <p>{len(items)} pages.</p>\n'
                    + article_list_html(items, "Nothing imported here yet."))
            out.append((gslug, f"{label} - {sec}", body))
        else:
            chunk_links = []
            for i in range(0, len(items), CHUNK):
                part = items[i:i + CHUNK]
                cslug = f"{gslug}-p{i // CHUNK + 1}"
                chunk_links.append(f'<a class="tchip" href="{cslug}.html">{i + 1} &ndash; {i + len(part)} <b>{len(part)}</b></a>')
                body = (build_crumb(("Java HOME", "index.html"), (sec, None), (label, gslug + ".html"))
                        + f'    <h1>{esc(label)}</h1>\n'
                        + f'    <p>Pages {i + 1} &ndash; {i + len(part)} of {len(items)}.</p>\n'
                        + article_list_html(part, ""))
                out.append((cslug, f"{label} ({i + 1}-{i + len(part)})", body))
            body = (build_crumb(("Java HOME", "index.html"), (sec, None), (label, None))
                    + f'    <h1>{esc(label)}</h1>\n'
                    + f'    <p>{len(items)} pages, split into {len(chunk_links)} parts.</p>\n'
                    + '    <div class="tchips">\n' + "\n".join(chunk_links) + '\n    </div>')
            out.append((gslug, f"{label} - {sec}", body))
    return out, nav


def x_title(p):
    m = re.match(r"(\d+)", p["slug"])
    return (int(m.group(1)) if m else 999999, p["title"].lower())


def certification_pages(pages: list):
    """OCA/OCP practice bank + SCJP hub."""
    qs = [p for p in pages if p.get("tgroup") == "OCA_OCP_PRACTICE"]
    def qnum(p):
        m = re.search(r"question-(\d+)", p["slug"])
        return int(m.group(1)) if m else 0
    qs.sort(key=qnum)
    out = []
    PER = 250
    parts = []
    for i in range(0, len(qs), PER):
        chunk = qs[i:i + PER]
        cslug = f"cert-oca-practice-{qnum(chunk[0])}-{qnum(chunk[-1])}"
        parts.append((cslug, qnum(chunk[0]), qnum(chunk[-1]), len(chunk)))
        body = (build_crumb(("Java HOME", "index.html"), ("Certification", "certification.html"),
                            (f"Questions {qnum(chunk[0])}-{qnum(chunk[-1])}", None))
                + f'    <h1>OCA/OCP Practice Questions {qnum(chunk[0])}&ndash;{qnum(chunk[-1])}</h1>\n'
                + article_list_html(chunk, ""))
        out.append((cslug, f"OCA/OCP Practice {qnum(chunk[0])}-{qnum(chunk[-1])}", body))
    chips = "\n".join(f'<a class="tchip" href="{c}.html">{a}&ndash;{b} <b>{n}</b></a>' for c, a, b, n in parts)
    modules = sorted({p["tgroup"] for p in pages if p["section"] == "Certification"
                      and p["tgroup"] not in ("OCA_OCP_PRACTICE", "SCJP")})
    mod_chips = "\n".join(
        f'<a class="tchip" href="grp-{slugify("Certification-" + m)}.html">{esc(pretty_group(m))} '
        f'<b>{sum(1 for p in pages if p.get("tgroup") == m)}</b></a>' for m in modules
    )
    scjp = [p for p in pages if p.get("tgroup") == "SCJP"]
    body = (
        build_crumb(("Java HOME", "index.html"), ("Certification", None))
        + '    <h1>Certification / OCA / SCJP</h1>\n'
        + f'    <p>Exam material from java2s: <strong>{len(qs)} OCA/OCP practice questions</strong>, '
        + f'OCA Java SE 8 modules, mock exams and SCJP pages.</p>\n'
        + '    <h2>OCA Java SE 8 study modules</h2>\n    <div class="tchips">\n' + mod_chips + '\n    </div>\n'
        + ('    <h2>SCJP</h2>\n    <div class="tchips">\n'
           f'<a class="tchip" href="grp-certification-scjp.html">SCJP pages <b>{len(scjp)}</b></a>\n    </div>\n' if scjp else "")
        + '    <h2>OCA/OCP practice questions</h2>\n    <div class="tchips">\n' + chips
        + '\n    </div>\n'
    )
    out.insert(0, ("certification", "Certification - OCA / SCJP", body))
    return out


def build_nav_cards(sections: list, flat: list, tut_chunks: list, grp_nav: dict) -> str:
    """Expandable home-page cards: java2s-like sections with links inside."""
    cards = []  # (title, icon, [items], count)

    # 1) the java2s tutorial tree
    is_tutorial = [p for p in flat if p["section"] == "Java Tutorial"]
    items = [{"label": f'{c["ch"]["num"]}. {c["ch"]["title"]}', "href": c["slug"] + ".html",
              "count": c["ch"].get("count", 0)} for c in tut_chunks]
    items.append({"label": "Open the full tutorial index", "href": "tutorial.html",
                  "count": sum(c["ch"].get("count", 0) for c in tut_chunks)})
    cards.append(("Java Tutorial", SECTION_ICONS["Java Tutorial"], items, len(is_tutorial)))

    # 2) certification
    cert_items = [{"label": "Certification home (OCA / SCJP)", "href": "certification.html",
                   "count": sum(1 for p in flat if p["section"] == "Certification")}]
    for it in grp_nav.get("Certification", []):
        if "oca" in it["label"].lower() or "scjp" in it["label"].lower() or "mock" in it["label"].lower():
            cert_items.append(it)
    cards.append(("Certification", SECTION_ICONS["Certification"], cert_items,
                  sum(1 for p in flat if p["section"] == "Certification")))

    # 3) everything else, as chips per group
    for sec in ("Tutorials & How-To", "Java Examples", "Java Articles", "Reference"):
        items = grp_nav.get(sec, [])
        if not items:
            continue
        cards.append((sec, SECTION_ICONS.get(sec, "&#128196;"), items,
                      sum(1 for p in flat if p["section"] == sec)))

    # 4) the original hand-written sections
    for s in sections:
        if s["title"] in ("Java Tutorial", "Certification", "Tutorials & How-To",
                          "Java Examples", "Java Articles", "Reference"):
            continue
        items = [{"label": p["nav"], "href": p["slug"] + ".html", "count": 0} for p in s["pages"]]
        cards.append((s["title"], SECTION_ICONS.get(s["title"], "&#128196;"), items, len(s["pages"])))

    out = ['<div class="topic-cards">']
    for i, (title, icon, items, count) in enumerate(cards):
        sid = "tc-" + slugify(title)
        opened = i == 0
        out.append(f'<div class="tcard{" open" if opened else ""}">')
        out.append(
            f'<button type="button" class="tcard-head" data-target="{sid}" '
            f'aria-expanded="{"true" if opened else "false"}">'
            f'<span class="tcard-icon">{icon}</span>'
            f'<span class="tcard-title">{esc(title)}</span>'
            f'<span class="tcard-count">{count} pages</span>'
            '<span class="tcard-caret">&#9662;</span></button>'
        )
        out.append(f'<div class="tcard-body" id="{sid}">')
        out.append('<div class="tchips">')
        for it in items:
            cnt = f' <b>{it["count"]}</b>' if it.get("count") else ""
            out.append(f'<a class="tchip" href="{it["href"]}">{esc(it["label"])}{cnt}</a>')
        out.append("</div></div></div>")
    out.append("</div>")
    out.append("""<script>
(function(){
  document.querySelectorAll('.tcard-head').forEach(function(btn){
    btn.addEventListener('click', function(){
      var card = btn.closest('.tcard');
      var open = card.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
})();
</script>""")
    return "\n".join(out)


def main() -> int:
    sections, flat = load_pages()
    classify_imported(flat)
    tree_map = load_tree_map()
    chapters = load_tutorial_chapters()

    tree_out, placement, skip_slugs = tutorial_tree_pages(flat, chapters, tree_map)
    grp_out, grp_nav = build_group_pages(flat, placement)
    cert_out = certification_pages(flat)
    keep = [p for p in flat if p["slug"] not in skip_slugs]
    flat = keep

    # regroup sections now that imported pages have their java2s homes
    by_sec: dict = {}
    for p in flat:
        by_sec.setdefault(p["section"], []).append(p)
    sections = [{"title": name, "pages": by_sec[name]} for name in SECTION_ORDER if name in by_sec]
    sections += [{"title": k, "pages": v} for k, v in by_sec.items() if k not in SECTION_ORDER]
    nav_cards = build_nav_cards(sections, flat, [c for c in
        [{"ch": ch, "slug": slug} for (slug, t_, b) in [] ] ] if False else
        [{"ch": ch, "slug": "tut-%s-%s" % (ch["num"], slugify(ch["title"]))} for ch in chapters],
        grp_nav)
    extra_pages = tree_out + grp_out + cert_out

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
        render_home(home_path, sections, flat, nav_cards), encoding="utf-8"
    )

    # pages
    for idx, page in enumerate(flat):
        body_html, headings = convert_markdown(page["body_md"])
        sidebar = build_sidebar(sections, active_slug=page["slug"])
        if page["layout"] == "home":
            inner = body_html
        else:
            plc = placement.get(page["slug"])
            if plc:
                ch, tp, tp_slug = plc
                crumb = build_crumb(
                    ("Java HOME", "index.html"),
                    ("Java Tutorial", "tutorial.html"),
                    (ch["title"], f'tut-{ch["num"]}-{slugify(ch["title"])}.html'),
                    (tp["title"], tp_slug + ".html"),
                )
            elif page["section"] == "Java Tutorial" and page.get("tgroup"):
                ch = next((c for c in chapters if c["folder"] == page["tgroup"]), None)
                if ch:
                    crumb = build_crumb(
                        ("Java HOME", "index.html"),
                        ("Java Tutorial", "tutorial.html"),
                        (ch["title"], f'tut-{ch["num"]}-{slugify(ch["title"])}.html'),
                    )
                else:
                    crumb = build_crumb(("Java HOME", "index.html"), ("Java Tutorial", "tutorial.html"))
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

    # generated tree / group / certification pages
    for slug, meta_title, main_html in extra_pages:
        doc = page_document(
            meta_title=meta_title,
            description=f"{meta_title} - JavaSchool",
            sidebar_html=build_sidebar(sections, active_slug=slug),
            main_html=main_html + "    <p class=\"arc-crumb\"><a href=\"index.html\">&larr; Java HOME</a></p>",
            is_home=False,
            body_class=f"page-{slug}",
        )
        (OUT_DIR / f"{slug}.html").write_text(doc, encoding="utf-8")

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

    print(f"Built {len(flat)} pages + {len(extra_pages)} tree/group pages + home + 404 -> {OUT_DIR}")
    for sec in sections:
        print(f"  [{sec['title']}] {len(sec['pages'])} pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
