# Case study: Microsoft's error reports, 2002

> Documented example. It is based on the sources listed below, and the details are limited to what those sources report.

Method: [Pareto Analysis](../methods/prioritisation/pareto-analysis.md)

## Context

In the early 2000s, Microsoft's products such as Windows and Office could send error reports from customers' computers back to Microsoft, using a "minidump" function. The reports were collected on dedicated servers and used only for fixing bugs, and Microsoft said this protected customer privacy. In a security e-letter distributed in early October 2002, the company's president, Steve Ballmer, described what the reports showed.

## What was done

Microsoft counted errors reported by customers and traced them to their underlying bugs, so it could see which bugs accounted for the most errors. According to the report in Route Fifty (originally by GCN), Ballmer wrote that:

- About 20 percent of the software's bugs cause 80 percent of its errors
- About 1 percent of the bugs cause half of all errors

The same report says the error data also exposed faults in applications and drivers from other vendors, and that about 450 companies had access to the database of error reports for drivers, utilities and applications.

## Outcome

The main result described in the source is the shape of the distribution: a small share of causes produces most of the effect. This gives a direct basis for prioritising fixes: start with the few bugs that cause the most errors.

## Lessons

- Real data can show a steeper concentration than 80/20; here, 1 percent of bugs caused half the errors
- Counting at scale (error reports from customers) turns a feeling about quality into a ranked list
- A Pareto result shows where to focus, not why a bug exists
- The data helped partners too, since it exposed other vendors' problems

## Caveats

- The source defines neither "bug" nor "error" beyond how Ballmer used the terms
- Other coverage cites specific reductions in errors after later service packs for Windows XP and Office XP. Those figures were not found in the source read for this entry and are not repeated here.
- The article is short, and the original letter was not read directly for this entry

## Sources

- [Microsoft's Ballmer says 1 percent of software bugs cause 50 percent of errors](https://route-fifty.com/digital-government/2002/10/microsofts-ballmer-says-1-percent-of-software-bugs-cause-50-percent-of-errors/285949), Route Fifty (GCN), by Susan M. Menke, 3 October 2002

Companion files: [cheat sheet](../cheatsheets/pareto-analysis.md) · [worksheet](../worksheets/pareto-analysis.md)
