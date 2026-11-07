# CLI contract tests and review checklist

## Tests

Spawn the built binary, not the in-process function, so the real exit code
and streams are tested.

1. **Argument cases.** A data-driven table; each row asserts the exit code,
   stdout (empty, a summary, or a JSON shape) and a stderr pattern. Example
   rows for a checker named `tool`:

   | argv | exit | stdout | stderr matches |
   |---|---|---|---|
   | (none) | 2 | empty | `usage:` |
   | `check` | 2 | empty | `<file>` |
   | `check a.txt --bogus` | 2 | empty | `--bogus` |
   | `check a.txt --rule` | 2 | empty | `--rule needs a value` |
   | `check a.txt --timeout-ms abc` | 2 | empty | `whole number` |
   | `check missing.txt --rule r` | error code | empty | the path |
   | `check ok.txt --rule r` | 0 | summary | empty or progress |
   | `check ok.txt --rule r --json` | 0 | parses, `status` is the success value | empty or progress |
   | `check bad.txt --rule r --json` | failure code | parses, failure `status` | empty or progress |
   | `--help`, `check --help` | 0 | contains `Examples` | empty |
   | `--version` | 0 | the package version | empty |
   | `check ok.txt --rule r`, stdout piped | 0 | no `\x1b[` | |

2. **JSON equals the library.** `--json` stdout deep-equals what the library
   returns for the same input. Keep one snapshot or schema per `status`, so a
   rename or a removed field fails the test.
3. **Help matches the parser.** Generate the synopsis from the option
   definitions, or test that `--help` and the reference page list the same
   flags.
4. **Interrupt (where the platform allows).** Send SIGINT and assert exit
   130 within a time limit.

## Checklist

**Parsing**

- [ ] A strict parser: an unknown flag, a missing value, a bad value or an extra positional exits with the usage code and a stderr message.
- [ ] Repeated single-value flags are rejected, or documented as last-wins.
- [ ] `--` ends options. `-` means stdin or stdout where a file is taken.
- [ ] `-h` and `--help` work anywhere on the line.

**Outcomes**

- [ ] A published exit-code table, matched by the code.
- [ ] No code collides with the shell (126 to 165, 255), the runtime or a wrapped tool.
- [ ] "Nothing was checked" does not exit 0.
- [ ] Timeout and interrupt have their own outcomes.

**Streams**

- [ ] stdout carries only the result; stderr carries everything else.
- [ ] `--json` prints exactly one valid document, on success and on failure, with the same exit code as human mode.
- [ ] No ANSI codes when the stream is not a TTY, or when `NO_COLOR` or `TERM=dumb` is set.
- [ ] No spinners or redraws on a non-TTY.

**Errors and help**

- [ ] Every user-caused error names the cause and the next command.
- [ ] No stack trace for expected errors.
- [ ] `--help` shows defaults and examples. `--version` prints to stdout and exits 0.

**Interaction, safety, stability**

- [ ] No prompts without a TTY; a flag bypasses every prompt.
- [ ] Destructive commands have a dry run or an explicit confirmation flag.
- [ ] Reruns are safe.
- [ ] The docs list the stable surface, and removing or renaming any of it is marked breaking.
