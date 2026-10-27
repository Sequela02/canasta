# canasta

The agent skills I use every day, cleaned up so anyone can use them. They keep
the agent on what I asked, make it show proof before it says "done", and leave
the big calls to me. They work in Claude Code, Codex and other agents.

Canasta is Spanish for basket. A basket of skills, and "Cana" from Canitas.

## Why I made these

Agents kept making the same mistakes on me:

- **I ask a question and the agent starts building.** `problem-clarification`
  makes it tell exploring, deciding and building apart.
- **The agent trusts a brief without checking it.** `codebase-scouting` and
  `implementation-planning` make it look at the real repo first.
- **It says "done" and the thing still doesn't work.** `tdd`,
  `formal-verification` and `benchmark-readiness-review` ask for real checks,
  and for what each check can't prove.
- **A small change turns into a framework.** `architecture-review`,
  `concept-modeling` and `refactor` keep the change small.
- **Handing work to subagents costs more than it saves.** `orchestration-workflow`
  starts with one agent and asks why before splitting work.
- **Green CI turns into "ship it".** `writing-pr` ends every PR with a risk note,
  and the agent doesn't merge unless your project says it can.

The workflow skills say what to do and why, not which tool to use. The stack
skills are my opinions on the tech I use, so take them as opinions. Your
project's own rules win.

