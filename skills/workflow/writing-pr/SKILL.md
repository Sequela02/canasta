---
name: writing-pr
description: Write or update a pull request title and description so a reviewer who never saw the conversation knows why the change exists, what changed and how it was checked. Use when preparing work for review or refreshing the body after the change grew.
tags:
  - writing
  - engineering
  - pull-requests
metadata:
  source: "tstack file-pr by Theo Browne, t3dotgg/tstack 11e37a7; pr by Matt Pocock, mattpocock/skills bbadaa6"
  changes: "Bad/good title and opening pairs from file-pr; the Door and Blast Radius risk note from pr; evidence rules and the secret check are canasta's"
---

# Writing pull requests

For your own or your organization's repository. For another project's, use
`upstream-contribution`. `writing-issues` covers the problem to solve; this
skill covers the work delivered.

1. **Look first.** Read the contribution rules, the PR template and two recent
   merged PRs. Check whether a PR for the branch already exists. Read the diff
   against the base branch, not the commit messages.
2. **Title.** Follow the repository's convention (a PR title often becomes the
   merge commit). Say what the change does for someone, not how.

   ```text
   BAD   perf(server): negotiate permessage-deflate on the websocket
   GOOD  perf(server): cut websocket frame size by 70% with gzip
   ```

   Put a number in the title only if you measured it (step 5).
3. **Open with the problem** in plain words, then the fix in a sentence or two.
   Leave the list of what you edited to the diff.

   ```text
   BAD   Removed workspace carry-over from every "new thread" entry point and
         deleted buildContextualThreadOptions and the sidebar seed context.
   GOOD  My "new worktree" default was ignored when starting a thread on an
         existing worktree. Now the configured defaults always apply.
   ```

4. **Say what a reader would miss:** a trade-off, a compatibility change, where
   to start reading a large diff. Skip a tour of each file and alternatives you
   never weighed.
5. **Show the checks.** Give the command you ran and what it printed. Mark each
   check passed, failed, not run or pending. For a bug fix, show the test that
   failed before and passes now. For UI, attach before and after captures of the
   real screen and name the viewport and data. For a speed claim, give both
   revisions, the workload, units and the spread of the runs; without
   comparable runs, call the gain unverified (`benchmark-readiness-review`
   judges the claim). Never present a generated image as proof.
6. **End with a risk note** when the repository or your organization asks for
   one:

   ```text
   Door: one-way | two-way   (can the merge be walked back?)
   Blast radius: what else breaks if this is wrong, and for whom
   Evidence: the check above that supports it
   ```

   A migration or a public API change is a one-way door. A PR to another
   project carries a note only if that project asks.
7. **Before publishing,** reread the title and body against the final diff and
   fix what the work no longer says. Check links exist. Scan text, quotes and
   attachments for secrets, personal paths and internal names (private
   repositories, hosts, secret-store names). Describe the final change, not the
   attempts or the session.

Open a real PR rather than a draft unless the repository says otherwise. Stop at
a ready PR: merging is the maintainer's call, and passing checks don't grant it.
