# Installation

**Pre-publication draft.** The owner reviews this pack and its licence before
publication. The GitHub commands below are intended for after the repository
is published; no remote installation is claimed today. For an unpublished
checkout, use the local plugin path or manual route.

Choose **one method per agent**. Installing a plugin and copying the same skills
creates duplicates. Workflow is the default group; stack is optional.

## Claude Code

After publication:

```sh
claude plugin marketplace add Sequela02/canasta
claude plugin install canasta-workflow@canasta
# Optional technology opinions:
claude plugin install canasta-stack@canasta
```

For a local checkout, replace the first command with:

```sh
claude plugin marketplace add /absolute/path/to/canasta
```

The root `.claude-plugin/marketplace.json` lists two plugin sources. The
workflow plugin is the repository root, so it can also ship `agents/`; the stack
plugin is `skills/stack`. Each has a `.claude-plugin/plugin.json` with an
explicit skill list. Workflow and stack do not load each other. Restart or start a fresh session if required
by your installed version, then check the installed plugin list and skill menu.

## Codex

Canasta follows the shared marketplace and `plugin.json` layout documented in
[Matt Pocock's installation guide](https://github.com/mattpocock/skills#installation-30-second-setup),
not a separate Codex-only manifest. **Codex ingestion of canasta's manifests is
not yet tested.** The Codex CLI help checked during preparation supports this
marketplace and plugin command syntax:

```sh
codex plugin marketplace add Sequela02/canasta
codex plugin add canasta-workflow@canasta
# Optional technology opinions:
codex plugin add canasta-stack@canasta
```

For a local checkout:

```sh
codex plugin marketplace add /absolute/path/to/canasta
```

Then use the same `codex plugin add` commands. Check `codex plugin list` and
start a fresh session to confirm discovery. If your Codex version lacks plugin
support, use the manual skill-folder route below rather than guessing syntax.

## Pi, other supported agents, and editable copies

skills.sh is a copy-based alternative to plugins, with agent selection and
manual updates, as described in [Matt Pocock's installation guide](https://github.com/mattpocock/skills#installation-30-second-setup).
After publication:

```sh
npx skills add Sequela02/canasta
```

Use `npx skills@latest add Sequela02/canasta` if you want to explicitly select
the latest installer. The installer lets you select skills and agents. Include
`setup-canasta` and the workflow skills; select stack skills only if you want
those opinions. Pocock's linked guide lists Pi as a supported adapter; canasta's
Pi installation has not been exercised. Omit agent flags to inspect the
installer's current choices.

For agents without an installer adapter, do **not** assume a named adapter
exists. Use the manual route and that tool's documented skills
directory. Restart the agent or refresh skill discovery as its documentation
requires. Invoke `setup-canasta` using the tool's supported skill invocation;
a literal slash-command form is not guaranteed across agents.

## Manual clone and copy

Clone into a neutral source directory, not inside an auto-loaded skills root:

```sh
git clone https://github.com/Sequela02/canasta.git ~/agent-packs/canasta
```

For Codex's conventional user skill directory, this POSIX-shell example copies
each skill as an immediate child:

```sh
mkdir -p ~/.codex/skills
cp -R ~/agent-packs/canasta/skills/workflow/* ~/.codex/skills/
# Optional:
cp -R ~/agent-packs/canasta/skills/stack/* ~/.codex/skills/
```

On Windows, use your shell's equivalent copy operation. Confirm the effective
skills directory from your installed tool's guidance; custom home settings can
change it. For Pi and other agents, replace the destination with the
documented user or project skills directory. Keep `references/`, evaluations
and `NOTICE` files with their skill. Do not copy the group's `.claude-plugin`
directory as a skill. Do not overwrite an existing skill of the same name:
inspect differences and resolve with the user first.

Update the source clone explicitly, review the diff, then copy only the chosen
skills again. Locally edited copies need reconciliation; they do not magically
update with the source clone. Remove only the plugin or copied folders you
installed when uninstalling; preserve unrelated skills and user changes.

## Agent types

The six files in `agents/` have no model. Each tool reads its own format, so
`setup-canasta` renders a copy per tool with the model you chose. Documented
formats, checked 2026-10-26:

| Tool | Where it reads agent types | Model field | If the model is omitted |
| --- | --- | --- | --- |
| Claude Code | `~/.claude/agents/`, `.claude/agents/`, or a plugin's `agents/` | `model:` (`sonnet`, a full ID, or `inherit`) | Inherits the session's model |
| Codex | `~/.codex/agents/` or `.codex/agents/`, one **TOML** file per agent with `name`, `description`, `developer_instructions` | `model` (and `model_reasoning_effort`) | Uses the `[agents]` default, else the parent's model |
| Tesota | `~/.tesota/agents`, `~/.agents/agents`, project `.agents/agents` | `model: provider/id` | Runs on the session's model |

Notes that change what setup writes:

- **Claude Code plugin.** `canasta-workflow` ships `agents/` through the plugin,
  with no model, so they inherit. To pick models, setup writes copies to
  `~/.claude/agents/`; a user copy outranks the plugin's. Setup adds a `tools`
  allowlist to the four read-only roles in those copies.
- **Codex.** The Markdown files are not read as they are; setup converts each to
  TOML. A Codex agent file cannot set `sandbox_mode`, approvals or MCP servers:
  those come from the parent session. A read-only role in Codex is therefore a
  prompt instruction plus the session's own sandbox, not a permission boundary.
  Say so to the user.
- **Tesota.** The Markdown files load as they are, on the session's model. Setup
  writes copies with a `provider/id` model to `~/.tesota/agents`, which wins by
  name over `~/.agents/agents`. Writer roles (worker, verifier) get `writes: true`.
- **Other tools.** No format is assumed. Leave them pending.

Setup keeps your earlier choices by reading the `model` already in each
installed copy. It never overwrites a file of yours without asking.

## What was verified, 2026-10-26

The following **read-only help commands ran successfully on this machine**:

```sh
claude plugin --help
claude plugin marketplace add --help
claude plugin install --help
codex plugin --help
codex plugin marketplace add --help
codex plugin add --help
```

They confirm marketplace `add <source>` accepts a local path or owner/repo,
Claude uses `install <plugin@marketplace>`, and Codex uses
`add <plugin@marketplace>`. Plugin manifests are also checked locally with
`claude plugin validate`; structural checks compare both plugin skill lists to
the actual directories.

**Verified on 2026-10-26, from the published repository on Windows, into
fresh, isolated configurations:**
- **Claude Code:** `claude plugin marketplace add Sequela02/canasta`, then
  `claude plugin install canasta-workflow@canasta`, listed as enabled.
- **Codex:** `codex plugin marketplace add Sequela02/canasta`, then
  `codex plugin add canasta-workflow@canasta`. It listed `canasta-workflow` as
  installed and enabled, and `canasta-stack` as available.

**Agent types.** Verified: the three formats above, from Claude Code's
subagent and plugin reference pages, the Codex subagents page and Tesota's
subagents guide; `claude plugin validate .` passes with `agents/` at the plugin
root. **Not verified:** that Claude Code or Codex loads a rendered copy, that a
Codex TOML file runs with its model, or that the plugin's agents appear in a
fresh session. Model detection depends on each tool's own listing.

**Not verified:** skills.sh (`npx skills add`) and Pi, automatic updates, and
an agent invoking a skill after restart. The manual route is available when a
tool cannot discover the grouped layout.
