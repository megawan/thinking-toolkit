# Fishbone Diagram

> Map every possible cause of a problem onto a "fish skeleton" so you can see the full picture before choosing where to dig.

| | |
| --- | --- |
| **Category** | Root cause analysis |
| **Time needed** | 30-60 minutes with a small group |
| **Best for** | Problems with many possible causes, where a single chain of "why" would miss branches |

## What it is

A fishbone diagram, also called an Ishikawa or cause-and-effect diagram, was developed by Kaoru Ishikawa in the 1960s. The problem sits at the "head" on the right. Major cause categories branch off a central spine like ribs, and specific causes attach to each rib as smaller bones.

```text
 Methods ----\        Materials ---\        People ------\
              \                     \                     \
 ---------------+--------------------+---------------------+---> Problem
              /                     /                     /
 Machines ---/        Environment --/        Measurement -/
```

## Why it works

When a problem has several possible causes, it is easy to fixate on the first one found. The diagram forces the group to look across categories, shows the whole set of candidates at once, and helps separate what is known from what is only suspected. It also gives a group a shared picture to point at.

## Common categories

| Setting | Categories |
| --- | --- |
| Manufacturing (6M) | Man, Machine, Method, Material, Measurement, Mother nature (environment) |
| Services (8P) | Product, Price, Place, Promotion, People, Process, Physical evidence, Performance |
| Software | Code, Infrastructure, Process, People, Tooling, External services |
| General | People, Process, Tools, Materials, Environment, Management |

Choose categories that fit your problem. They are a prompt, not a rule.

## When to use

- The problem has many possible causes
- A group needs a shared view before deciding what to investigate
- A simple chain of "why" has stalled or branched too much
- You want to document the analysis for others

## When not to use

- The cause is almost certainly a single linear chain; use [Five Whys](five-whys.md)
- You already have data pointing to one cause
- You need to prove which cause matters most; add data or a Pareto analysis

## How to apply

1. **Write the problem** as a specific, measurable statement and place it at the head.
2. **Draw the spine** and the main category bones.
3. **Brainstorm causes** for each category. Ask "Why does this happen?" for every cause.
4. **Attach sub-causes.** Add a smaller bone for each, and go one or two levels deeper where useful.
5. **Review the whole diagram.** Look for causes that appear in more than one place.
6. **Mark the likely ones.** Use evidence, such as data, logs, or observation. Circle the few worth testing.
7. **Verify.** Test the top candidates before acting.
8. **Act and follow up.** Fix confirmed causes and check whether the problem declines.

## Example: late deliveries

**Problem:** 25% of orders arrive after the promised date.

| Category | Causes found |
| --- | --- |
| People | New staff not trained on packing; shifts understaffed on Mondays |
| Process | Orders batched only twice a day; no check for address errors |
| Tools | Label printer jams; stock system updates with a delay |
| Materials | Boxes arrive late from the supplier |
| Environment | Peak season volume; road works near the depot |
| Management | Delivery promises set without checking warehouse capacity |

**Findings after checking records:** Most late orders were placed after the second batch cut-off, and many had address errors.

**Actions:** Add a third daily batch, validate addresses at checkout, and base delivery promises on the actual cut-off.

## Tips

- Use a whiteboard or sticky notes so the group can move things
- Keep each bone to a short phrase
- Do not argue about causes while brainstorming; verify afterwards
- Combine with data: count how often each cause appears

## Pitfalls

- **Treating all causes as equal.** A diagram lists candidates; evidence ranks them.
- **Vague problem statement.** "Quality is bad" cannot be analysed; "6% of units fail inspection" can.
- **Stopping at a category.** Go down to specific, testable causes.
- **Forcing the categories.** Rename or add categories that fit.
- **Drawing it and filing it away.** The point is to choose what to test.

## Quick checklist

- [ ] Problem stated specifically
- [ ] Categories chosen to suit the problem
- [ ] Causes and sub-causes captured
- [ ] Likely causes backed by evidence
- [ ] Top causes verified before acting
- [ ] Follow-up measured

## Related

- [Five Whys](five-whys.md): follow a single promising branch deeper
- [Pareto Analysis](pareto-analysis.md): rank causes by how much they contribute
