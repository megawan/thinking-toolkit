#!/usr/bin/env python3
"""Maintenance helper for the toolkit.

    python3 scripts/toolkit.py build   # regenerate the method index in README.md
    python3 scripts/toolkit.py check   # validate methods, links and README (used by CI)

Guides live in methods/<category>/<method>.md. Metadata is read from each guide:
the H1 title, the first blockquote (summary) and the Category / Best for rows of
the header table. Every guide also needs a cheat sheet, a worksheet and a case
study with the same file name in cheatsheets/, worksheets/ and case-studies/.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
METHODS = ROOT / "methods"
README = ROOT / "README.md"
START, END = "<!-- methods:start -->", "<!-- methods:end -->"

# Folder name under methods/ -> the Category shown in the guide and the index.
CATEGORIES = {
    "root-cause": "Root cause analysis",
    "ideation": "Idea generation",
    "decision-making": "Decision making",
    "prioritisation": "Prioritisation",
    "planning": "Planning and goals",
    "strategy-and-risk": "Strategy and risk",
    "mental-models": "Mental models",
    "critical-thinking": "Critical thinking",
    "design-and-product": "Design and product",
    "reflection-and-learning": "Reflection and learning",
}
# Companion folder -> label used in the index.
EXTRAS = {"cheatsheets": "Cheat sheet", "worksheets": "Worksheet", "case-studies": "Case study"}

# A guide must contain a heading starting with each of these.
REQUIRED = ["What it is", "When to use", "How to apply", "Example", "Pitfalls", "Related"]
LINK = re.compile(r"\]\(([^)\s]+)\)")


def parse(path):
    text = path.read_text(encoding="utf-8")
    title = re.search(r"^# (.+)$", text, re.M)
    summary = re.search(r"^> (.+)$", text, re.M)
    row = lambda key: re.search(rf"^\|\s*\*\*{key}\*\*\s*\|\s*(.+?)\s*\|\s*$", text, re.M)
    category, best_for = row("Category"), row("Best for")
    headings = re.findall(r"^## (.+)$", text, re.M)
    return {
        "path": path,
        "slug": path.stem,
        "folder": path.parent.name,
        "text": text,
        "title": title.group(1).strip() if title else None,
        "summary": summary.group(1).strip() if summary else None,
        "category": category.group(1) if category else None,
        "best_for": best_for.group(1) if best_for else None,
        "headings": headings,
    }


def guides():
    return [parse(p) for p in sorted(METHODS.glob("*/*.md"))]


def extra_label(folder, slug, label):
    """Case studies backed by sources are marked as documented in the index."""
    if folder == "case-studies" and "\n## Sources" in (ROOT / folder / f"{slug}.md").read_text(encoding="utf-8"):
        return f"{label} (documented)"
    return label


def index_table(items):
    rows = ["| Method | Category | In short | Extras |", "| --- | --- | --- | --- |"]
    order = list(CATEGORIES)
    key = lambda g: (order.index(g["folder"]) if g["folder"] in order else len(order), g["title"] or "")
    for g in sorted(items, key=key):
        extras = " · ".join(f"[{extra_label(d, g['slug'], label)}]({d}/{g['slug']}.md)" for d, label in EXTRAS.items())
        rows.append(
            f"| [{g['title']}](methods/{g['folder']}/{g['slug']}.md) | {g['category']} | {g['summary']} | {extras} |"
        )
    return "\n".join(rows)


def render_readme(items):
    text = README.read_text(encoding="utf-8")
    block = f"{START}\n{index_table(items)}\n{END}"
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        sys.exit(f"README.md is missing the {START} / {END} markers")
    return pattern.sub(lambda _: block, text)


def problems(items):
    errors = []
    for g in items:
        name = g["path"].relative_to(ROOT)
        for field in ("title", "summary", "category", "best_for"):
            if not g[field]:
                errors.append(f"{name}: missing {field}")
        if g["folder"] not in CATEGORIES:
            errors.append(f"{name}: folder '{g['folder']}' is not a known category (see CATEGORIES)")
        elif g["category"] != CATEGORIES[g["folder"]]:
            errors.append(f"{name}: Category must be '{CATEGORIES[g['folder']]}' to match its folder")
        for folder in EXTRAS:
            companion = ROOT / folder / f"{g['slug']}.md"
            if not companion.exists():
                errors.append(f"{name}: missing {folder}/{g['slug']}.md")
            else:
                text = companion.read_text(encoding="utf-8")
                if f"methods/{g['folder']}/{g['slug']}.md" not in text:
                    errors.append(f"{folder}/{g['slug']}.md: must link back to its guide")
                if folder == "case-studies" and not (
                    "Illustrative scenario" in text or ("\n## Sources" in text and "](http" in text)
                ):
                    errors.append(
                        f"{folder}/{g['slug']}.md: must be labelled 'Illustrative scenario' or list linked '## Sources'"
                    )
        for section in REQUIRED:
            if not any(h.startswith(section) for h in g["headings"]):
                errors.append(f"{name}: missing section '## {section}'")
    for md in ROOT.rglob("*.md"):
        rel = md.relative_to(ROOT)
        if rel.parts[0] in {"templates", ".git", "node_modules"}:
            continue
        for target in LINK.findall(md.read_text(encoding="utf-8")):
            if re.match(r"[a-z]+:", target) or target.startswith("#"):
                continue
            if not (md.parent / target.split("#")[0]).exists():
                errors.append(f"{rel}: broken link '{target}'")
    return errors


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    items = guides()
    if cmd == "build":
        README.write_text(render_readme(items), encoding="utf-8")
        print(f"README.md updated with {len(items)} methods")
    elif cmd == "check":
        errors = problems(items)
        if render_readme(items) != README.read_text(encoding="utf-8"):
            errors.append("README.md index is out of date; run: python3 scripts/toolkit.py build")
        if errors:
            print("\n".join(errors))
            sys.exit(1)
        print(f"OK: {len(items)} methods")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
