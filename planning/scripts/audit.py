"""Site audits. Run from the project root AFTER `.venv/bin/mkdocs build --strict`:

    python3 planning/scripts/audit.py

1. Every relative link with a #fragment points at an id that exists in the built site.
2. Every number in each unit's PDF pages appears on that unit's page
   (reports leftovers; most are reference URLs/ISBNs/page footers — check them by hand).
3. Every numbered PDF section heading (e.g. 6.3.4) appears as a heading or § reference.
4. Collapsible count in source (???) equals <details> count in the built HTML.
"""
import pathlib
import re
import subprocess

PDF = "CSC 584-ICT for Development.pdf"
UNITS = [
    (1, 6, 23, "unit-1-ict.md"),
    (2, 24, 30, "unit-2-applications.md"),
    (3, 31, 38, "unit-3-design-reality-gap.md"),
    (4, 39, 54, "unit-4-development-informatics.md"),
    (5, 55, 68, "unit-5-design-methodologies.md"),
    (6, 69, 89, "unit-6-technologies.md"),
    (7, 90, 116, "unit-7-standards-theory.md"),
]
DOCS, SITE = pathlib.Path("docs"), pathlib.Path("site")


def built_page(md):
    rel = md.resolve().relative_to(DOCS.resolve())
    if rel.name == "index.md":
        return SITE / rel.with_suffix(".html")
    return SITE / str(rel)[:-3] / "index.html"


def pdf_text(first, last):
    out = subprocess.run(["pdftotext", "-f", str(first), "-l", str(last), PDF, "-"],
                         capture_output=True, text=True).stdout
    return "\n".join(l for l in out.split("\n") if not re.fullmatch(r"\s*\d{1,3}\s*", l))


# 1. anchors
bad = n = 0
for md in DOCS.rglob("*.md"):
    for target, frag in re.findall(r"\]\(([^)\s]+?\.md)#([^)\s]+)\)", md.read_text()):
        n += 1
        if f'id="{frag}"' not in built_page(md.parent / target).read_text():
            bad += 1
            print("MISSING ANCHOR", md, target, frag)
print(f"[anchors] {n} checked, {bad} missing")

for u, a, b, f in UNITS:
    text, page = pdf_text(a, b), (DOCS / f).read_text()
    # 2. numbers
    nums = set(re.findall(r"\d[\d,\.]*\d%?|\d%", text))
    flat = page.replace(",", "")
    missing = sorted(x for x in nums if x.replace(",", "").rstrip(".") not in flat)
    # 3. section numbers
    secs = {s for pair in re.findall(rf"^\s*({u}\.\d+(?:\.\d+)?)\.?\s*$|^\s*({u}\.\d+(?:\.\d+)?)\s", text, re.M)
            for s in pair if s}
    miss_secs = sorted(s for s in secs if not re.search(rf"#+ {re.escape(s)}\b|§{re.escape(s)}\b|\*\*{re.escape(s)} ", page))
    # 4. collapsibles
    src = len(re.findall(r"^\s*\?\?\? ", page, re.M))
    html = built_page(DOCS / f).read_text().count("<details")
    print(f"[unit {u}] numbers not found: {missing}; sections not found: {miss_secs}; "
          f"collapsibles {src} source / {html} built")
