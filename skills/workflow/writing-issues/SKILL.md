---
name: writing-issues
description: Write or revise an issue, bug report or feature request for your own tracker, with who is affected, evidence, and acceptance criteria someone can check. Also turns notes or a plan into tickets. Use when asked to file or draft an issue, report a bug, or split work into tickets.
tags:
  - writing
  - engineering
  - issues
metadata:
  source: "triage AGENT-BRIEF and to-tickets by Matt Pocock, mattpocock/skills bbadaa6"
  changes: "Acceptance criteria, scope and durability rules from AGENT-BRIEF; vertical slices and blocking links from to-tickets; the reproduced-or-not rule is canasta's"
---

# Writing issues

For your own or your organization's tracker. For another project's, use
`upstream-contribution`. The issue describes the problem; `writing-pr`
describes the work that fixes it.

1. **Look first.** Read the request, the evidence, the repository's issue
   template and its contribution rules. Search for a duplicate (same problem)
   and for related issues (same area); link the related ones. Invent no ids,
   labels, priorities or links.
2. **Title and opening.** The title names the problem or the missing
   capability. The first lines say who is affected, what they hit and why it
   matters, in words someone outside this conversation can follow.

   ```text
   BAD   Fix export bug
   GOOD  CSV export drops rows after the first 1,000 when a filter is active
   ```

3. **A bug** gets: the smallest steps that reproduce it, the version or
   environment, expected versus actual, and the evidence (output, log, capture).
   Say whether you reproduced it yourself. Keep what you saw apart from what you
   suspect; a likely cause is a guess until a check confirms it.
4. **A feature** gets: the use case, the constraints, and the behavior wanted.
   Add a proposed solution only if you have one, and label it a proposal.
5. **Acceptance criteria** are things someone can check against the running
   system, written as behavior, not as files to edit. Name what is out of scope
   when a neighbor feature invites scope creep. For an investigation, state the
   question and the evidence that answers it.

   ```text
   BAD   Export should work correctly.
   GOOD  - [ ] Exporting 5,000 filtered rows produces 5,000 CSV rows.
         - [ ] Exporting with no filter is unchanged.
         Out of scope: the XLSX export.
   ```

   Describe interfaces and behavior; skip file paths and line numbers, which go
   stale before anyone picks the issue up.
6. **Splitting a plan** into several issues: one issue per slice that cuts
   through every layer and can be checked on its own (`implementation-planning`
   draws the slices). Give each its blockers, using the tracker's blocking link
   if it has one. Show the list and get it approved before creating anything.
7. **Before filing,** reread the title against the body, confirm the links work,
   and strip credentials, personal data and internal names (private
   repositories, hosts, secret stores) from the evidence. Return the draft; file
   it only when asked.
