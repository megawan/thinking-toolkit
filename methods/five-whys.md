# Five Whys

**Category:** Root cause analysis

## What it is

Ask "why?" repeatedly, starting from a problem, until you reach a cause you can actually fix. Five is a rule of thumb, not a quota: stop when the answer is a process or system issue rather than another symptom.

## When to use

- A problem keeps coming back after "fixes"
- You suspect the obvious cause is only a symptom
- The problem is small to medium in scope and has a fairly linear cause

## How to apply

1. Write the problem as a specific, observable statement.
2. Ask why it happened. Answer with facts, not guesses.
3. Take that answer and ask why again.
4. Repeat until you reach a cause that is within your control to change.
5. Check the chain in reverse: if the root cause is fixed, does the problem go away?
6. Define an action for the root cause, and one to stop recurrence.

## Example

**Problem:** The website was down for 30 minutes.

1. Why? The server ran out of disk space.
2. Why? Log files filled the disk.
3. Why? Log rotation was not running.
4. Why? The cron job was removed during the last server migration.
5. Why? The migration had no checklist of existing scheduled jobs.

**Root cause:** No migration checklist.
**Action:** Create a migration checklist and add disk usage alerts.

## Pitfalls

- Stopping at a person ("Alex forgot") instead of a process
- Answering from assumption instead of evidence
- Following a single chain when the problem has several causes; branch when needed
- Using it for complex problems with many interacting factors

## Related

- [Lateral Thinking](lateral-thinking.md) for when the root cause is known but the fix is not obvious
