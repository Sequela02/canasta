# End-to-end verification

Use when a change must be proven in the running product: a UI flow, a CLI, a
service, a migration or a parser. "It compiles" and "the unit tests pass" do not
show that the real artifact works.

State the finish condition up front, as checks someone can run, then make the
run repeatable through the repository's own scripts:

1. **Launch:** the one command that starts the product locally, from the
   repository's task runner.
2. **Doctor:** a quick check that it is up and in the expected state (health
   endpoint, version, seeded data) before driving it.
3. **Drive:** the journey itself, through the existing E2E harness, a browser
   or HTTP script, a PTY, or the real CLI command. Replay saved input for a
   parser or migration; read back the written value for storage.
4. **Evidence:** keep what someone else can inspect: command output, a
   screenshot or recording, a trace, the failing then passing test. Say
   "inconclusive" when a check could not run.
5. **Cleanup:** stop what was started and remove temporary data, then confirm
   the evidence survived.

When a repository has no such script, use the available capability for this
change and propose adding one; do not build a global generator or schedule a
full-app sweep by default. Tool syntax comes from the tool's `--help`, not from
a skill.

## Web applications

A web application should own a deterministic browser smoke suite: entry screen,
main navigation and critical journeys, at the target widths. When a change
creates or changes a screen and the repository has none, say so in the
verification report and propose one. A model-judged step (an agentic
`act`/`assert`) is review evidence, never a passed check.
