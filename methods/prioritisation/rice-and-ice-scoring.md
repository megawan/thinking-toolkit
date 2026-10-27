# RICE and ICE Scoring

> Give each idea a score from its reach, impact, confidence and effort, so a backlog can be ranked on evidence instead of opinion.

| | |
| --- | --- |
| **Category** | Prioritisation |
| **Time needed** | 30-90 minutes for a backlog of 10-20 items |
| **Best for** | Ranking features, experiments or projects when many ideas compete for limited effort |

## What it is

RICE and ICE are scoring models that turn a list of ideas into a ranked one.

**RICE** was popularised by the product team at Intercom. Each item gets a score from four factors:

| Factor | Meaning | Typical scale |
| --- | --- | --- |
| Reach | How many people or events are affected in a period | A real number, such as users per quarter |
| Impact | How much each person is affected | 3 massive, 2 high, 1 medium, 0.5 low, 0.25 minimal |
| Confidence | How sure you are about the estimates | 100% high, 80% medium, 50% low |
| Effort | Total work needed | Person-months or person-weeks |

The formula is: RICE score = (Reach x Impact x Confidence) / Effort.

**ICE** is a lighter version attributed to Sean Ellis, who coined the term "growth hacking". It uses three factors, each scored 1-10: **I**mpact, **C**onfidence and **E**ase. The score is the product (or the average) of the three. It suits quick ranking of experiments.

## Why it works

Without a shared method, the most senior or most persuasive person wins. Scoring forces each idea to be described in the same terms and makes assumptions visible. The confidence factor penalises ideas with little evidence, which rewards finding out before betting. Dividing by effort favours ideas that give a lot for a little.

## When to use

- A long backlog needs ordering
- Stakeholders disagree on priority
- You have rough numbers for reach and effort
- You want a record of why something was prioritised

## When not to use

- You have fewer than a handful of items; just discuss them
- Items are not comparable, such as a legal requirement and a feature; handle musts first with [MoSCoW](moscow.md)
- The estimates would be invented to get a desired result

## How to apply

1. **List the candidate items,** each described clearly.
2. **Choose the model.** RICE if you can estimate reach and effort in numbers; ICE for quick comparison.
3. **Define the scales** before scoring, and write them down.
4. **Score each factor** for each item. Use data where possible. In a group, score alone first, then compare.
5. **Calculate the score** and sort from highest to lowest.
6. **Sanity-check the result.** Does the order feel wrong? Find out why: a bad estimate, a missing factor, or a gut bias.
7. **Check dependencies** and any hard constraints that scores ignore.
8. **Decide the cut-off** and plan the top items.
9. **Revisit** the scores as new data arrives.

## Example 1: RICE for a product backlog

Reach is users per quarter, effort is person-months.

| Item | Reach | Impact | Confidence | Effort | Score |
| --- | --- | --- | --- | --- | --- |
| A: Saved searches | 2,000 | 1 | 80% | 2 | 800 |
| B: Team accounts | 500 | 3 | 50% | 3 | 250 |
| C: Dark mode | 8,000 | 0.5 | 100% | 4 | 1,000 |
| D: Faster signup | 1,000 | 2 | 80% | 1 | 1,600 |

**Ranking:** D (1,600), C (1,000), A (800), B (250).

**Reading it:** Team accounts have the highest impact per user but low confidence and high effort, so they rank last. A cheap test of demand would raise the confidence and might change the order.

## Example 2: ICE for growth experiments

Each factor is scored 1-10, and the score is the product.

| Experiment | Impact | Confidence | Ease | Score |
| --- | --- | --- | --- | --- |
| A: New headline on landing page | 8 | 5 | 6 | 240 |
| B: Email reminder after sign-up | 5 | 8 | 9 | 360 |
| C: Referral programme | 9 | 3 | 4 | 108 |

**Ranking:** B (360), A (240), C (108). Run B first because it is easy and likely to work.

## RICE or ICE?

| Question | RICE | ICE |
| --- | --- | --- |
| Do you have reach data? | Yes | Not needed |
| Time to score | Longer | Fast |
| Detail | Higher | Lower |
| Good for | Product backlogs | Experiments and quick ranking |

## Pitfalls

- **False precision.** A score of 800 versus 780 is a tie.
- **Gaming the numbers.** Adjusting inputs until a favourite wins defeats the purpose.
- **Inconsistent scales.** Define them and use them the same way for all items.
- **Ignoring strategy.** A high score does not mean it fits the goal; add a filter.
- **Letting the score replace judgment.** Use it as input to a decision.
- **Forgetting to update.** Scores age as data changes.

## Quick checklist

- [ ] Items clearly described
- [ ] Model and scales defined before scoring
- [ ] Scores based on data where possible
- [ ] Ranking sanity-checked
- [ ] Dependencies and hard constraints considered
- [ ] Scores revisited when data changes

## Related

- [MoSCoW](moscow.md): set the scope before ranking
- [Impact-Effort Matrix](impact-effort-matrix.md): a visual, quicker version of the same trade-off
- [Decision Matrix](../decision-making/decision-matrix.md): weighted scoring with your own criteria
