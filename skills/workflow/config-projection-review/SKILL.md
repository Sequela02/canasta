---
name: config-projection-review
description: Review canonical configuration, generated or synchronized copies, ownership, drift, and safe convergence.
tags:
  - config
  - projection
  - review
---

# Config Projection Review

Use when one configuration source generates or synchronizes other files,
settings or installed copies. A projection is a derived copy, not a second
source of truth. This applies to build configuration, editor settings and agent
instructions alike; it does not require a particular configuration service.

1. Inventory the canonical sources, generator or synchronization mechanism,
   revisions, source digests, current target bytes and ownership evidence.
   Prefer the project's existing status evidence over a competing scanner.
   If no shared status exists, inspect the relevant files directly and state
   the limits; do not infer ownership merely from a matching filename.
2. Classify each source and target as canonical, current, missing, stale,
   drifted or unmanaged. Record which fields or files are managed, source and
   target identities, comparison evidence and unreadable or unresolved state.
3. Separate incorrect source content from incorrect synchronization. Use
   `documentation-hygiene` to assess repository guidance and its source facts;
   this review owns whether the selected derived copies can converge safely.
4. Do not mutate during review. Preserve unrelated fields and unmanaged content.
   Block automatic repair when ownership is ambiguous, source configuration is
   invalid, inventory is incomplete, permission has changed, or a safe merge
   has not been established.
5. Recommend the narrow owning action: correct the source if needed, preview
   the target diff, then synchronize only explicitly selected targets under the
   project's authorization rules. Recheck the source and target before applying
   an approved change; stale approval must not overwrite newer work. Do not
   recommend hand-editing a generated copy to hide a canonical-source defect.
6. Account for partial failure per target. Say whether convergence is safe,
   needs review or is blocked. One unreadable or unsettled target prevents a
   claim that the whole operation succeeded.

Report findings first, overall status (valid, needs_changes or blocked),
per-target evidence and owning action, verification performed and residual
unknowns. A proposed repair is not permission to execute it.
