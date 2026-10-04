# JavaSchool — a W3Schools-style Java tutorial site (static, GitHub Pages ready)

A complete, self-contained static website — **2,393 pages, zero build step required to deploy**:

- **65 original, hand-written pages**: full Java tutorial (basics → OOP → threads → streams →
  collections → JDBC → modern Java), **Advanced Java** (Applets, AWT/Swing, Struts, Spring,
  Hibernate & JPA, EJB), a full **Collections** deep-dive (List, Set, Queue, Map — class by class),
  and an interconnected **Interview & Certification** section:
  - **Interview hub** + **8 cross-linked topic banks**: Core Java & JVM (35), Collections (30),
    Threads & Concurrency (28), Strings (22), Java 8–21 (25), JDBC (20), Web & Frameworks (25),
    Coding & Puzzles (20) → **205 topical Q&A**
  - **Master list**: all **115 core interview questions** on one expandable page
  - **3 OCJP/OCJA practice tests** — 50 questions each (**150 total**), timed scoring + explanations
  - Interactive topic quiz (10 questions)
- **3,103 pages restored from the java2s.com archive** — the dead site's Java content,
  restored page by page (bytecode examples, tutorial chapters, collections, threads, generics,
  servlets/JSP, J2EE/EJB, Spring, Hibernate/JPA, Struts, JDBC, regex, file I/O, networking,
  design patterns, 2D/3D graphics, SWT/JFace, XML, web services, i18n and more) — all reachable from the
  *"Imported - java2s Archive"* card on the home page.
- **W3Schools-style design**: expandable **topic cards on the home page** (links embedded
  inside each card), a minimal sidebar (Java HOME link only), a **Home breadcrumb at the top
  of every page**, fixed top bar with live search + dark mode, green article layout, code boxes with copy buttons, syntax highlighting, prev/next
  pagers, responsive mobile menu, 404 page, expandable interview Q&A accordions.
- Footer on every page: auto-updating year (`@Year` via JavaScript) + attribution
  **Shafakhatullah Khan Mohammed**.
- **Wayback Machine importer** (`tools/wayback_fetch.py`) — resumable, polite crawler used to
  build the archive section; re-run any time to pull more, then `python3 build.py`.
- Zero runtime dependencies: plain HTML/CSS/JS.

**Want the ready-to-push site only?** Use `javaschool-website-static.zip`: its zip root IS the
site root (`index.html`, `assets/`, `.nojekyll`, …). Unzip into a GitHub repo, enable Pages —
no compilation or execution anywhere.

The generated site lives in **`docs/`** — that's the folder you upload / deploy.
Live: **https://shafakhat.github.io/JavaSchool/**

---

## 1. Build (only needed after editing content)

```bash
python3 build.py        # Python 3.8+, no packages required
```

Output: `docs/` (2,393 pages + assets). To preview locally:

```bash
python3 -m http.server 8000 --directory docs
# open http://localhost:8000
```

## 2. Deploy to GitHub Pages (free)

**Option A — repository root (simplest):**

1. Create a new GitHub repository (e.g. `JavaSchool`).
2. Copy the *contents* of `docs/` to the repository root (including `.nojekyll`).
3. Push. In the repo: **Settings → Pages → Source: Deploy from a branch → Branch: `main` / `root`**.
4. Your site is live at `https://<user>.github.io/JavaSchool/`.

**Option B — keep sources + `docs/` folder:**

1. Push the whole project (`build.py`, `content/`, `assets/`, `tools/`, `docs/`) to `main`.
2. **Settings → Pages → Source: Deploy from a branch → Branch: `main` / `/docs`**.
3. Every time you edit content: run `python3 build.py` and commit the regenerated `docs/`.

> All links and assets are **relative**, so the site works at any sub-path
> (`user.github.io/repo/`, a custom domain, or any static host).

**Other free hosts** (drag & drop the `docs/` folder): Netlify Drop, Cloudflare Pages,
GitHub Pages, Vercel, Surge.sh — anything that serves static files.

---

## 3. Collecting java2s.com content from the Internet Archive

`tools/wayback_fetch.py` is a polite, resumable crawler for the Wayback Machine.
It has pulled 2,328 of the site's pages so far. Usage:

```bash
# dry run — list matching archived URLs, download nothing
python3 tools/wayback_fetch.py --list --limit 20 --include /Tutorial/Java/

# import tutorial articles (recommended starting point)
python3 tools/wayback_fetch.py --limit 100 --include /Tutorial/Java/ --exclude 'Catalog'

# Java CODE example pages
python3 tools/wayback_fetch.py --limit 100 --include /Code/Java/

# long collection run (resumable — re-run any time, it skips what it has)
python3 tools/wayback_fetch.py --limit 5000 --include /Tutorial/Java/ --delay 1.5

# one category at a time (recommended — multi-include runs spend the limit on the first)
python3 tools/wayback_fetch.py --limit 100 --include /Code/Java/Collections/ --delay 0.7
```

Imported pages land in `content/imported/` (with front-matter and cleaned HTML), plus
`tools/wayback_manifest.csv` listing every URL fetched, its timestamp and hash.

---

## 4. Project layout

```
java-school/
├── build.py                  # zero-dependency site generator → docs/
├── assets/ (style.css, script.js)   # W3Schools-style theme, search, quizzes
├── content/                  # original tutorial pages (Markdown + front-matter)
│   └── imported/             # 2,328 java2s archive pages (auto-generated)
├── tools/wayback_fetch.py    # Wayback Machine importer
├── docs/                     # THE SITE (upload this)
└── README.md
```

## 5. Site structure (v3)

Four top sections, reachable from the home-page cards and the slim sidebar:

1. **Java Tutorial** - written lessons + the 39 java2s tutorial chapters. Each chapter is ONE page
   per part with its sub-topics as **tabs** (thin pages are merged; huge chapters auto-split).
2. **Certifications** - OCA/OCP practice questions, OCA Java SE 8 modules, exam papers, SCJP and
   the three original OCJP practice tests (50 Q each).
3. **Interview Questions** - 8 cross-linked topic banks (205 Q&A) + 115-question master list.
4. **Java Examples** - the code-example categories.

Colours: SeaGreen `#2E8B57`, Dark Gray `#404040`, AccentBlue `#2F6FED`.
`tools/clean_imported.py` de-duplicates and strips java2s boilerplate before every build.

## 6. Content notes


- **Interview & certification content is original** — the java2s.com archive had no interview
  question bank or exam dumps, so those pages (115 master questions, 205 topic-bank questions,
  150 practice-test questions) were written from scratch for this project.
- **"Imported - java2s Archive"** pages are restored from the Internet Archive's snapshots of
  the now-dead java2s.com. Text/code is reproduced as archived; layout is rebuilt in this
  site's own template, and each page keeps a link back to its snapshot source.
- The three OCJP/OCJA practice tests are original exam-style questions, not leaked dumps.