How I work, and where each idea comes from, is in [how I work](docs/how-i-work.md).
If you know [Theo's tstack](https://github.com/t3dotgg/tstack) or poteto's pstack,
this is the same kind of thing.

## Install

Pick one method per agent. The [installation guide](skills/workflow/setup-canasta/references/installation.md)
has the manual and local-checkout options.

### Claude Code

```sh
claude plugin marketplace add Sequela02/canasta
claude plugin install canasta-workflow@canasta
# Optional:
claude plugin install canasta-stack@canasta
```

### Codex

```sh
codex plugin marketplace add Sequela02/canasta
codex plugin add canasta-workflow@canasta
# Optional:
codex plugin add canasta-stack@canasta
```

### Pi and other agents

```sh
npx skills add Sequela02/canasta
```

Pick the workflow skills (including `setup-canasta`) and any stack skills you
want. If your agent has no installer, use the
[manual clone-and-copy route](skills/workflow/setup-canasta/references/installation.md#manual-clone-and-copy),
and keep each skill folder whole.

I tested the Claude Code and Codex installs from this repo. I haven't tested
`npx skills` or Pi yet. Some agents need a new session before they see the
skills.

### Or let your agent do it

Paste this into your agent:

```text
Install canasta from https://github.com/Sequela02/canasta for the agent tools
I have installed. Include all workflow and optional stack skills. First inspect
my tools and existing installs, read the trusted installation guide and
setup-canasta skill, and explain which files/settings you will change.
Use one installation method per tool and preserve local edits. Ask together
about any unresolved scope or conflicts. Tell me when I must run an interactive
command or restart an agent. Verify installation and discovery separately;
report anything you could not check. Do not change project instructions,
install agent executables, publish, push or merge anything.
```

For a local copy, swap the GitHub URL for your checkout path.

## Agent types

I use six helpers, each with a small job:

- [explorer](agents/explorer.md): answer a repository question without editing.
- [clerk](agents/clerk.md): inventories, searches and other bounded read-only work.
- [worker](agents/worker.md): implement within assigned files and check the result.
- [reviewer](agents/reviewer.md): find concrete defects without changing the work.
- [verifier](agents/verifier.md): independently check the outcome; may write test artifacts, not repairs.
- [advisor](agents/advisor.md): weigh a hard decision without editing.

I ship them without models. Run `setup-canasta` to inspect your tools and choose
one for each role, or keep the session's model. It suggests light models for
explorer, clerk and worker, and stronger ones for reviewer, verifier and advisor.
When available, I prefer another model family for review and verification to
help catch shared blind spots, not as proof of correctness. Setup keeps your
choices on later runs and asks before replacing your own files. See the
[agent setup guide](skills/workflow/setup-canasta/references/installation.md#agent-types).

## Skills

### Workflow

- [architecture-review](skills/workflow/architecture-review/SKILL.md): module boundaries, dependency direction and contracts.
- [benchmark-readiness-review](skills/workflow/benchmark-readiness-review/SKILL.md): whether a benchmark claim holds up.
- [clear-writing](skills/workflow/clear-writing/SKILL.md): accurate prose written for the reader.
- [code-review-findings](skills/workflow/code-review-findings/SKILL.md): real defects, with evidence and gaps.
- [codebase-scouting](skills/workflow/codebase-scouting/SKILL.md): find owners, dependencies and the checks a change affects.
- [concept-modeling](skills/workflow/concept-modeling/SKILL.md): sort out terms that mean different things in different places.
- [config-projection-review](skills/workflow/config-projection-review/SKILL.md): one source of truth for configuration.
- [documentation-hygiene](skills/workflow/documentation-hygiene/SKILL.md): where docs go, and keeping them current.
- [formal-verification](skills/workflow/formal-verification/SKILL.md): prove contracts without mistaking the proof for the intent.
- [implementation-planning](skills/workflow/implementation-planning/SKILL.md): small steps, each with its check.
- [orchestration-workflow](skills/workflow/orchestration-workflow/SKILL.md): delegate only with a reason, and check what comes back.
- [problem-clarification](skills/workflow/problem-clarification/SKILL.md): questions, decisions and building, kept apart.
- [product-copy](skills/workflow/product-copy/SKILL.md): interface and marketing copy that's true.
- [refactor](skills/workflow/refactor/SKILL.md): change structure, keep behavior.
- [repository-text-hygiene](skills/workflow/repository-text-hygiene/SKILL.md): fix encoding, line-ending and Git drift.
- [research](skills/workflow/research/SKILL.md): research that answers a question and knows when to stop.
- [security-scope-review](skills/workflow/security-scope-review/SKILL.md): follow authority and untrusted data to where it matters.
- [setup-canasta](skills/workflow/setup-canasta/SKILL.md): find your agents, install, and tell you what you need to do.
- [system-design](skills/workflow/system-design/SKILL.md): system designs with real numbers and tradeoffs.
- [tdd](skills/workflow/tdd/SKILL.md): small test-first steps with tests you can trust.
- [writing-issues](skills/workflow/writing-issues/SKILL.md): problems you can see, and how to know they're fixed.
- [writing-pr](skills/workflow/writing-pr/SKILL.md): what changed, how it was checked, and a risk note.

### Stack (optional)

- [astro](skills/stack/astro/SKILL.md): pages, content, rendering and islands.
- [bun-standards](skills/stack/bun-standards/SKILL.md): runtime, packages and toolchain.
- [postgres](skills/stack/postgres/SKILL.md): schemas, queries, locks and operations.
- [react-engineering](skills/stack/react-engineering/SKILL.md): composition, rendering and measured performance.
- [rust-standards](skills/stack/rust-standards/SKILL.md): Rust 2024, determinism, errors and crates.
- [spring-boot](skills/stack/spring-boot/SKILL.md): Java backend boundaries, persistence and operations.
- [tailwind-v4](skills/stack/tailwind-v4/SKILL.md): CSS-first tokens, utilities and responsive styles.
- [typescript-standards](skills/stack/typescript-standards/SKILL.md): language, imports, compiler and types.
- [vitest-testing](skills/stack/vitest-testing/SKILL.md): suite behavior, isolation and test speed.

## Changing this pack

- `python scripts/check.py` checks the manifests, the skill list, local links
  and notices. It doesn't prove the skills work, or that an agent installed them.
- When you change a skill, keep what it says, its credits, and its tool
  independence. Install steps go in the installation guide.
- Cloning the repo installs nothing.

## License

[MIT](LICENSE), copyright Ricardo Armenta. The debugging reference adapted from
Matt Pocock keeps its own MIT notice in the [tdd folder](skills/workflow/tdd/NOTICE).
