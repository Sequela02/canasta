---
name: typescript-standards
description: "Write or review TypeScript language code, imports, compiler configuration, and type-level idioms."
---

# TypeScript Standards

Language-level standards for every project that ships TypeScript: published
libraries, CLIs, services, and application surfaces alike. Framework choices live in
`react-engineering`, `astro`, and the upstream shadcn guidance (not bundled). Exact dependency versions belong to stack
governance, not here.

When TypeScript work adds, changes, reviews, optimizes, or migrates runtime
schemas, load [references/zod.md](references/zod.md). It owns Zod selection, boundary parsing, inferred
types, version compatibility, migration, and compilation; this skill continues
to own the surrounding TypeScript language rules.

**Basis.** Every rule below is derived from current official documentation, published
style guides, and measured results — not from what any repository happens to
do today. Existing repos are evidence of drift, never justification for a rule. When
revising this file, research first and cite the authority; where sources genuinely
disagree, name the tradeoff instead of picking silently. The one section marked
_cross-project doctrine_ is the deliberate exception.

## Compiler line

Use the **current stable native compiler line, TypeScript 7 or later**. TypeScript 7
is the Go rewrite of the same compiler, generally available since 8 July 2026,
measured 8–12x faster on full builds, shipped under the normal `typescript` package
and the normal `tsc` command.

- Do not select TypeScript 6 as the primary compiler to accommodate lagging tooling.
- `@typescript/typescript6` may be installed side-by-side as a scoped compatibility
  API for a named consumer that needs the old compiler API. Record the consumer and
  the removal condition. It must never become the primary compiler.
- Resolve exact versions from the repository manifest and lockfile, never from this
  file. Skills consume stack policy; they do not own versions.

## Module resolution

The rule that decides everything here: **who resolves this import at run time?**

| Resolver             | Surfaces                           | `module`   | Specifiers                         |
| -------------------- | ---------------------------------- | ---------- | ---------------------------------- |
| A runtime (Node/Bun) | published packages, CLIs, services | `nodenext` | explicit `.js` on relative imports |
| A bundler            | Vite/Astro/Next applications       | `preserve` | extensionless is fine              |

**Runtime-resolved code writes `.js`, even in `.ts` files.** TypeScript does not
rewrite import specifiers on emit, so the path you write is the path Node receives.
Node's ESM resolver does not guess extensions by design. You are naming the file that
will exist _after_ build, not the file you are editing.

`module: "preserve"` is the current answer for bundled code. It implies
`moduleResolution: "bundler"`, `esModuleInterop`, and `resolveJsonModule`, and models
what bundlers actually do. Prefer it over `esnext` in new projects.

### Aliases

Use **`package.json` `imports` subpaths** with a `#` prefix. Do not use `tsconfig`
`paths`.

```json
{ "imports": { "#src/*": "./src/*.js" } }
```

`tsconfig` `paths` is a type-level fiction: TypeScript resolves it for typechecking
and emits it unchanged, so it only works where a bundler or loader happens to resolve
it too. Subpath imports are resolved natively by Node, Bun, and Vite, and understood
by TypeScript since 5.4 — the same specifier works in a bundled app and a plain Node
process.

- `#/*` alone is invalid. Use a segment: `#src/*`, `#internal/*`.
- Ecosystem tooling support is thinner than blog coverage suggests. Verify that
  linters, codegen, and analysis tools in the repository resolve `#` before adopting
  it broadly.
- `@/*` is legacy. Do not introduce it into new projects.

Prefer relative imports within a bounded context and subpath imports across them.

## tsconfig baseline

`strict: true` is the floor, not the ceiling. Enable all of these:

| Option                               | Why                                                                 |
| ------------------------------------ | ------------------------------------------------------------------- |
| `strict`                             | The baseline bundle, including `useUnknownInCatchVariables`         |
| `noUncheckedIndexedAccess`           | `arr[i]` and `record[key]` are `T \| undefined`, which is the truth |
| `exactOptionalPropertyTypes`         | Distinguishes "absent" from "present and undefined"                 |
| `noImplicitOverride`                 | `override` must be written when overriding                          |
| `noFallthroughCasesInSwitch`         | Catches missing `break`                                             |
| `noPropertyAccessFromIndexSignature` | Index-signature access must use brackets                            |
| `verbatimModuleSyntax`               | Type-only imports must say `import type`; emit is predictable       |
| `moduleDetection: "force"`           | Every file is a module; no accidental globals                       |
| `isolatedDeclarations`               | Declaration emit stops depending on inference, so it parallelizes   |

`isolatedDeclarations` is on by default for new projects and is the strongest lever
available for any package that emits declarations. It makes `.d.ts` generation
independent of type inference, so packages emit in parallel and external tools can
emit without invoking `tsc` at all; reported build improvements run 3x–15x on
monorepos. The cost is explicit types at export boundaries, which is mechanical work
an editor can generate and which improves the published API surface anyway. Enable it
from day one on new packages. Retrofitting an existing package is a bounded task, not
a rewrite.

`erasableSyntaxOnly` is required for any package a runtime may execute directly via
type stripping, and is good discipline everywhere else. It rejects syntax that emits
runtime code: `enum`, `namespace` with a runtime body, parameter properties, and
`import =` / `export =`.

## Type-level idiom

**Do not use `enum`.** It emits a runtime object, has surprising bidirectional
mapping for numeric variants, and is banned by `erasableSyntaxOnly`. Use a string
literal union, or a const object when the values are needed at run time:

