# Contributing

New methods are welcome.

## Add a method

1. Copy [templates/method.md](templates/method.md) to `methods/<method-name>.md` (lowercase, hyphenated).
2. Fill in every section. Keep it practical and include a worked example.
3. Run `python3 scripts/toolkit.py build` to add the method to the index in `README.md`. Do not edit that table by hand.
4. Run `python3 scripts/toolkit.py check` to validate your guide.
5. Open a pull request.

## What a guide needs

- An H1 title, a one-line summary as the first `>` quote, and the header table with **Category**, **Time needed** and **Best for**
- Sections: What it is, When to use, How to apply, Example, Pitfalls, Related
- Links to other guides must be relative and point to files that exist

CI runs the same check plus Markdown linting (`npx markdownlint-cli2 "**/*.md"`).

## Pull requests

- One method per pull request is easiest to review
- Use a [Conventional Commits](https://www.conventionalcommits.org/) title, for example `feat: add Pareto analysis`
- Branch names follow `feat/...`, `fix/...`, `docs/...` or `chore/...`
