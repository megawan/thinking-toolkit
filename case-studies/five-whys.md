# Case study: Invoices sent twice to customers

> Illustrative scenario. It is a composite written to show the method in use, not a report about a real organisation.

Method: [Five Whys](../methods/root-cause/five-whys.md)

## Context

A small software company sent duplicate invoices to about 40 customers in one month. Finance spent days apologising and issuing credit notes. The first fix, a reminder to double-check the export, did not stop it recurring the next month.

## What was done

- Why were invoices duplicated? The billing export ran twice on the same day.
- Why did it run twice? One run was scheduled, and one was started by hand after the scheduled run looked stuck.
- Why did it look stuck? The job gives no progress indicator and takes 40 minutes.
- Why was there no indicator? The job was written as a quick script and never reviewed as a production process.
- Why not reviewed? Finance-facing scripts had no owner in engineering.

## Outcome

The team added a lock that blocks a second run, a progress message, and an owner for finance scripts. No duplicates occurred in the next six months of invoicing.

## Lessons

- The first answer (human error) pointed to a reminder; the fifth pointed to ownership
- Each answer was checked against job logs, not assumed
- One action fixed the cause, another contained the symptom

Companion files: [cheat sheet](../cheatsheets/five-whys.md) · [worksheet](../worksheets/five-whys.md)
