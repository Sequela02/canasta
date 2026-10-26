> Reference for `tdd`, adapted from the `diagnosing-bugs` skill in
> mattpocock/skills (revision 5beb35b, 2026-10-19), MIT; notice below. Local
> changes: a budget instead of "refuse to give up", hypotheses scaled to the
> bug, probes kept out of source, and repository docs instead of fixed files.

# Diagnosing hard bugs

Use when a failure's cause is not obvious. A trivial bug needs only steps 1, 5
and 6: reproduce it, fix it test-first, rerun the repro.

Set a budget for the investigation (time, attempts or runs) before starting.
When it runs out, stop and report what you tried, what you ruled out, and what
would unblock you.

**Redact.** Before showing commands, output or captured artifacts, replace every
secret with `<REDACTED>`. Pass credentials as environment variables so they stay
out of what you show, and quote only the lines of a capture that carry the
signal. If the redacted output is not enough to diagnose, say so and ask.

## 1. Build a feedback loop

The loop is most of the work. With a pass/fail signal that goes red on *this*
bug, bisection, hypotheses and probes all have something to consume; without
one, reading code produces theories, not causes.

Ways to build one, roughly in this order:

1. A failing test at whatever seam reaches the bug.
2. An HTTP script against a running dev server.
3. A CLI call with a fixture input, diffed against a known-good output.
4. A headless browser script that drives the UI and asserts on DOM, console or
   network.
5. A captured trace (request, payload, event log) saved to scratch and replayed
   through the code path.
6. A minimal harness in the session scratch that exercises the path with mocked
   dependencies.
7. A property or fuzz loop when the output is only sometimes wrong.
8. A bisection script for `git bisect run` when the bug appeared between two
   known states.
9. A differential run of the same input through two versions or configurations.
10. Last resort, a structured script that prompts a human for each manual step
    and prints what they report as `KEY=VALUE` lines.

Then tighten it: faster (skip unrelated setup, narrow scope), sharper (assert the
exact symptom, not "didn't crash"), deterministic (pin time, seed randomness,
isolate files and network). For a non-deterministic bug, aim for a higher
reproduction rate rather than a clean repro: repeat, parallelise, add stress.

The loop is ready when you can name one command, already run once with its
redacted output shown, that drives the real code path, asserts the user's exact
symptom, gives the same verdict each run (or a pinned high rate), runs in
seconds, and runs unattended. If you cannot build one within the budget, say so,
list what you tried, and ask for access to an environment that reproduces it, a
redacted capture, or permission for temporary production instrumentation. Do not
move on to hypotheses without a loop.

## 2. Reproduce and minimise

Run the loop and confirm it shows the failure the user described, not a nearby
one, across several runs. Record the exact symptom.

Then cut inputs, callers, configuration, data and steps one at a time, rerunning
after each cut, until every remaining element is load-bearing. The minimal repro
narrows the hypotheses and becomes the regression test.

## 3. Hypothesise

Before testing, write falsifiable hypotheses, as many as the bug's uncertainty
warrants, ranked: "if X is the cause, changing Y makes it disappear." A
hypothesis without a prediction is a guess; sharpen it or drop it. Share the
ranked list with the user when they are present, since they may know what
changed; do not block on an answer.

## 4. Probe

Each probe tests one prediction and changes one variable. Prefer, in order, a
debugger or REPL, the repository's existing logging or tracing configuration,
and a probe script in the session scratch. Do not add temporary instrumentation
to source; if only a source change can observe the behavior, ask first.

For a performance regression, measure a baseline (timing harness, profiler,
query plan) and bisect; logs are usually the wrong tool.

## 5. Fix with a regression test

Turn the minimal repro into a failing test at a seam that reproduces the real
bug pattern, watch it fail for the right reason, fix, and watch it pass. If you
forced the red by mutating code or a fixture, diff against a pristine copy to
prove the mutation took effect. If no seam can reproduce the pattern, report
that as a finding about the design instead of writing a shallow test.

## 6. Close

- Rerun the original, unminimised loop: it no longer reproduces.
- The regression test passes, or the missing seam is reported.
- Scratch harnesses and captures are gone, or kept only in the session scratch.
- The commit or PR message names the hypothesis that proved correct.

---

MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
