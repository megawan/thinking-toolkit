# Case study: An online service outage

> Illustrative scenario. It is a composite written to show the method in use, not a report about a real organisation.

Method: [OODA Loop](../methods/decision-making/ooda-loop.md)

## Context

An online service began returning errors for customers in one region shortly after a release.

## What was done

- Observe: error rates and support tickets rose within minutes, in one region only
- Orient: the change began 20 minutes after a release, and a similar pattern earlier had come from a database setting
- Decide and act: roll back the release for the affected region
- Observe: errors fell; the next loop confirmed the cause and checked for data damage

## Outcome

The service recovered within minutes because dashboards, a rollback procedure and clear authority were already in place. The team updated its playbook with the database check.

## Lessons

- The first orient step used past experience, and it could have been wrong; checking the result in the next loop caught that
- Pre-agreed authority shortened the decide stage
- The post-incident update improved orientation for next time

Companion files: [cheat sheet](../cheatsheets/ooda-loop.md) · [worksheet](../worksheets/ooda-loop.md)
