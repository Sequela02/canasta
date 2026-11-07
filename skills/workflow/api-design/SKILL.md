---
name: api-design
description: Design or review the public surface of a library or SDK that people and coding agents call from code (functions, options, results, errors, cancellation, exports, names). Use before adding or changing an export, and when reviewing one. Not for HTTP/REST endpoints, command lines (cli-design) or module boundaries (architecture-review).
tags:
  - api
  - sdk
  - library
  - design
  - review
---

# API design

An API is judged where it is called. Design from the call sites of real
consumers, and make every result say exactly what it established. A surface
that reads well but promises more than it checked has failed.

Use the language's standards skill, such as `typescript-standards`, for
idioms (unions, `readonly`, exports); `architecture-review` for module
boundaries; `cli-design` for a command line that wraps this API; and
`technical-writing` for its documentation.

## Design a surface

Each step ends when its output exists. Stop at a product or taste decision
and ask.

1. **Consumers.** List the consumers that exist today: repository, file,
   function, and what each needs. No consumer, no export: explore instead.
2. **Call sites.** Write two or three real call sites per consumer, with
   error handling and cancellation, before any type. They must read clearly
   to someone who has seen only these lines.
3. **Outcomes.** Write a table: outcome, trigger, the caller's next action,
   and whether it is a returned value or a throw (rules below). Add what
   each result guarantees and what it does not.
4. **Vocabulary.** One name per concept across functions, options, results,
   errors, docs and CLI. Reuse the terms the caller's ecosystem and domain
   already use. Record rejected synonyms.
5. **Alternatives.** Two or three designs that differ in shape, not naming:
   a function or a handle, a union or a throw, one entry point or several.
   Include the simplest design that serves the listed consumers. Every
   alternative serves those consumers; none is designed for imagined ones.
6. **Recommendation.** Pick one. Name the simpler design you rejected and
   what it loses. Write a one-sentence summary per export; if it needs "and"
   or "unless", the export does two things.
7. **Challenge.** Run [the review checklist](references/review-checklist.md)
   on the recommendation. Then the probe: can a caller holding only the type
   declarations handle every outcome, cancel, and tell a retryable failure
   from a final one?
8. **Enforcement.** For each convention that must outlive this change, name
   the tool that checks it (lint rule, type test, package-shape check), or
   say none is needed.

## Rules

**Shape**

- Prefer a plain function to a handle, class or builder. Use a handle only
  when real state outlives one call (a long remote job, a configured
  client). A declarative object (`{ when, require, otherwise }`) earns its
  place only when the domain is a table of rules with a consumer.
- Positional parameters only for the one or two required subjects
  (`check(file, options)`). Everything else in one options object, written
  inline unless several exports share it, with `readonly` fields and
  optional fields typed `?: T | undefined`.
- Keep the surface to what every implementation honours. Put special cases
  behind an explicit escape hatch (`client.raw`), not in core options.
- Sibling operations return one shape with the same field names.

**Honesty**

- Refuse what you cannot do, before any side effect. An option that is
  accepted and then ignored, or a result weaker than it looks, is a bug.
- When support varies by backend or mode, expose a queryable capability
  description that defaults to "no", built from the same data as the
  runtime check. Add it only with two or more implementations.
- When a result's meaning depends on scope, method or version, put that on
  the result (a `guarantee` or `scope` field), so forwarding the result
  keeps the caveat.
- Reading a field never triggers I/O or heavy work. Costly actions are
  explicit calls.

**Outcomes and errors**

- Return every outcome the caller is expected to handle, including "could
  not decide", as a union discriminated on one literal field (`status`,
  `kind`). Each variant carries only its own fields.
- Throw only for misuse (a bad argument: `TypeError`, `RangeError`) and
  broken invariants. Validate at runtime too: JavaScript callers and agents
  bypass types.
- When failures are thrown, use a small set of codes grouped by the
  caller's next action (fix the call, not possible here, retry), not one
  class per cause. Mark deterministic failures as not retryable.
- Errors carry a stable `name` and `code`, keep the original in `cause`, and
  pass instance checks across duplicate copies of the package. Keep secrets
  out of messages and `cause`.
- "Unsupported": return it as a value when it depends on the input being
  analysed; throw when it depends on options or environment the caller can
  check up front.

**Cancellation and time**

- Every async operation takes `signal?: AbortSignal` in its options, checks
  it before starting, and rejects with `signal.reason`. Normalize the abort
  into the library's own error only when the library already funnels every
  failure through one error type; document which one you chose.
- A time limit has its unit in the name (`timeoutMs`) and is its own outcome,
  distinct from a caller's abort. A timeout is never success.

**Exports and change**

- Named exports, small entry points, no wildcard re-exports. Keep
  third-party types out of the core surface; if one must appear, mark that
  export less stable.
- When a safe and an unchecked variant coexist, the unchecked one carries a
  suffix (`getUnsafe`, `getOrThrow`).
- Before release, change the API, migrate the callers and delete the old
  path in one change, with no aliases. After release, adding is safe and
  renaming, retyping or removing is a break: record it in the changelog with
  the old form, the new form and why.

## Review an existing surface

Run [the review checklist](references/review-checklist.md). Report each
"no" with file and line, the rule it breaks, and the smallest fix. A rename
with no behaviour change is a `refactor`.

## Done when

- every export has a named consumer and a one-sentence summary;
- the outcome table covers every result and every throw;
- the checklist passes, or each failure is listed with its reason;
- the open decisions are listed for the owner.

[Sources](references/sources.md) lists the evidence behind these rules and
where sources disagree.
