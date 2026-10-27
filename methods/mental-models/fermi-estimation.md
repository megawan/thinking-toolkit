# Fermi Estimation

> Break an unknown quantity into smaller guesses you can make, and combine them to get a number that is close enough.

| | |
| --- | --- |
| **Category** | Mental models |
| **Time needed** | 5-20 minutes |
| **Best for** | Sizing a market, checking a claim, or getting an order-of-magnitude answer when you have no data |

## What it is

A Fermi estimate is a quick calculation that gets an approximate answer from rough assumptions. It is named after the physicist Enrico Fermi, who was known for estimating quantities from very little information. A classic example attributed to his teaching is "How many piano tuners are there in Chicago?" Another is his estimate of the Trinity test explosion in 1945 from how far scraps of paper were blown by the blast, which came out at about 10 kilotons, within the same order of magnitude as the measured yield.

The goal is to be within a factor of two or three, or at least the right order of magnitude.

## Why it works

Errors in guesses tend to be in both directions: some too high, some too low. When you multiply several independent guesses, the errors partly cancel. Breaking a big unknown into pieces also exposes which pieces you know well and which you do not.

## When to use

- You need a rough size before deciding whether to spend time on a detailed analysis
- Checking whether a claim or forecast is plausible
- Sizing a market, a workload or a budget
- Practising structured thinking in interviews and planning

## When not to use

- Precision matters, such as in accounting, safety or engineering tolerances
- You have reliable data already
- The pieces are not independent and errors would compound in one direction

## How to apply

1. **State the question** with a unit: how many, how much, how long.
2. **Break it down** into factors you can estimate. Think of a formula: quantity = A x B x C.
3. **Estimate each factor,** with a range if you are unsure. Use round numbers.
4. **Anchor on known numbers:** population, household size, hours in a year, typical prices.
5. **Calculate** step by step. Keep the arithmetic simple.
6. **Check the unit** of the answer.
7. **Sanity-check** against another approach or a known figure.
8. **Give a range,** and say which assumption matters most.
9. **Decide:** is the answer large or small enough to change your plans?

## Useful anchors

| Quantity | Rough value |
| --- | --- |
| People per household | 2.5-4 |
| Working days per year | about 250 |
| Working hours per year | about 2,000 |
| Hours in a year | about 8,800 |
| Seconds in a day | about 86,000 |
| Litres of water used per person per day | 100-300 |

## Example 1: piano tuners in Chicago

| Step | Assumption | Result |
| --- | --- | --- |
| Population | 3 million | |
| Households | 3 million / 2.5 people | about 1.2 million |
| Share with a piano | 1 in 20 households | about 60,000 pianos |
| Tunings per piano per year | 1 | 60,000 tunings a year |
| Tunings per tuner | 4 a day x 250 days | 1,000 a year |
| Tuners | 60,000 / 1,000 | about 60 |

**Answer:** Around 60 tuners, probably between 30 and 120. The most uncertain assumption is the share of households with a piano.

## Example 2: sizing a market

**Question:** How big is the yearly market for a coffee subscription in a city of 1 million adults?

| Step | Assumption | Result |
| --- | --- | --- |
| Adults who drink coffee at home | 60% | 600,000 |
| Share who would pay for a subscription | 3% | 18,000 |
| Spend per subscriber | $20 a month = $240 a year | |
| Market | 18,000 x $240 | about $4.3 million a year |

**Answer:** Around $4 million a year. If the share is 1% rather than 3%, it falls to about $1.4 million. The team decides whether a market of that size justifies the effort.

## Pitfalls

- **False precision.** Report one or two significant figures.
- **Skipping a sanity check.** A second route often catches a wrong factor.
- **Hiding assumptions.** Write them down so others can challenge them.
- **Forgetting units.** Per day, per year and per person are easy to confuse.
- **Anchoring on a first guess.** Estimate the pieces independently.
- **Using it as proof.** It is a plausibility check, not evidence.

## Quick checklist

- [ ] Question stated with a unit
- [ ] Broken into estimable factors
- [ ] Assumptions written down
- [ ] Round numbers, simple arithmetic
- [ ] Result sanity-checked by a second route
- [ ] Range and key assumption stated

## Related

- [Bayesian Thinking](bayesian-thinking.md): update your estimate as data arrives
- [First Principles](first-principles.md): break a problem into basic elements
- [Expected Value and Opportunity Cost](../decision-making/expected-value-and-opportunity-cost.md): turn estimates into a decision
