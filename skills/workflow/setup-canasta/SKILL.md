---
name: setup-canasta
description: Detect agent tools and available models, install canasta, and confirm a model or session inheritance for each agent role without replacing local choices.
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

## Choose models and install agent types

Use the [agent types guide](references/installation.md#agent-types) for native
formats, paths and evidence limits. The six public `agents/*.md` files have no
model settings. If the skill installer did not include them, locate the trusted
source checkout or obtain the matching revision with the user's approval; do
not reconstruct role prompts from memory or fetch an unrelated branch.

1. Inspect only documented model/provider listings and relevant non-secret
   settings for each selected tool. Use current help, the session's model list,
   or a documented model picker/API. Provider configuration is evidence of a
   provider, not proof of model entitlement. Never read credential stores, print
   tokens, sign in, or run a paid inference just to detect availability. If the
   tool cannot enumerate models, ask for the user's available identifiers and
   mark them user-confirmed. Do not guess model names from the author's setup.
2. Load existing native role definitions first. Their model values are the
   current choices; an omitted model means inheritance where documented. Keep
   those choices, including inheritance, on reruns. If an earlier model is no
   longer listed, flag it as unverified and ask; never silently replace it.
3. Propose this table separately for each tool, using only detected or
   user-confirmed choices:

   | Role | Tier | Authority |
   | --- | --- | --- |
   | explorer | Light | Read-only investigation |
   | clerk | Light | Read-only mechanical support |
   | worker | Light | Writes within assigned ownership |
   | reviewer | Strong | Read-only defect review |
   | verifier | Strong | Writes verification artifacts, not product repairs |
   | advisor | Strong | Read-only decision support |

   Light means lower cost/latency for bounded tasks; strong means more capable
   reasoning for judgment. Do not infer capability from a provider name alone.
   Prefer a strong model from a different family than the implementation model
   for reviewer and verifier when available in that tool. This can expose shared
   blind spots; it is not proof of independence or correctness. A different model
   size in the same family does not count. If only one family is available, say
   so and use it without inventing a cross-provider route. Inheritance has an
   unknown family if the parent model can change; explain that limit.
4. Show all six proposed choices per tool with identifiers, evidence, rationale
   and destination. Ask the user to confirm the whole table or change individual
   rows; every row must be covered by confirmation. Offer **inherit the session's
   model** for every role. If no light/strong ranking is known, ask instead of
   inventing one. Model choice does not authorize file replacement: separately
   list existing same-name files and ask before changing them, including files
   with different prompts but the same model. Respect check-only mode.
5. Render the public description and body in each tool's documented native
   format. Set only its supported `model` field to the chosen identifier; encode
   inheritance by omitting it, not by writing an invented alias. Use the native
   read-only sandbox or a tool allowlist for the four read-only roles where
   supported; a prompt is not a permission boundary. Do not allow a general
   shell merely to make a read-only role convenient. Worker and verifier may
   write only in authorized scope; verifier must not repair product code.
6. Preview the diff, then write only authorized files, preserving unrelated
   fields and configuration entries. If a target already matches, do nothing.
   The installed native model fields are the saved choices; no shared model
   defaults or extra global rule file is needed. On updates, preserve them and
   ask before replacing changed role bodies. Do not edit a plugin cache to save
   choices: updates would discard them. If the native format cannot be verified,
   leave that tool's agent setup pending, rather than copying Markdown into an
   unrecognized directory.

## Verify and hand back

Check the installed plugin listing or actual immediate-child skill files for
each tool. After any required restart, ask the user to confirm skill discovery
inside the agent; seeing files on disk does not prove they loaded.
Report per tool: selected groups, method, scope, revision, checks and results,
local edits preserved, each role's saved model or inheritance, permission limits,
and any user action still needed. Check agent discovery as well as skills;
confirm the actual selected role and model when a user-authorized invocation is
available. A model proposal or a plugin validation is not a model execution.
Mark installation,
discovery and execution as separate states. Re-running setup should check what
exists and change only what is missing or explicitly authorized for update.
