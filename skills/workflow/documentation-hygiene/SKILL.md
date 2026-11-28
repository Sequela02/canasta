---
name: documentation-hygiene
description: Decide where a document belongs, whether it should exist, and what to merge, move or retire. Use before creating a durable doc or ADR, when moving or generating docs (including a library, SDK or CLI docs set and files for agents), when a docs folder has stale, duplicated or misplaced pages, and when copies of settings, editor config or agent instructions drift from their source. Not for closing a task (task-closeout) or for the prose itself (technical-writing).
tags:
  - documentation
  - maintenance
metadata:
  source: "documentation-and-adrs by Addy Osmani, addyosmani/agent-skills e997ac5"
  changes: "ADR rules (match the existing convention, mark superseded, never delete) from documentation-and-adrs; the rest is canasta's"
---

# Documentation hygiene

Keep a repository's docs useful to the people who read them. Work on the scope
you were given and the docs this task touched; finishing a task is not a license
to clean up the whole repository.

## Before you write a document

1. **Find the owner.** Read the repository guidance and the docs entry points.
   Name the reader, the purpose and how long it will stay true. Update the
   existing page before creating a parallel one.
2. **Ask whether it needs to exist.** Code, types and tests already record what
   was built. Write what a maintainer would get wrong without it: a reason, a
   constraint that spans components, a trap the source hides. Skip field lists,
   file catalogs, narrated control flow and change summaries; they drift.

   ```text
   BAD   docs/export.md: "export.ts has three functions: start, stream, finish."
   GOOD  docs/export.md: "Rows are streamed in 1,000-row pages because the
         billing API times out on larger requests."
   ```

3. **Sort what you hold.** A plan, report, transcript or scratch note an agent
   produced is not permanent for that reason. Keep working notes in private
   project state or a temp folder, outside tracked docs.
4. **Check the audience.** Access to a repository is access to its system, not
   to the organization behind it. The repository holds what someone with only
   that access needs to understand, run, change and contribute to the system.
   Other projects and clients, strategy, finances, internal infrastructure
   (hosts, accounts, secret-store names, an operator's machine and paths), real
   personal data and session history go to the organization's private store. A
   folder called `internal`, a dot directory or an ignore rule is not privacy.
   When a private record backs a decision, keep a self-contained summary in the
   repository with no link or id to the record: a reference can expose what it
   names.

## Keep the set healthy

- **Verify before you retire.** Check each claim against the code or tests. An old
  date, a TODO or a broken link is a reason to look, not to delete. Mark the page
  keep, update, merge, move or retire by its content, its readers and any
  retention duty.
- **Merge into the owner.** Move unique content into the canonical page and link
  to it. When the code changes what a page says, rewrite that text; don't append
  a second account beside it.
- **Generated docs have one source** and a check that regenerates them and fails
  on a diff. Edit the source, never the copy. For any file with copies (docs,
  settings, editor config, agent instructions), check each copy against its
  source with [sources-and-copies.md](references/sources-and-copies.md).
- **Examples use invented names** and reserved domains (`example.com`, `.test`,
  `.invalid`). Test reports, logs and snapshots carry the machine's paths and
  user names: neutralize them before committing.
- **Decisions.** Record one only when it is hard to reverse, surprising without
  context and a real trade-off; a paragraph is enough. Follow the project's
  existing ADR location, numbering and headings before inventing any. Mark a
  replaced decision "superseded by" the new one; keep the old text.
- **Finished plans** stay only while their evidence or obligations matter.
  Promote the conclusion to the owner page, then retire the plan. An archive
  folder is not a place to hide clutter.

## Close out

1. Update links, indexes and build references for every move or removal. Keep a
   redirect only for a published link that others rely on.
2. Run the link check and the docs build, regenerate generated docs and confirm
   no diff, run the examples' check, and `git diff --check`. Follow any changed
   setup steps as written from a clean checkout. A tidy tree doesn't prove the
   docs are right.

Load a reference only for its task:

- Reviewing or trimming agent instructions or skills:
  [instruction-review.md](references/instruction-review.md).
- Auditing what an existing repository holds against step 4:
  [repository-audit.md](references/repository-audit.md).
- Placing, moving or retiring pages, examples or agent files of a library, SDK or
  CLI docs set: [developer-docs-site.md](references/developer-docs-site.md).

For the rest of closing a task use `task-closeout`; for prose, `technical-writing`;
for Git and line-ending drift, `line-ending-drift`. This skill grants no
authority to publish, rewrite history or delete beyond the user's task.
