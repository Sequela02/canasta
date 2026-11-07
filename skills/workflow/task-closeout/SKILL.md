---
name: task-closeout
description: Close out a task before saying it is done; remove the scratch files it created, check the diff for private material and unsupported claims, write a handoff, or retire a branch or worktree. Use when finishing work, when asked for a handoff or session summary, or before deleting a branch. Not for where docs belong (documentation-hygiene).
tags:
  - workflow
  - artifacts
  - handoff
---

# Task closeout

Leave the tree with the task's useful changes and nothing else, and leave
the next person what they cannot reconstruct. Apply this to the files this
task created or changed; finishing a task does not authorize a
repository-wide cleanup.

1. **Inventory.** Inspect the diff and new files, including untracked ones.
   Mark each as kept, removed, or someone else's.
2. **Stop and remove what you started.** Stop the processes, servers and
   watchers the task started, and close its browser tabs, also when the task
   failed or was cancelled. Delete task-created scratch files and generated
   media that have no remaining use. Keep user work and files of unknown origin until their
   owner and disposition are known. Never use broad clean or reset commands
   to make the tree look clean. Honor legal, audit, release and repository
   retention requirements.
3. **Check what goes public.** Review additions for private material
   (personal paths, credentials, session context) and for completion claims
   no check supports. If sensitive material is already committed or
   published, removing the working copy does not repair it: surface it for a
   security response without reproducing it.
4. **Docs.** When the task touched documentation, finish
   `documentation-hygiene`'s close-out checks.
5. **Report.** Give the useful changes, the checks run with their results,
   and the material gaps in the reply. Not a new cleanup report by default.
6. **Learn from repeats.** When the same correction came up again, find why
   the existing feedback missed it and propose a safeguard where it belongs
   (a validation rule, clearer ownership, better instructions), with what it
   would catch and what it leaves to judgment. Get approval before adding
   enforcement beyond the task.

Load a reference only for its task:

- A handoff or session summary for whoever continues:
  [handoff.md](references/handoff.md).
- Retiring a branch, worktree or remote ref:
  [branch-retirement.md](references/branch-retirement.md). Local and remote
  deletion each need their own explicit authorization.

## Done when

- every file the task created is kept with a reason, or removed;
- the diff holds no private material and no unsupported claim;
- the reply lists the checks run and the gaps left.

This procedure grants no publication, history-rewrite or deletion authority
beyond the user's task.
