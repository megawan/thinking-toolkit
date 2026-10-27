# Case study: Wrong prices on a website

> Illustrative scenario. It is a composite written to show the method in use, not a report about a real organisation.

Method: [Occam's and Hanlon's Razor](../methods/mental-models/occams-and-hanlons-razor.md)

## Context

An online shop found that some users saw outdated prices after a price update.

## What was done

- Three explanations were listed: a stale cache, a hacker changing prices for some users, a rare regional bug
- The cache needed one assumption (it was not cleared after the update); the hacker explanation needed several; the bug needed two
- The team checked the cache first because it was simplest and cheapest to test

## Outcome

The cache had not been cleared after the update. Clearing it fixed the problem and a step was added to the release checklist.

## Lessons

- The razor decided what to test first, not what was true
- The team stayed ready to test the next explanation
- Hanlon's side of the same habit: a colleague missed from an email thread turned out to be on an outdated mailing list

Companion files: [cheat sheet](../cheatsheets/occams-and-hanlons-razor.md) · [worksheet](../worksheets/occams-and-hanlons-razor.md)
