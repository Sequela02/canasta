---
name: config-projection-review
description: Review canonical config, projection ownership, provenance, drift,
  and safe convergence through shared status evidence.
tags:
  - config
  - projection
  - review
---

# Config Projection Review

Use this skill when reviewing global config, private project config, or opt-in
native harness projection.

Workflow:
1. Inventory canonical sources, generator and adapter revision, ownership or
   install-state evidence, source identity and digest, and current target bytes.
   Consume the shared config-status evidence when its typed contract owns these
   facts; do not create a competing scanner or infer state independently.
2. Classify every source and target as canonical, current, missing, stale,
   drifted, or unmanaged. For each projection record ownership, source identity
   and digest, target path, managed fields or files, target evidence, and any
   unresolved read or version failure.
3. Separate canonical-content defects from projection-lifecycle defects.
   Repository-context review owns whether private project facts are true;
   agent-context-doctor owns repository guidance placement and ownership; this
   skill owns whether selected native surfaces converge safely.
4. Never mutate while reviewing. Preserve unmanaged content and unrelated
   operator-owned fields. Block automatic repair for unmanaged content,
   ambiguous ownership, invalid canonical config, stale approval, incomplete
   inventory, or authority/permission drift whose safe merge is unproven.
5. Recommend the narrow owning operation: edit canonical state, review a
   preview, then synchronize an explicitly selected native projection.
   Model-callable mutations must use proposal, approval, and apply with
   stale-base rejection. Never recommend direct edits to repository guidance or
   native skill files.
6. Account for partial failure per target. State whether convergence is safe,
   needs review, or is blocked; do not report a whole operation successful when
   one target is unreadable or unsettled.

Output findings first, followed by overall status (valid, needs_changes, or
blocked), per-target evidence and action, verification performed, and residual
unknowns.
