# Occam's and Hanlon's Razor

> Prefer the simpler explanation, and do not assume bad intent when carelessness or a mistake explains it.

| | |
| --- | --- |
| **Category** | Mental models |
| **Time needed** | 5-15 minutes |
| **Best for** | Choosing between explanations, debugging, and handling conflict at work |

## What it is

A **razor** is a rule of thumb that helps you cut away unlikely explanations. Two are especially useful.

| Razor | Statement | Origin |
| --- | --- | --- |
| Occam's razor | When several explanations fit the facts, prefer the one with the fewest assumptions | William of Ockham, 14th-century English philosopher |
| Hanlon's razor | Do not attribute to malice what is adequately explained by neglect or error | Named after Robert J. Hanlon, in a 1980 collection of Murphy's Law jokes |

Both are heuristics, not laws. They tell you where to look first, not what is true.

## Why it works

Explanations with many moving parts need many things to be true at once, so they are less likely to be right than simpler ones with the same explanatory power. Likewise, mistakes, misunderstandings and overload are far more common than deliberate harm. Starting with the simple or the charitable explanation saves time and avoids needless conflict.

## When to use

- Several explanations fit the same evidence
- A system fails and you need a place to start looking
- Someone's behaviour seems hostile and you are about to react
- A theory is becoming more and more complicated

## When not to use

- The simple explanation does not fit all the facts; do not force it
- There is real evidence of intent; Hanlon's razor is not a reason to ignore it
- High-stakes safety, security or legal situations, where you should test the less likely explanation too

## How to apply

### Occam's razor

1. **List the explanations** that fit the evidence.
2. **List the assumptions** each one needs.
3. **Count and weigh them.** Which requires the fewest unlikely assumptions?
4. **Start by testing the simplest.** Look for a cheap way to confirm or reject it.
5. **Move to the next** only if the evidence rules it out.
6. **Stay open.** If new facts do not fit, drop the simple explanation.

### Hanlon's razor

1. **Notice the interpretation** you are making ("they did this on purpose").
2. **List the innocent explanations:** forgot, did not know, overloaded, misunderstood, a system error.
3. **Rank by likelihood.** Which is most common in this setting?
4. **Check with a question,** not an accusation: "I noticed X. Can you help me understand what happened?"
5. **Treat patterns differently.** One slip is likely an error; repeated, consistent behaviour needs a direct conversation.

## Example 1: Occam's razor in debugging

**Situation:** A website shows wrong prices to some users.

| Explanation | Assumptions needed |
| --- | --- |
| A cache is serving old prices | One: the cache was not cleared after the price update |
| A hacker changed prices for some users | Several: a breach, access to the database, a targeted change |
| A rare bug in the pricing code that only affects some regions | Two: a bug, a regional condition |

**Action:** Check the cache first. It is the simplest and the cheapest to test. It was the cause, and clearing it fixed the problem.

## Example 2: Hanlon's razor at work

**Situation:** A colleague did not copy you on an important email.

| Explanation | Likelihood |
| --- | --- |
| They forgot or used the wrong list | High |
| They did not know you needed to be included | High |
| They wanted to exclude you on purpose | Low, without other evidence |

**Action:** Ask: "Can you add me to the thread? I want to keep up with this." The answer was an outdated mailing list, which was then corrected.

## Pitfalls

- **Treating the simplest as always right.** The razor sets priorities for testing; it does not prove anything.
- **Confusing simple with familiar.** The simplest explanation is the one with fewer assumptions, not the one you like.
- **Using Hanlon's razor to excuse harmful patterns.** Repeated harm needs action whatever the cause.
- **Dismissing real malice.** Some people do act on purpose.
- **Stopping the search too early.** Test the simple explanation, and be ready to go on.
- **Using it to shut down inquiry.** The razor should start an investigation, not end one.

## Quick checklist

- [ ] All explanations that fit the facts listed
- [ ] Assumptions of each counted
- [ ] Simplest tested first
- [ ] Innocent explanations considered before blaming
- [ ] A question asked instead of an accusation
- [ ] Ready to revise if new facts appear

## Related

- [Five Whys](../root-cause/five-whys.md): use after you pick the likeliest explanation
- [Steel-manning](../critical-thinking/steel-manning.md): give the other side its best explanation too
- [Cognitive Biases](../critical-thinking/cognitive-biases.md): why we tend to assume bad intent
