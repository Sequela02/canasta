---
name: typescript-standards
description: "TypeScript types that rule out illegal states, narrowing without casts, parsing input at the boundary, imports, modules and tsconfig. Use when reading or editing .ts or .tsx files or a tsconfig."
paths: ["**/*.ts", "**/*.tsx", "**/tsconfig*.json"]
license: Complete terms in LICENSE.txt
metadata:
  source: "pstack typescript-best-practices by Lauren Tan, cursor/plugins 190d287"
  changes: "Model invocation allowed; merged with canasta's earlier TypeScript standards (modules and imports, tsconfig, tooling, project structure, enum and readonly rules); principle skills folded in; Real tests and Structured telemetry dropped as not TypeScript-specific; versions and benchmark figures removed"
---

# TypeScript standards

For versions, defaults and compiler behavior, read the version the repository
pins and its release notes. In an existing repository, follow its conventions
and propose changes to them as their own change.

## Procedure

1. Read the `tsconfig` and a neighboring file to learn the conventions in force.
2. Model the data first: pick the type that cannot hold an invalid value (see
   Types), then write the code.
3. Parse external data once, where it enters, into a named type. Inside, trust it.
4. Run `tsc --noEmit` (or the repository's typecheck) and the tests, and say
   which ran. A bundler or type stripping never checks types.

Example:

```ts
// Bad: any shape passes, and every caller guesses
type Result = { ok: boolean; value?: User; error?: string };

// Good: each state carries exactly its data
type Result =
  | { kind: "ok"; value: User }
  | { kind: "failed"; error: string };
```

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

- **Node runs compiled output** (services and CLIs built with `tsc`):
  `module: "nodenext"` and an explicit `.js` on relative imports, even in `.ts`
  files. Node doesn't guess extensions, and the path you write is the path it
  receives.
- **Node runs the `.ts` files directly** (type stripping): `module: "nodenext"`,
  `.ts` on relative imports, `rewriteRelativeImportExtensions` if `tsc` also
  emits, and `erasableSyntaxOnly`. Node ignores `tsconfig`, so `paths` never
  applies.
- **A bundler** (Vite, Astro, Next applications): `module: "preserve"`, or
  `esnext` with `moduleResolution: "bundler"`, and `noEmit`; extensionless
  imports are fine.
- **A published library:** check under the strictest consumer setting
  (`module: "node18"` or newer `node*`), with `.js` specifiers, `declaration`
  and a separate `outDir`. Bundler resolution lets code through that only
  works in a bundler.

Aliases are `package.json` `imports` subpaths with a segment (`#src/*`), not
`tsconfig` `paths`, which only type-checks and is emitted unchanged. Check that
the repository's linters and codegen resolve `#` before adopting it. If `paths`
is already in use, TypeScript 7 resolves it relative to the `tsconfig`, since
`baseUrl` is gone.

Named exports only: no default exports and no wildcard re-exports, so renames
are mechanical and imports are greppable. No `namespace`; use modules.

## Compiler and checks

- `strict` plus `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`,
  `noImplicitOverride`, `noFallthroughCasesInSwitch`,
  `noPropertyAccessFromIndexSignature`, `verbatimModuleSyntax`,
  `moduleDetection: "force"` and `skipLibCheck`. Write `strict` even where the
  pinned version defaults to it, so the file states its contract.
- Declare `types` (`["node"]`, `["bun"]`, a test runner's) and `rootDir`
  explicitly. Since TypeScript 6, `types` defaults to none and `rootDir` to the
  config's folder, and the missing-global errors don't name the cause.
- TypeScript 7 removed `baseUrl`, `moduleResolution: node10`, `target: es5` and
  `esModuleInterop: false`; use `nodenext` or `bundler` and `imports` subpaths.
- `isolatedDeclarations` for any package that emits declarations, from day one.
- `tsc --noEmit` runs in CI. Type stripping and bundlers delete types without
  checking them.
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
