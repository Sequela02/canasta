---
name: setup-canasta
description: Detect the user's agent tools, check or install canasta for each chosen tool, explain the changes, and identify steps the user must complete.
---

# Set up canasta

Help the user install this pack without assuming one agent, operating system,
or skills directory. Installation is the exception to this pack's tool-neutral
working procedures. Use the current [installation guide](references/installation.md) packaged with this skill;
do not assume a remote release exists yet.

## Inspect before changing anything

1. Detect available agent executables and existing agent configuration or skill
   directories using the environment's read-only inspection capabilities.
   Check Claude Code, Codex, Pi and other tools the user names. A directory alone
   is not proof a tool is installed; distinguish found, absent and unknown.
   Do not crawl unrelated home files or read credentials to detect a tool.
2. Read each detected tool's current help or official skill-loading guidance.
   Find existing canasta installs, their scope, revision and installation method.
   Check for duplicates and locally edited copies; do not overwrite them.
3. Explain the findings in plain English. Recommend one installation method per
   tool: native plugin where supported, skills.sh for supported agents, otherwise
   immediate-child skill folders in the tool's documented skills directory.
   Do not invent a skills.sh adapter for an unsupported tool.

## Agree on the installation

Batch the related choices: which tools, project or user scope, workflow only or
workflow plus optional stack, and install versus check-only. The workflow group
includes this setup skill. Explain what will be downloaded, which files or
settings will change, and how the user can remove the installation later.
A request to check is not permission to install. If the user already explicitly
requested all groups for all detected tools, do not ask the same question again;
ask only for unresolved scope or conflicting local edits.

## Install or check each chosen tool

- Use the verified commands and layout in the installation guide, checking local
  help when syntax differs. Do not run installation commands in check-only mode.
- Explain each step before doing it, in terms of its effect rather than assuming
  the user knows plugin or marketplace jargon.
- Install each selected skill once per tool. Do not use both a plugin and a
  copied-skills install for the same group. Do not install excluded upstream
  skills as if they were part of canasta.
- For manual installation, copy each selected skill directory with its references
  and notices intact; do not copy only SKILL.md or nest the whole repository in
  a skill directory and assume recursive discovery.
- Never change the project's behavioral instructions or merge policy as a side
  effect. Do not push, publish, grant new access, install an agent executable,
  or bypass permissions to complete setup.
- Stop when a tool requires the user: interactive marketplace approval, a slash
  command, authentication, a restart or a new session. Give the exact action
  supported by that tool's current help, say where to do it and what success
  looks like. Never claim the interaction happened on the user's behalf.
- If a download, permission or tool capability is unavailable, leave that tool
  pending. Continue with independent authorized checks, not a fabricated install.

## Verify and hand back

Check the installed plugin listing or actual immediate-child skill files for
each tool. After any required restart, ask the user to confirm skill discovery
inside the agent; seeing files on disk does not prove they loaded.
Report per tool: selected groups, method, scope, revision, checks and results,
local edits preserved, and any user action still needed. Mark installation,
discovery and execution as separate states. Re-running setup should check what
exists and change only what is missing or explicitly authorized for update.
