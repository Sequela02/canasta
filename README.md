# canasta

**Canasta** is Spanish for basket—a basket of skills, with “Cana” from Canitas, just as pstack carries poteto's “p”.

Ricardo Armenta's (Canitas) working practices for coding agents. Small skills
for keeping intent, scope, evidence and authority intact—not a new agent
harness or a mandatory process for every edit.

**Owner-review draft, not yet published.** Intended home:
[`Sequela02/canasta`](https://github.com/Sequela02/canasta). Publication is planned
for roughly a week after 2026-10-27, only after owner review and licence
confirmation. Nothing here authorizes an agent to publish or merge.

## Why these skills exist

- **A question becomes an implementation.** `problem-clarification` separates
  exploration, decisions and authorized building.
- **A plausible brief becomes an unchecked premise.** `codebase-scouting` and
  `implementation-planning` ground the work in the actual repository.
- **The agent says “done,” but the user path still fails.** `tdd`,
  `formal-verification` and `benchmark-readiness-review` distinguish checks
  from confidence, and say what each check cannot prove.
- **A small change becomes a framework.** `architecture-review`,
  `concept-modeling` and `refactor` keep responsibility and scope visible.
- **Delegation creates more supervision than progress.** `orchestration-workflow`
  starts with one agent and requires a reason for handing work off.
- **A green check becomes permission to ship.** `writing-pr` ends with a risk
  note; merge authority still comes from the project's stated policy.

The workflow skills describe what matters and why, independently of your tool.
The optional stack group contains my technology opinions, not universal rules.
Keep your project's explicit constraints; check version-sensitive guidance
against its installed toolchain. Third-party skills stay with their upstreams.

Read [how I work](docs/how-i-work.md) for the method, its sources, and the
boundary between evidence and my preferences. Matt Pocock's skills and poteto's
pstack influenced the presentation and ideas; this is not a copy of pstack.

## Installation

Choose one method per agent. **These remote commands are for after publication.**
Use a local checkout today. [Full installation guide and verification limits](skills/workflow/setup-canasta/references/installation.md).

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

Select workflow skills (including `setup-canasta`) and any stack skills you
want. For Tesota or an agent without an installer adapter, use the
[manual clone-and-copy route](skills/workflow/setup-canasta/references/installation.md#manual-clone-and-copy).
Keep each skill folder intact in the agent's documented skills directory.

CLI syntax was checked against local Claude Code and Codex help. Remote
installation, Codex manifest ingestion, skills.sh and in-agent discovery were
**not** exercised. After installing, run `setup-canasta` with your agent's skill
invocation mechanism; some tools require a new session or a user interaction.

### Copy-and-paste setup prompt

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

Before publication, replace the GitHub URL in that prompt with your local
checkout path. The prompt requests installation, not unrelated outward actions.

## Skills

### Workflow

- [architecture-review](skills/workflow/architecture-review/SKILL.md) — Module boundaries, dependency direction and contracts.
- [benchmark-readiness-review](skills/workflow/benchmark-readiness-review/SKILL.md) — Benchmark validity and defensible performance claims.
- [clear-writing](skills/workflow/clear-writing/SKILL.md) — Accurate prose shaped around the reader.
- [code-review-findings](skills/workflow/code-review-findings/SKILL.md) — Actionable defects, evidence and verification gaps.
- [codebase-scouting](skills/workflow/codebase-scouting/SKILL.md) — Find owners, dependencies and affected checks.
- [concept-modeling](skills/workflow/concept-modeling/SKILL.md) — Resolve ambiguous terms and semantic ownership.
- [config-projection-review](skills/workflow/config-projection-review/SKILL.md) — Canonical configuration, provenance and safe convergence.
- [documentation-hygiene](skills/workflow/documentation-hygiene/SKILL.md) — Place and maintain durable documentation.
- [formal-verification](skills/workflow/formal-verification/SKILL.md) — Prove contracts without confusing proof with intent.
- [implementation-planning](skills/workflow/implementation-planning/SKILL.md) — Small, evidenced implementation sequences.
- [orchestration-workflow](skills/workflow/orchestration-workflow/SKILL.md) — Bounded delegation and verified adoption.
- [problem-clarification](skills/workflow/problem-clarification/SKILL.md) — Separate questions, decisions and build intent.
- [product-copy](skills/workflow/product-copy/SKILL.md) — Evidence-led interface and marketing copy.
- [refactor](skills/workflow/refactor/SKILL.md) — Change structure while preserving behavior.
- [repository-text-hygiene](skills/workflow/repository-text-hygiene/SKILL.md) — Repair encoding, line-ending and Git drift.
- [research](skills/workflow/research/SKILL.md) — Question-driven investigation with a stopping condition.
- [security-scope-review](skills/workflow/security-scope-review/SKILL.md) — Trace authority, untrusted data and consequential effects.
- [setup-canasta](skills/workflow/setup-canasta/SKILL.md) — Detect agents, install or check, and explain user steps.
- [system-design](skills/workflow/system-design/SKILL.md) — Requested system designs with constraints and tradeoffs.
- [tdd](skills/workflow/tdd/SKILL.md) — Small test-first slices with trustworthy oracles.
- [writing-issues](skills/workflow/writing-issues/SKILL.md) — Observable problems and acceptance criteria.
- [writing-pr](skills/workflow/writing-pr/SKILL.md) — Aggregate change, verification and a final risk note.

### Stack — optional

- [astro](skills/stack/astro/SKILL.md) — Pages, content, rendering and islands.
- [bun-standards](skills/stack/bun-standards/SKILL.md) — Runtime, package management and toolchain alignment.
- [postgres](skills/stack/postgres/SKILL.md) — Schemas, queries, locks and database operations.
- [react-engineering](skills/stack/react-engineering/SKILL.md) — Composition, rendering and measured performance.
- [rust-standards](skills/stack/rust-standards/SKILL.md) — Rust 2024, determinism, errors and crate choices.
- [spring-boot](skills/stack/spring-boot/SKILL.md) — Java backend boundaries, persistence and operations.
- [tailwind-v4](skills/stack/tailwind-v4/SKILL.md) — CSS-first tokens, utilities and responsive styles.
- [typescript-standards](skills/stack/typescript-standards/SKILL.md) — Language, imports, compiler and type idioms.
- [vitest-testing](skills/stack/vitest-testing/SKILL.md) — Suite semantics, isolation and measured test speed.

## Reviewing and maintaining this pack

- [Classification](docs/CLASSIFICATION.md) is a temporary owner-review file;
  review authorship/exclusions, then delete it before publication.
- `python scripts/check.py` checks manifests, inventory, local links, notices
  and generic skill metadata. It does not prove skill effectiveness or
  successful installation in an agent.
- Skill changes should preserve substance, attribution and tool independence.
  Keep installation syntax in the installation guide, not working procedures.
- No build, service or agent configuration is installed merely by cloning.

## Licence

[MIT](LICENSE), copyright Ricardo Armenta. The owner will confirm or change the
licence before publication. The adapted Matt Pocock debugging reference retains
its own MIT notice in the [tdd folder](skills/workflow/tdd/NOTICE).
