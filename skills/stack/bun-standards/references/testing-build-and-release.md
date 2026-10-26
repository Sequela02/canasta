# Testing, Build, and Release

Read this reference when changing a test runner, test scheduling, bundling,
compiled executables, containers, or release behavior.

## Test contract

- Run the repository's canonical script (`bun run test` or a focused script),
  not an assumed direct `bun test`. A script may compose Vitest, Playwright,
  Bun tests, fixtures, and multiple workspaces.
- `bun run test` selects the package script; it does not prove the runtime.
  `[run].bun = true`, `--bun`, or missing Node on `PATH` can alias Node shebangs
  to Bun. Record `process.execPath` and versions for material compatibility or
  performance experiments.
- Preserve the existing runner unless migration parity is explicitly in scope.
  `bun:test` is appropriate for Bun-owned code when its API, mocks, environment,
  reporters, coverage, and integrations satisfy the repository.
- For portable or multi-runtime software, keep one owning portable suite and add
  small probes under each materially different runtime. Do not duplicate every
  assertion across Bun, Node, browsers, workerd, or other deployment targets.
- Test observable behavior through public boundaries. Keep test fixtures
  portable, synthetic, isolated, and free of operator paths or credentials.
- Give tests explicit resource ownership: temp directories, ports, databases,
  servers, clocks, subprocesses, and environment changes must settle even on
  failure.

## Bun test execution

- Plain `bun test` shares one global and module registry across files. Use
  `--isolate` when file independence is an invariant.
- `--parallel` distributes files across worker processes and implies isolation.
  Measure it on the real suite; small files with a large shared import graph can
  be slower. Cap workers when tests contend for memory, ports, databases, or
  external services.
- `test.concurrent` overlaps async tests within one file; it does not add CPU
  threads. Use it only for independent I/O-bound cases and cap concurrency.
- Give each worker unique resources via `BUN_TEST_WORKER_ID` when parallel tests
  need databases, ports, or directories.
- Use `--shard` for CI distribution and `--timings` when file count does not
  reflect duration. Treat timings as scheduling data, not committed benchmark
  evidence unless its production and refresh method are owned.
- Use deterministic seeds for randomized runs and report the seed on failure.
  Retries diagnose instability; they must not turn a flaky test into a passing
  quality gate without recording the original failure.
- Coverage identifies unexercised loaded files; it does not prove behavior.
  Apply thresholds only to meaningful owned code, and keep generated/vendor
  paths out of the denominator.

## Vitest under Bun 1.4

Bun 1.4 claims Vitest support with forks, threads, and V8 coverage. Current
Vitest documentation conflicts: its coverage guide still says V8 coverage does
not work on Bun, while an experimental Node-loader path documents narrower Bun
limitations for selected transform/mock features. Treat these as path-specific
claims, not a complete compatibility matrix.

Do not force Vitest through Bun as a generic speed switch. Verify the exact
suite's collection, mocks, aliases/transforms, snapshots, coverage, handles,
memory, failures, and repeatability. An open Bun 1.4.0 reproducer shows Vite SSR
dropping explicit exports beside `export *`, preventing affected suites from
collecting. An independent local comparison is required before adoption.

An open report also describes intermittent `bun test --parallel` deadlock in a
roughly 1,100-file suite. This does not implicate `bun run --parallel`, and one
report does not establish prevalence. Use soak repetitions, deterministic
watchdogs, fixed worker budgets, and a proven fallback before making native
file parallelism a required large-suite gate.

## Performance evidence

1. State the workload, correctness invariant, Bun revision, OS/architecture,
   CPU/worker budget, reporter/output, cache state, and comparison command.
2. Separate startup, steady state, install, build, discovery/import, test body,
   environment, and coverage time. They have different owners.
3. Warm up when appropriate, interleave repeated variants, and report median
   plus spread or p95. One favorable run is not a performance result.
