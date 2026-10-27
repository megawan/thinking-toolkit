# Cost-Benefit Analysis

> Put a value on everything a choice costs and gives, over time, and see whether the benefits outweigh the costs.

| | |
| --- | --- |
| **Category** | Decision making |
| **Time needed** | 1-3 hours, plus time to gather figures |
| **Best for** | Investments and projects where costs and benefits can be estimated in money |

## What it is

Cost-benefit analysis (CBA) compares the total expected costs of an option with its total expected benefits, expressed in the same unit, usually money. If benefits exceed costs, the option creates value. If you compare several options, the one with the highest net benefit is usually preferred.

The idea goes back to the French engineer Jules Dupuit in the 1840s and became a standard tool for public projects in the twentieth century. It is now used for business investments, hiring, tools, policy, and personal decisions.

## Why it works

Gut feeling tends to weigh vivid costs and benefits heavily and ignore the rest. Listing every cost and benefit, estimating each, and adding them up makes the choice visible and comparable. Discounting future amounts shows that money later is worth less than money now, which stops long-term promises from looking better than they are.

## Key measures

| Measure | Formula | Reading |
| --- | --- | --- |
| Net benefit | Total benefits - total costs | Positive means it pays off |
| Net present value (NPV) | Sum over years of (benefit - cost) / (1 + r)^t | Value in today's money; r is the discount rate and t the year |
| Benefit-cost ratio (BCR) | Present value of benefits / present value of costs | Above 1 means benefits exceed costs |
| Payback period | Time until cumulative benefits cover the cost | Shorter means less exposure |
| Break-even | The value of one input at which NPV is zero | Shows how much room for error you have |

## When to use

- A significant spend or commitment, such as equipment, software, hiring, or a project
- Several options need ranking by value
- You need to justify a choice to others
- Costs and benefits can be estimated, at least roughly

## When not to use

- Key factors cannot be measured, such as safety or ethics; use CBA for the measurable part and handle the rest separately
- The decision is small or easily reversed
- Estimates would be pure guesses; gather data first

## How to apply

1. **Define the options and the time horizon.** Include "do nothing" as the baseline.
2. **List all costs.** One-off (purchase, setup, training) and recurring (running, maintenance, staff time). Include indirect and hidden costs.
3. **List all benefits.** Savings, extra income, time saved, risk avoided. Be careful not to count the same benefit twice.
4. **Put values on them.** Use data where possible; otherwise a range with a best guess.
5. **Choose a discount rate** that reflects your cost of money or an alternative use, such as 5-10% for a business.
6. **Compute** net benefit, NPV, BCR, and payback for each option.
7. **Test sensitivity.** Change the most uncertain estimates and see if the result flips. Find the break-even point.
8. **Add non-monetary factors** next to the result: risk, morale, strategic fit.
9. **Decide and record** the assumptions so you can review them later.

## Example: buying a 3D printer for a small workshop

**Decision:** Buy a 3D printer for $4,000, or keep outsourcing prints.

| Item | Amount |
| --- | --- |
| Purchase price (year 0) | $4,000 |
| Materials and maintenance | $600 per year |
| Savings on outsourced prints | $2,000 per year |
| Time horizon | 5 years |
| Discount rate | 8% |

The 5-year annuity factor at 8% is about 3.993.

| Measure | Calculation | Result |
| --- | --- | --- |
| Present value of benefits | 2,000 x 3.993 | $7,985 |
| Present value of costs | 4,000 + 600 x 3.993 | $6,396 |
| NPV | 7,985 - 6,396 | about $1,590 |
| BCR | 7,985 / 6,396 | about 1.25 |

**Sensitivity:** If annual savings fall to $1,500, NPV becomes about -$410. The break-even is at about $1,600 savings per year. The owner checks how many prints are outsourced per year before buying.

## Tips

- Show ranges: best, likely, worst
- Use the same time horizon and discount rate for all options
- Count opportunity costs, such as staff time that could be used elsewhere (see [Expected Value and Opportunity Cost](expected-value-and-opportunity-cost.md))
- Do not include sunk costs, which are already spent and cannot change
- Keep the assumptions visible on one page

## Pitfalls

- **Missing costs.** Hidden and recurring costs are the most commonly forgotten.
- **Optimistic benefits.** Be sceptical of benefits that depend on perfect adoption.
- **Double counting.** One benefit can show up under several names.
- **Ignoring time.** Without discounting, long-run benefits look larger than they are.
- **False precision.** Estimates have ranges; a small NPV is a toss-up.
- **Forcing everything into money.** Keep important unmeasured factors in view.

## Quick checklist

- [ ] Options and baseline defined
- [ ] One-off and recurring costs listed
- [ ] Benefits listed without double counting
- [ ] Same horizon and discount rate for all options
- [ ] NPV, BCR and payback calculated
- [ ] Sensitivity and break-even tested
- [ ] Non-monetary factors noted

## Related

- [Decision Matrix](decision-matrix.md): use when criteria are not all measured in money
- [Expected Value and Opportunity Cost](expected-value-and-opportunity-cost.md): handle uncertainty and the value of the next-best option
- [Pre-mortem](../strategy-and-risk/pre-mortem.md): test the assumptions behind your benefits
