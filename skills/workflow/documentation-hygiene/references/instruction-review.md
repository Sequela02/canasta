> Reference for `documentation-hygiene`, formerly the `repo-context-review` skill.

# Repo Context Review

Use this reference when a task asks to review, write, or trim a repository's agent
instruction files from repository evidence.

Workflow:
1. Inspect root and workspace manifests, lockfiles, workspace metadata, CI or
   build configuration, and the claimed canonical docs. Account for nested
   packages, submodules, and linked content when they are material.
2. Separate facts, inferences, conflicts, and unknowns. Resolve conflicts from
   direct executable or configuration evidence before documentation, then
   explain any remaining ambiguity. A document being named canonical does not
   make every claim inside it true.
3. Compare those facts with the instruction files. Verify that named commands
   exist and are portable, but reject frontmatter/body disagreement and do not
   execute destructive or externally mutating commands merely to review them.
4. Keep derived repository facts in their executable or source owners: point
   to commands, structure, workspace metadata, and package facts instead of
   copying them into the instruction files. Project and team guidance belongs
   in the project-owned instruction file; tool-specific projections should
   refer to its canonical owner rather than duplicate it. Do not encode personal
   preferences, transient incidents, branch state, provider/model policy, or
   duplicated architecture doctrine as project facts. Preserve reviewed durable
   human notes when evidence still supports them.
5. Recommend concrete canonical edits when context is missing, misleading, or
   unsupported. Treat the review as blocked only when critical evidence cannot
   be resolved; optional missing metadata is not a blocker.
6. Do not mutate repository guidance during review. Existing instruction files are project-owned. Do not repair native projection drift;
   route that to config-projection review.

Review Criteria:
- Project name, package manager, scripts, workspaces, and canonical docs match the repository.
- Guidance points to canonical architecture/docs instead of duplicating them.
- No local absolute paths, secrets, machine-specific state, or provider/runtime
  instructions are introduced as project facts.
- Any proposed addition is backed by a file path, script, or architecture doc.
- One instruction file per project; another tool's file only imports or
  links it. Two maintained copies drift apart.
- No overview of the repository: measured context files gain nothing from one,
  and every line costs every session. The file holds what an agent can't work
  out from the repository, in this order: what can cause damage (live data,
  shared processes, irreversible commands), then commands and checks, the
  non-obvious conventions, and a short index of which doc to read for each
  area.
- Each rule carries its reason, so a later review can tell whether it still
  applies. A rule a lint, script, or check can enforce moves there, and its
  prose goes. Prefer replacing or removing a rule to adding one.

When the review covers skills (adding, keeping, merging, or removing one):
- A skill earns its slot with a current consumer, a distinct trigger, a
  recurring judgment it changes, and an output or check. One odd session is
  not a pattern; prefer replacing an entry over adding one.
- A mechanical rule belongs in a compiler, lint, config, test, or script, not
  in skill prose. Tool syntax belongs in the tool's help.
- One owner per decision. A reference loads only on its trigger; duplicate
  rules hidden in references are still sprawl. Project-only guidance stays in
  its project.
- Ask of each sentence whether it still changes a decision with current
  models; propose removing ordinary advice. A model judge's preference is not
  evidence; compare a few representative tasks with and without the change.
- Retire a skill when its consumer is gone, its procedure is enforced, or
  another owner subsumes it, keeping unique safeguards and attribution. Low
  usage is a lead to investigate, not a reason to delete.
- Third-party material records origin, licence, and reviewed revision beside
  it. Do not install the same skill twice or track a removed wrapper.

Output:
- status: valid, needs_changes, or blocked.
- evidence: concise references for each accepted fact, conflict, or unknown.
- recommendedChanges: concrete edits for the instruction files.

Sources: Gloaguen et al., [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988)
(2026); Shanto et al., [agent instruction files in 1,000 repositories](https://arxiv.org/abs/2611.02383)
(2026); Chakrabarti, [Why does CLAUDE.md keep growing?](https://arxiv.org/abs/2608.11095)
(2026); T3 Code's [AGENTS.md](https://github.com/pingdotgg/t3code/blob/37d3d199e8/AGENTS.md)
(its opening hazards, docs index and Documentation section); pstack's
principle-encode-lessons-in-structure (cursor/plugins b7b93c3). The skill's
test for recording a decision follows Matt Pocock's domain-modeling
[ADR format](https://github.com/mattpocock/skills/blob/6f7f783/skills/engineering/domain-modeling/ADR-FORMAT.md).
