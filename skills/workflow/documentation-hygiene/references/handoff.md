> Reference for `documentation-hygiene`, formerly the `handoff` skill.

# Handoff

Use when the user asks for a handoff, session summary, or notes for whoever
continues the work. A handoff is a reply or an update to the canonical record,
not a new file by default. An explicitly requested handoff document belongs
with the repository's existing continuation records; a summary request alone
does not authorize a commit.

Cover what the next person cannot reconstruct from the repository:

- **Objective and status:** the goal, and whether it is done, in progress or
  blocked (and on what).
- **What changed:** the commits or diff range, not a file inventory the diff
  already shows.
- **Decisions:** what was chosen, what was rejected and why, and which choices
  are still open.
- **Evidence:** the checks run with their results, the checks not run, and the
  limits of each. Mark claims as verified, inferred or unknown.
- **Next steps:** where to continue, what to read first, and runnable commands.

Assume the reader knows the project but not this session. Be honest about
known bugs and debt. Keep private details out of anything that will be
published.
