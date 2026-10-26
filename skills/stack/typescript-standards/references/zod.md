> Reference for `typescript-standards`, formerly the `zod-standards` skill.

# Zod Standards

Use Zod to turn untrusted runtime input into a trusted typed value at an owned
TypeScript boundary. The schema parses the wire or configuration contract; it
does not replace domain modeling, authorization, database constraints, or an
external schema that another system owns.

## Resolve Authority First

1. Identify the boundary, its consumers, and the canonical contract owner.
2. Inspect the repository manifest, lockfile, imports, schema conventions, and
   focused tests before selecting APIs or changing versions.
3. Use Zod as the default runtime parser when the TypeScript package owns the
   input contract and repository evidence does not select another supported
   validator.
4. Preserve OpenAPI, JSON Schema, Protobuf, database schemas, or provider
   contracts as authority when they own interoperability. Generate or adapt at
   that boundary instead of creating an independently maintained Zod truth.
5. Treat a Zod major-version change, unknown-key behavior change, default,
   coercion, transform, or error-shape change as a contract change.

Do not add Zod merely to re-check values already constructed behind a trusted
typed boundary. Parse external data, persisted schemaless values, environment
and configuration input, form submissions, messages, and provider responses.

## Version Governance

- Applications use the current stable compatible Zod line and commit the exact
  resolution in the repository lockfile. Resolve `latest` from the registry at
  execution time; never copy an exact version from this skill.
- Upgrade deliberately through the owning package's package manager, review
  release and migration notes, and run focused contract tests before broad
  gates. A newly published release is a candidate until those checks pass.
- Libraries expose a peer range based on the oldest Zod API they intentionally
  support, not an exact current version. Keep the current stable release in
  development dependencies and test both the supported minimum and current
  stable when the public API accepts or returns Zod schemas.
- Avoid multiple Zod copies across a workspace when shared schema identity or
  consumer interoperability matters. Diagnose the dependency graph before
  adding overrides or resolutions.
- Dependency automation may propose upgrades, but manifests, lockfiles, CI, and
  compatibility tests enforce adoption. Prose does not.

## Schema And Type Ownership

Define one canonical schema for each owned runtime contract and derive types
from it:

```ts
import * as z from "zod";

export const CreateOrderInputSchema = z.strictObject({
  customerId: z.string().min(1),
  quantity: z.number().int().positive(),
});

export type CreateOrderInput = z.input<typeof CreateOrderInputSchema>;
export type CreateOrder = z.output<typeof CreateOrderInputSchema>;
```

- Do not hand-maintain a matching interface beside a schema. Use `z.infer` when
  input and output are identical; use `z.input` and `z.output` when defaults,
  coercions, pipes, codecs, or transforms make them differ.
- Name schemas as runtime values with a `Schema` suffix when the distinction
  improves greppability. Keep the schema and its inferred public types in the
  module that owns the contract.
- Reuse a schema only when the concepts and evolution policy are genuinely the
  same. Similar fields do not prove shared ownership.
- Prefer discriminated unions for runtime variants. Make optionality,
  nullability, defaults, and unknown-key behavior explicit from contract
  semantics rather than client convenience.
- Use brands only when the runtime validation establishes the branded
  invariant. A brand is not a substitute for validation.

## Parse At The Edge

- Accept `unknown` at untrusted boundaries, parse once, and pass only the parsed
  output inward. Do not scatter repeated validation through the core.
- Use `safeParse` for expected invalid user or network input that must become a
  typed application error. Use `parse` when failure indicates a violated
  invariant or startup/configuration failure that should throw.
- Use `safeParseAsync` or `parseAsync` whenever the schema contains async
  refinements or transforms. Never call the synchronous API on an async schema.
- Use `z.validate(schema, input)` only when the caller needs a boolean/type guard
  and does not need parsed output, transformations, defaults, or detailed
  issues. Use `z.validateAsync` for async schemas.
- Keep authorization, tenant isolation, uniqueness, availability, and other
  effectful business decisions outside structural schemas. A refinement may
  express a bounded pure cross-field invariant; it must not hide remote I/O or
  consequential effects.

Choose object behavior intentionally:

- `z.strictObject()` when unknown keys are contract violations.
- `z.object()` when stripping unknown keys is the intended normalization.
- `z.looseObject()` only when preserving unknown keys is part of the contract.

Treat coercion as parsing policy, not convenience. Constrain the accepted input
before `z.coerce.*` when broad JavaScript coercion would admit surprising values.
Keep lossy transforms visible and test input and output types separately.

