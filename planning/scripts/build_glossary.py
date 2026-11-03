"""Regenerate docs/glossary.md from the "## Key terms" definition lists in each unit page.

Run from the project root:  python3 planning/scripts/build_glossary.py
"""
import pathlib
import re

UNITS = [
    (1, "unit-1-ict.md", "Information & Communication Technology"),
    (2, "unit-2-applications.md", "Applications of ICT"),
    (3, "unit-3-design-reality-gap.md", "Design–Reality Gap"),
    (4, "unit-4-development-informatics.md", "Development Informatics & Big Data"),
    (5, "unit-5-design-methodologies.md", "Design Methodologies"),
    (6, "unit-6-technologies.md", "Technologies Discussed"),
    (7, "unit-7-standards-theory.md", "ICT Standards & Theoretic Concerns"),
]

entries = []
for num, fname, _ in UNITS:
    text = pathlib.Path("docs", fname).read_text()
    block = text.split("## Key terms", 1)[1].split("\n---", 1)[0]
    lines = block.strip("\n").split("\n")
    i = 0
    while i < len(lines):
        term = lines[i].strip()
        if term and not term.startswith(":") and i + 1 < len(lines) and lines[i + 1].startswith(":   "):
            definition = lines[i + 1][4:].strip()
            entries.append((term, definition, num, fname))
            i += 2
        else:
            i += 1

def sort_key(e):
    return re.sub(r"[^a-z0-9]", "", e[0].lower())

entries.sort(key=sort_key)

out = [
    "# Glossary",
    "",
    "Every key term from the seven units, A–Z. Each entry links to the unit where it is explained in full; "
    "open the unit's **Key terms** section or use the search box for the detailed section.",
    "",
    "!!! tip \"How to use this page\"",
    "    Cover the definitions and test yourself. Exam answers should *start* with a definition like these, "
    "then explain and give an example. This page is generated from the units' Key terms lists "
    "(`planning/scripts/build_glossary.py`), so it always matches them.",
    "",
]
letter = None
for term, definition, num, fname in entries:
    first = sort_key((term,))[:1].upper() or "#"
    if first.isdigit():
        first = "#"
    if first != letter:
        letter = first
        out += [f"## {letter}", ""]
    out += [term, f":   {definition} — *[Unit {num}]({fname}#key-terms)*", ""]

pathlib.Path("docs/glossary.md").write_text("\n".join(out))
print(f"{len(entries)} terms written")
