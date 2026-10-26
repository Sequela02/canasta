---
name: writing-pr
description: Write or refresh a pull request title and body from the current
  aggregate change, with reviewer-relevant decisions, verification, and risks;
  use when preparing work for review.
tags:
  - writing
  - engineering
  - pull-requests
---

# Writing Pull Requests

Use for PR titles and bodies. Apply clear-writing for prose and visual
explanations. This procedure describes delivered work; writing-issues describes
the problem to solve. Neither owns branch, publication, or merge authority.

1. Establish the intended base and current candidate. Inspect the aggregate diff,
   linked issue or accepted objective, repository PR template, and contribution
   rules. Check whether a PR for the branch already exists, and inspect its
   metadata when updating. Verify claims inherited
   from commits or previous summaries; report unavailable material evidence.
2. Write the title and opening around the concrete problem and resulting behavior.
   A reviewer unfamiliar with the conversation should understand why this change
   exists. Follow repository naming conventions; recent merged PRs and history
   show them, and a PR title often becomes the merge commit. Name the effect
   that matters, not the mechanism. Do not promise unverified
   benefits in the title. Describe the final aggregate
   change, not intermediate attempts, session history, or transient line counts.
3. Explain mechanisms, meaningful tradeoffs, compatibility changes, and review
   focus only where the diff does not make their implications clear. Name affected
   boundaries and give a reading order when it materially helps. Do not invent
   rejected alternatives or narrate each changed file.
4. Use the smallest useful representation from clear-writing. For UI changes,
   prefer comparable real before/after captures; use a short recording when
   interaction or timing matters. Identify the states and revisions shown. Missing
   captures stay missing, never replaced by generated images presented as proof.
   Narration and diagrams explain behavior; they do not verify it.
5. Include relevant observed verification and material gaps once. Distinguish
   passed, failed, unrun, and pending checks; collect executable evidence with
   `tdd` and its end-to-end verification reference when it is missing. Never claim TDD from passing
   tests alone: a red/green claim needs an observed relevant failure and subsequent
   pass. Skip test inventories and generic claims that everything works.
6. For performance claims, show the actual baseline and candidate revisions,
   workload, conditions, units, and measurement uncertainty with the comparison.
   Use benchmark-readiness-review for claim validity. Missing comparable results
   mean the improvement is unverified; never fabricate a before/after table.
7. Preserve unresolved findings, meaningful residual risks, and required evidence
   even when concise. Respect repository templates; otherwise scale from a short
   paragraph and verification line to a structured explanation for complex work.
   Omit empty sections, repeated facts, raw metadata dumps, and ceremonial lists.
8. Reconcile the whole title and body with the current candidate after scope or
   implementation changes. Check every linked artifact exists and is suitable for
   its audience. Before publishing, check the title, body, quotes and
   attachments for secrets and private names. Return the draft or use the
   already authorized publication workflow (a real PR, not a draft, unless the
   repository says otherwise); do not add approval gates or infer authority
   from the skill.
9. End every PR with a risk note: one-way or two-way door, blast radius, and
   evidence. The agent never merges unless the project's stated policy allows it;
   passing checks and drafting a PR do not grant merge authority.
