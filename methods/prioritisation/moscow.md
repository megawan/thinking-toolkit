# MoSCoW

> Sort requirements into Must, Should, Could and Won't, so everyone agrees what is essential and what can wait.

| | |
| --- | --- |
| **Category** | Prioritisation |
| **Time needed** | 30-90 minutes with the people who own the scope |
| **Best for** | Fixing the scope of a project or release with a fixed deadline or budget |

## What it is

MoSCoW is a prioritisation method that places each requirement in one of four groups. The vowels in the name are only there to make it pronounceable.

| Group | Meaning | Test |
| --- | --- | --- |
| Must have | Essential. Without it the delivery fails or is unusable, illegal or unsafe | Would the release be pointless without it? |
| Should have | Important, but there is a workaround or it can wait for a short time | Painful to leave out, but survivable |
| Could have | Desirable, small impact if left out | Nice to have if time allows |
| Won't have (this time) | Agreed to be out of scope for now | Not forgotten, just not now |

It was created by Dai Clegg at Oracle in 1994 and became part of the DSDM agile project framework.

## Why it works

When everything is "high priority", teams over-commit and then fail late. MoSCoW forces an explicit conversation about what happens if a feature is missing. The "Won't" group gives people a safe place for ideas that are good but not now, which reduces scope creep. Treating Should and Could as flexible gives the team room to deliver on time.

## When to use

- A project or release has a fixed date or budget
- Stakeholders disagree about scope
- A backlog is long and everything is labelled urgent
- You need a simple shared vocabulary for scope

## When not to use

- You need to rank items against each other in detail; use [RICE and ICE Scoring](rice-and-ice-scoring.md)
- There is no fixed boundary; everything could be done eventually
- The audience cannot agree on what "Must" means; fix that first

## How to apply

1. **Set the boundary.** State the goal, the date, and the capacity (people, days, money).
2. **List the candidate requirements,** each as a clear sentence.
3. **Define "Must"** for this project: what makes the delivery fail, illegal or unusable?
4. **Sort each item** into a group. Challenge every Must: what happens if we ship without it?
5. **Estimate effort** for each item.
6. **Check the balance.** Keep the Musts within a safe share of capacity. DSDM guidance suggests about 60% of effort for Musts, leaving the rest as contingency for Shoulds and Coulds.
7. **Record the Won'ts** and why, so they are not reopened without reason.
8. **Agree with stakeholders** and keep the list visible.
9. **Re-check as work proceeds.** If estimates grow, drop Coulds first, then Shoulds. Musts are protected.

## Questions to challenge a "Must"

- What is the consequence if this is missing on launch day?
- Is there a manual workaround?
- Could it follow within a few weeks?
- Is it needed by the law, safety or contract?
- Does it block other Must items?

## Example: first release of a booking app

**Capacity:** 100 person-days before the launch date.

| Group | Item | Effort (days) |
| --- | --- | --- |
| Must | Search and book a time slot | 25 |
| Must | Payment | 20 |
| Must | Confirmation email | 10 |
| Should | Cancel and reschedule | 15 |
| Should | Reminders by SMS | 15 |
| Could | Customer reviews | 15 |
| Could | Dark mode | 10 |
| Won't (this time) | Loyalty points | 20 (not counted) |

**Balance:** Musts total 55 days, or 55% of capacity. Shoulds total 30, Coulds 25. Planned work is 110 days against a capacity of 100, so Coulds will be cut first if estimates grow. The 45 days outside Musts act as a buffer.

**Result:** The team ships on time with the three Musts and cancellation, drops dark mode, and schedules loyalty points for the next release.

## Pitfalls

- **Too many Musts.** If most items are Musts, nothing has been prioritised.
- **Treating Should as "do it anyway".** Plan for them to move.
- **Hiding the Won'ts.** Write them down so people know they were heard.
- **No capacity check.** Without effort estimates the list is a wish list.
- **Different meanings of Must.** Agree on the test.
- **Never revisiting.** Priorities change; review at each milestone.

## Quick checklist

- [ ] Goal, date and capacity stated
- [ ] Each item described clearly and estimated
- [ ] Every Must tested against "what if it is missing?"
- [ ] Musts fit within about 60% of capacity
- [ ] Won'ts recorded
- [ ] Review points set

## Related

- [RICE and ICE Scoring](rice-and-ice-scoring.md): rank items numerically once scope is set
- [Impact-Effort Matrix](impact-effort-matrix.md): a visual way to find quick wins
- [Eisenhower Matrix](eisenhower-matrix.md): prioritise your own tasks by urgency and importance
