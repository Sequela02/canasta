> Reference for `documentation-hygiene`, formerly the `branch-retirement` skill.

# Branch Retirement

A provisional integration branch is retired only when its evidence is preserved,
no consumer still depends on it, and a human has authorized the deletion.
Retirement is irreversible in practice; treat it as a destructive action.

## Retirement Criteria

Define the retirement criteria when the branch is created, not when someone
wants it gone. A branch without stated retirement criteria is not eligible for
retirement until they are written down and agreed.

Record, at minimum:

- what promotion looks like — the merge, release, or adoption that ends the branch
- what evidence must survive the branch
- who authorizes deletion

## Preconditions

Verify every item before proposing deletion. Report findings before summaries;
a single unmet precondition blocks retirement.

1. **Promotion is complete.** The work has landed in its destination, or has been
   explicitly abandoned with that decision recorded.
2. **Closeout evidence is preserved** somewhere that outlives the branch —
   decisions, rationale, benchmark or verification results, and anything a future
   reader would need to understand why the branch existed.
3. **No open pull requests** target or originate from the branch.
4. **No dependent branches** are based on it.
5. **No worktrees** reference it.
6. **No active sessions** are working on it.
7. **No symlinks or other consumers** point at it.
8. **A human explicitly authorizes** local *and* remote deletion. Authorization for
   one is not authorization for the other. Never infer authorization from a
   general cleanup request.

## Verification Commands

Gather evidence rather than asserting the preconditions hold.

```bash
git worktree list                        # precondition 5
git branch --contains <branch>           # precondition 4
git branch -a --merged                   # promotion state
gh pr list --head <branch> --state all   # precondition 3
gh pr list --base <branch> --state all   # precondition 3
git log --oneline <destination>..<branch>  # unmerged work
```

Treat a non-empty `<destination>..<branch>` log as unpromoted work. Do not
retire it, and do not describe it as merged.

## Retirement

Only after every precondition is verified and authorization is explicit:

```bash
git branch -d <branch>                   # -d, never -D
git push origin --delete <branch>        # separate authorization
```

Use `git branch -d`. It refuses to delete unmerged work, which is a safety
property worth keeping. Reaching for `-D` means a precondition is unmet —
stop and surface that instead of forcing the delete.

## Anti-Patterns

- Deleting a branch because it "looks stale" or is old.
- Bulk-deleting merged branches without checking worktrees and dependents.
- Treating a merged PR as sufficient evidence that closeout evidence survives.
- Using `-D` to get past a refusal.
- Deleting the remote ref because local deletion was approved.
