#!/usr/bin/env python3
"""Maintenance helper for the toolkit.

    python3 scripts/toolkit.py build   # regenerate the method index in README.md
    python3 scripts/toolkit.py check   # validate methods, links and README (used by CI)

Method metadata is read from each guide in methods/: the H1 title, the first
blockquote (summary) and the Category / Best for rows of the header table.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
METHODS = ROOT / "methods"
README = ROOT / "README.md"
START, END = "<!-- methods:start -->", "<!-- methods:end -->"

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
        "text": text,
        "title": title.group(1).strip() if title else None,
        "summary": summary.group(1).strip() if summary else None,
        "category": category.group(1) if category else None,
        "best_for": best_for.group(1) if best_for else None,
        "headings": headings,
    }


def guides():
    return [parse(p) for p in sorted(METHODS.glob("*.md"))]


def index_table(items):
    rows = ["| Method | Category | In short |", "| --- | --- | --- |"]
    for g in sorted(items, key=lambda g: (g["category"] or "", g["title"] or "")):
        rows.append(f"| [{g['title']}](methods/{g['path'].name}) | {g['category']} | {g['summary']} |")
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
