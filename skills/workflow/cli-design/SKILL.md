---
name: cli-design
description: Design or review a command-line interface that people, scripts and coding agents run (commands, flags, output, --json, exit codes, help, errors, prompts, signals). Use before adding or changing a command or flag, and when reviewing one.
tags:
  - cli
  - design
  - review
---

# CLI design

A command line is an API whose callers are people, scripts and agents. An
agent reads the exit code first, then stdout, and never answers a prompt.
Design for that reader and for a person at a terminal at once.

When the CLI wraps a library, design the library first with `api-design`:
the command line maps arguments onto it and prints its result. Document the
CLI with `technical-writing`.

## Design a command line

Each step ends when its output exists. Stop when a step shows that no
consumer needs the feature.

1. **Consumers.** List the real callers (a person at a terminal, an agent's
   tool call, a CI job), each with the exact command line it will run.
2. **Result.** Fix the result type first. `--json` prints exactly that
   result. The CLI adds fields only for failures that happen before the
   library is called.
3. **Grammar.** A synopsis per command: at most one positional (usually the
   input file), long names for every flag, value names, which flags repeat,
   defaults, and mutual exclusions. Reuse the standard names below and the
   wrapped tool's names.
4. **Outcomes.** One row per outcome: exit code, stream, human summary line,
   JSON `status`. Include usage error, crash, interrupt and timeout.
5. **Errors.** For each failure a user can cause: the message and the next
   command or flag to try.
6. **Terminal behaviour.** Colour, progress and prompts, split by TTY and
   non-TTY.
7. **Help.** `--help` per command, leading with examples, plus the short
   help printed when required input is missing.
8. **Contract tests**, written before the implementation: see
   [contract tests](references/contract-tests.md).

For a change to an existing CLI, run steps 2 to 5 and 8 against the diff and
mark every removed or renamed flag, exit code or JSON field as breaking.

## Rules

**Parsing**

- Use the platform's parser in strict mode (`util.parseArgs` with
  `strict: true`, clap, argparse). An unknown flag, a missing value, a bad
  value or an extra positional is a usage error.
- Prefer flags to positionals. Every flag has a long name. Reserve
  `-h`/`--help` and `--version`. Standard names: `--json`, `-n`/`--dry-run`,
  `--no-input`, `-o`/`--output`, `-q`/`--quiet`, `-f`/`--force`. `--` ends
  options; `-` means stdin or stdout where a file is taken.
- When a value can contain commas, as an expression can, repeat the flag
  instead of splitting on commas.
- No catch-all command and no prefix matching of command names.

**Output**

- The result goes to stdout. Progress, logs, warnings, hints and errors go
  to stderr.
- Human-readable output by default. `--json` prints one JSON document on
  stdout, with the same exit code as human mode. Add another format only for
  a consumer that needs it. Use JSON Lines only for long runs that emit
  events.
- Once parsing succeeded, failures in `--json` mode use the result's error
  shape on stdout. Usage errors stay text on stderr with the usage code,
  since no result exists yet.
- Keep the JSON deterministic: the same input gives the same bytes. Put
  timestamps and durations in a separate field, or leave them out.
- `--json` fields, exit codes, flag names and environment variable names are
  a versioned interface. Human text may change.

**Exit codes**

- 0 only when the command did what was asked. A check that examined nothing
  is not a success.
- Usage error is 2. Uncaught crash is 1.
- Give distinct codes only to outcomes a caller branches on, and publish
  them as a table.
- Keep codes clear of the shell (126 to 165, 255), the runtime (Node uses 1
  and 3 to 14) and any tool you wrap. A range such as 20 to 29 is clear of
  all three for a Node CLI.
- Interrupt exits 130 (SIGINT) or 143 (SIGTERM), after a bounded cleanup.

**Errors and help**

- Every error says what went wrong, where, and the exact next command to
  run. Put the key line last. No stack trace for an expected error.
- `--help` goes to stdout with exit 0, shows defaults, and leads with real
  examples. Missing required input prints short help to stderr with the
  usage code.

**Terminal and environment**

- Never require a prompt. Without a TTY on stdin, or with `--no-input`, fail
  fast and name the flag to pass. Read stdin only when it is not a TTY or
  when `-` is given.
- Colour and animation only when that stream is a TTY. Respect `NO_COLOR`,
  `TERM=dumb` and `--no-color`. On a non-TTY, print progress as plain lines.
- Print something within about 100 ms for anything slow.
- Bound every wait with a timeout that has a default. A timeout is its own
  outcome, never success.
- Configuration precedence: flags, then environment, then project file, then
  user file. Read secrets from a file or stdin, never from a flag.
- Make state-changing commands safe to rerun. Destructive ones get
  `--dry-run` and an explicit `--yes` or `--force`.

## Review an existing CLI

Run the checklist in [contract tests](references/contract-tests.md). Report
each failure with the command line that shows it, its exit code and output,
and the rule it breaks.

## Done when

- the synopsis, the outcome table and the error messages exist;
- the contract tests run the built binary, and pass;
- the stable surface (flags, exit codes, JSON fields) is listed in the docs.

[Sources](references/sources.md) lists the evidence behind these rules and
where sources disagree.
