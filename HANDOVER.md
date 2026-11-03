# Handover — site complete

*Last updated after completing **all seven units, the glossary, exam technique and both mock exams**, plus a final coverage audit. There is no "next unit"; future work is maintenance.*

## Read these first (in order)

1. `CLAUDE.md` — project rules and commands.
2. `planning/STRUCTURE.md` — page template, admonition and quiz markup.
3. `planning/QUESTION_STYLE.md` — exam format (UI style: a/b/c parts, ~20 marks, scenario part c).
4. `planning/CONTENT_MAP.md` — coverage checklist (every row ticked).
5. `planning/ERRATA.md` — 36 known PDF errors and how the site handles each.

## What is done

| Page | Source pages | Highlights |
|---|---|---|
| `docs/index.md` | 2–3 | General introduction, course map, unit table, how-to-use, links to exam pages and glossary |
| `docs/unit-1-ict.md` | 6–23 | 4 SVGs, 13 MCQs, 3 exam questions |
| `docs/unit-2-applications.md` | 24–30 | 2 SVGs, 14 MCQs, 3 exam questions |
| `docs/unit-3-design-reality-gap.md` | 31–38 | 3 SVGs (framework + drawing steps, Colombia chart, score bands), scoring drills, 3 exam questions |
| `docs/unit-4-development-informatics.md` | 39–54 | 3 SVGs, 16 MCQs, number table, 3 exam questions |
| `docs/unit-5-design-methodologies.md` | 55–68 | 2 SVGs (waterfall vs agile, diverge/converge), 15 MCQs, 3 exam questions incl. PD and post-colonial computing |
| `docs/unit-6-technologies.md` | 69–89 | 4 SVGs (e-Health domains = Fig 6.1, e-gov types, GIS layers, raster/vector), 16 MCQs, **4** exam questions |
| `docs/unit-7-standards-theory.md` | 90–116 | 3 SVGs (Moses bridge, macro/meso/micro, UCD framework), 16 MCQs, **4** exam questions |
| `docs/glossary.md` | — | 116 terms, **generated** by `planning/scripts/build_glossary.py` from each unit's Key terms |
| `docs/exam/crash-course.md` | — | One-page cheatsheet: 5 big ideas, practical frameworks toolkit (DRG, big data, PD, e-Health, e-Gov, IIs/GIS/archiving, standards, artifacts & politics, tech transfer/INGOs/UCD, Unit 1 lists), unit cards, 19 traps, confusable-pairs table, 6 answer outlines, 6 quick sketches, 32 flashcards. Essentials visible; explanations in collapsed `???` boxes. Summarises the unit pages, so update it if a unit fact changes |
| `docs/exam/exam-technique.md` | — | Paper format, timing, command words, I-A-J-A scenario method, diagram list, count-mismatch table, high-yield lists, revision plan |
| `docs/exam/mock-exam-1.md`, `mock-exam-2.md` | — | 6 questions each (20 marks), mixing units, full model answers with marking points |

