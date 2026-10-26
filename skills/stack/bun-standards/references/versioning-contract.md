# Cross-Project Bun Toolchain Version Contract

Contract id: `cross-project-bun-toolchain-version-v1`

Revision: `1`

Status: active

Scope: repositories that declare Bun as package manager, runtime, script
runner, test runner, bundler, or release tool.

## Invariant

Every execution path must resolve one reviewable Bun version, and observed
local, CI, build, and release runtimes must agree with the repository declaration
before their evidence can prove that repository.

## Authority chain

1. Root `package.json#packageManager` owns the repository's exact executable
   version: `bun@<exact-version>`.
2. `bun.lock` owns dependency resolution and records the lockfile/config format
   produced by that toolchain.
3. CI setup, builder images, release metadata, and setup documentation are
   projections of the manifest declaration.
4. `bun --version` and `bun --revision` are observed environment evidence only.

The global Bun installation is never repository authority. Bun does not
automatically switch the ambient executable to match `packageManager`.

The manifest is execution authority, not proof that the selected version is the
intended target. Take a target version from an explicit upgrade request or a
written organization standard; do not invent one.

## Declaration rules

- Use one exact stable version: `"packageManager": "bun@x.y.z"`.
- Do not use `latest`, `canary`, ranges, wildcards, or a major/minor-only value
  as a reproducibility contract.
- Do not add `.bun-version`, `engines.bun`, a CI literal, or a Docker argument as
  a second exact-version owner. A consumer that cannot read `packageManager`
  may receive a generated projection only when its owner and refresh mechanism
  are explicit.
- `engines.bun`, when required for a published package's consumer
  compatibility, expresses a supported range; it does not select the
  repository toolchain.
- CI should use the official `oven-sh/setup-bun` action and let it resolve
  `packageManager`, or explicitly set `bun-version-file: "package.json"` when
  clarity is useful. Do not also set `bun-version`.
- Commit `bun.lock`. A change in its `lockfileVersion` or `configVersion` is a
  toolchain migration artifact and must be reviewed, not normalized away.
- Documentation may name the exact version only when operators must install it.
  Keep that statement aligned in the same change; it is not authority.

## Read-only check

Before trusting local verification, use the repository's own check to compare
its exact `packageManager` declaration with the observed Bun executable version.
Reject absent, malformed, non-exact or mismatched declarations. This is a
read-only check, not permission to install or upgrade a toolchain.

`bun ci` separately proves that the manifest and committed lockfile agree. A
version match does not replace that check.

## Drift states

| Evidence | Classification | Consequence |
| --- | --- | --- |
| Missing or non-exact `packageManager` | undeclared | runtime evidence is not reproducible |
| Observed Bun differs from manifest | environment drift | do not run mutation or claim verification |
| CI or image literal differs from manifest | projection drift | repair the projection before trusting CI |
| Lockfile format is unreadable by the declared Bun | incompatible | align toolchain before installing |
| Documentation differs from manifest | stale guidance | correct it in the same bounded change |
| Canary/nightly runtime without an exception | unsupported | use only in a disposable probe |
| Desired stack policy unavailable | unresolved target | report installed state without claiming standards compliance |

## Selecting a version

- For a new repository, select the current stable Bun patch verified from the
  official release feed on that date, then pin it exactly.
- For an existing repository, keep its declared version until an explicit
  upgrade task changes it. Do not silently use the globally installed newer
  binary.
- Stable patch updates still require release-note review and repository gates.
- Minor or major updates additionally require the official breaking-change or
  upgrade guide, lockfile-format review, Node-compatibility review, native-addon
  review, and supported-platform evidence.
- Canary builds are diagnostic inputs only. They do not become the declared
  baseline without an explicit time-bounded exception and removal condition.

## Upgrade evidence contract

An upgrade is complete only when evidence binds to the declared version and
includes:

1. official release/tag identity and publication date;
2. old and new `bun --version` plus `bun --revision`;
3. reviewed breaking changes that intersect the repository;
4. manifest and lockfile diff;
5. `bun ci`, typecheck, tests, and build/release gates;
6. native-addon, compiled-artifact, and supported-platform checks where
   applicable;
7. updated CI or documentation projections;
8. residual limitations or a rollback version.

Do not use vendor performance claims as upgrade proof. Measure a repository
property only when performance is part of the decision.

## Current research observation

At the 2026-08-23 research cutoff, Bun's official latest stable release was
`1.4.0`, published 2026-08-20. This observation explains the basis of revision
1; it is not a standing version authority and must be refreshed before future
selection.

Official anchors:

- <https://github.com/oven-sh/bun/releases/latest>
- <https://bun.com/blog/bun-v1.4>
- <https://github.com/oven-sh/bun/issues/28792>
- <https://github.com/oven-sh/setup-bun>
- <https://bun.com/docs/installation>
