# Five Whys

> Ask "why?" again and again until you reach a cause you can fix, not just a symptom you can patch.

| | |
| --- | --- |
| **Category** | Root cause analysis |
| **Time needed** | 15-30 minutes, solo or with a small group |
| **Best for** | Recurring problems with a fairly linear chain of causes |

## What it is

Five Whys is a root cause analysis technique. You start from a specific problem and ask why it happened. You then ask why about that answer, and keep going until the answer points to something in a process, system, or decision that you can change.

It was developed by Sakichi Toyoda and used inside Toyota Motor Corporation as part of its manufacturing method. It later became a core tool in lean manufacturing, Six Sigma, and, more recently, incident reviews in software teams.

The number five is a rule of thumb. Some problems reach a root cause in three questions, others need seven. The real stopping rule is: **stop when the answer is something you can act on and that, if fixed, prevents the problem from coming back.**

## Why it works

Most fixes target the first visible cause. That treats the symptom, so the problem returns in a different form. Asking why repeatedly forces the conversation past the immediate trigger and into the conditions that allowed it, which are usually missing checks, unclear ownership, or gaps in a process.

## When to use

- The same problem keeps coming back after being "fixed"
- A failure happened and you want to prevent a repeat, not just recover
- The problem is small to medium in scope
- You need a quick, low-cost analysis without special tools
- A team needs a shared, blame-free way to discuss what went wrong

## When not to use

- The problem has many interacting causes (consider a fishbone diagram or fault tree instead)
- You lack facts about what happened; gather evidence first
- You need statistical proof of a cause

## How to apply

1. **Gather the right people.** Include those who were close to the problem. One person's view of the chain is usually incomplete.
2. **Write a specific problem statement.** Describe what was observed, where, and when. "Deploys are slow" is vague. "Friday's deploy took 4 hours instead of 20 minutes" is workable.
3. **Ask the first why.** Why did this happen? Answer with something that is true and can be checked.
4. **Check the answer against evidence.** Logs, data, timelines, or direct observation. If you cannot verify it, mark it as a guess and go verify.
5. **Ask why about that answer.** Write it down as the next link in the chain.
6. **Repeat** until you reach a cause that is a process, system, or decision rather than a person's mistake or an unlucky event.
7. **Test the chain in reverse.** Read it from the root cause up, using "therefore". If each step follows, the chain holds.
8. **Define actions.** One to fix the root cause, and where useful, one to contain the symptom now and one to detect it earlier next time.
9. **Assign an owner and a date** to each action, and follow up.

## Writing good whys

| Weak | Better |
| --- | --- |
| "Because Sam made a mistake." | "Because the deploy step has no confirmation, so a wrong target is easy to select." |
| "Because we were busy." | "Because two releases were scheduled in the same week with one reviewer." |
| "Because it is a bad system." | "Because the report is exported manually and has no validation." |

If the answer names a person, ask one more why: what allowed that mistake to happen and go unnoticed?

## Example 1: Website outage

**Problem:** The website was down for 30 minutes on Tuesday at 14:00.

1. Why was it down? The server ran out of disk space.
2. Why was the disk full? Log files had grown to 80 GB.
3. Why did the logs grow unchecked? Log rotation was not running.
4. Why was it not running? The scheduled job was lost during the server migration last month.
5. Why was it lost? The migration had no checklist of existing scheduled jobs.

**Root cause:** No migration checklist.

**Actions:**

- Add a scheduled-jobs inventory step to the migration checklist (owner: ops, this week)
- Add an alert at 80% disk usage (owner: ops, this week)
- Restore log rotation (done)

## Example 2: Branching chain

Real problems often have more than one cause. When an answer has two valid causes, follow both.

**Problem:** A customer received the wrong item.

1. Why? The picker took the wrong product.
   - 1a. Why? Two products have near-identical packaging.
   - 1b. Why? The shelf label did not match the product in that slot.
2. (From 1a) Why was nothing done about similar packaging? No one owns product-packaging risk review for new items.
3. (From 1b) Why was the label wrong? Shelf labels are updated by hand when stock is rearranged.

**Root causes:** No packaging review for new items; manual label updates.

**Actions:** Add a packaging check to the new-product process; print labels from the inventory system.

## Example 3: A non-technical problem

**Problem:** Team meetings regularly run 30 minutes over.

1. Why? Discussions drift away from the agenda.
2. Why? There is no clear owner keeping to time.
3. Why? The meeting has no designated facilitator.
4. Why? The role was never defined when the meeting was created.

**Root cause:** The meeting has no defined facilitator role.
**Action:** Rotate a facilitator each week, with timeboxes on the agenda.

## Pitfalls

- **Stopping at a person.** "Alex forgot" is not a root cause. Ask what made forgetting possible.
- **Answering from assumption.** Every link should be backed by evidence or marked for verification.
- **Jumping to a solution early.** Finish the chain first, then decide on actions.
- **Following only one path.** If an answer has several causes, branch.
- **Going too far.** "Because humans are imperfect" is not actionable. Stop where you can still change something.
- **Skipping follow-up.** An analysis with no owned actions changes nothing.
- **Leading questions.** Ask "why did this happen?" rather than "was it because of X?".

## Quick checklist

- [ ] Problem stated as a specific, observable fact
- [ ] Every answer verified or flagged as a guess
- [ ] Final cause is a process, system, or decision
- [ ] Chain reads correctly in reverse
- [ ] Actions have owners and dates

## Related

- [Lateral Thinking](lateral-thinking.md): use it after the root cause is known, when the fix is not obvious
