---
name: bun-standards
description: "Use Bun for installs, lockfiles, workspaces, scripts, bundling, tests and CI: pin the version, install reproducibly, decide Bun-only vs Node-compatible code. Use when a repository has bun.lock, bunfig.toml or Bun APIs, or when Bun CI or install steps fail."
paths: ["**/bun.lock", "**/bunfig.toml"]
---

# Bun

Bun is a runtime, package manager, test runner and bundler. Decide which of those
roles the repository uses before you touch anything, and keep to them.

Check current behavior in the docs for the Bun version the repository pins
(`bun.com/docs`, which also serves `llms.txt` for agents). Typing, modules and
`tsconfig` belong to `typescript-standards`; Vitest belongs to `vitest-testing`.

## Procedure

1. Read `package.json` (`packageManager`, `engines`, workspaces, scripts,
   `trustedDependencies`), `bun.lock`, `bunfig.toml` and the CI workflow. Run
   `bun --version`: it is the machine you are on, not the repository's choice.
2. Say which kind of code you are changing:
   - **Bun-owned**: deployment requires Bun. `Bun.*` APIs are fine.
   - **Node-compatible**: the same artifact must run on Node. Use Web and `node:`
     APIs, and check Bun's Node-compatibility page for the ones you use.
   - **Browser-bundled**: the framework or bundler owns runtime behavior.
   A script in a Bun-owned repository must not turn a published library into a
   Bun-only one.
3. Run package scripts with `bun run <script>`, the way CI does.
4. Keep installs reproducible: one exact version in `package.json#packageManager`
   (`"bun@x.y.z"`, never `latest` or a range), a committed text `bun.lock`, and
   `bun ci` in CI. Change the pinned version only for an upgrade task, with the
   release notes read and `bun ci`, typecheck, tests and build run.
5. Bun does not typecheck. Keep `tsc --noEmit` (or the repository's check) in CI.
6. Before you finish, run the install, typecheck, test and build scripts your
   change touches, and name any you could not run (another OS, a native addon).

## Example

A CI job fails with "lockfile had changes, but lockfile is frozen".

Bad: delete `bun.lock` or switch the job to `bun install`.

Good: run `bun install` locally with the pinned Bun version, read the
`package.json` and `bun.lock` diff, commit both, and keep `bun ci` in CI. If
the lockfile changed with no dependency change, compare `bun --version` with
`packageManager` first.

## Guardrails

- Never edit `bun.lock` by hand.
- Pass subprocess arguments as an array (`Bun.spawn({ cmd: [...] })`), with a
  timeout or `AbortSignal`. Never interpolate untrusted text into Bun Shell with
  `{ raw }`.
- In CI and production, turn off automatic `.env` loading when the environment is
  the source of values (`env = false` in `bunfig.toml` or `--no-env-file`).
- Replace a dependency with a Bun built-in only after checking that behavior,
  error cases and supported platforms match for your consumer. Treat APIs the docs
  mark experimental as unstable and name who depends on them.
- Keep the repository's test runner unless you are asked to migrate it.

## References

- [references/installs-and-supply-chain.md](references/installs-and-supply-chain.md):
  workspaces, catalogs, install scripts and trust, audit, release age.
- [references/runtime-test-build.md](references/runtime-test-build.md): runtime
  APIs, `bun test`, bundling, compiled executables, containers.