## Composition And Errors

- Prefer object spread for composing stable object shapes when it keeps
  ownership clear and improves TypeScript performance. Use `.extend()` for a
  genuine derived schema; do not build long mutation-like chains.
- Do not reach into undocumented Zod internals. Packages that accept schemas
  generically should follow Zod's library-author guidance and depend on the
  documented core interfaces.
- Translate `ZodError` at the owning boundary into the repository's stable error
  contract. Preserve machine-usable paths and codes where consumers need them,
  but do not expose secrets, raw payloads, stack traces, or unstable internal
  details.
- Centralize locale and error-map policy per application boundary. Do not embed
  presentation copy throughout shared schemas unless that schema owns the user-
  facing contract.
- Use current Zod 4 error APIs such as the `error` parameter and supported error
  formatting helpers. Do not introduce APIs deprecated by the official migration
  guide.

## Zod 4.5 Compilation

Compilation is an optimization, not a correctness feature or universal default.

- Measure a representative boundary first. Favor wide or nested objects,
  arrays, tuples, and unions on demonstrated hot paths; simple or infrequent
  schemas rarely justify added policy.
- Compile the final schema after refinements, transforms, metadata, and other
  derivation. Methods that derive another schema return an uncompiled schema.
- Use `z.compile(FinalSchema)` for explicit local ownership. In tests, use
  `{ strict: true }` when the requirement is to prove the selected schema is
  actually compilable rather than silently falling back.
- `import "zod/compile"` is application-only. It must execute before schema
  construction, and adoption requires an entry-point ownership review, a Content
  Security Policy/runtime review, representative benchmarks, and equivalence
  tests. Never preload it from a published library.
- Compilation generates functions dynamically. Respect CSP or no-eval
  environments and configure `jitless` where required. Do not weaken CSP to gain
  parser throughput.
- Async schemas, recursion, coercions, transforms, and other unsupported shapes
  may fall back to the normal parser. Inspect the current official compilation
  documentation rather than assuming support.
- Benchmark valid and invalid traffic separately. Invalid inputs may take the
  compiled fast path and then fall back for detailed errors.

## Testing Gate

For every changed boundary, cover the smallest representative set of:

- accepted input and exact parsed output;
- missing, null, malformed, boundary, and excess values;
- unknown-key behavior;
- defaults, coercions, transforms, and input/output type divergence;
- discriminated-union variants and cross-field invariants;
- stable error translation without sensitive payload leakage;
- async behavior where applicable;
- serialized or generated contract agreement when another schema is authority.

For compilation, run the same behavioral corpus against compiled and ordinary
schemas, then benchmark a production-shaped workload with warmup and multiple
samples. Report the environment, payload shapes, valid/invalid mix, baseline,
and uncertainty. Do not repeat upstream benchmark numbers as project evidence.

## Migration Workflow

1. Inventory direct and transitive Zod versions, import subpaths, schema owners,
   public schema types, error translation, and dependent packages.
2. Read the official migration guide for the installed and target lines. Record
   behavior changes that affect defaults, records, unknown keys, coercion,
   errors, and inferred types.
3. Add or strengthen characterization tests before a major upgrade.
4. Update the manifest and lockfile through the repository package manager.
   Remove deprecated APIs rather than adding compatibility wrappers.
5. Run the owning package's focused tests and typecheck. Widen to consumers and
   workspace gates when schemas cross package or public boundaries.
6. Evaluate new performance features as a separate measured change. A version
   migration does not authorize global compilation.
7. Report unresolved consumers, unsupported schemas, benchmark gaps, and any
   contract behavior intentionally changed.

## Review Findings

Flag these as defects or risks when evidence supports them:

- a duplicated interface that can drift from its owning schema;
- parsed data discarded while raw input continues inward;
- `safeParse` failure ignored or converted to an untyped generic error;
- broad coercion admitting unintended values;
- effectful authorization or network calls hidden in refinements;
- a library pinning consumers to one exact Zod release;
- global compilation in a library or without entry-point/CSP ownership;
- performance claims copied from upstream without a representative benchmark;
- two independently maintained schemas claiming authority for one contract.

## Official References

- [Zod documentation](https://zod.dev/)
- [Zod 4 migration guide](https://zod.dev/v4/changelog)
- [Zod 4.5 release](https://zod.dev/blog/zod-4-5)
- [AOT compilation](https://zod.dev/compile)
- [Library-author guidance](https://zod.dev/library-authors)

Verify these sources and the current stable release before changing version or
performance policy; Zod's API and release line are time-sensitive.