**Final audit** (`planning/scripts/audit.py`): 130 anchored links valid; every PDF section number present; every collapsible renders. Numbers the script still lists as "not found" were checked by hand: they are reference URLs, ISBNs, fetch dates and page footers, not content. One real gap (Unit 1's "more than 90 countries" summary sentence) was found and added.

## Maintaining the site

- **Hosting:** git repo on `main`; `.github/workflows/deploy.yml` deploys to GitHub Pages on every push. One-time setup: create the GitHub repo, `git remote add origin <url>`, `git push -u origin main`, then in the repo **Settings → Pages → Source: GitHub Actions**. The PDF and past-question photos are git-ignored on purpose.

- **Edit a unit:** keep the template order; then `.venv/bin/mkdocs build --strict`, then `python3 planning/scripts/audit.py`.
- **Change a unit's Key terms:** rerun `python3 planning/scripts/build_glossary.py` (the glossary is generated; never hand-edit it).
- **Add an exam question:** follow QUESTION_STYLE.md; check marks sum to ~20; put a sentence between a bullet list and a numbered list (see lessons below).
- **Change a fact in a unit:** check whether `docs/exam/crash-course.md` repeats it and update it there too.
- **Found a new PDF error:** add a `!!! warning "Courseware note"` on the page and a row in `planning/ERRATA.md`.
- Possible extras if the student asks: a third mock paper; printable PDF export; per-unit flashcards from the glossary.

## Workflow used per unit (for reference)

1. Read the PDF text: `pdftotext -f <first> -l <last> "CSC 584-ICT for Development.pdf" - | sed '/^\s*$/d'` (printed page number = PDF page number). Read figure pages as images with the Read tool and `pages`.
2. Write the page following the template (At a glance + mind map → Learning outcomes → Introduction → numbered sections → Key terms → Unit summary → Quick-check MCQs → Self-test with model answers → Practice exercises → Sample exam questions).
3. SVGs: hand-write into `docs/assets/diagrams/u<N>-<name>.svg` (light palette, `font-family="Inter, Arial, sans-serif"`), embed with `![alt](assets/diagrams/x.svg){ .diagram }` + `<p class="caption">…</p>`.
4. `.venv/bin/mkdocs build --strict` must pass.
5. Visual check (optional but useful). Chromium needs the sandbox disabled, and an http server in the sandbox is unreachable from it, so screenshot the built file directly:
   ```bash
   SP=<scratchpad dir>
   chromium --headless=new --disable-gpu --no-sandbox --hide-scrollbars --user-data-dir=$SP/chr \
     --window-size=1280,30000 --virtual-time-budget=25000 --screenshot=$SP/page.png \
     "file://$PWD/site/unit-2-applications/index.html"
   magick $SP/page.png -crop 1280x3000 +repage -resize 55% $SP/part_%02d.png   # then view parts
   ```
6. Tick the unit's rows in `planning/CONTENT_MAP.md`; update the Status list in `CLAUDE.md`; update this HANDOVER.md.

## Lessons learned (avoid repeating)

- **Mermaid `flowchart LR` with a big subgraph renders tiny.** Use `direction TB` inside subgraphs, use `flowchart LR` for wide trees (leaves stack vertically), or use a table instead.
- Mermaid `mindmap` and `xychart-beta` work (Material loads a recent Mermaid). Avoid `(`, `)`, `[`, `]` inside mindmap node text (they change node shape).
- Never put your own paraphrase in a `>` blockquote. Blockquotes are reserved for courseware wording.
- Don't invent facts in comparison tables. If the courseware doesn't say it, write "Not stated" or label the column as added explanation (e.g. a "Beyond the notes" box).
- When interpreting (e.g. ranking segments by ease of entry), say so in the caption.
- Model answers end with marking points matching the marks.
- **Mermaid mindmaps with ~10 branches *and* leaves are unreadable** (Unit 2 impacts). Keep big mindmaps to branch names only and put the detail in a table under them.
- The headless Chromium screenshot fails inside the Bash sandbox (`socket() failed: Operation not permitted`); run that one command with the sandbox disabled.
- When the PDF names something without describing it (e.g. Unit 2 POS), say so and explain it in a Beyond-the-notes box.
- Check learning outcomes vs section counts vs self-test counts and flag any mismatch under the outcomes.
- **A bullet list directly followed by a numbered list (blank line between) merges into one list** in Python-Markdown — put a sentence (e.g. "Answer the following:") between them. Also put a blank line between a `**Heading:**` line and a nested list inside a list item, or the list renders before the heading. Check scenario questions in the built HTML.
- The 30000px screenshot cuts off long pages; use `--window-size=1280,60000` for long units, or check the end in the built HTML. Count `<details` in the HTML against `???` in the source to confirm all collapsibles render.
- Mermaid `flowchart TB` with one root and 4+ wordy leaves renders tiny — use `flowchart LR`.
- Before writing, run `pdfimages -list` on the unit's pages: the CONTENT_MAP/ERRATA may be wrong about which figures exist (Unit 4's were all present).
- Nigerian/West African examples are welcome in examples and scenarios, but keep them in Example or Beyond-the-notes boxes.

## Student preferences (from the conversation)

- Essay exam, UI format (see `pq1.jpg`, `pq2.jpg`). Questions should be **a bit challenging**: application, justification, scenarios (e.g. rate a project on the Design–Reality Gap scale, choose and justify a methodology).
- MCQs are for pointing out key facts, not a practice test.
- Reveal-style answers on the same page.
- Extras are fine if clearly labelled and only there to explain the material.
- Keep `CLAUDE.md` up to date.
