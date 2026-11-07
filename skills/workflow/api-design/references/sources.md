# Sources for api-design

Read on 2026-11-07. Paths are inside each project's repository.

## Where the rules come from

| Rule | Evidence |
| --- | --- |
| Start from call sites | tla-ts `README.md` opens with one `await check(...)` call and its result; Matt Pocock's `codebase-design/DESIGN-IT-TWICE.md` asks each candidate for a usage example |
| One word per concept | Google [AIP-190](https://google.aip.dev/190): "Use the same name or term for the same concept"; files-sdk 3.0.0 renamed `type` to `contentType` and `name` to `key` on every surface (`CHANGELOG.md`) |
| Small surface, escape hatch | files-sdk `AGENTS.md`: "Common subset, not lowest common denominator ... 'Use `raw`' beats 'add it to the core'" |
| Refuse instead of degrading | files-sdk `AGENTS.md`: "Fail loud, never degrade silently"; its 3.0.0 changelog fixes `url(key, { expiresIn })` returning a permanent link and an ignored `defaultUrlExpiresIn`; Chat SDK throws `NotImplementedError` for a missing adapter method |
| Capabilities default to "no" | files-sdk `src/index.ts` capabilities snapshot ("an adapter that says nothing never advertises a wrong `true`"); vercel/chat `catalog` ("Omitted keys mean `no`") |
| Outcomes as a discriminated union | Effect, [two error types](https://effect.website/docs/error-management/two-error-types/): expected errors are tracked in the type, defects are not; tla-ts `ProofObligation` (good) against `CheckResult`, a bag of optional fields |
| Throw codes by next action | files-sdk `internal/errors.ts`: `Invalid` ("Fix the call"), `Unsupported`, `Provider` (the only retried code); Effect "reason" errors, one error with a tagged reason; Google [AIP-193](https://google.aip.dev/193): stable machine-readable reason, actionable message |
| Error identity across bundles | files-sdk brands errors with `Symbol.for` and `Symbol.hasInstance`; the AI SDK uses `isInstance` |
| `signal` and `signal.reason` | [DOM standard, AbortController API integration](https://dom.spec.whatwg.org/#abortcontroller-api-integration): reject unsettled promises with the signal's abort reason |
| Options object, inline, `readonly`, `\| undefined` | Effect `.agents/skills/effect-development`; [TypeScript Do's and Don'ts](https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html) on overloads and callbacks |
| Guarantee on the result | files-sdk `signedUrl.expiry: "exact" \| "provider" \| "none"` says who decides a link's lifetime; tla-ts carries checker-specific fidelity fields on its result, which shows the cost of too many |
| No hidden I/O on reads | files-sdk 3.0.0: "No more hidden downloads" |
| One shape for siblings | files-sdk 3.0.0 replaced four bulk result arrays with one `BulkResult<T>` |
| Unchecked suffix | Effect v4 renamed `unsafeX` to `xUnsafe` (`migration/v3-to-v4.md`) |
| Exports and stability | Effect `jsdocs/declarations.md`: APIs exposing a third-party dependency are `@stability unstable` |
| Migrate callers, then delete | pstack `principle-migrate-callers-then-delete-legacy-apis`; Stripe, [API versioning](https://stripe.com/blog/api-versioning): fields stay present, additions are safe |
| Enforce with a tool | vercel/chat enforces adapter naming with konsistent; files-sdk drift tests between its catalog, exports and adapters |

## Community context

Posts read on X, as context and not as rules:

- Hayden Bleasel, 2026-10-09, Files SDK v3: "Clearer errors and consistent results / Rebuilt docs + 20 guides".
- Matt Pocock, 2026-10-01: Effect's "typed errors/dependencies power up your type checking" when working with agents.
- Dillon Mulroy, 2025-02-13: treating errors generically leads to fragile software; errors as values make you handle them.
- Vanilagy, 2026-08-20: against Rust-style `Result` objects in TypeScript (verbose, an allocation per return); prefers `T | Error`.
- grimcodes, 2026-11-05/06: a small declarative SDK surface took hours of iteration.

## Where sources disagree

- **Unsupported input.** tla-ts and files-sdk throw it; a checker whose callers treat "unsupported" like any other non-proof is better served by a status. The skill's rule (value when it depends on the analysed input, throw when the caller can check it up front) is a synthesis, not a quoted source.
- **Abort.** The DOM standard rejects with `signal.reason`; files-sdk wraps it in its own error. The skill defaults to the standard.
- **Errors as values.** No consensus for public libraries. The skill keeps exceptions for misuse and unions for expected outcomes, and does not require a `Result` type.

## Gaps

- No measured evidence that any rule improves how agents use an API.
- Streaming and `AsyncIterable` results are not covered.
