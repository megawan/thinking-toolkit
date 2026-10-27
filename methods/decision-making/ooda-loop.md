# OODA Loop

> Observe, orient, decide, act, and repeat faster and better than the situation changes.

| | |
| --- | --- |
| **Category** | Decision making |
| **Time needed** | Seconds to hours per loop; repeated continuously |
| **Best for** | Fast-changing situations, competition, and incident response, where learning and speed matter |

## What it is

The OODA loop is a decision cycle developed by John Boyd, a United States Air Force fighter pilot and strategist. Boyd studied why some pilots won air combat even when their aircraft were not superior. He concluded that they cycled through observing, understanding, deciding and acting faster than their opponents, and so kept the initiative.

| Stage | Question | What happens |
| --- | --- | --- |
| Observe | What is happening? | Collect information from the environment, results, and feedback |
| Orient | What does it mean? | Interpret the information using experience, knowledge, culture and analysis; form a picture of the situation |
| Decide | What will we do? | Choose an action or a hypothesis to test |
| Act | Do it | Carry out the decision, which changes the situation and produces new information |

The loop is continuous: acting creates new information, which feeds the next observation.

## Why orientation matters most

Boyd saw orientation as the most important stage. It is where observations are filtered through mental models, past experience and assumptions. A poor orientation leads to a poor decision, even with perfect data. It is also where you can be misled: if your picture of the world is out of date, you act on the wrong problem. The fast learner revises their picture quickly.

## When to use

- The situation changes quickly, such as an incident, a market shift or a competitive contest
- You can take small actions and learn from the result
- Your team is stuck analysing and not acting
- You want a shared language for a fast response

## When not to use

- A one-time, irreversible decision with time to analyse; use [Decision Matrix](decision-matrix.md) or [One-way and Two-way Doors](one-way-and-two-way-doors.md)
- The situation is stable and slow-moving
- Speed would cause harm without checks, as in some safety-critical work

## How to apply

1. **Observe.** Gather the facts you can get quickly: data, signals, customer feedback, the state of your own systems. Note what you cannot see.
2. **Orient.** Ask what the facts mean. Which assumptions are you relying on? What has changed? What would an outsider see? Update your mental model.
3. **Decide.** Choose the next action, as a hypothesis if you are unsure. Prefer a small, reversible step.
4. **Act.** Do it without delay.
5. **Observe the result.** Check what changed because of your action, and begin the next loop.
6. **Shorten the loop.** Remove delays between stages: faster data, clearer authority, pre-agreed responses.
7. **Improve orientation.** After each loop or incident, update assumptions and playbooks.

## Ways to speed up a loop

| Stage | Speed-up |
| --- | --- |
| Observe | Dashboards, alerts, direct customer contact, shorter reporting lines |
| Orient | Shared models, checklists, practice scenarios, diverse viewpoints |
| Decide | Pre-agreed rules for common cases, clear decision rights, small reversible steps |
| Act | Automation, trained teams, simple procedures |

## Example 1: an online service outage

1. **Observe.** Error rates rise; support tickets spike; one region is affected.
2. **Orient.** The change began after a release 20 minutes ago; similar patterns in the past came from a database setting.
3. **Decide.** Roll back the release for the affected region.
4. **Act.** Roll back.
5. **Observe.** Errors fall in the region. Tickets slow. Next loop: confirm the cause and check for hidden damage.

The team that has dashboards, a rollback procedure and clear authority completes this loop in minutes.

## Example 2: a small shop facing a new competitor

1. **Observe.** A competitor opens nearby with lower prices. Footfall drops 15% in two weeks.
2. **Orient.** Customers who leave are price-sensitive, but loyal customers cite service and quality.
3. **Decide.** Test a loyalty offer for regular customers and a small range of lower-priced items.
4. **Act.** Run the test for two weeks.
5. **Observe.** Regulars stay; footfall stabilises. Repeat with the next idea.

## Pitfalls

- **Speed without orientation.** Fast but wrong decisions compound errors.
- **Stuck in orient.** Endless analysis is a loop that never acts.
- **Acting without observing the result.** Without feedback, there is no loop.
- **Fixed assumptions.** A model that is not revised leads to a wrong picture.
- **Large irreversible actions.** In an uncertain situation, prefer small steps.
- **Treating it as a one-way sequence.** It is a cycle, and stages overlap.

## Quick checklist

- [ ] Current situation observed with fresh data
- [ ] Assumptions stated and challenged
- [ ] Next action chosen, small and reversible if unsure
- [ ] Action taken promptly
- [ ] Result observed and the next loop started
- [ ] Delays between stages reduced over time

## Related

- [One-way and Two-way Doors](one-way-and-two-way-doors.md): choose which decisions need the loop and which need care
- [Five Whys](../root-cause/five-whys.md): in orient, find what is really going on
- [First Principles](../mental-models/first-principles.md): rebuild a wrong picture of the situation
