---
name: rust-standards
description: "Write Rust: error handling, borrowing vs cloning, module and crate layout, clippy, tests, deterministic output and NAPI bindings to Node. Use when editing .rs files or Cargo.toml."
paths: ["**/*.rs", "**/Cargo.toml"]
metadata:
  source: "rust-best-practices by Apollo GraphQL, apollographql/skills 13ff457"
  changes: "Borrowing, lint-expectation and type-state guidance adapted; workspace, determinism and NAPI rules are canasta's own"
---

# Rust standards

A repository's own Rust guidance wins. Read the toolchain and edition in
`rust-toolchain.toml` and `Cargo.toml`, and the Rust docs for that version.
New crates take the latest stable edition (`cargo new` picks it) and pin the
toolchain in `rust-toolchain.toml`.

## Procedure

1. Read the crate's `Cargo.toml`, its public API in `lib.rs` and a neighboring
   module before you add code.
2. Keep one concept per module. Expose the public API from `lib.rs` with explicit
   `pub use`; everything else is `pub(crate)`. Import names explicitly, no `use foo::*`.
3. Take `&str`, `&[T]` and `&T` in parameters. Clone only when you need ownership,
   and not inside a loop. Pass small `Copy` types by value.
4. Libraries return a `thiserror` enum from fallible functions. Binaries and
   examples use `anyhow::Result` in `main`. Validate at the public entry points and
   trust internal state after that.
5. Library code has no `unwrap()` or `expect()` outside tests; use `?`. Use
   `unreachable!("why")` only for states that cannot happen.
6. Log with `tracing` events, not `println!`. Keep hot loops free of logging
   above `trace!`.
7. Run `cargo fmt` and `cargo clippy --all-targets --all-features --locked -- -D warnings`.
   Fix the warning; if you must silence one, use `#[expect(clippy::lint)]` with a
   reason, which fails once the warning goes away.
8. Test: unit tests in `#[cfg(test)] mod tests`, integration tests in `tests/`
   through the public API, `proptest` for domain invariants, `insta` snapshots
   where output must not change. Benchmark hot-path changes before and after with
   `criterion` and report the difference.

## Example

A function that returns a name from a config.

Bad:

```rust
pub fn name(cfg: &Config) -> String {
    cfg.name.clone().unwrap()
}
```

Good:

```rust
pub fn name(cfg: &Config) -> Result<&str, ConfigError> {
    cfg.name.as_deref().ok_or(ConfigError::MissingName)
}
```

It borrows instead of cloning, and the caller learns what is missing.

## Layout

- A Cargo workspace at the root with one crate per concern. The core library knows
  nothing about Node, NAPI or JavaScript; a separate bridge crate wraps it.
- `benches/` for benchmarks, `examples/` for runnable tools.
- Put `unsafe` behind a safe API and write `// SAFETY:` above each block with the
  invariant it relies on.
- Prefer a plain `match` over nested `if let`, and iterators over index loops.
- Add types that make illegal states unrepresentable, such as a type-state
  `Connection<Connected>` that alone has `send`, when a wrong call order is a real bug.
- Add a framework (async runtime, ECS, graphics) only when the project's size needs it.

## Reproducible output

When output must repeat exactly (simulation, replay, content hashes):

1. Pass one seeded RNG handle (`rand_chacha`) into the code; never `thread_rng()` or
   `rand::random()`. The seed is part of the input.
2. Do not read the wall clock inside the computation; pass time in.
3. Do not depend on `HashMap` iteration order: use `BTreeMap` or sort the keys.
4. Do not rely on floating-point operation order across platforms.
5. Pin it with a snapshot test: seed X and input Y give output Z.

## NAPI bridge

- `crate-type = ["cdylib"]`; the bridge only wraps library calls and holds no
  domain logic.
- Mark exports with `#[napi]` and run expensive calls as async tasks on the thread pool.
- Send large binary data as `Uint8Array` or `Buffer`, not JSON strings.
- Generate the TypeScript declarations with the NAPI CLI (check its docs for the
  installed major's flag) and commit them on the
  TypeScript side.
