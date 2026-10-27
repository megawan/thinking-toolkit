# Pre-mortem

> Imagine the project has already failed, then work out why, so you can fix the plan while it is still cheap.

| | |
| --- | --- |
| **Category** | Risk and planning |
| **Time needed** | 30-60 minutes with the team, before the project starts |
| **Best for** | Projects, launches, and decisions where people are optimistic and failure would be costly |

## What it is

A pre-mortem is a planning exercise by psychologist Gary Klein. The usual post-mortem happens after a failure. A pre-mortem asks the team to assume, before work starts, that the project has failed badly, and to write down the reasons. The reasons become a list of risks to deal with now.

## Why it works

Teams that have committed to a plan tend to see its strengths and ignore its weaknesses. Doubters often stay quiet to avoid seeming negative. Saying "it has already failed" changes the task: finding reasons becomes the assignment, and it is safe to speak up. Research on prospective hindsight suggests that imagining an event as already happened helps people produce more, and more specific, reasons for it.

## When to use

- At the kickoff of a project, launch, or major change
- Before committing to an expensive or hard-to-reverse decision
- When the team seems very confident and no one is raising risks
- When a past project failed for reasons that were predictable

## When not to use

- The plan is trivial or easy to undo
- The team does not feel safe to be honest; fix that first
- The plan is not yet concrete enough to fail in a specific way

## How to apply

1. **Brief the team.** Summarise the plan, goal, and date in a few minutes.
2. **Set the scene.** Say: "It is one year from now. The project has failed completely. Take a few minutes to write down every reason you can think of."
3. **Write silently and alone.** Each person lists reasons on their own, without discussion. This avoids groupthink.
4. **Share one by one.** Go around the room; each person reads one reason at a time until everything is out.
5. **Group similar reasons** into themes, such as people, schedule, technology, market, or dependencies.
6. **Rate the themes** by likelihood and by impact, for example high, medium, or low.
7. **Plan for the top risks.** For each, choose one: prevent it, reduce it, prepare a response, or accept it.
8. **Update the plan** and assign an owner and a review date per risk.

## Prompts that help

- Who would have to let us down for this to fail?
- What would we wish we had known at the start?
- Which assumption, if wrong, would sink us?
- What did we ignore because it was uncomfortable to raise?
- What outside event could break the plan?

## Example: launching a mobile app

**Prompt:** "It is six months after launch and the app has failed."

| Theme | Reasons raised | Likelihood | Impact |
| --- | --- | --- | --- |
| Delivery | Only one developer knows the payment code; release slipped three months | Medium | High |
| Market | Users did not see a reason to switch from the existing tool | High | High |
| Technical | App was slow on older phones; reviews turned negative | Medium | Medium |
| Operations | No one owned customer support after launch | High | Medium |

**Actions:**

- Pair a second developer on payments (owner: tech lead, this month)
- Run ten user interviews to test the reason to switch before building more (owner: product, 2 weeks)
- Test on three older phone models before release (owner: QA)
- Name a support owner and write a response guide (owner: ops)

## Pitfalls

- **Treating it as a mood exercise.** The output must be actions with owners.
- **Letting the senior person speak first.** Silent writing comes first for a reason.
- **Vague reasons.** "Poor communication" is weak; "Design and engineering did not share a roadmap" can be acted on.
- **Doing it too late.** The value is in changing the plan, so run it early.
- **One-and-done.** Revisit the risk list at milestones.
- **Dismissing outlandish reasons.** Check them before discarding.

## Quick checklist

- [ ] Plan summarised and dated
- [ ] Failure framed as already happened
- [ ] Reasons written silently first
- [ ] Reasons grouped and rated
- [ ] Top risks have an owner and a response
- [ ] Plan updated

## Related

- [Five Whys](five-whys.md): use it afterwards on a real failure to find its cause
- [Six Thinking Hats](six-thinking-hats.md): the Black Hat covers similar ground in a live discussion
- [SWOT Analysis](swot.md): a broader view of risks and opportunities
