---
name: rust-standards
description: Rust 2024-edition coding standards, tooling, and crate choices for all projects. Covers workspace layout, determinism, testing, errors, NAPI bindings, and anti-patterns. Load before writing any Rust code.
---

# Rust Standards (cross-project)

Coding standards, tooling, and crate choices for any project that uses
Rust. A repository's own Rust guidance wins where the two differ.

## Edition & toolchain

- **Rust edition: 2024** (stable since Rust 1.85, the default for `cargo new`).
  Default new projects to it.
- Pin the toolchain with `rust-toolchain.toml` at the repo root so everyone
  builds with the same version.
- Target MSRV: latest stable at project start. No nightly features.

## Project structure

- Cargo workspace at the repo root, one crate per concern.
- Keep the core library free of host-binding knowledge (no Node, NAPI or JS in
  it). A separate bridge crate wraps it for the host.
- Integration tests in `tests/` (black-box, through the public API), benchmarks
  in `benches/`, runnable dev tools in `examples/`.

## Module rules

- Public API lives in `lib.rs` with explicit `pub use` re-exports.
- Internal modules are `pub(crate)` by default.
- No wildcard `use` imports. Always explicit.
- One logical concept per module; split when a file exceeds ~300 lines.

## Dependencies

| Crate | Purpose | Note |
|---|---|---|
| `serde` + `serde_json` | Serialization | The standard choice |
| `thiserror` | Error types in library code | Idiomatic for libraries |
| `anyhow` | Error context in binaries and examples | Not inside library code |
| `tracing` + `tracing-subscriber` | Structured logging | Structured, async-ready |
| `rand` + `rand_chacha` | Seeded RNG when output must be reproducible | ChaCha is deterministic across platforms |

Dev dependencies: `criterion` (benchmarks), `proptest` (property tests),
`insta` (snapshot tests). Add others when a project needs them; do not pull in
a framework (ECS, async runtime, graphics) a project's scale does not need.

## Determinism rules

Apply when output must be reproducible (simulation, replay, content hashes):

1. Every source of randomness goes through a single seeded RNG handle passed
   explicitly. No `thread_rng()`. No `rand::random()`.
2. The seed is part of the input.
3. No wall-clock reads in the computation; model time explicitly.
4. No `HashMap` iteration-order dependence. Use `BTreeMap` when order matters,
   or sort keys before iterating.
5. Floating-point ordering matters. Avoid relying on non-associative FP
   operations in cross-platform paths.
6. A snapshot test pins it: seed X + inputs Y always produce output Z.

## Code style

- `cargo fmt` on every save.
- `cargo clippy -- -D warnings` passes before commit; CI enforces it.
- Default clippy lint level is enough unless a repository opts into more.
- Prefer `&str` over `String` in signatures unless ownership is needed.
- Prefer iterators over index loops, and `match` over nested `if let` chains.
- Doc comments (`///`) on every public item. One-liner minimum.
- No `unwrap()` or `expect()` in library code outside tests and examples.
- `#[must_use]` on public constructors whose result can be silently dropped.

## Testing standards

- Unit tests live beside the code in `#[cfg(test)] mod tests`.
- Integration tests in `tests/` exercise only the public API.
- Property tests (proptest) for invariants the domain guarantees.
- Snapshot tests (insta) where output must stay byte-identical.
- Run benchmarks before and after any hot-path change, and report the delta.

## Error handling

- **Library code:** error enums with `thiserror`. Never panic in the public API
  except for truly unreachable states (`unreachable!()` with a comment why).
- **Binaries / examples:** `anyhow::Result<()>` in `main`; convert library
  errors with `?`.
- Validate at boundaries (public entry points). Trust internal state after.

## Logging / tracing

- Use `tracing` structured events, not `println!`, in library code.
- Keep hot loops free of logging above `trace!`.

## NAPI bridge rules

- The bridge crate only wraps library APIs; no domain logic lives there.
- `crate-type = ["cdylib"]` in its `Cargo.toml`.
- Use the `#[napi]` macro; back expensive calls with async thread-pool tasks.
- Prefer `Uint8Array` / `Buffer` for large binary payloads over JSON strings.
- Check the generated TypeScript bindings (`napi build --dts`) into the TS side.

## Tooling

```bash
rustup default stable
rustup component add rustfmt clippy
cargo install cargo-nextest        # faster test runner
cargo install cargo-llvm-cov       # coverage
cargo install flamegraph           # profiling (requires perf/dtrace)
```

## Anti-patterns to never commit

- Wildcard imports (`use foo::*`)
- `unwrap()` / `expect()` in non-test library code
- `Box<dyn Error>` in a library instead of a proper error enum
- Panics used as control flow
- `unsafe` without a `// SAFETY:` comment stating the invariant it relies on
