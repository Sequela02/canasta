# Vitest 4.1 evidence boundary

Research cutoff: 2026-08-23. Stable subject: Vitest 4.1.10. Resolve the repository
version before applying these facts; Vitest 5 beta behavior is outside this file.

## Stable configuration facts

- The default pool is `forks`. Threads have cheaper communication but cannot use
  `process.chdir()` and may be unsafe with some native modules. VM pools have ESM
  cache/global differences and potential memory leaks; they are not generic speed.
- Run mode can use all available processors; watch mode defaults lower. Percent
  worker settings are relative to each process, so concurrent package suites can
  multiply the requested CPU budget.
- `isolate` defaults true. Disabling it shares module/global state across files.
- `fileParallelism: false` constrains file workers; it does not serialize concurrent
  tests inside one file.
- `test.projects` replaces the deprecated workspace form. Project options do not
  automatically inherit root config unless configured to do so; coverage and
  reporters are root-owned. Maintainers describe each project as carrying an
  isolated Vite transform pipeline in the current architecture; treat its measured
  overhead as workload-specific, not a stable ratio.
- `setupFiles` run in test workers before files. `globalSetup` runs once in a
  separate global scope and can provide only serializable values.
- Cached file durations normally schedule slow files early. Randomization is useful
  for detecting shared-state dependence but gives up this speed ordering.
- Config docs and tagged 4.1.10 source say `sequence.hooks` defaults to `stack`,
  while current CLI reference text says `parallel`. Configure hook order explicitly
  when correctness depends on it.

## Performance and feedback

- Built-in timing separates transform, setup, import, tests, and environment.
  Experimental import-duration reporting can identify expensive graphs.
- `experimental.fsModuleCache` persists transformed modules and can make focused
  warm reruns much faster. Its keys cannot observe every plugin option or external
  input, so validate invalidation before using it as authority or in CI.
- Dependency optimization is off by default and best reserved for profiled external
  packages with deep import trees. It does not repair broad internal barrels.
- `related` follows static imports. `--changed` has wider force-rerun semantics for
  selected config/package changes, but neither proves dynamic registration,
  generated state, or filesystem discovery.
- Sharding splits files, not tests. Uneven file durations can make count-based
  shards poorly balanced. Blob reports merge run-mode output but omit attachments;
  collect `attachmentsDir` separately and verify merged evidence counts.
- Machine-readable reports can expose duration concentration. The hanging-process
  reporter is intentionally expensive and diagnostic only.

## Mocks, types, and coverage

- `vi.mock` is hoisted. Clear/restore ownership must be deliberate; global reset
  settings default false and can interfere with concurrent tests.
- Vitest 4 changed cleanup semantics: `vi.restoreAllMocks` does not clear spy state
  and does not restore automocks. Audit clear, reset, restore, and suite-wide helpers
  separately during migration and probe cross-test contamination.
- Restore real timers. Under forks, faking `nextTick` can interfere with child
  process internals.
- Runtime transformation does not typecheck TypeScript. Preserve an explicit type
  gate; use Vitest type tests only for an intentionally owned type contract.
- V8 coverage is often faster and now has strong AST remapping, but Istanbul may
  win when V8 observes many loaded modules. Measure the actual suite.
- Vitest 4 coverage includes loaded files unless `coverage.include` declares a
  broader source surface. A high number can therefore omit unimported code.

## Bun boundary

Vitest's official guide tells Bun package-manager users to run `bun run test`, not
`bun test`, but this selects a script rather than proving its runtime. `[run].bun`,
`--bun`, or missing Node on `PATH` can cause Bun to satisfy Node shebangs. Record
`process.execPath` and versions in material experiments.

The evidence conflicts at cutoff. Bun 1.4 claims Vitest support with forks, threads,
and V8 coverage. Vitest's coverage guide still says V8 coverage does not work on
Bun, and its experimental Node-loader path documents Bun limitations for selected
transform/mock features. Those limitations are path-specific, not a justified list
of everything unsupported. An open 1.4.0 reproducer shows a Vite SSR export transform
defect that prevents affected suites from collecting. Treat native-Bun Vitest as a
bounded compatibility experiment until the exact project's mocks, transforms,
coverage, snapshots, handles, and repeatability pass.

## Upstream reports — not established facts

- A July 2026 Windows report says all-file collection failures are much more frequent
  in 4.1.10 than 4.1.9, without a public minimal reproducer or maintainer confirmation:
  https://github.com/vitest-dev/vitest/issues/10812
- Maintainers explain current project transform-pipeline isolation in a report about
  hundreds of projects; Vitest 5 plans differ. This is one workload plus maintainer
  explanation, not a universal performance contract:
  https://github.com/vitest-dev/vitest/discussions/10572

For upstream reports, record status, date, affected version/platform, reproduction
quality, and any experimental workaround. Do not convert a report into prevalence or
a permanent project setting.

## Primary sources

- Release: https://github.com/vitest-dev/vitest/releases/tag/v4.1.10
- Getting started/Bun command: https://vitest.dev/guide/
- Projects: https://vitest.dev/guide/projects.html
- Performance: https://vitest.dev/guide/improving-performance.html
- Profiling: https://vitest.dev/guide/profiling-test-performance.html
- Pools: https://vitest.dev/config/pool.html
- Workers: https://vitest.dev/config/maxworkers.html
- Isolation: https://vitest.dev/config/isolate.html
- Sequence: https://vitest.dev/config/sequence.html
- Setup: https://vitest.dev/config/setupfiles
- Global setup: https://vitest.dev/config/globalsetup.html
- Experimental config: https://vitest.dev/config/experimental.html
- Coverage: https://vitest.dev/guide/coverage
- Mocking: https://vitest.dev/guide/mocking.html
- Vitest 4 migration: https://vitest.dev/guide/migration.html
- CLI/filtering: https://vitest.dev/guide/cli
- Reporters/shards: https://vitest.dev/guide/reporters
- Tagged 4.1.10 config source:
  https://raw.githubusercontent.com/vitest-dev/vitest/v4.1.10/packages/vitest/src/node/config/resolveConfig.ts
- Native-Bun discussion: https://github.com/vitest-dev/vitest/discussions/7823
- Bun runner configuration: https://bun.com/docs/runtime/bunfig
- Bun 1.4 Vitest/coverage claim: https://bun.com/blog/bun-v1.4
- Bun 1.4 Vite SSR export report: https://github.com/oven-sh/bun/issues/39866
