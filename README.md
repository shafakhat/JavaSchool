# JavaSchool — a W3Schools-style Java tutorial site

A complete, self-contained static website, deployed on GitHub Pages:
**https://shafakhat.github.io/JavaSchool/**

Zero runtime dependencies — plain HTML/CSS/JS, no build step needed to deploy.

## The four sections

The site stores exactly four sections (plus the home page); everything is reachable from them:

| Section | What is inside | Pages |
|---|---|---|
| **Java Tutorial** | 65 written lessons + the java2s tutorial restored chapter by chapter (39 chapters, each topic on **one page with sub-topics as tabs**) | 39 chapter pages |
| **Certifications** | OCA/OCP practice bank, OCA Java SE 8 modules, exam papers, SCJP tutorial, 3 original 50-question OCJP tests | 4 hubs + ~180 pages |
| **Interview Questions** | 8 cross-linked banks (Core Java & JVM, Collections, Threads, Strings, Java 8–21, JDBC, Web, Coding) + 115-question master list + quiz | 11 pages |
| **Java Examples** | the archived example library, grouped into categories with filter boxes | 38 categories |

Coverage is complete for the archive window **2014–2020** (106,158 URLs inventoried from the
Wayback Machine); pages continue to be imported in the background — see *Importing* below.

## Design rules

* Colours are used for **backgrounds only** — SeaGreen `#2E8B57`, Grey `#404040`,
  AccentBlue `#2F6FED`, LemonYellow `#FFF44F` (top bar, page-title bands, cards, tabs,
  chips, callouts, footer, code panels).
* Text is always **white or near-black grey** — no coloured type anywhere.
* Every page carries a **Home link at the top**; the sidebar holds HOME + the four sections
  only; the home page is four expandable topic cards.
* java2s boilerplate, nav chains, copyright lines and in-code URL branding are stripped.
* Footer on every page: auto-updating year (`@Year` via JavaScript) + attribution
  **Shafakhatullah Khan Mohammed**.

## Layout

```
/                 site root (this is what GitHub Pages serves)
  index.html                    home: hero + 4 topic cards
  java-tutorial.html            Java Tutorial hub (39 chapters)
  tutorial-01-*.html …          one page per topic, sub-topics as tabs
  certification.html            Certifications hub
  oca-questions.html            OCA/OCP practice bank (filterable)
  oca-exams.html                OCA Java SE 8 modules + exam papers
  scjp.html                     SCJP tutorial
  ocjp-practice*.html           3 original scored practice tests
  interview*.html               interview banks + master list
  quiz.html                     interactive quiz
  archive-index.html            Java Examples categories
  assets/                       style.css, script.js, search-index.js, favicon.svg
  .nojekyll                     (keeps GitHub Pages from running Jekyll)
build.py                        site generator (reads content/ → writes docs/)
tools/                          archive importer + data (see below)
content/                        written lessons + imported archive pages (markdown)
source-assets/                  copy of the source assets
```

## Building

```bash
python3 tools/clean_imported.py    # strip boilerplate, deduplicate imported pages
python3 build.py                   # -> docs/  (then copy docs/ to the repo root)
```

`build.py` wipes `docs/` and regenerates everything, so `docs/` is always in sync with
`content/`. To preview locally:

```bash
python3 -m http.server 8000 --directory docs
```

## Importing more of the archive (resumable)

```bash
# 1. discover every URL in the 2014-2020 window (writes tools/data/cdx_inventory.txt)
python3 tools/cdx_inventory.py --from 2014 --to 2020

# 2. fetch pages (manifest-resumable; a shard file is just a list of URLs)
JAVA2S_MANIFEST=tools/shard0.csv python3 tools/wayback_fetch.py \
    --urls-file tools/data/shards/shard0.txt --stamp 2016 --retries 3 --delay 0.2 --overwrite
```

`tools/wayback_fetch.py` pins the 2016 snapshot, retries with an https→http fallback,
keeps a manifest for resume, and writes one clean markdown page per archived URL into
`content/imported/`. Failed URLs are recorded with a `-` slug — delete those rows to retry.

`tools/data/` holds the crawl state: `catalog_tree.json` (39 chapters / 1,410 sub-topics),
`scjp_tree.json`, `chapter_counts.json` (real archived page counts per chapter),
`cdx_inventory.txt` (106,158 URLs), `shards/*.txt` (3,000-URL batches) and `remaining.txt`.

## Deploying

The repository root **is** the site (Pages → branch `main`, folder `/root`).
To redeploy after a rebuild, replace the root HTML/`assets/` with the new `docs/` output
and push. `.nojekyll` must stay at the root.
