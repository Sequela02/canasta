---
name: problem-clarification
description: "Pin down what a request actually means when you're not sure, or grill me on an idea or proposal before building it: find the open decisions, ask about them in rounds with a recommendation each, and stop when the answers no longer change the work. Skip a clear, small request."
tags:
  - engineering
  - requirements
  - decisions
metadata:
  source: "grilling by Matt Pocock, mattpocock/skills bbadaa6; interview-me by Addy Osmani, addyosmani/agent-skills e997ac5"
  changes: "Rounds ask only the decisions whose prerequisites are settled, each with a recommendation (grilling); a stated guess that the user corrects (interview-me); investigation before asking, small budgeted experiments and a stop rule tied to whether the answer changes the work are this pack's own"
---

# Problem clarification

Use it when an unanswered question would change what you build, and when the
user asks to be grilled or to have a proposal stress-tested. For a small,
clear request, do the work. A request to write an issue or PR needs no
interview.

## Procedure

1. Write a one-sentence guess of what the user wants, and what you can't tell
   yet. It is the thing they will correct.
2. Look before you ask. Read the code, docs, issues and decisions that touch
   the request, and treat earlier drafts and agent notes as claims to check.
   Ask only what the repository can't tell you.
3. List the open decisions and which ones depend on others. Rank them by how
   much the answer changes the outcome, scope or acceptance check.
4. Ask a round: every decision whose prerequisites are already settled, and
   no others. Number the questions. Give each a recommended answer and its
   tradeoff, worded so "yes" accepts it. Keep to the decisions that matter,
   usually two to five.
5. Use the answers to redraw the list. A question that was waiting on another
   moves into the next round. Keep working on whatever the open questions
   don't block.
6. When only running code can answer a question, run one small experiment with
   a stated budget and the result that would settle it. Keep it out of the
   deliverable and record what it showed.
7. Stop when the remaining doubt wouldn't change the outcome or the next safe
   step. Hand back: the problem, the acceptance check, what is out of scope,
   and any decision still open. Then continue the authorized work.

A user's silence is not an answer, so keep the question open or park the work
that depends on it. "Whatever you think" is delegation: offer two concrete
options and a recommendation. A choice within the authorized scope is yours to
make; report it.

## Example

Request: "Add export to the reports page."

```text
Guess: a button that downloads what the page shows. Unclear: format,
whether filters apply, who may export.
Found in the repo: reports are already built as rows in reports/query.ts,
and the page has no auth beyond login.

Q1 - Format: CSV, or also XLSX?
-> CSV only; no XLSX library is installed, and the rows are flat.

Q2 - Scope: the filtered rows, or the whole report?
-> Filtered rows, so the file matches the screen.

Held for the next round: row limit (depends on Q2).
```

"Who is the user?" is not asked: the repository answered it.

## Related

Overloaded terms go to `domain-modeling`; outside evidence to `research`;
sequencing a settled goal to `implementation-planning`. Record durable
decisions where the repository already keeps them. A hypothesis is not a
confirmed cause, and agreement with a proposal does not show it works.
