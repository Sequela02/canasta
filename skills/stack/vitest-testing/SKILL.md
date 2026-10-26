---
name: vitest-testing
description: "Configure or debug Vitest suites, mocks, pools, isolation, coverage, sharding, flaky tests, or test performance."
---

# Vitest Testing

Use Vitest as a behavior-verification tool, not a test-count generator. Route
behavior slicing, oracle quality, redundancy, and red-green-refactor decisions
through `tdd`.

## Resolve the effective suite

Before changing tests or configuration:

1. Resolve the installed Vitest, Vite, Node, and coverage-provider versions.
2. Read package scripts, every effective project config, setup/global-setup
   files, CI topology, supported runtimes, and existing performance evidence.
   Projects do not necessarily inherit root options.
3. Map which tests own pure behavior, integration state, runtime compatibility,
   browser behavior, contracts, and end-to-end journeys.
4. Identify the correctness invariants behind isolation, worker caps, ordering,
   environment choice, and custom pools before tuning them.
5. For Vitest 4.1 specifics and current caveats, read
   [references/vitest-4.1.md](references/vitest-4.1.md). Recheck official docs
   and tagged source when the resolved version differs or docs conflict.

## Add or change tests

- Use the narrowest layer that can faithfully observe the behavior. Prefer the
  existing owner over a parallel assertion in a new file.
- Pair `-t` with a file path when known; name filtering alone can still load many
  files for discovery.
- Keep fixtures synthetic, portable, minimal, and owned by the boundary under
  test. Use isolated temporary resources for filesystem/database behavior.
- Mock at a real boundary only when the fake preserves the semantics the test
  needs. Restore mocks, timers, environment, globals, cwd, and resources.
- Do not enable global mock reset options mechanically; they can change concurrent
  test semantics and hide local ownership.
- During Vitest 3/Jest to Vitest 4 migration, distinguish clear, reset, and restore
  semantics. `vi.restoreAllMocks` no longer clears spy state and does not restore
  automocks; add a cross-test contamination probe before relying on global cleanup.
- Keep runtime tests separate when behavior depends on Bun, workerd, a browser,
  Node, or another deployed runtime. Runner compatibility is not runtime proof.
- Keep TypeScript compilation/typechecking as a separate explicit gate unless a
  repository has intentionally adopted Vitest type tests for a distinct contract.

## Diagnose speed before tuning

Capture repeated baselines and use Vitest's transform, setup, import, tests, and
environment buckets to find the owner. Agent-aware reporters can hide these buckets;
temporarily select `--reporter=default` or default plus JSON/outputFile for diagnosis.
An explicit reporter disables automatic GitHub Actions reporter insertion, so include
`github-actions` explicitly when annotations are required. Then apply the matching
lever:

- Slow import/transform: inspect import durations and broad barrels; reduce the
  graph at ownership boundaries. Use dependency optimization only for a measured
  costly external dependency.
- Slow setup/environment: measure per-file setup. `globalSetup` has a separate
  scope and is not a semantics-preserving replacement for `setupFiles`.
- Slow test bodies: remove real waits, excessive subprocesses/network, redundant
  setup, or unsuitable fixture scope while preserving the real contract.
- CPU contention: budget workers across all concurrently running packages,
  pools, services, and CI jobs. Benchmark fixed budgets on the target host.
- Memory pressure or hangs: profile with a simplified worker topology and a
  watchdog. Lower concurrency only after distinguishing leaks from contention.

Do not use `isolate: false`, another pool, VM pools, sharding, or more workers as
generic speed switches. Each changes resource use or semantics:

- Keep isolation unless a stateless bounded project passes repeated shuffled and
  order-dependence probes.
- Keep `forks` as the safe starting point. Try `threads` only where `process.chdir`,
  native modules, process isolation, and runtime globals are not required.
- Shards divide files, not individual tests. Measure duration skew and duplicated
  setup/install cost before distributing them. Blob merge is run-mode only and
  excludes attachments; collect/merge `attachmentsDir` separately and verify shard,
  test, report, and artifact counts.
- Persistent filesystem module cache is a local fast-feedback experiment until
  source, alias, plugin-option, environment, and config invalidation are proven.

For performance comparisons, state the correctness invariant, versions, host,
cache state, seed/order, reporter, `maxWorkers`, file parallelism, pool, concurrent
package/service topology, and memory pressure. Hold them constant; separate cold
and warm runs, interleave variants, warm up when appropriate, and report median plus
spread or p95 across repeated samples. Record failures, retries, hangs, RSS, and
semantic parity. One favorable run is not a performance result.

## Fast feedback versus proof

- Use focused files during the inner loop, then the owning package/suite, affected
  downstream suites, and repository-required gates before completion.
- `related` and `--changed` follow discoverable dependency evidence and can miss
  dynamic imports, registration, configuration, generated projections, and
  filesystem discovery. They are acceleration, never the only authority.
- Watch mode is for development; use explicit `vitest run` in CI.
- A retry-pass is evidence of flakiness, not success. Repair nondeterminism or
  quarantine it with an owner, reason, expiry/removal condition, and deterministic
  alternate gate.

## Coverage and diagnostics

- Coverage shows exercised code, not assertion quality. Define the intended source
  surface explicitly; loaded-file-only coverage can omit unimported production code.
- Preserve thresholds and semantics when comparing V8 and Istanbul. Profile the
  actual suite; neither provider is universally faster.
- Use targeted mutation testing when assertion sensitivity on changed/high-risk
  code is uncertain. Interpret surviving and equivalent mutants; avoid global
  score chasing.
- Use JSON or other machine-readable duration output for concentration analysis.
  Use hanging-process diagnostics only while debugging because they are expensive.
- Treat CPU/heap profiles, traces, reports, and attachments as sensitive. Prefer
  synthetic workloads, ignored/access-limited paths, bounded retention, and content
  review/redaction before upload, commit, issue attachment, or model input.

## Bun boundary

When Bun is the package manager, `bun run test` selects the configured Vitest
script; `bun test` invokes Bun's separate runner. The script command does not prove
the runtime: inspect `[run].bun`, flags, Node availability, `process.execPath`, and
reported versions. Do not force Vitest onto Bun's runtime without bounded
compatibility and performance evidence. Use `bun-standards` to choose a native-Bun,
Vitest, or hybrid portfolio.

## Completion

Report behavior exercised and evidence established, effective config/version,
focused and broader gates, timing protocol and distribution for performance claims,
and residual untested runtime or integration risks. Do not equate passing, coverage,
or test count with correctness.
