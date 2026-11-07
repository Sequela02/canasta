---
name: documentation-hygiene
description: Place, consolidate, or retire repository documentation; use before
  creating a durable doc, when moving or generating docs (including a library,
  SDK or CLI docs set and files for agents), and when auditing stale,
  duplicated, or misplaced material. Not for closing a task (task-closeout)
  or for prose (technical-writing).
tags:
  - documentation
  - maintenance
---

# Documentation Hygiene

Keep repository documentation useful to its intended readers. Apply this
procedure to the requested scope and the docs the task created or changed;
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
  required by a published contract, build, or distribution. Every generated
  document has one source and a check that regenerates it and fails on a
  diff; never edit the generated copy.
- Preserve significant decision rationale and future-useful migration or evaluation
  evidence. Mark superseded decisions honestly rather than rewriting history.
  Completed plans need retention only when their remaining evidence or obligations
  justify it. Promote useful conclusions before retiring obsolete task records;
  do not move clutter into an archive merely to hide it.

Close out the docs:
1. Update links, indexes, build references, and affected consumers with moves or
   removals. Preserve redirects only for a real published-link compatibility need;
   otherwise remove the old path instead of leaving duplicate documents.
2. Run repository link checks and documentation builds when affected,
   regenerate generated docs and confirm no diff, run the doc examples' check,
   verify changed claims against code or tests, and run git diff --check. A tidy
   tree is not proof that documentation is accurate.

The rest of closing a task (scratch files, private material, handoffs,
branches) belongs to `task-closeout`.

Load a reference only for its task:
- Reviewing, writing, or trimming project-owned agent instructions or skills
  from repository evidence:
  [instruction-review.md](references/instruction-review.md).
- Placing, moving or retiring the pages, examples or agent files of a
  library, SDK or CLI docs set:
  [developer-docs-site.md](references/developer-docs-site.md).

Use technical-writing for prose and page content (its developer-docs reference
for library and CLI docs), research for external evidence, and repository-text-hygiene
for Git, encoding, and line-ending drift. This procedure grants no publication,
history-rewrite, or deletion authority beyond the user's task.