4. Hold output and concurrency constant. Record failures, retries, hangs, RSS,
   CPU, and semantic parity; speed without equivalent behavior is a failed test.
5. Use wall time first, then the narrowest CPU/heap profile, trace, import report,
   or build metafile that can explain the dominant bucket.

Heap snapshots, CPU profiles, traces, and reports can contain complete objects,
strings, credentials, payloads, and personal data. Prefer synthetic workloads;
write artifacts outside the repository or to ignored access-limited paths with
bounded retention. Review and redact before committing, uploading, attaching to
issues, or sending them to another system or model.

## Typecheck and build

- Bun strips/transpiles TypeScript but does not typecheck. Run the repository's
  authoritative `tsc` gate independently.
- Do not bundle server code by default. Direct Bun execution is simpler unless
  measured startup, distribution, or asset ownership requires a bundle.
- Set the build target explicitly (`browser`, `bun`, or `node`) from the runtime
  contract. Do not let a shebang or default browser target choose silently.
- Use production settings deliberately. Keep source maps available to the error
  owner and out of public artifacts when they disclose source. Never inline
  secret environment variables; only explicitly public build-time values may be
  embedded.
- Inspect build outputs/metafiles when dependency inclusion, bundle size,
  licenses, or unexpected runtime code matters. A successful build is not proof
  the target can start.
- Framework build tools continue to own framework semantics unless a separate
  migration proves Bun bundler parity.

## Compiled executables

- `bun build --compile` embeds Bun and changes distribution, platform, asset,
  native-addon, dynamic-import, configuration, and update semantics. Treat the
  executable as a release artifact with its own smoke tests.
- Declare assets explicitly. Bun 1.4 compiled executables no longer auto-load
  project `tsconfig.json` or `package.json` from the working directory unless
  the corresponding compile autoload flags are selected.
- Keep original-source stack traces through appropriate source maps. Minify only
  when artifact size/startup is valuable and diagnostics remain acceptable.
- Bytecode can improve startup but increases build coupling and does not obscure
  source. Admit it only from measured startup evidence.
- Cross-compile only to supported OS/CPU targets, then execute a smoke test on
  the actual target. Building an artifact is not runtime verification.
- Codesigning, notarization, Windows metadata, and installer/update ownership
  are separate release concerns; do not imply them from `--compile`.

## Containers and CI

- Derive the Bun version from `packageManager` in CI. For containers, use an
  image or build argument resolved from the same declaration rather than a
  separately maintained version literal.
- Copy manifests and `bun.lock` before `bun ci` to preserve dependency layers,
  then copy source. Do not copy local `node_modules` into a target-platform
  image.
- Use multi-stage builds when production needs only artifacts or production
  dependencies. Run the final image as a non-root user and keep build
  credentials out of layers and provenance.
- Verify the final artifact/image starts with production configuration, handles
  shutdown, exposes only intended ports/files, and reports its Bun version or
  embedded provenance in a bounded diagnostic surface.

## Release gate

A Bun-affecting release should bind its evidence to the exact version/revision,
lockfile, target OS/CPU, command, and artifact. Run install, typecheck, test,
build, package, and smoke gates owned by the repository. Report skipped platform
or live checks explicitly.

## Official sources

- <https://bun.com/docs/test>
- <https://bun.com/docs/test/parallel>
- <https://bun.com/docs/test/code-coverage>
- <https://bun.com/docs/bundler>
- <https://bun.com/docs/bundler/executables>
- <https://bun.com/docs/guides/ecosystem/docker>
- <https://bun.com/docs/guides/runtime/cicd>
- <https://bun.com/blog/bun-v1.4>
- <https://vitest.dev/guide/>
- <https://vitest.dev/guide/coverage>
- <https://vitest.dev/config/experimental.html>
- <https://github.com/oven-sh/bun/issues/4145>
- <https://github.com/oven-sh/bun/issues/39866>
- <https://github.com/oven-sh/bun/issues/39987>