```ts
export type Effect = "inspect" | "modify_source" | "external_write";

export const EFFECTS = [
  "inspect",
  "modify_source",
  "external_write",
] as const satisfies readonly Effect[];
```

`as const satisfies T` is the load-bearing pattern: `as const` keeps the literal
types, `satisfies` checks conformance without widening. Reach for `satisfies` wherever
you would otherwise annotate and lose specificity.

- **Discriminated unions over optional-field bags.** Give every variant a literal
  `kind` and let exhaustiveness checking do the work. Model impossible states out of
  existence rather than validating them later.
- **`readonly` by default** on interface fields, arrays, and parameters. Mutability
  is the exception and should be visible.
- **Branded types for identifiers.** A `UserId` that is structurally a `string` will
  eventually be passed where an `OrderId` belongs.
- **`unknown`, never `any`.** Narrow at the boundary with a type guard or a schema
  parser. `any` disables checking silently and spreads.
- **Parse, don't validate.** Untrusted input crosses the boundary once, into a typed
  value; downstream code receives the type, not the raw shape. Follow
  [references/zod.md](references/zod.md) when Zod owns that parser.
- **Infer return types**; annotate parameters and public API surfaces. Explicit return
  types on exported functions are worth the redundancy, and `isolatedDeclarations`
  requires them.

## Project structure (cross-project doctrine)

These are the operator's architectural choices rather than externally-derived language
rules. They are binding here, but do not present them as general TypeScript practice.

- One logical concern per module. Name the module by its concern; a split is not
  complete until the residual is also named.
- The module that owns a concern owns its vocabulary. Types live with the logic that
  decides over them, not in a shared type dump.
- Bounded contexts communicate through explicit interfaces and their own barrels.
  Import the context, never a package-root barrel that re-exports everything.
- No wildcard re-exports. No default exports; named exports only, so renames are
  mechanical and imports are greppable.
- Prefer pure functions with normalized inputs at the core, and push validation,
  I/O, and throwing to the edge. A pure core is testable, cheap to reason about, and
  the only shape a deterministic verifier can consume.

Folder layout for applications, following Bulletproof React's project structure
(https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md):

- Organize by feature: `src/features/<feature>/` holds that feature's components,
  hooks, API calls, state and types, with only the subfolders it needs. Files that
  change together live together.
- Shared code (`src/components`, `src/hooks`, `src/lib`) is for what two or more
  features actually use; move it there when the second one needs it.
- Imports flow one way: shared → features → app. Features do not import from each
  other; the app layer composes them. Enforce it with the linter's import rules
  where it can express them.
- In an existing repository, follow its structure. Propose a reorganization as its
  own change, never mixed into a feature.

## Tooling

- **Biome** is the default formatter, linter, and import organizer for new projects:
  roughly 20x faster than ESLint and 25x faster than Prettier on equivalent checks,
  in one tool with one config. Its documented limit is rule coverage — it implements
  most common ESLint rules but not the long tail, and type-aware linting is thinner.
- **`tsc --noEmit` is the authoritative typecheck.** Type stripping and bundlers do
  not check types; they delete them. A type error will not stop a stripped program at
  run time, so `tsc` must run in CI regardless of how the code executes.
- Add ESLint plus `typescript-eslint` only for a named, repository-relevant plugin or
  type-aware rule Biome cannot provide. Do not run two overlapping checkers by default.
  A repository already invested in ESLint plugins should keep them rather than lose
  rule depth; the current pattern there is a fast pre-pass linter ahead of ESLint, not
  a rewrite.
- Use `tsc -b` project references in monorepos; set `composite: true` per package.
- **Vitest** for tests. Test behavior through the public API, not internals.
- `@ts-expect-error` with a reason, never `@ts-ignore`. The former fails when the
  underlying error is fixed, so it cannot rot silently.

## Anti-patterns

| Do not                                                  | Instead                                                    |
| ------------------------------------------------------- | ---------------------------------------------------------- |
| `enum` / `const enum`                                   | string literal union, or const object `as const satisfies` |
| `namespace`                                             | ES modules                                                 |
| `any`                                                   | `unknown` plus narrowing                                   |
| `as Foo` to silence an error                            | type guard, `satisfies`, or fix the type                   |
| Non-null `!`                                            | narrow explicitly, or make the type honest                 |
| `@ts-ignore`                                            | `@ts-expect-error` with a reason                           |
| `tsconfig` `paths` aliases                              | `package.json` `imports` subpaths                          |
| Extensionless relative imports in runtime-resolved code | explicit `.js`                                             |
| Default exports                                         | named exports                                              |
| `Function`, `Object`, `{}` as types                     | a precise signature or `unknown`                           |
| Optional fields to model variants                       | discriminated union                                        |
| Mutating a parameter                                    | return a new value                                         |

## References

- [TypeScript TSConfig reference](https://www.typescriptlang.org/tsconfig/) — strict
  flag semantics, `module: "preserve"`, `verbatimModuleSyntax`
- [TypeScript modules theory](https://www.typescriptlang.org/docs/handbook/modules/theory.html)
  — why specifiers are not rewritten on emit
- [`isolatedDeclarations`](https://www.typescriptlang.org/tsconfig/isolatedDeclarations.html)
  — parallel declaration emit and its export-annotation requirement
- [Node.js TypeScript support](https://nodejs.org/api/typescript.html) — type
  stripping, erasable syntax, and why `tsc` must still run
- [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html) —
  enum and export conventions
- [ts.dev style guide](https://ts.dev/style/) — the public form of the same guidance

Verify currency before relying on this file: the compiler line, `module` defaults, and
tooling landscape all moved during 2026.
