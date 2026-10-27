# Workflows

Methods work best in sequence: one finds the problem, the next generates options, another picks and stress-tests. This page shows common chains and when to use them.

## How to chain methods

1. Decide what you need now: understand, generate, choose, or de-risk.
2. Pick one method for that need and finish it before switching.
3. Carry the output forward: the root cause becomes the problem statement for idea generation, and the ideas become the options in a decision.
4. End with something concrete: an action, an owner and a date.

## 1. From recurring problem to chosen fix

Sequence: Five Whys → Lateral Thinking → Decision Matrix → Pre-mortem

| Step | Method | Output |
| --- | --- | --- |
| Understand | [Five Whys](../methods/root-cause/five-whys.md) | A root cause you can act on |
| Generate | [Lateral Thinking](../methods/ideation/lateral-thinking.md) | Many candidate fixes, including unusual ones |
| Choose | [Decision Matrix](../methods/decision-making/decision-matrix.md) | A ranked shortlist with stated reasons |
| De-risk | [Pre-mortem](../methods/strategy-and-risk/pre-mortem.md) | A list of risks to the chosen fix and responses |

### Worked example

**Problem:** Customers often leave the checkout page without paying.

1. **Five Whys.** Why do they leave? Many stop at the account form. Why? It asks for a password before showing the total. Why? The shop was built to push people into accounts. Why? A past goal was growing the mailing list. Why was that never revisited? No one owned checkout conversion. **Root cause:** forced account creation, with no owner for conversion.
2. **Lateral Thinking.** Challenge the assumption that an account is required, and reverse the goal ("how to make people leave?"). Ideas: guest checkout, social sign-in, account creation after payment, pay on delivery, show the total first.
3. **Decision Matrix.** Criteria: effect on conversion (weight 5), build effort (3), effect on the mailing list (2), risk (3). Guest checkout with an optional account after payment scores highest.
4. **Pre-mortem.** Imagine it failed. Reasons: fewer sign-ups hurt repeat sales, payment errors for guests, no owner again. **Responses:** invite an account after payment, test the guest payment flow, name an owner for conversion.

## 2. A problem with many possible causes

Sequence: Fishbone → Pareto → Five Whys → SCAMPER

| Step | Method | Output |
| --- | --- | --- |
| Map | [Fishbone Diagram](../methods/root-cause/fishbone.md) | All candidate causes by category |
| Rank | [Pareto Analysis](../methods/prioritisation/pareto-analysis.md) | The few causes that matter most, from data |
| Dig | [Five Whys](../methods/root-cause/five-whys.md) | The root of each top cause |
| Improve | [SCAMPER](../methods/ideation/scamper.md) | Variations on the process to remove those causes |

## 3. A new initiative

Sequence: First Principles → Lateral Thinking → SWOT → Decision Matrix → Pre-mortem

| Step | Method | Output |
| --- | --- | --- |
| Ground | [First Principles](../methods/mental-models/first-principles.md) | The facts the plan must respect |
| Generate | [Lateral Thinking](../methods/ideation/lateral-thinking.md) | Different approaches |
| Assess | [SWOT Analysis](../methods/strategy-and-risk/swot.md) | Strengths and gaps of the leading approaches |
| Choose | [Decision Matrix](../methods/decision-making/decision-matrix.md) | One approach with reasons |
| De-risk | [Pre-mortem](../methods/strategy-and-risk/pre-mortem.md) | Risks and responses before commitment |

## 4. Overloaded and unsure where to start

Sequence: Pareto → Eisenhower

| Step | Method | Output |
| --- | --- | --- |
| Find what matters | [Pareto Analysis](../methods/prioritisation/pareto-analysis.md) | The few items behind most of the effect |
| Schedule | [Eisenhower Matrix](../methods/prioritisation/eisenhower-matrix.md) | A plan that protects important work |

## 5. A stuck group decision

Sequence: Six Thinking Hats → Decision Matrix → Pre-mortem

| Step | Method | Output |
| --- | --- | --- |
| Align | [Six Thinking Hats](../methods/decision-making/six-thinking-hats.md) | Shared facts, concerns and options |
| Choose | [Decision Matrix](../methods/decision-making/decision-matrix.md) | An agreed ranking |
| De-risk | [Pre-mortem](../methods/strategy-and-risk/pre-mortem.md) | Risks to address before committing |

## 6. Making a plan robust

Sequence: Inversion → Pre-mortem

| Step | Method | Output |
| --- | --- | --- |
| Find failure modes | [Inversion](../methods/mental-models/inversion.md) | Rules that avoid obvious mistakes |
| Test as a team | [Pre-mortem](../methods/strategy-and-risk/pre-mortem.md) | Risks you had not thought of, with owners |

## 7. From a vague complaint to tested ideas

Sequence: How Might We → Brainwriting 6-3-5 → Crazy 8s → Decision Matrix

| Step | Method | Output |
| --- | --- | --- |
| Frame | [How Might We](../methods/ideation/how-might-we.md) | One to three open questions |
| Diverge (words) | [Brainwriting 6-3-5](../methods/ideation/brainwriting-635.md) | Dozens of written ideas without loud voices dominating |
| Diverge (pictures) | [Crazy 8s](../methods/ideation/crazy-8s.md) | Concrete sketches of the strongest directions |
| Choose | [Decision Matrix](../methods/decision-making/decision-matrix.md) | A ranked shortlist to prototype |

## 8. Designing something with many choices

Sequence: Mind Mapping → Morphological Analysis → Analogical Thinking → Decision Matrix

| Step | Method | Output |
| --- | --- | --- |
| Explore | [Mind Mapping](../methods/ideation/mind-mapping.md) | The parts of the problem and how they connect |
| Structure | [Morphological Analysis](../methods/ideation/morphological-analysis.md) | A box of parameters and options |
| Widen | [Analogical Thinking](../methods/ideation/analogical-thinking.md) | More options per row, borrowed from other fields |
| Choose | [Decision Matrix](../methods/decision-making/decision-matrix.md) | The best combination, with reasons |

## Tips

- Do not run every method on every problem; two or three usually suffice
- Write the output of each step in a sentence before starting the next
- Re-run an earlier step if a later one reveals the problem was framed wrongly
- Use the [worksheets](../worksheets/five-whys.md) to keep records short and comparable
