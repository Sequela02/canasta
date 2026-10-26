---
name: bun-standards
description: "Configure or change Bun runtime APIs, package management, workspaces, bundling, tests, or CI commands."
---

# Bun Standards

Use Bun as an intentional runtime and toolchain, not as a drop-in assumption.
Preserve reproducibility, explicit runtime ownership, portable boundaries, and
the repository's canonical verification surface.

## Ownership boundaries

- `typescript-standards` owns TypeScript language, module, type, and `tsconfig`
  rules. This skill owns Bun runtime, package manager, test runner, bundler,
  executable, CI, and Bun-native API decisions.
- `vitest-testing` owns Vitest semantics, configuration, and performance even
  when Bun is the package manager. Load this skill too only when Bun's runtime,
  installer, workspace, shell, build, or native test-runner role changes.
- A repository manifest and lockfile own its declared and resolved
  installed state. This skill never owns an exact Bun version.
- Repository scripts are the public developer and CI contract. Prefer
  `bun run <script>` over bypassing a script with an underlying tool command.
- Framework-specific build behavior remains with the framework skill. Do not
  replace Vite, Astro, Next, or another framework pipeline merely because Bun
  has overlapping features.

## Establish evidence first

Before changing Bun behavior, inspect:

1. `package.json` (`packageManager`, `engines`, workspaces, scripts, catalogs,
   overrides, `trustedDependencies`) and `bun.lock` header.
2. `bunfig.toml`, CI setup, containers, release scripts, deployment target, and
   operator-facing setup documentation.
3. Direct `Bun.*`, `bun:*`, `bun:test`, and Bun Shell use; native addons; and
   assumptions about Node.js, browsers, operating systems, CPU architecture, or
   installed executables.
4. The installed `bun --version` and `bun --revision`. For spawned scripts also
   inspect `[run].bun`, CLI flags, Node availability, and `process.execPath`.
   Treat them as observed environment evidence, not policy.

Classify each runtime surface before choosing APIs:

- **Bun-owned:** Bun is an explicit deployment/runtime requirement. Bun-native
  APIs may be the simplest owner.
- **Node-compatible:** the same artifact must run on Node.js. Keep runtime code
  on Web and Node APIs whose exact behavior is verified on both runtimes.
- **Browser-bundled:** browser semantics and the framework/bundler own runtime
  behavior; Bun is development tooling unless deployment says otherwise.

Do not let a Bun-owned script silently make a published library Bun-only.

## Load the relevant contract

- For setup, version drift, CI pinning, or upgrades, read
  [references/versioning-contract.md](references/versioning-contract.md).
- For installs, lockfiles, workspaces, catalogs, dependency security, or
  registries, read
  [references/package-management-and-security.md](references/package-management-and-security.md).
- For runtime APIs, subprocesses, servers, storage clients, or new Bun 1.4
  built-ins, read
  [references/runtime-and-apis.md](references/runtime-and-apis.md).
- For tests, bundling, compiled executables, containers, or releases, read
  [references/testing-build-and-release.md](references/testing-build-and-release.md).

Load every reference whose boundary the task actually changes; do not load the
whole set for a narrow edit.

## Binding standards

- Pin one exact stable Bun version in the repository's root
  `package.json#packageManager`. Derive CI from it; do not duplicate a mutable
  version literal across workflows, Dockerfiles, and prose.
- Commit the text `bun.lock`. Use `bun ci` (equivalent to
  `bun install --frozen-lockfile`) in CI and release verification. Never edit
  the lockfile manually.
- Keep `tsc --noEmit` or the repository's authoritative typecheck in CI. Bun's
  runtime transpiler, test runner, and bundler do not typecheck.
- Preserve the selected test runner unless a bounded migration proves behavior,
  fixtures, mocking, coverage, reporting, and watch/CI parity. Built-in is not
  by itself a reason to replace Vitest or framework test tooling.
- Prefer Web-standard APIs at portable boundaries. Prefer Bun-native APIs when
  Bun owns the runtime and they remove a real dependency or lifecycle without
  exporting compatibility complexity.
- Treat experimental APIs as unstable contracts. Name the admitted consumer,
  supported platforms, failure behavior, and removal or stabilization
  condition before production use.
- Pass subprocess arguments as arrays. Bound subprocesses with cancellation or
  timeouts, consume or redirect output intentionally, and settle child
  lifecycles on every exit path.
- Disable automatic `.env` loading in CI and production when the environment is
  the authority. Parse required variables once at the boundary and never log
  the complete environment.
- Do not remove a dependency in favor of a Bun built-in until behavior,
  platform support, data formats, error semantics, and tests prove parity for
  the repository's actual consumer.

## Verification

Run the smallest focused check first, then the repository-owned gates affected
by the change. A toolchain or runtime change normally requires:

1. version-contract check;
2. `bun ci` from a clean dependency state in CI or an equivalent portable
   fixture;
3. authoritative typecheck;
4. focused and complete test scripts;
5. production build or compiled-executable smoke test when applicable;
6. every supported OS/architecture lane affected by native addons, system
   services, compiled artifacts, or platform-specific Bun APIs.

Do not report upgrade or replacement completion from install success alone.

## Currency

This skill was researched against official Bun 1.4 documentation on
2026-08-23. For version-sensitive work, re-check the official release notes,
breaking-change guide, API stability labels, and compatibility page before
acting. Vendor benchmarks are discovery evidence, not project verification.
