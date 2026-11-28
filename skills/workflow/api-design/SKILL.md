---
name: api-design
description: "Design or review the public surface of a library or SDK that people and coding agents call from code: functions, options, results, errors, cancellation, exports, names. Use before adding or changing an export, and when reviewing one. Not for HTTP services, command lines (cli-design) or module boundaries (architecture-review)."
tags:
  - api
  - sdk
  - library
  - design
  - review
---

# API design

An API is judged where it is called. Design from the call sites of real
consumers, and make every result say what was established, no more. A surface
that reads well but promises more than it checked has failed.

Idioms (unions, `readonly`, exports) come from the language's standards skill,
such as `typescript-standards`. Module boundaries go to `architecture-review`,
a command line over this API to `cli-design`, its docs to `technical-writing`.

## Design a surface

Stop at a product or taste decision and ask the owner.

1. **Consumers.** List who calls this today: repository, file, function, what
   each needs. No consumer, no export.
2. **Call sites.** Write two or three real calls per consumer, with error
   handling and cancellation, before any type. Someone who has seen only those
   lines should understand them.
3. **Outcomes.** A table: outcome, trigger, the caller's next action, returned
   or thrown. Add what each result guarantees and what it does not.
4. **Names.** One name per concept across functions, options, results, errors
   and docs, taken from the caller's own ecosystem. Note the synonyms you
   rejected.
5. **Alternatives.** Two or three designs that differ in shape (function or
   handle, union or throw, one entry point or several), including the simplest
   that serves the consumers. Pick one and say what the simplest rejected one
   loses. Give each export a one-sentence summary; if it needs "and", it does
   two jobs.
6. **Challenge** it with [the review checklist](references/review-checklist.md).
   Then the probe: can a caller holding only the type declarations handle every
   outcome, cancel, and tell a retryable failure from a final one?
7. **Enforce.** For each convention that must outlive this change, name the
   tool that checks it (lint rule, type test, package-shape check).

## Rules

**Shape**

- A plain function beats a handle, class or builder. Use a handle only when
  real state outlives one call.
- Positional parameters are the one or two required subjects
  (`check(file, options)`). Everything else is one inline options object with
  `readonly` fields and optional fields typed `?: T | undefined`.
- Offer what every implementation honours. Special cases go behind an explicit
  escape hatch (`client.raw`).
- Sibling operations return one shape with the same field names.

**Honesty**

- Refuse what you cannot do before any side effect. An option accepted and
  ignored is a bug.
- When support varies, expose a capability description that defaults to "no",
  built from the same data as the runtime check (only with two or more
  implementations).
- When a result's meaning depends on scope, method or version, put that on the
  result (`guarantee`, `scope`), so a forwarded result keeps its caveat.
- Reading a field does no I/O. Costly work is an explicit call.

**Outcomes and errors**

- Return every outcome a caller must handle, including "could not decide", as a
  union on one literal field (`status`). Each variant has only its own fields.
- Throw for misuse (`TypeError`, `RangeError`) and broken invariants, and
  validate at runtime too, since JavaScript callers and agents bypass types.
- Thrown errors use a few codes grouped by the caller's next action (fix the
  call, not possible here, retry), carry `name`, `code` and `cause`, and keep
  secrets out of messages. Mark deterministic failures not retryable.
- "Unsupported" is a value when it depends on the analysed input, a throw when
  the caller could check options or environment up front.

**Cancellation and time**

- Every async operation takes `signal?: AbortSignal`, checks it before
  starting, and rejects with `signal.reason`.
- A time limit names its unit (`timeoutMs`) and is its own outcome, never
  success.

**Exports and change**

- Named exports, small entry points, no wildcard re-exports. Third-party types
  stay out of the core surface, or that export is marked less stable.
- The unchecked variant carries the suffix (`getUnsafe`).
- Every observable behavior becomes a dependency for someone (Hyrum's Law), so
  expose only what you will keep. Before release, change the API, migrate the
  callers and delete the old path in one change, with no aliases. After
  release, adding is safe; renaming, retyping or removing is a break, recorded
  in the changelog with the old form, the new form and why.

## Example

A checker whose `check(file)` returns `{ ok: boolean, error?: string }`.

- Bad: `ok: false` covers a violation, a timeout and an unsupported input, and
  a caller cannot tell a retry from a fix.
- Good: `check(file, { signal, timeoutMs })` returns a union:

  ```ts
  type Result =
    | { status: "passed"; guarantee: "bounded"; depth: number }
    | { status: "failed"; trace: Trace }
    | { status: "unsupported"; construct: string }
    | { status: "timeout"; timeoutMs: number };
  ```

  It throws `TypeError` for a bad `file`, and `passed` says it was bounded.

## Review an existing surface

Run [the review checklist](references/review-checklist.md). Report each "no"
with file and line, the rule it breaks and the smallest fix. A rename with no
behavior change is a `refactor`.

## Done when

- every export has a named consumer and a summary;
- the outcome table covers every result and every throw;
- the checklist passes, or each failure is listed with its reason;
- the open decisions are listed for the owner.

[Sources](references/sources.md) holds the evidence and where sources disagree.
