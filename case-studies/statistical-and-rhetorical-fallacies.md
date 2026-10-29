# Case study: Two famous errors with numbers

> Documented examples. They are based on the sources listed below, and the details are limited to what those sources report. The first concerns real people and a court case; it is described briefly and factually.

Method: [Statistical and Rhetorical Fallacies](../methods/critical-thinking/statistical-and-rhetorical-fallacies.md)

## Part 1: The "1 in 73 million" in the Sally Clark trial

### Context

Sally Clark, an English solicitor, lost two infant sons: Christopher in December 1996 and Harry in January 1998. She was charged with murder and the defence argued that both were cases of sudden infant death syndrome (SIDS, or "cot death"). At her trial at Chester Crown Court, which began in October 1999, the paediatrician Sir Roy Meadow testified that the chance of two children in an affluent family both dying of SIDS was 1 in 73 million. She was convicted in November 1999 by a majority verdict.

### What was done

The figure came from multiplying a single-death probability by itself. For a family such as the Clarks, Meadow put the chance of one cot death at about 1 in 8,543 and multiplied 8,543 by 8,543. He added that, given about 700,000 live births a year in the United Kingdom, a double cot death would be expected about once every hundred years, and compared it with backing an 80-to-1 outsider in the Grand National four years running.

### Outcome

Statisticians identified problems in how the number was derived and used:

- **An unsupported independence assumption.** Multiplying the two probabilities assumes that two cot deaths in one family are independent. The Royal Statistical Society said in October 2001 that there was "no statistical basis" for the figure, and in January 2002 that the calculation was false. It noted strong reasons to think the assumption wrong, because unknown genetic or environmental factors might make a second case more likely. A later analysis by the statistician Ray Hill, using English SIDS data, found that the chance of a second cot death rose by a factor of about 5 to 10 after a first.
- **The prosecutor's fallacy.** Press reports treated 1 in 73 million as the probability that Clark was innocent. Even if valid, it was not that. The jury needed to weigh the competing explanations against each other: double SIDS is very rare, but double infant murder is rarer still.

The conviction was upheld at a first appeal in October 2000. After the Criminal Cases Review Commission referred it back, it was overturned in January 2003 and Clark was released. The main ground was that a pathologist had not disclosed microbiology results suggesting a natural death. On the statistics, the Court of Appeal noted that Meadow's calculation had qualifications not mentioned to the jury, so the headline figure would be uppermost in jurors' minds, and said the evidence should never have been before the jury in the way it was. The Attorney General ordered a review of other cases involving multiple infant deaths, and some convictions were overturned or ended in acquittal.

### Lessons

- Multiplying probabilities is only valid if events are independent; check that before you multiply
- A very small probability for the evidence does not give the probability of guilt; compare it with the probability of the alternative explanation
- A vivid analogy (an 80-to-1 outsider winning four years running) can make a weak number sound decisive
- Experts need to state the limits of a calculation, and decision-makers need to ask for them

## Part 2: Monte Carlo, 1913

### Context

On 18 August 1913, at the Monte Carlo Casino, the ball on a roulette wheel fell on black 26 times in a row. The page cited below puts the chance of 26 consecutive results of either colour on a single-zero wheel at about 1 in 68.4 million, assuming a fair wheel.

### What was done

Gamblers bet heavily against black, reasoning that the long run of black had unbalanced the wheel and that red had to follow.

### Outcome

The page says the gamblers lost millions of francs, and that the episode gave the error its alternative name, the Monte Carlo fallacy.

### Lessons

- Each spin of a fair wheel is independent, so the chance of black on the next spin is the same as on any spin
- A streak is not "due" to end; the odds before the first spin of a run differ from the odds on the next one
- A very long streak can be evidence that the wheel is biased; betting on the streak is then a reasonable inference, not the fallacy
- The error is common in other settings too, and the page also mentions the opposite error of expecting a streak to continue (the hot-hand fallacy)

## Caveats

- Both parts rest on Wikipedia articles, which are secondary sources; the original court judgment, the Royal Statistical Society letters and Hill's paper were not read for this entry
- The Sally Clark page was read verbatim up to the end of the article body; the Gambler's fallacy page was read verbatim for the definition and the Monte Carlo section, and the rest, including studies of real-world decisions, was not used
- The Monte Carlo source's own citation was not seen, so the episode is described as the page reports it
- In the Clark case the conviction was overturned mainly because of undisclosed medical evidence, not because of the statistics alone

## Sources

- [Sally Clark](https://en.wikipedia.org/wiki/Sally_Clark), Wikipedia
- [Gambler's fallacy](https://en.wikipedia.org/wiki/Gambler%27s_fallacy), Wikipedia

Companion files: [cheat sheet](../cheatsheets/statistical-and-rhetorical-fallacies.md) · [worksheet](../worksheets/statistical-and-rhetorical-fallacies.md)
