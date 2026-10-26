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

The root `.claude-plugin/marketplace.json` lists two plugin sources. Each source
has its own `.claude-plugin/plugin.json` with an explicit skill list. Workflow
and stack do not load each other. Restart or start a fresh session if required
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

**Not verified:** remote installation (the repository is not published),
marketplace registration or installation into a real user's configuration,
Codex manifest ingestion, skills.sh execution/recursive discovery, automatic
updates, or in-agent skill invocation after restart. We did not run `npx`,
install plugins, or modify any agent configuration just to test these docs.
Command help proves syntax, not successful installation. The manual route is
available when a tool cannot discover the grouped layout.
