# API review checklist

Each line is a yes-or-no question. Every "no" needs a file and line.

**Consumers and names**

- [ ] Every export has a consumer that exists today. Nothing is left to delete.
- [ ] One word per concept across functions, options, results, errors, docs and CLI.
- [ ] No vague names: `info`, `data`, `manager`, `service`, `instance`, `handle`.

**Honesty**

- [ ] Every option is honoured by every implementation, or refused before any side effect.
- [ ] Capability differences are queryable, default to "no", and come from the same data as the runtime check.
- [ ] Results whose meaning depends on scope, method or version carry it.
- [ ] No field read does I/O or heavy work.

**Outcomes and errors**

- [ ] Expected outcomes, including "could not decide", are in the return type as a discriminated union.
- [ ] No variant carries another variant's fields.
- [ ] Exceptions mean only misuse or broken invariants, and are also checked at runtime.
- [ ] Thrown codes are grouped by the caller's next action. Deterministic failures are marked not retryable.
- [ ] Errors have a stable `name` and `code`, keep `cause`, and pass instance checks across bundles.
- [ ] No secret reaches a message or `cause`.

**Cancellation and time**

- [ ] Every async operation takes `signal`, checks it before starting, and rejects with `signal.reason` or a documented equivalent.
- [ ] A timeout and an abort are distinguishable. The timeout's unit is in its name or its doc.

**Shape**

- [ ] Positional parameters are only the required subjects. Options are one object, `readonly`, with `?: T | undefined`.
- [ ] No overload that a union or an optional parameter would replace. Callbacks return `void`.
- [ ] Sibling operations return the same shape.
- [ ] No handle, class or builder without state that outlives one call.

**Exports and change**

- [ ] Named exports and small entry points, with no wildcard re-exports.
- [ ] Third-party types are absent from the core surface, or marked less stable.
- [ ] Each export has a one-sentence summary, a declared stability, and an example only for behaviour the signature doesn't show.
- [ ] Breaking changes have changelog entries naming the old form, the new form and the reason. No aliases or shims remain without a removal date.
- [ ] Conventions that span many exports or packages are checked by a tool.
