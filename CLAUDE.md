# CLAUDE.md — CSC 584 (ICT for Development) lecture notes site

Keep this file up to date whenever the structure, conventions, status or commands change.

## What this project is

A MkDocs Material study site built from the courseware `CSC 584-ICT for Development.pdf` (116 pages, 7 units). The student (500L Computer Science, University of Ibadan) wants notes that **cover everything in the PDF** with clear explanations, diagrams, interactive MCQs, practice exercises and essay-style exam questions with reveal answers.

## Key rules

- **Do not over-summarise or skip content.** Every PDF heading, list item, example, statistic and figure must appear (see `planning/CONTENT_MAP.md`). Summaries come after full content, never instead of it.
- Courseware wording first, then a plain explanation. Extras only to explain the material, always in `!!! info "Beyond the notes"`.
- PDF errors → `!!! warning "Courseware note"`; log in `planning/ERRATA.md`.
- Exam questions follow `planning/QUESTION_STYLE.md` (UI format: attempt any 3, a/b/c parts with marks ≈ 20, scenario part requiring justification). Reference papers: `pq1.jpg`, `pq2.jpg`.
- Answers are on the same page in `??? success "Model answer"` collapsibles.
- Diagrams: Mermaid where it fits; custom SVG in `docs/assets/diagrams/` when more control is needed.
- Page template and markup conventions (admonitions, quiz HTML) are in `planning/STRUCTURE.md`.

## Commands

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt   # first time
.venv/bin/mkdocs serve          # live preview at http://127.0.0.1:8000
.venv/bin/mkdocs build --strict # must pass with no warnings
python3 planning/scripts/build_glossary.py   # after changing any unit's Key terms
python3 planning/scripts/audit.py            # after building
pdftotext -f <first> -l <last> "CSC 584-ICT for Development.pdf" -   # read source pages (printed page no. = PDF page no.)
```

## Gotchas

- Mermaid: big `flowchart LR` subgraphs render tiny; use `direction TB` in subgraphs or a table. No brackets/parentheses inside mindmap node text.
- Blockquotes (`>`) are only for courseware wording, never paraphrase.
- Headless Chromium for visual checks needs the sandbox disabled and must load `file://…/site/...` (see `HANDOVER.md`).

## Layout

- `HANDOVER.md` — state of work + next steps for a fresh agent.
- `planning/` — PLAN, STRUCTURE, CONTENT_MAP (coverage checklist), QUESTION_STYLE, ERRATA. Not built into the site.
- `planning/scripts/build_glossary.py` — regenerates `docs/glossary.md` from every unit's "Key terms" list (never edit the glossary by hand).
- `planning/scripts/audit.py` — post-build audit: anchors, PDF numbers, section numbers, collapsibles.
- `docs/` — site source: `index.md`, `unit-N-*.md`, `glossary.md`, `exam/`, `assets/diagrams/`, `javascripts/quiz.js`, `stylesheets/`.
- `mkdocs.yml` — theme, extensions, nav.
- `.github/workflows/deploy.yml` — on push to `main`, builds with `--strict` and deploys to GitHub Pages.
- Git: the courseware PDF and `pq1.jpg`/`pq2.jpg` are deliberately **not** committed (`.gitignore`); they stay local.

## Status

See `HANDOVER.md` for the state of work, maintenance steps and lessons learned. Update both files after any change.

- [x] Planning files written
- [x] MkDocs scaffold (config, quiz JS/CSS, home page)
- [x] Unit 1 (`docs/unit-1-ict.md`) — reference unit for depth/style
- [x] Unit 2 (`docs/unit-2-applications.md`)
- [x] Unit 3 (`docs/unit-3-design-reality-gap.md`)
- [x] Unit 4 (`docs/unit-4-development-informatics.md`)
- [x] Unit 5 (`docs/unit-5-design-methodologies.md`)
- [x] Unit 6 (`docs/unit-6-technologies.md`)
- [x] Unit 7 (`docs/unit-7-standards-theory.md`)
- [x] Glossary (generated), exam technique, mock exams 1 & 2
- [x] Crash course cheatsheet (`docs/exam/crash-course.md`) — repeats unit facts, so update it when a unit changes
- [x] Final coverage audit (`planning/scripts/audit.py`)

The site is complete. Future work is maintenance: see "Maintaining the site" in `HANDOVER.md`.
