# Package Management and Supply-chain Safety

Read this reference for dependency, workspace, registry, lockfile, or install
changes.

## Reproducible installs

- Keep one text `bun.lock` at the workspace root and commit it. Never hand-edit
  it or maintain another package-manager lockfile as an alternate authority.
- Use `bun ci` in CI and release paths. It is equivalent to
  `bun install --frozen-lockfile` and fails when manifests and lockfile differ.
- Use ordinary `bun install` only when dependency resolution is intentionally
  allowed to change. Review both manifest and lockfile diffs afterward.
- Treat lockfile format changes as toolchain changes. Bun 1.4 normally creates
  lockfile version 2 and can read older formats. Nested or version-scoped
  overrides raise the lockfile to version 3, which older Bun versions cannot
  read. Review those migrations separately from dependency-content changes.
- The global cache/store is an optimization, never authority or verification.
  A successful warm install does not prove a clean install.
- The global virtual store is opt-in. Benchmark it on every supported install
  path before enabling it; symlink-unaware tooling and project-local patched or
  trusted-script dependencies can behave differently.

## Workspaces and dependency ownership

- Declare workspaces at the root and express local package dependencies with
  `workspace:`. Use `--filter` for bounded workspace commands rather than
  scripts that manually traverse directories.
- Use the isolated linker for new monorepos and libraries so phantom
  dependencies fail. Keep hoisted installs only for a named compatibility
  consumer or environment that cannot use symlinks.
- Use root catalogs when the same dependency version is intentionally shared by
  multiple workspace packages. Do not create a catalog for a single consumer
  or unrelated packages that should evolve independently.
- Keep dependency declarations with their real consumer. Hoisting and the
  global store do not make an undeclared dependency valid.
- Use root-owned `overrides`, `resolutions`, or patches only for an observed
  transitive defect or security requirement. Record the affected consumer,
  reason, and removal condition, then verify the selected graph with `bun why`
  and lockfile diff. Bun supports only one nested parent level; version selectors
  compare against declared ranges, not the currently resolved version.

## Install scripts and trust

- Resolve one of Bun's three trust modes explicitly. With `trustedDependencies`
  omitted, Bun trusts its built-in npm allowlist. An explicit list replaces that
  allowlist rather than extending it. `trustedDependencies: []` or
  `install.ignoreScripts = true` closes the policy completely.
- Inspect both `bun pm default-trusted` and `bun pm untrusted` when a package
  needs a script. Verify the resolved identity, source, script, platform effect,
  and why the artifact is needed before changing trust.
- Never use `bun pm trust --all` as routine setup. Trust the smallest named set.
- Packages from `file:`, `link:`, git, or GitHub sources require explicit trust;
  a familiar package name is not sufficient identity.
- Use `--ignore-scripts` for read-only dependency inspection or when install
  scripts are not required. Do not use it if doing so silently produces an
  unusable native addon; make that limitation visible.

## Supply-chain controls

- Run `bun audit` as a read-only CI or release gate at the severity selected by
  repository security policy. It reads `bun.lock`, does not require
  `node_modules`, sends package/version data to the configured advisory service,
  and does not prove coverage for registries without that service.
- Treat `bun audit fix` as mutation. Inspect `--dry-run` first, because it may
  change `bun.lock`, `node_modules`, direct pins, catalogs, or dependency major
  versions with `--latest`.
- A registry without an advisory endpoint leaves scoped packages unaudited;
  report them instead of treating a zero exit for other packages as complete
  coverage.
- Prefer a minimum release age for new resolutions when the project does not need
  immediate publication uptake. A 72-hour (`259200` seconds) default is a
  reasonable supply-chain delay, with narrow named exclusions for urgent,
  reviewed packages. Existing locked versions are unaffected, and releases
  without timestamps can pass; this is delay, not complete supply-chain proof.
- Configure a package security scanner only after selecting a real scanner and
  validating its authority, availability, failure behavior, and credentials.
  Bun documentation's `@oven/bun-security-scanner` name is an example, not a
  package to install.
- Keep registry tokens and scanner credentials outside committed `bunfig.toml`,
  `.npmrc`, manifests, and lockfiles. Use the runtime/CI secret owner.

## Dependency changes

- Use `bun outdated`, `bun why`, and manifest/lockfile inspection to understand
  the selected package and its consumers before updating. For source review use
  exact-version `bun pm diff pkg@old new`; the short form compares the lockfile
  to mutable `latest`, performs registry egress, and is not reproducible evidence.
- Add/remove/update packages through Bun, not by editing the lockfile.
- A dependency is removable only after its behavior and supported platforms are
  replaced. A Bun built-in with a similar headline is not automatic parity.
- `bun dedupe` and `bun prune` are maintenance tools, not universal gates. Use
  dedupe when duplicate versions have a measured cost and prune production
  installs when the deployment artifact actually uses `node_modules`.
- Pin executable tooling invoked by `bunx` in CI or release paths. Do not let an
  unqualified `latest` download determine a reproducible build.

## Official sources

- <https://bun.com/docs/pm/cli/install>
- <https://bun.com/docs/pm/lockfile>
- <https://bun.com/docs/pm/workspaces>
- <https://bun.com/docs/pm/catalogs>
- <https://bun.com/docs/pm/isolated-installs>
- <https://bun.com/docs/pm/lifecycle>
- <https://bun.com/docs/pm/cli/audit>
- <https://bun.com/docs/pm/security-scanner-api>
- <https://bun.com/docs/runtime/bunfig>
