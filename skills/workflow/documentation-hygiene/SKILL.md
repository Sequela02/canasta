---
name: documentation-hygiene
description: Place, consolidate, or retire repository documentation and task
  artifacts; use before creating durable docs, when closing work that created
  files, or when auditing stale, duplicated, or misplaced material.
tags:
  - documentation
  - maintenance
  - artifacts
---

# Documentation Hygiene

Keep repository documentation useful to its intended readers. Apply this
procedure to the requested scope and files created or changed by the task;
ordinary task completion does not authorize a repository-wide cleanup.

Before creating or retaining a document:
1. Read the repository guidance, documentation entry points, and relevant
   existing owners. Identify the reader, purpose, sensitivity, expected lifetime,
   and canonical destination. Prefer updating the existing owner to creating a
   parallel explanation. Do not create folders or templates just to fill a taxonomy.
2. Distinguish maintained documentation, durable decision or evaluation evidence,
   requested deliverables, and temporary working state. A plan or report is not
   automatically permanent because an agent produced it. Keep scratch notes,
   transcripts, intermediate reports, and task bookkeeping in the configured
   private project state or an appropriate temporary location outside tracked
   documentation.
3. Decide whether content belongs in the repository before writing it. Contributor
   guides, architecture, and public design discussions can be legitimate public
   docs. Private operational details, personal paths, or session context require
   an appropriate private destination or a sanitized public explanation. A folder
   named internal, a dot directory, or an ignore rule does not establish privacy.
   An explicit requested deliverable still needs an appropriate audience and home.

Maintain the collection:
- Organize by reader need and existing conventions: learning, doing, reference,
  explanation, and consequential decisions may need different forms. Keep the
  README useful for orientation and navigation. Do not impose a universal folder
  tree, language, filename style, or document length over project requirements.
- Verify current claims against their source owners. Dates, TODO markers, file
  extensions, and missing links are investigation signals, not deletion criteria.
  Classify affected material as keep, update, merge, move, or retire using content,
  unique value, consumers, and retention obligations.
- Consolidate unique information into its canonical owner and link to it. Prefer
  generated references for mechanically derived facts when the project supports
  them; retain human explanation that adds value. Do not delete generated outputs
  required by a published contract, build, or distribution.
- Preserve significant decision rationale and future-useful migration or evaluation
  evidence. Mark superseded decisions honestly rather than rewriting history.
  Completed plans need retention only when their remaining evidence or obligations
  justify it. Promote useful conclusions before retiring obsolete task records;
  do not move clutter into an archive merely to hide it.

Close the task:
1. Inspect the diff and newly created files, including untracked artifacts from
   this task. Remove task-created scratch files once they have no remaining use.
   Keep user work and unknown-origin files intact until ownership and disposition
   are established. Never use broad clean/reset commands to manufacture a clean
   worktree. Honor legal, audit, release, and repository retention requirements.
2. Review public-facing additions for private material and unsupported completion
   claims. If sensitive material is already committed or published, removing the
   working copy alone does not repair that exposure; surface it for the appropriate
   security response without reproducing the sensitive content.
3. Update links, indexes, build references, and affected consumers with moves or
   removals. Preserve redirects only for a real published-link compatibility need;
   otherwise remove the old path instead of leaving duplicate documents.
4. Run repository link checks and documentation builds when affected, verify
   changed claims against code or tests, and run git diff --check. Report the useful
   changes and material gaps in the requested response, not a new cleanup report
   by default. A tidy tree is not proof that documentation is accurate.
5. If the user corrected the same mistake twice during the work, propose where
   to make it impossible, at the highest level that works: structure (one
   owner, one supported way), then types, then a lint or check whose error
   names the fix, then a test, and a written rule last, only for a judgment
   call. Show the check failing on the real mistake. Do the approved
   enforcement as its own task, not inside this one.

Load a reference only for its task:
- Reviewing, writing, or trimming project-owned agent instructions or skills
  from repository evidence:
  [instruction-review.md](references/instruction-review.md).
- A handoff or session summary for whoever continues the work:
  [handoff.md](references/handoff.md).
- Retiring a branch, worktree, or remote ref:
  [branch-retirement.md](references/branch-retirement.md). Local and remote
  deletion each need their own explicit authorization.

Use clear-writing for prose, research for external evidence, and repository-text-hygiene
for Git, encoding, and line-ending drift. This procedure grants no publication,
history-rewrite, or deletion authority beyond the user's task.
