# Site Structure and Conventions

## File layout

```
notes_site/
  CLAUDE.md                     # project guide for Claude (kept up to date)
  mkdocs.yml                    # site config + navigation
  requirements.txt              # mkdocs-material
  CSC 584-ICT for Development.pdf   # source courseware (read-only)
  pq1.jpg, pq2.jpg              # sample exam papers (style reference)
  planning/                     # planning docs (not built into the site)
  docs/
    index.md                    # home: course intro (PDF pp.2–3) + how to use the site
    unit-1-ict.md               # Unit 1  Information and Communication Technology
    unit-2-applications.md      # Unit 2  Application of ICTs in the Developmental Agenda
    unit-3-design-reality-gap.md# Unit 3  Design Reality Gap
    unit-4-development-informatics.md # Unit 4 Developmental Informatics
    unit-5-design-methodologies.md    # Unit 5 Design Methodologies
    unit-6-technologies.md      # Unit 6  Technologies Discussed
    unit-7-standards-theory.md  # Unit 7  ICT Standards and Theoretic Concerns
    glossary.md                 # A–Z key terms, each linked to its section
    exam/
      exam-technique.md         # how to write essay answers that earn marks
      mock-exam-1.md            # full paper: 6 questions, attempt any 3, 2 hours
      mock-exam-2.md
    assets/diagrams/*.svg       # custom SVG figures
    javascripts/quiz.js         # interactive MCQ behaviour
    stylesheets/extra.css       # theme tweaks + SVG colour variables
    stylesheets/quiz.css        # quiz styling
```

A very long unit (likely Unit 1 or Unit 6) may be split into sub-pages under a folder, e.g. `docs/unit-6/e-health.md`. Nav in `mkdocs.yml` must be updated if so.

## Navigation (mkdocs.yml)

```
Home
Units
  1. Information & Communication Technology
  2. Applications of ICT
  3. Design–Reality Gap
  4. Development Informatics & Big Data
  5. Design Methodologies
  6. Technologies Discussed
  7. ICT Standards & Theoretic Concerns
Exam Preparation
  Exam technique
  Mock exam 1
  Mock exam 2
Glossary
```

## Unit page template

Every unit page follows this order:

1. **Title** — `# Unit N — <PDF title>`
2. **At a glance** — a short "what this unit is about" paragraph and a Mermaid mind map of the unit.
3. **Learning outcomes** — exactly as in the PDF. Where the PDF has none (Unit 6 partly, Unit 7 intro), write them and flag with a Courseware note.
4. **Introduction** — the PDF's introduction, explained.
5. **Numbered sections** — mirror PDF numbering (`## 1.1 Technologies Included in ICT`, `### 1.14.1 …`). For each:
    - the courseware content (faithful, complete — every list item kept);
    - plain-language explanation, example, analogy;
    - diagram/table where useful;
    - `!!! tip "Exam angle"` when a point is likely to be examined, saying how it could be asked.
6. **Key terms** — definition list of the unit's terms.
7. **Unit summary** — recap after the full content.
8. **Quick-check MCQs** — 8–15 interactive questions.
9. **Self-test assessment (from the courseware)** — the PDF's questions verbatim, each with a model answer.
10. **Practice exercises** — short-answer, compare/contrast, apply-it tasks with reveal answers.
11. **Sample exam questions** — 2–3 full UI-style questions (a/b/c with marks, ~20 marks each) with model answers and marking points.

## Markdown conventions

### Admonitions

| Purpose | Syntax |
|---|---|
| Plain explanation / "in simple terms" | `!!! note "In plain terms"` |
| Example | `!!! example "Example"` |
| Likely exam point | `!!! tip "Exam angle"` |
| Extra material not in the PDF | `!!! info "Beyond the notes"` |
| PDF error or inconsistency | `!!! warning "Courseware note"` |
| Revealed answer | `??? success "Model answer"` (collapsed by default) |

### Interactive MCQ

```html
<div class="quiz" markdown>
<p class="quiz-q">Which statement best describes the relationship between IT and ICT?</p>
<ul class="quiz-options">
  <li>ICT is a subset of IT</li>
  <li data-correct>IT is a subset of ICT</li>
  <li>They are unrelated</li>
  <li>They mean exactly the same thing</li>
</ul>
<div class="quiz-explain" markdown>
IT focuses on managing information technologies (hardware, software, networking) and excludes telecommunications, while ICT includes telecommunications too — so IT is a subset of ICT (§1.2).
</div>
</div>
```

`quiz.js` shuffles nothing (order is authored), marks the clicked option right/wrong, reveals the correct one, and shows `.quiz-explain`. Without JavaScript the explanation is still readable (hidden only by JS).

### Exam question format

```markdown
**Question 1**

**1a.** Explain ... *(6 marks)*

??? success "Model answer"
    ...
    **Marking points:** (1) ... — 2 marks; (2) ... — 2 marks; ...
```

### Diagrams

- Mermaid: fenced ```` ```mermaid ```` blocks (enabled via `pymdownx.superfences` custom fence).
- SVG: saved in `docs/assets/diagrams/`, embedded with `![alt text](assets/diagrams/name.svg){ .diagram }`. SVGs use `currentColor` and CSS-friendly fills that read in both light and dark mode (draw on a light card background that is fixed in `extra.css`, so colours are predictable).
- Every diagram has a caption line in italics: `*Figure 3.2 — Design–Reality Gap framework (redrawn).*` Keep PDF figure numbers where the diagram replaces a PDF figure.
