> Reference for `task-closeout`.

# Handoff

Use when the user asks for a handoff, session summary or notes for whoever
continues. Give it as a reply, or as an update to the repository's existing
continuation record. Create a new file only when asked, and don't commit it
unasked.

Write what the next person can't get from the repository:

- **Objective and status:** the goal, and whether it is done, in progress or
  blocked (and on what).
- **What changed:** the commit range, not a file list the diff already shows.
- **Decisions:** what you chose, what you rejected and why, what is still open.
- **Evidence:** each check run with its result, the checks not run, and each
  one's limits. Mark every claim verified, inferred or unknown.
- **Next steps:** what to read first and the commands to run.

Point to specs, plans, issues and commits by path or URL; don't copy them in.
Redact keys, passwords and personal data. Be plain about known bugs and debt.

```text
BAD   Worked on the export feature, mostly done, a few things left.
GOOD  Goal: CSV export respects filters. Done: filter plumbing (a1b2c3..d4e5f6).
      Open: rows past 1,000 are dropped (repro in #212, not yet fixed).
      Ran: bun test export (pass); not run: the browser flow.
      Start at src/export/stream.ts.
```
