# Plan — CSC 584 (ICT for Development) Lecture Notes Site

## Goal

Turn the courseware `CSC 584-ICT for Development.pdf` (OGUNTUNDE Toyin, Ph.D; 116 pages, 7 units, ~39,000 words) into a study website that:

1. **Covers everything in the PDF.** Every section, every list item, every example, figure and table. Nothing is summarised away. Summaries are added *after* the full content, never instead of it.
2. **Explains clearly.** Each point is given in the courseware's terms first, then explained in plain language with an example or analogy, so the student can both recognise the examinable wording and understand it.
3. **Is visual.** Diagrams and illustrations wherever a picture helps (Mermaid for flows, mind maps and comparisons; hand-drawn SVG where more layout control is needed).
4. **Prepares for an essay exam.** Sample exam questions in the style of University of Ibadan Computer Science papers (see `QUESTION_STYLE.md`), including scenario questions that require justification, plus interactive MCQs that point out key facts.
5. **Keeps answers on the same page** in click-to-reveal boxes.

## Decisions (agreed with the user)

| Topic | Decision |
|---|---|
| Site technology | **MkDocs + Material theme**. Markdown sources in `docs/`, static site output, search, dark mode. |
| MCQs | Interactive, via a small custom script (`docs/javascripts/quiz.js`). Click an option → green/red + explanation. Purpose is to highlight key facts, not to be a mock test. |
| Essay / exam questions | Reveal-style model answers (`??? success "Model answer"`) directly under each question, with marking points that add up to the marks. |
| Diagrams | Mermaid where it makes sense; custom SVG (in `docs/assets/diagrams/`) when more control is needed. All diagrams are redrawn, not copied from the PDF. |
| Extra material | Allowed only when it helps explain the course material. Always in a clearly labelled `!!! info "Beyond the notes"` box so the student knows what is not from the courseware. |
| PDF errors | Flagged in `!!! warning "Courseware note"` boxes and listed in `ERRATA.md`. The courseware wording is still taught (it is what the examiner set), with the correction alongside. |

## Workflow

1. Planning files in `planning/` (this folder): PLAN, STRUCTURE, CONTENT_MAP, QUESTION_STYLE, ERRATA.
2. Scaffold MkDocs: `mkdocs.yml`, `requirements.txt`, quiz JS/CSS, extra CSS, home page.
3. Write units one at a time, 1 → 7. After each unit, tick its rows in `CONTENT_MAP.md`. Pause after Unit 1 for the student to check depth and style.
4. Glossary, exam technique page, two full mock exams with marking guides.
5. Final coverage audit: every row in `CONTENT_MAP.md` ticked; list counts checked against the PDF.

## Quality bar (checked for every unit)

- Every PDF heading in the unit appears as a heading on the page with the same number (e.g. `1.14.1`).
- Every list in the PDF is reproduced in full, with the same count of items (e.g. 9 developmental characteristics, 10 ICT components, 10 gadgets, 10 impacts, 10 engineering-mindset features, 8 digital-archiving best practices).
- Every named example, statistic, case study, person and organisation in the PDF appears on the page.
- Every PDF self-test question is answered.
- Every figure/table in the PDF has an equivalent (redrawn) diagram or table.
- Explanations do not contradict the courseware; where the courseware is wrong or unclear, a Courseware note says so.
- `mkdocs build --strict` passes with no warnings.

## Verification

- `.venv/bin/mkdocs build --strict` — no broken links or warnings.
- `.venv/bin/mkdocs serve` — check pages render, Mermaid draws, SVGs show in light and dark mode, quizzes respond, collapsibles open.
- Coverage audit against `CONTENT_MAP.md` and `pdftotext` output of the PDF.
