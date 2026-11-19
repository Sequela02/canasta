---
name: typescript-standards
description: "TypeScript judgment: modeling types, narrowing, imports and modules, tsconfig strictness and checks. Use when reading or editing .ts or .tsx files or a tsconfig."
paths: ["**/*.ts", "**/*.tsx", "**/tsconfig*.json"]
license: Complete terms in LICENSE.txt
metadata:
  source: "pstack typescript-best-practices by Lauren Tan, cursor/plugins 190d287"
  changes: "Model invocation allowed; merged with canasta's earlier TypeScript standards (modules and imports, tsconfig, tooling, project structure, enum and readonly rules); principle skills folded in; Real tests and Structured telemetry dropped as not TypeScript-specific; versions and benchmark figures removed"
---

# TypeScript standards

This file holds judgment, not reference. For versions, defaults and compiler
behavior, read the version the repository pins and the official docs at
typescriptlang.org. In an existing repository, follow its conventions and
propose changes to them as their own change.

## Types

Make the compiler reject impossible states, mixed-up primitives and unhandled
variants. Examples for each rule: [references/patterns.md](references/patterns.md).

| Rule | Summary |
|------|---------|
| Discriminated unions | Model variants with a `kind` literal discriminant so impossible states can't be represented. No optional-field bags. |
| Constructive modeling | Build the shape so the illegal value can't be constructed: `[T, ...T[]]` for non-empty, `start` plus `duration` for a range. |
| Simplest total type | Keep `T[]` while every operation on it stays total. Strengthen to `NonEmpty<T>` only where the loose type forces `!`, a cast or a "should never happen" throw. |
| Branded types | Brand an identifier when code handles two kinds of the same base type, so a `UserId` can't go where an `OrderId` belongs. In a public API, add a brand only when callers really mix them: each costs callers a constructor. A brand comes from a verifying type guard, never from `as`. |
| No `enum` | Use a string literal union, or a const object `as const satisfies readonly T[]` when the values are needed at run time. |
| `readonly` by default | On fields, arrays and parameters. Mutability is the visible exception; return a new value instead of mutating a parameter. |
| Optional means `\| undefined` | Under `exactOptionalPropertyTypes`, write `timeoutMs?: number \| undefined` so callers can forward a maybe-undefined value. |
| `unknown` over `any` | External data is `unknown` until parsed. |
| Parse at the boundary | Where data crosses in (CLI args, config, env, network, database rows), parse it once into a named domain type with the repository's schema library and infer the type from the schema. Inside, trust the types: no re-validation. |
| Schema-derived types | Reach for `Pick`/`Omit`/`Parameters`/`ReturnType`/`Awaited`/`typeof` before declaring a parallel interface. |
| No `as` casts | Cast only after validation. Use `satisfies` to check a value without widening its literal types. |
| Narrowing hierarchy | Discriminant switch > `in` > `typeof`/`instanceof` > user-defined type guard > `as`. Narrow explicitly instead of `!`. |
| Type guards verify | A guard must check what its name claims; a lying guard is worse than `as`. Name them `isX` or `hasX`. |
| Exhaustiveness | `const _exhaustive: never = x;` in default arms, so a new variant is a compile error. |
| Annotate the surface | Annotate parameters and exported functions' return types; infer locals. |
| Object args | Pass one object, not positional arguments, except on hot paths. |
| `@ts-expect-error` | With a reason, never `@ts-ignore`: it fails once the error is fixed, so it can't rot. |

## Modules and imports

Ask who resolves the import at run time:

- **A runtime** (published packages, CLIs, services): `module: "nodenext"` and
  an explicit `.js` on relative imports, even in `.ts` files. TypeScript doesn't
  rewrite specifiers, and Node doesn't guess extensions.
- **A bundler** (Vite, Astro, Next applications): `module: "preserve"`;
  extensionless imports are fine.

Aliases are `package.json` `imports` subpaths with a segment (`#src/*`), not
`tsconfig` `paths`, which only type-checks and is emitted unchanged. Check that
the repository's linters and codegen resolve `#` before adopting it.

Named exports only: no default exports and no wildcard re-exports, so renames
are mechanical and imports are greppable. No `namespace`; use modules.

## Compiler and checks

- `strict` plus `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`,
  `noImplicitOverride`, `noFallthroughCasesInSwitch`,
  `noPropertyAccessFromIndexSignature`, `verbatimModuleSyntax` and
  `moduleDetection: "force"`.
- `isolatedDeclarations` for any package that emits declarations, from day one.
- `erasableSyntaxOnly` for code a runtime executes by stripping types.
- `tsc --noEmit` runs in CI. Type stripping and bundlers delete types without
  checking them.
- Biome formats, lints and organizes imports. Add ESLint with
  `typescript-eslint` only for a named rule Biome lacks; a repository already
  invested in ESLint plugins keeps them.
- `tsc -b` with `composite: true` per package in monorepos.

## Project structure (owner doctrine)

These are the owner's architectural choices, not general TypeScript practice.

- One concern per module, named by that concern. The module that owns a
  concern owns its types.
- Bounded contexts talk through explicit interfaces and their own entry
  points, never a package-root barrel that re-exports everything.
- A pure core with normalized inputs; validation, I/O and throwing at the edge.
- Applications are organized by feature (`src/features/<feature>/`), following
  [Bulletproof React's structure](https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md).
  Shared code moves to `src/components`, `src/hooks` or `src/lib` when a second
  feature needs it. Imports flow shared → features → app; features don't import
  each other.
