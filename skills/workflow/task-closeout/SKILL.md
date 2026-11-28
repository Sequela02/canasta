---
name: task-closeout
description: Close out a task before calling it done. Remove the scratch files and processes it started, check the diff for private material and claims no check supports, write a handoff for the next session, or retire a finished branch or worktree. Use when finishing work, when asked for a handoff or session summary, or before deleting a branch.
tags:
  - workflow
  - artifacts
  - handoff
metadata:
  source: "handoff by Matt Pocock, mattpocock/skills bbadaa6; finishing-a-development-branch by Jesse Vincent, obra/superpowers 22f0b46"
  changes: "References only: the handoff rules (point to records, redact secrets) and the worktree-removal refusal rule; the procedure is canasta's"
---

# Task closeout

Leave the tree with the task's useful changes and nothing else, and leave the
next person what they can't reconstruct. This covers the files and processes
this task made; it is not a repository-wide cleanup.

1. **Inventory.** List the diff and every new file, untracked ones too. Mark each
   one kept, removed or someone else's.
2. **Remove what you started.** Stop the servers, watchers and processes the
   task started and close its browser tabs, even if the task failed. Delete the
   scratch files and generated media you made and no longer need. Leave
   files of unknown origin alone and ask whose they are. Run no broad `clean`
   or `reset` to make the tree look tidy.
3. **Check what goes public.** Read the additions for personal paths,
   credentials, session context, private project or client names and internal
   infrastructure (hosts, accounts, secret-store names, private repositories),
   and for "done" claims no check supports. Editing published text doesn't
   unpublish it, and a removed secret stays in history: flag it for a security
   response without repeating the secret in your reply.
4. **Docs.** If the task touched documentation, run the close-out checks in
   `documentation-hygiene`.
5. **Report** the useful changes, each check you ran with its result, and what
   is still open. Name a check you skipped.
6. **Repeated correction.** If the user corrected the same thing twice, find why
   the instructions missed it and propose a safeguard where a tool can enforce
   it (a test, a lint rule, a hook). Ask before adding enforcement beyond the
   task.

Load a reference only for its task:

- Handoff or session summary: [handoff.md](references/handoff.md).
- Deleting a branch, worktree or remote ref:
  [branch-retirement.md](references/branch-retirement.md). Local and remote
  deletion each need their own explicit authorization.

Done when every file the task created is kept with a reason or removed, the diff
holds no private material and no unsupported claim, and the reply lists the
checks run and the gaps left. This skill grants no authority to publish, rewrite
history or delete beyond what the user asked.
