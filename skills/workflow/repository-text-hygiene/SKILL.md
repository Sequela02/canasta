---
name: repository-text-hygiene
description: Diagnose and repair Git, encoding, line-ending, formatter, or
  editor drift while preserving real changes; use for mass text rewrites or
  disagreement between status and diff.
tags:
  - git
  - maintenance
  - text
---

# Repository Text Hygiene

Establish the cause of text drift before modifying files or configuration.

1. Inspect repository guidance, .gitattributes, .editorconfig, formatter rules,
   hooks, and CI. Inspect only relevant Git settings and their origins; avoid
   dumping unrelated configuration that may contain credentials. Compare status,
   unstaged and staged diffs, and numstat; inspect attributes for representative
   paths. A large status count does not authorize normalization.
2. Separate real edits, intentional generated changes, line-ending differences,
   and index/stat noise. Compare a suspicious path's index blob with its filtered
   working-tree hash, using git hash-object --path for that same path. Equality
   supports refreshing that path's index metadata; it does not prove the entire
   worktree is safe to stage. Preserve staged/unstaged boundaries and user work.
3. Keep encoding and line-ending policy in repository configuration. Prefer UTF-8
   without BOM and LF for text when establishing a policy, but inspect platform
   entry points, binary files, raw-byte fixtures, and digest contracts first.
   Respect required exceptions. Align editor, formatter, and Git attributes rather
   than repeatedly rewriting files or changing global Git defaults. Use
   non-mutating CI checks and explicit formatter application.
4. Repair only diagnosed paths within scope. Never use git reset --hard, broad
   checkout/restore, or git clean to clear status noise. Refresh the index only
   for individually verified byte-equivalent paths. Reserve bulk renormalization
   for an isolated change with unrelated work preserved, reviewed attributes, and
   the complete normalization diff inspected. Do not stage unrelated changes.
5. Verify remaining status against actual diffs and intentional untracked files,
   inspect staged changes, and recheck representative bytes and attributes. Run
   git diff --check, applicable formatter checks, and affected build or digest
   checks. Refresh the IDE view if it still disagrees with Git; report unresolved
   discrepancies rather than rewriting files to make the display quiet.

Use documentation-hygiene for document ownership and lifecycle. This procedure
does not choose a repository's language, directory layout, release policy, or
global tool configuration.
