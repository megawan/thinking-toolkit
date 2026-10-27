# Case study: The problem of points, 1654

> Documented example. It is based on the source listed below, and the details are limited to what that source reports. It illustrates the expected-value half of this method; it does not cover opportunity cost.

Method: [Expected Value and Opportunity Cost](../methods/decision-making/expected-value-and-opportunity-cost.md)

## Context

The "problem of points", also called the division of the stakes, is a classic puzzle of early probability. Two players with equal chances of winning each round put equal amounts into a pot and agree that the first to win a set number of rounds takes everything. The game is interrupted before anyone has won. How should the pot be divided?

Around 1654 the Chevalier de Méré (Antoine Gombaud) posed the problem to Blaise Pascal, who discussed it in correspondence with Pierre de Fermat.

## What was done

**Earlier answers.** Luca Pacioli (1494) divided the pot in proportion to the rounds already won. Niccolò Tartaglia saw that this gives absurd results: if the game stops after one round, the winner of that round would take everything. He proposed dividing by the ratio of the size of the lead to the length of the game, which is still flawed: in a game to 100, a 65-55 lead and a 99-89 lead would get the same split, though the first is still open and in the second the leader is almost certain to win. Tartaglia doubted that any division could convince both players that it was fair.

**Pascal and Fermat's shared insight.** The fair split should depend less on what has already been played than on the ways the game could have continued. What matters is how many rounds each player still needs. The source gives an example: a 7-5 lead in a game to 10 gives the same chance of winning as a 17-15 lead in a game to 20, so both interruptions should produce the same split.

**Fermat's method.** If one player needs r more rounds and the other needs s, someone is certain to have won after r + s - 1 further rounds. Imagine playing exactly that many rounds, even if the game would really have ended sooner. That gives 2^(r+s-1) equally likely outcomes. Count how many favour each player and divide the pot in that proportion.

**Pascal's method.** Imagine one more round is played. If the fair split is already known for each of its two possible results, and the players are equally likely to win the round, they should take the average of the two. Repeating this builds the answer for games with many rounds left from games with fewer left. The source describes this as one of the earliest uses of expected values.

## Outcome

The correspondence between Pascal and Fermat is regarded as a starting point for the mathematical theory of probability. The source says the idea later underpinned Huygens's 1657 treatise on games of chance.

## Lessons

- A fair value is the probability-weighted average of the possible outcomes
- What has already happened matters only through what is still left to play; the past score is not what decides the split
- Both methods give the same answer, but one counts outcomes and the other averages step by step
- The approach replaced rules of thumb (proportion to wins so far) that fail in simple cases

## Caveats

- The source is a Wikipedia article, a secondary summary; the original letters were not read for this entry
- The page gives no numerical worked example of a pot division, so none is given here
- This case covers expected value only. Opportunity cost is not part of it.

## Sources

- [Problem of points](https://en.wikipedia.org/wiki/Problem_of_points), Wikipedia (page revision of 26 May 2026)

Companion files: [cheat sheet](../cheatsheets/expected-value-and-opportunity-cost.md) · [worksheet](../worksheets/expected-value-and-opportunity-cost.md)
