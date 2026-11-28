---
name: line-ending-drift
description: Find out why Git shows files as changed when they aren't, and fix line-ending, encoding, formatter or editor drift without losing real edits. Use when every file shows modified but the diff is empty, after a formatter rewrote the repo, when CRLF and LF fight, or when status and diff disagree.
tags:
  - git
  - maintenance
  - text
---

# Line-ending drift

Find the cause of the drift before you touch a file or a setting. A long list in
`git status` is not permission to normalize anything.

1. **Look at the rules.** Read `.gitattributes`, `.editorconfig`, formatter
   config, hooks and CI. Read only the Git settings that matter and where they
   come from (`git config --show-origin --get core.autocrlf`); don't dump the
   whole config, which can hold credentials.
2. **Sort the changes** into real edits, intended generated changes,
   line-ending differences and stat noise.

   ```bash
   git status --short && git diff --stat && git diff --ignore-cr-at-eol --stat
   git ls-files --eol <path>                 # index vs working-tree endings
   git check-attr -a <path>                  # attributes that apply to it
   ```

   If the second `--stat` is empty, only line endings differ. For one suspect
   path, compare `git rev-parse :<path>` with `git hash-object --path=<path> <path>`;
   equal hashes mean the content matches, so refreshing that path's index entry
   (`git add --renormalize <path>` or `git update-index --refresh`) is safe.
   That proves one path, not the whole tree.
3. **Put the policy in the repository.** Set endings and encoding in
   `.gitattributes` and `.editorconfig`, and make the formatter agree with them
   (UTF-8 without BOM and LF is a sound default for text). Check platform
   scripts, binary files, byte-exact fixtures and digest contracts first; they
   may need an exception. Run the formatter as an explicit step, and check it in
   CI without writing.
4. **Repair only the paths you diagnosed.** Keep staged and unstaged work where
   it is. Don't run `git reset --hard`, a broad `checkout` or `restore`, or
   `git clean` to clear noise. Bulk renormalization (`git add --renormalize .`)
   goes in its own change, with other work set aside and the whole diff read.
5. **Verify.** What remains in `git status` must match a real diff or an
   intended untracked file. Run `git diff --check`, the formatter check and any
   build or digest check the paths affect. If the IDE still disagrees with Git,
   refresh it; don't rewrite files to quiet it. Report any gap you can't explain.

This skill doesn't pick a repository's language, layout or release policy, or
change global Git settings. For where documents belong use `documentation-hygiene`.
