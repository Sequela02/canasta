> Reference for `task-closeout`.

# Branch retirement

Deleting a branch can't be undone in practice. Delete only when its evidence
is kept, nothing depends on it, and a person authorized the deletion.

Agree the retirement criteria when the branch is created: what promotion looks
like (the merge, release or adoption that ends it), what evidence must outlive
it, and who authorizes deletion. A branch without them waits until they are
written down.

## Check every item, then report what you found

1. The work landed in its destination, or was abandoned and that is recorded.
2. The decisions, rationale and verification results live somewhere that
   outlives the branch. A merged PR alone doesn't prove it.
3. No open PR targets or comes from the branch.
4. No branch is based on it, no worktree uses it, no session works on it.
5. A person authorized deleting the local branch and, separately, the remote ref.

```bash
git worktree list                          # worktrees using it
git branch --contains <branch>             # branches based on it
gh pr list --head <branch> --state all     # PRs from it
gh pr list --base <branch> --state all     # PRs into it
git log --oneline <destination>..<branch>  # unmerged work
```

A non-empty last log is unpromoted work: don't retire the branch and don't call
it merged.

## Delete

```bash
git branch -d <branch>                 # refuses unmerged work; keep it that way
git push origin --delete <branch>      # needs its own authorization
```

If `-d` refuses, a check above is unmet. Surface it; don't switch to `-D`.
If `git worktree remove` refuses because of modified or untracked files, those
files exist nowhere else: list them with `git -C <path> status --porcelain`,
ask whether to commit, move or delete them, and never add `--force` on your own.

## Don't

- Delete a branch because it looks old or stale.
- Bulk-delete merged branches without checking worktrees and dependents.
- Treat approval to delete locally as approval to delete the remote.
