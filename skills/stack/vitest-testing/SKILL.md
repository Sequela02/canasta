---
name: vitest-testing
description: "Write Vitest tests: choose the test layer, mock only real boundaries, isolate state, diagnose slow or flaky suites, projects, coverage and CI. Use when editing test files or a vitest config."
paths: ["**/*.test.ts", "**/*.test.tsx", "**/*.spec.ts", "**/vitest.config.*", "**/vitest.workspace.*"]
---

# Vitest

Tests exist to show behavior works, not to raise a count. For which behavior to
test and how to judge an assertion, use `tdd`. For API details, read the docs for
the installed Vitest (`vitest.dev/llms.txt` lists pages for agents; the migration
guide lists what changed between majors).

## Procedure

1. Read the Vitest and Vite versions, the `test` scripts and the effective
   config: every project, setup file and the CI command. Inline `test.projects`
   inherit the root config in Vitest 5; projects loaded from their own config file
   do not.
2. Put the test at the narrowest layer that can see the behavior (pure function,
   integration with real state, runtime-specific, browser, end to end). Extend the
   test file that already owns that behavior.
3. Use small synthetic fixtures. Create temporary directories and databases per
   test and clean them up.
4. Mock a boundary you cannot run (network, clock, third-party service), and only
   when the fake behaves like the real one for what the test needs. Restore mocks,
   timers, env vars, globals and `cwd` when the test ends.
5. Run the file you changed with its path first (`vitest run path/to/file.test.ts`),
   then the owning package, then the repository's gate. Use `vitest run` in CI;
   watch mode is for your terminal.
6. Report what the tests exercised, the config and versions in effect, which
   commands ran, and what stayed untested.

## Example

A test passes alone and fails after another test runs.

Bad: add `retry: 2` or `isolate: true` to hide it.

Good: find what leaks. Run with `--sequence.shuffle --sequence.seed=1` to
reproduce, then look for a mock, fake timer, env var or module-level state that
the first test sets and never undoes. Fix the cleanup (`afterEach` with
`vi.restoreAllMocks()`, `vi.useRealTimers()`, `vi.unstubAllEnvs()`), and confirm
by running the shuffled order again with several seeds.

## Defaults worth knowing (Vitest 5)

- `clearMocks` is on by default: call history resets before each test. Calls
  recorded in `beforeAll` or at module top level are cleared too.
- `-t` matches the full name joined with ` > ` (`'math > adds'`); match one segment
  or use `.*` between segments.
- Clear, reset and restore differ (history, implementation, original). Check the
  docs for the installed major before relying on a global option, and probe for
  leaks between tests before you do.
- `vitest run --changed` and `related` follow static imports. They miss dynamic
  imports, registration and generated files, so they speed up feedback but do not
  replace the full run.
- A test that passes on retry is flaky. Fix it, or quarantine it with an owner, a
  reason and a removal date.
- Coverage shows which code ran, not whether assertions are strong. Set which
  source files count (`coverage.include`), or unimported code is missing from the
  report. Use mutation testing when you must know whether assertions would catch a
  change.
- Keep the typecheck (`tsc --noEmit`) a separate step.
- Runner compatibility is not runtime proof: test Bun, workerd or browser
  behavior in that runtime. With Bun, `bun run test` runs the Vitest script and
  `bun test` runs Bun's own runner; see `bun-standards`.

## Slow suites

Measure before you tune: [references/speed-and-ci.md](references/speed-and-ci.md).
