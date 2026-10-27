# Red Team and Devil's Advocate

> Give someone the job of attacking the plan, so its weaknesses come out before reality finds them.

| | |
| --- | --- |
| **Category** | Critical thinking |
| **Time needed** | 1-3 hours for a devil's advocate session; days for a full red team |
| **Best for** | Important plans, strategies and security-sensitive decisions where agreement may be too easy |

## What it is

Both methods use deliberate opposition to test a plan.

| Method | Description |
| --- | --- |
| Devil's advocate | One person argues against the plan, whatever they personally think, to test the reasoning |
| Red team | A group is assigned to act as an adversary or critic: to find ways to defeat, break or exploit the plan |

The term "devil's advocate" comes from the Catholic Church's *advocatus diaboli*, an official who argued against the canonisation of a candidate for sainthood. The role was formally discontinued in 1983. "Red teaming" comes from military exercises, where a red force plays the opponent, and is now common in security, business strategy and product review.

## Why it works

Groups tend to converge on a view and then support it. Dissent feels disloyal, and people see what they expect. Making opposition a formal role gives permission to criticise without social cost, and the red team has an incentive to look hard. The result is that weak assumptions and blind spots are found while they can still be fixed.

## When to use

- The decision is significant and hard to reverse
- The team is confident or in strong agreement
- You are in a field with adversaries, such as security or competition
- A plan depends on assumptions nobody has tested

## When not to use

- The decision is small
- The culture punishes criticism and a formal role would not be safe
- You cannot act on the findings; a red team without authority is a waste

## How to apply

1. **Define the plan** and the question: What are we trying to protect or achieve?
2. **Choose the role.** One devil's advocate for a discussion, or a separate red team for a deep review.
3. **Select people** who are capable and independent of the plan's authors. Rotate the role so it is not always the same person.
4. **Set the rules.** The role is to challenge ideas, not people. The plan's owners must listen without defending.
5. **Give the red team the information** they would realistically have, and the aim: to make the plan fail.
6. **Run the challenge.** Ask: How would we defeat this? What assumption is weakest? What would a competitor or attacker do? What are we not seeing?
7. **Record the findings** with their severity and likelihood.
8. **Respond.** The owners decide for each finding to fix, mitigate, accept or reject, and say why.
9. **Follow up.** Check that agreed changes were made.

## Question set for the challenger

- What must be true for this plan to work? Which is least likely?
- How would a determined opponent beat it?
- What happens if a key person, supplier or customer leaves?
- What have we ignored because it is unpleasant?
- What would we regret not having asked?

## Example 1: a product launch review

**Plan:** Launch a new subscription product in three markets in two months.

**Devil's advocate findings:**

- The launch depends on one payment partner, whose approval has not been confirmed
- The price was tested with only one segment
- Customer support has not been staffed for three time zones

**Response:** Confirm the partner in writing, run a price test in a second segment, and phase the launch: one market first, the others after support is ready.

## Example 2: a security review

**Plan:** A company is moving staff records to a new online system.

**Red team approach:** Try to obtain records by phishing staff, guessing weak passwords, and exploiting an old test account.

**Findings:** Two staff handed over credentials, and an old test account had full access.

**Response:** Staff training, multi-factor authentication, and removal of old accounts.

## Making it work

- Ask for the challenge early, when changes are cheap
- Reward people for good objections
- Keep the role separate from the person: the advocate argues the position, not their own view
- Pair with [Steel-manning](steel-manning.md): first state the plan fairly, then attack it

## Pitfalls

- **Ceremonial challenge.** If the answer is already decided, the exercise is theatre.
- **A defensive owner.** Reacting to every finding teaches people to stop raising them.
- **Always the same critic.** The role becomes ignored or resented; rotate.
- **No follow-up.** Findings without actions waste the effort.
- **Contrarianism.** The aim is to find real weaknesses, not to oppose everything.
- **Treating it as the only check.** Combine with data and testing.

## Quick checklist

- [ ] Plan and question defined
- [ ] Challengers independent of the authors
- [ ] Safe rules set for criticism
- [ ] Findings recorded with severity
- [ ] Owner response for each finding
- [ ] Changes tracked to completion

## Related

- [Pre-mortem](../strategy-and-risk/pre-mortem.md): the whole team imagines failure together
- [Steel-manning](steel-manning.md): understand the best form of an argument before attacking it
- [Six Thinking Hats](../decision-making/six-thinking-hats.md): the Black Hat is a structured form of challenge
