# Pareto Analysis

> Roughly 80% of the effect often comes from 20% of the causes, so find the few that matter most and start there.

| | |
| --- | --- |
| **Category** | Prioritisation |
| **Time needed** | 30-60 minutes, plus time to gather data |
| **Best for** | Choosing where to focus when there are many problems, causes, or tasks and limited time |

## What it is

Pareto analysis ranks items by how much they contribute to a total and shows where a small number of items account for most of the effect. It is based on the Pareto principle, named after the economist Vilfredo Pareto, who observed that about 80% of the land in Italy was owned by about 20% of the people. Joseph Juran later applied the idea to quality problems and called it "the vital few and the useful many".

The 80/20 split is a pattern, not a law. In some cases it is 70/30 or 90/10. What matters is that the contribution is usually very uneven.

## Why it works

Effort is limited, but problems are many and rarely equal. If you spread effort evenly, most of it goes to items that barely change the outcome. Ranking by contribution shows where a given effort pays off most.

## When to use

- Many causes or complaints compete for attention
- You have data or can collect counts or costs
- You need to justify focusing on a few items
- You want to check whether a long list can be shortened

## When not to use

- You have no data and cannot get any
- Items are close to equal in size
- The biggest contributor is not the one that matters most (for example, a rare but dangerous issue); weigh severity too

## How to apply

1. **Define what you are measuring.** Count, cost, time, or complaints, and for which period.
2. **List the categories** of causes or problems. Group similar items.
3. **Collect the data.** Use records where possible; otherwise a short tally sheet.
4. **Total each category** and sort them from largest to smallest.
5. **Calculate each share and the running total** as a percentage of the grand total.
6. **Draw the chart.** Bars show each category in descending order, and a line shows the cumulative percentage.
7. **Find the cut.** Identify the categories that account for roughly 70-80% of the total.
8. **Act on those first.** Re-measure afterwards, since the ranking will shift.

## Example: customer support tickets

A support team received 500 tickets last month.

| Category | Tickets | Share | Cumulative |
| --- | --- | --- | --- |
| Password reset | 180 | 36% | 36% |
| Billing errors | 120 | 24% | 60% |
| Login failures | 70 | 14% | 74% |
| Slow app | 50 | 10% | 84% |
| Feature questions | 40 | 8% | 92% |
| Other (6 types) | 40 | 8% | 100% |

**Reading it:** Three categories out of nine produce 74% of the tickets. Password reset alone is more than a third.

**Actions:** Add self-service password reset, fix the billing export that causes errors, and review the login flow. Re-count next month.

## Variations

- **Weight by cost or severity.** Rank by money lost, not by count, if a few rare items are costly.
- **Break down the top item.** Run another Pareto inside the largest category.
- **Before and after.** Chart the same categories after an improvement to confirm it worked.

## Pitfalls

- **Using bad data.** Inconsistent categories or guesses give misleading results.
- **Too many "other".** If "other" is large, the categories are too coarse.
- **Ignoring severity.** A rare but critical issue may deserve attention regardless of rank.
- **Assuming exactly 80/20.** The shape matters more than the numbers.
- **Doing it once.** Re-run after changes; the biggest item shifts.
- **Mistaking correlation for cause.** The chart shows where, not why. Use [Fishbone Diagram](../root-cause/fishbone.md) or [Five Whys](../root-cause/five-whys.md) for the cause.

## Quick checklist

- [ ] Measure and period defined
- [ ] Categories consistent and not overlapping
- [ ] Data collected and totalled
- [ ] Sorted with cumulative percentage
- [ ] Vital few identified and severity considered
- [ ] Re-measure planned

## Related

- [Fishbone Diagram](../root-cause/fishbone.md): find the possible causes behind each category
- [Eisenhower Matrix](eisenhower-matrix.md): prioritise tasks by urgency and importance instead of data
