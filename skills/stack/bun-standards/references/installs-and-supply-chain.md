# Installs, workspaces and supply chain

Read this when you change dependencies, workspaces, registries or CI installs.

## Reproducible installs

- Commit one text `bun.lock` at the workspace root. A newer Bun can write a
  lockfile format an older one cannot read; review that as a toolchain change.
- CI and release: `bun ci` (same as `bun install --frozen-lockfile`). Bun does
  not freeze the lockfile in CI by itself.
- A warm cache proves nothing about a clean install.
- Use `oven-sh/setup-bun`; it reads `packageManager`. Do not repeat the version
  in workflows or Dockerfiles. If a tool cannot read `packageManager`, generate
  its copy from it.

## Workspaces

- Root `workspaces`, local dependencies as `workspace:`, bounded commands with
  `--filter`.
- New workspace projects (lockfile `configVersion = 1`) use the isolated linker,
  which makes undeclared dependencies fail. Existing projects keep hoisted
  installs until you change `install.linker`; switch only with a test run.
- Use a root catalog for a version that several packages share on purpose.
- Add `overrides` or patches only for a known transitive defect, with a note on
  why and when to remove it. Check the result with `bun why`.

## Install scripts

- `trustedDependencies` omitted: Bun trusts its built-in allowlist. A list you
  write replaces that allowlist. `[]` or `install.ignoreScripts = true` runs none.
- When a package needs a script, see `bun pm untrusted`, check what the script
  does, and trust that package by name. Do not run `bun pm trust --all`.
- Packages from `file:`, `link:` or git need explicit trust.

## Supply chain

- `bun audit` reads `bun.lock` and works without `node_modules`. It covers only
  registries that offer an advisory service; report the rest as unaudited.
  `bun audit fix` changes files: run `--dry-run` first.
- `install.minimumReleaseAge` (seconds, e.g. `259200` for three days) delays new
  releases; list urgent exceptions in `minimumReleaseAgeExcludes`. Versions already
  locked are unaffected.
- Compare versions with `bun pm diff pkg@old new` (exact versions).
- Pin tools you run with `bunx` in CI.
- Keep registry tokens out of `bunfig.toml`, `.npmrc`, manifests and lockfiles.
