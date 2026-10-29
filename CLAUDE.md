# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Source for the CS-POGIL website (cspogil.org), built with MkDocs + Material theme, plus the `awesome-nav`, `redirects`, and `tags` plugins. Pushing to `main` triggers `.github/workflows/deploy.yml`, which runs `mkdocs gh-deploy --force`. There are no tests or linters; a clean build is the check.

## Commands

```sh
python -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install --pre -r requirements.txt

./serve.sh          # mkdocs serve with MkDocs 2.0 warnings suppressed; http://127.0.0.1:8000/
mkdocs build        # full build into site/; watch the log for hook warnings
```

Run commands from the repo root: the hooks open files via relative paths (`docs/...`, `templates/`).

## Architecture

Most dynamic content is produced by Python hooks in `hooks/`, run in the order listed in `mkdocs.yml` (order matters: `people.py` imports `bib2md.py` via `sys.modules["hooks/bib2md.py"]`).

- **`bib2md.py`** – the core generator. BibTeX is the source of truth for activities and research:
  - **Activity pages** (`docs/activities/<Category>/*.md`) are hand-written Markdown ending in a single ```` ``` bibtex ```` code block. At build time the block is replaced with Abstract/Contents/Metadata sections, and a downloadable `<name>.bib` is generated alongside.
  - **Research pages** are *only* `.bib` files at `docs/research/<year>/<citekey>.bib` (filename must match cite key). Each becomes a generated `.md` page rendered via `templates/research.md`. Tags (SIGCSE, ITiCSE, ASEE, PLoP, Inroads, else entry type) are derived from the raw entry. A `file = {x.pdf}` field links a PDF stored next to the `.bib`.
  - Appends grouped lists (via `templates/listitem.md`) to `activities/index.md` and `research/index.md`.
  - Fields `abstract` and `contents` may contain LaTeX formatting macros, converted by `tex_to_md`.
- **`people.py`** – each `docs/people/*.md` has front matter `names:` (first is primary; others are aliases). Person pages get auto-appended "Classroom Activities" / "Related Research" lists by matching bib authors. It also auto-links every occurrence of any person's name in the body of every page, so don't hand-link people's names.
- **`short.py`** – text shortcuts like `{EngageCSEdu}`, `{The POGIL Project}`, `{{AWP}}`; also strips `<!-- DO NOT EDIT ... -->` comments and inlines `--8<-- "path"` snippets early.
- **`bread.py`** – injects breadcrumbs above the `<h1>` and moves tags into them (or to a `<!-- tags -->` marker). Pages listed in `not_in_nav` can set front matter `parent: <path.md>` to get a nav parent.
- **`home.py`** – makes the header site name link to `/`, including in `404.html`.

Other pieces:
- Navigation is controlled by `.nav.yml` files (awesome-nav), not `mkdocs.yml`. Research is sorted descending by year directory.
- `includes/abbreviations.md` is auto-appended to every page (ACM CS2023 knowledge-area abbreviations used as activity tags, e.g. `SDF`, `AL`).
- `overrides/main.html` holds the announcement banner and GoatCounter analytics.
- `docs/extra.css` is cache-busted via a `?v=` date in `mkdocs.yml`; bump it when changing CSS.
- `archive/` holds retired scripts that are no longer part of the build.
