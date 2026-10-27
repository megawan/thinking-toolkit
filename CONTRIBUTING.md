# Contributing

New methods are welcome.

## Add a method

1. Pick the category folder under `methods/` (see below) and copy [templates/method.md](templates/method.md) to `methods/<category>/<method-name>.md` (lowercase, hyphenated).
2. Fill in every section. Keep it practical and include a worked example.
3. Add the three companion files, using the same file name:
   - `cheatsheets/<method-name>.md` from [templates/cheatsheet.md](templates/cheatsheet.md)
   - `worksheets/<method-name>.md` from [templates/worksheet.md](templates/worksheet.md)
   - `case-studies/<method-name>.md` from [templates/case-study.md](templates/case-study.md)
4. Add the method to [docs/choose-a-method.md](docs/choose-a-method.md), and to [docs/workflows.md](docs/workflows.md) or [docs/glossary.md](docs/glossary.md) where it fits.
5. Run `python3 scripts/toolkit.py build` to update the index in `README.md`. Do not edit that table by hand.
6. Run `python3 scripts/toolkit.py check` to validate your changes.
7. Open a pull request.

## Categories

| Folder | Category value in the guide |
| --- | --- |
| `root-cause` | Root cause analysis |
| `ideation` | Idea generation |
| `decision-making` | Decision making |
| `prioritisation` | Prioritisation |
| `planning` | Planning and goals |
| `strategy-and-risk` | Strategy and risk |
| `mental-models` | Mental models |
| `critical-thinking` | Critical thinking |
| `design-and-product` | Design and product |
| `reflection-and-learning` | Reflection and learning |

To add a category, create the folder and add it to `CATEGORIES` in `scripts/toolkit.py`.

## What a guide needs

- An H1 title, a one-line summary as the first `>` quote, and the header table with **Category**, **Time needed** and **Best for**
- Sections: What it is, When to use, How to apply, Example, Pitfalls, Related
- Links to other guides must be relative and point to files that exist

## Case studies

Case studies are composite scenarios, marked as illustrative. If you add a real, documented case, name the organisation, cite the source, and keep to what the source says.

## Checks

CI runs `python3 scripts/toolkit.py check` plus Markdown linting (`npx markdownlint-cli2 "**/*.md"`).

## Pull requests

- One method per pull request is easiest to review
- Use a [Conventional Commits](https://www.conventionalcommits.org/) title, for example `feat: add Pareto analysis`
- Branch names follow `feat/...`, `fix/...`, `docs/...` or `chore/...`
