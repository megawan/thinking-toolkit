# Bayesian Thinking

> Start with how likely you think something is, then update that belief in proportion to the strength of new evidence.

| | |
| --- | --- |
| **Category** | Mental models |
| **Time needed** | 15-30 minutes |
| **Best for** | Judging claims, forecasts and test results, and revising your views as evidence comes in |

## What it is

Bayesian thinking applies Bayes' theorem, named after the English minister Thomas Bayes, whose essay was published after his death in 1763. The idea has three parts:

| Part | Meaning |
| --- | --- |
| Prior | How likely you thought the hypothesis was before the new evidence |
| Likelihood | How likely the evidence is if the hypothesis is true, compared with how likely it is if it is false |
| Posterior | Your updated belief after considering the evidence |

In its basic form: P(H given E) = P(E given H) x P(H) / P(E).

You do not need to calculate precisely every time. The habit matters: begin with a base rate, then move your belief by an amount that matches how diagnostic the evidence is.

## Why it works

People tend to treat evidence as if it were the only information. A positive test, a dramatic story or a sharp trend feels convincing, even if the thing it points to was very rare to start with. Starting from the base rate prevents over-reacting to a single piece of evidence. Updating in steps lets you change your mind gradually and honestly as the evidence accumulates.

## When to use

- Interpreting a test, a signal or a report where false alarms are possible
- Forecasting, where you need to revise as news arrives
- Judging a claim that seems surprising
- Deciding how much to trust a new piece of data

## When not to use

- You have no basis for a prior and no way to find a base rate
- The situation is purely deterministic
- The decision is too minor to justify the effort

## How to apply

1. **State the hypothesis** in a clear form that can be true or false.
2. **Find the base rate (prior).** How often is this true in similar cases? Start there, even if rough.
3. **Collect the evidence** and ask two questions: how likely is this evidence if the hypothesis is true, and how likely if it is false?
4. **Compare the two.** The bigger the ratio, the stronger the evidence.
5. **Update** your belief: raise it if the evidence is more likely under the hypothesis, lower it if less likely. Strong evidence moves it a lot, weak evidence barely at all.
6. **Use natural frequencies** when calculating: think of 1,000 cases rather than percentages.
7. **Repeat** with each new piece of evidence, using the posterior as the next prior.
8. **State the result** as a probability, and decide whether it is high or low enough to act.

## Example 1: a medical test

**Facts:** 1% of people have a condition. The test is positive for 90% of people who have it, and falsely positive for 9% of people who do not. Someone tests positive. What is the chance they have the condition?

Think of 1,000 people.

| Group | People | Test positive |
| --- | --- | --- |
| Have the condition (1%) | 10 | 9 (90%) |
| Do not have it (99%) | 990 | about 89 (9%) |
| Total positive | | about 98 |

**Answer:** 9 of about 98 positives are true, so the chance is about 9%. The test is useful, because it raised the chance from 1% to 9%, but it is far from certain. The low base rate matters.

## Example 2: judging a start-up idea

**Hypothesis:** Customers will pay for a new service.

- **Prior:** About 1 in 10 similar ideas get paying customers, so start at 10%.
- **Evidence 1:** Twenty interviews, with 12 people saying they would pay. Such enthusiasm is common even for ideas that fail, so it is only a little stronger under success than failure. The belief rises to maybe 20%.
- **Evidence 2:** Five customers pay a deposit. That is far more likely if the idea works than if it does not. The belief rises to 60% or more.

**Decision:** Build a first version, and keep watching repeat purchases.

## Habits that follow from it

- Ask "compared to what?" for any number
- Ask "how common is this to begin with?" before reacting to a case
- Ask "how likely would I see this evidence even if I were wrong?"
- Change your mind by small amounts as evidence accumulates, not all at once
- Keep a record of predictions and the probabilities you gave

## Pitfalls

- **Ignoring the base rate.** The most common error.
- **Treating weak evidence as strong.** Check what else would produce it.
- **Over-precision.** Rough numbers are fine; do not pretend to know 37.4%.
- **Anchoring on the prior.** If strong evidence keeps arriving, the prior should not hold.
- **Confusing P(E given H) with P(H given E).** The chance of a positive result given the condition is not the chance of the condition given a positive result.
- **Not updating.** Beliefs that never move are not Bayesian.

## Quick checklist

- [ ] Hypothesis stated clearly
- [ ] Base rate found or estimated
- [ ] Evidence assessed under both true and false
- [ ] Belief updated by the right amount
- [ ] Natural frequencies used for calculation
- [ ] Next evidence planned

## Related

- [Fermi Estimation](fermi-estimation.md): produce rough priors when there is no data
- [Cognitive Biases](../critical-thinking/cognitive-biases.md): biases that stop people from updating
- [Expected Value and Opportunity Cost](../decision-making/expected-value-and-opportunity-cost.md): use your updated probabilities in a decision
