# Systems Thinking

> See a problem as part of a connected whole with feedback loops, not as a single event with a single cause.

| | |
| --- | --- |
| **Category** | Mental models |
| **Time needed** | 45-90 minutes, solo or with a team |
| **Best for** | Problems that persist despite repeated fixes, or where solutions create new problems |

## What it is

Systems thinking looks at how the parts of a situation affect each other over time. Instead of asking "what caused this event?", it asks "what structure keeps producing this pattern?". It draws on the work of Jay Forrester on system dynamics at MIT in the 1950s and 1960s, Donella Meadows (*Thinking in Systems*, 2008) and Peter Senge (*The Fifth Discipline*, 1990).

A **causal loop diagram** is the main tool. It shows variables connected by arrows. Each arrow has a sign:

| Sign | Meaning |
| --- | --- |
| + (same direction) | When A goes up, B goes up (and when A goes down, B goes down) |
| - (opposite direction) | When A goes up, B goes down |

Loops come in two kinds:

| Loop | Behaviour | Example |
| --- | --- | --- |
| Reinforcing (R) | Amplifies change: growth or collapse | More users bring more content, which brings more users |
| Balancing (B) | Resists change and seeks a target | A thermostat; a waiting queue that discourages new customers |

Delays between cause and effect are often the reason that systems surprise us.

## Why it works

Many problems are the result of feedback. A quick fix may relieve a symptom and, through a loop, make the problem worse later. By drawing the loops, a team can see why efforts keep failing and find the points where a small change has a large effect.

## When to use

- A problem keeps returning in a different form
- A solution produced side effects
- Many people and factors interact over time
- A team disagrees about causes because each sees only one part

## When not to use

- A simple, linear cause with a clear fix; use [Five Whys](../root-cause/five-whys.md)
- You need a precise forecast; a diagram gives understanding, not numbers
- The system boundary is too large to draw usefully

## How to apply

1. **Name the problem** as a pattern over time: what is rising, falling or repeating? Sketch a simple trend line.
2. **Set the boundary.** What is inside the system, and what is outside?
3. **List the key variables** that change over time, as nouns that can go up or down (for example "workload", "quality", "trust").
4. **Draw the links.** Connect variables with arrows where one affects another. Mark each with + or -.
5. **Find the loops.** Trace circles of arrows. A loop with an even number of minus signs is reinforcing; an odd number is balancing.
6. **Mark the delays** where the effect takes a long time.
7. **Tell the story.** Walk through each loop aloud: "As A rises, B rises, which makes..." Check that it matches what you have seen.
8. **Look for leverage points:** where a small change could shift a loop, break a vicious cycle or strengthen a virtuous one.
9. **Test your ideas.** Try a small change, watch the effect, and update the diagram.

## Example: a support team that never catches up

```text
 Workload --(+)--> Overtime --(+)--> Fatigue and errors --(+)--> Rework --(+)--> Workload
```

This is a reinforcing loop: more work leads to more overtime and mistakes, which create more work.

```text
 Workload --(+)--> Hiring pressure --(+)--> New hires --(-)--> Workload
```

This is a balancing loop with a delay: hiring takes months before new staff relieve the workload, and training new staff first adds work.

**Reading the system:** Adding overtime relieves the queue this week, but strengthens the rework loop. The delay in hiring makes managers cut corners in the meantime.

**Leverage points:** Reduce rework with a short checklist and training, which weakens the reinforcing loop, and start hiring earlier to shorten the delay.

## Common patterns

| Pattern | Description |
| --- | --- |
| Fixes that fail | A quick fix has a side effect that brings the problem back |
| Shifting the burden | A symptom fix reduces the effort to find the real solution |
| Limits to growth | Growth meets a limit, such as capacity or market size |
| Escalation | Two parties respond to each other's actions with more of the same |
| Tragedy of the commons | Individuals using a shared resource each gain, but the group loses |

## Pitfalls

- **Drawing everything.** A diagram with fifty variables explains nothing; keep it to the key ones.
- **Boxes without direction.** Mark arrows with signs.
- **Ignoring delays.** They explain overshoot and oscillation.
- **Blaming one party.** Look for the structure that makes the pattern.
- **Stopping at the diagram.** Use it to choose an experiment.
- **Treating it as fact.** A causal loop diagram is a hypothesis to test.

## Quick checklist

- [ ] Problem described as a pattern over time
- [ ] Boundary set
- [ ] Key variables listed
- [ ] Arrows drawn with + and - signs
- [ ] Loops identified as reinforcing or balancing
- [ ] Delays marked
- [ ] Leverage points chosen and tested

## Related

- [Second-order Thinking](second-order-thinking.md): follow the effects of one decision through the system
- [Five Whys](../root-cause/five-whys.md): for simpler, linear causes
- [Fishbone Diagram](../root-cause/fishbone.md): list causes before you map how they interact
