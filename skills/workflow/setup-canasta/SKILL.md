---
name: setup-canasta
description: Install or update canasta in Claude Code, Codex or Pi, link its pack, and pick a model for each agent role (explorer, clerk, worker, reviewer, verifier, advisor), keeping local choices. Use when installing canasta, setting it up in a new agent, or choosing which model each role uses.
---

# Set up canasta

Install canasta's skills and agent roles into the agent tools the user has,
without overwriting anything they edited. Follow the
[installation guide](references/installation.md) for exact commands and paths;
check each tool's current `--help` when syntax differs.

## 1. Inspect (change nothing)

1. For each tool (Claude Code, Codex, Pi, others the user names), run its version
   command or look for its executable. Record found, absent or unknown. A config
   directory alone doesn't prove the tool is installed.
2. Look for an existing canasta install: scope, revision, method, and locally
   edited copies.
3. Don't read credentials or crawl the home directory.

## 2. Agree on the plan

Ask once, in one message: which tools, project or user scope, workflow skills
only or plus the stack skills, and install or check only. Say what will be
downloaded, which files will change and how to remove it. Skip a question the
user already answered. A request to check is not permission to install.

Recommend one method per tool: the native plugin where the tool has one, else
skills.sh, else copy each skill folder (with its `references/` and `NOTICE`) into
the tool's skills directory. Use one method per tool, or skills appear twice.

## 3. Install or check

Do each step, saying what it does in plain words. When a step needs the user (a
marketplace approval, a slash command, a restart), give the exact command and
where to run it, then stop. Don't claim it happened. If a download or permission
is missing, leave that tool pending and continue with the others.

Don't push, publish, change the project's own instructions, or install an agent
executable.

## 4. Choose models for the agent roles

The six `agents/*.md` files carry no model. Per tool:

1. List models from the tool's own picker or help. If it can't list them, ask the
   user for identifiers and mark them user-confirmed. Don't guess names and don't
   run a paid call to test availability.
2. Keep models already set in existing role files, including inheritance (no
   `model` field). If a saved model is no longer listed, flag it and ask.
3. Propose this table using only models you have evidence for:

   | Role | Tier | Access |
   | --- | --- | --- |
   | explorer, clerk | light | read-only |
   | worker | light | writes in its assigned files |
   | reviewer, advisor | strong | read-only |
   | verifier | strong | writes checks, not product fixes |

   Prefer a strong reviewer and verifier from a different model family than the
   one that writes code, when the tool offers one. That reduces shared blind
   spots; it doesn't prove correctness. Offer "inherit the session's model" for
   every role.
4. Ask the user to confirm the whole table or change rows. List existing
   same-name files separately and ask before replacing one.
5. Write each role in the tool's native format. Set only its `model` field (omit
   it for inheritance). Use the tool's read-only sandbox or tool allowlist for the
   read-only roles, because a prompt is not a permission boundary. If you can't
   verify the native format, leave that tool's agents pending.

## 5. Verify and hand back

After any restart, ask the user to confirm the skills show up inside the agent;
files on disk don't prove they loaded. Report per tool: groups installed, method,
scope, revision, checks and results, local edits kept, each role's model or
inheritance, and what the user still has to do. Installed, discovered and
executed are three separate states; report which you reached. Re-running should
change only what is missing or approved.

## Example

> Claude Code 2.x found, Codex 0.x found, Pi absent.
> Plan: Claude Code via the plugin (user scope), Codex via skills.sh. Workflow
> skills only. Nothing installed yet. Confirm, or tell me what to change.
