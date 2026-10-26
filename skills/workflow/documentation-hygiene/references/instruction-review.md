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
