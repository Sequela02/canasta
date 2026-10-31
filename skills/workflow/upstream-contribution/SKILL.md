---
name: upstream-contribution
description: "Prepare an issue, commit or pull request for a project you don't maintain, following its contribution and AI policy, its conventions and its CI. Use before writing anything to submit to another project's repository."
---

# Upstream contribution

The project's rules decide what you submit. Your own organization's
conventions, such as risk notes, merge policies, templates and attribution
habits, stay out unless the project asks for them.

1. **Read the project's rules before writing.** Read `CONTRIBUTING`, any AI or
   agent policy it links, its pull request and issue templates, any
   contributor `AGENTS.md`, and three recently merged pull requests from
   outside contributors. Note what it asks for and what it forbids.
2. **Stop when the policy forbids the contribution.** If it rules out this
   contribution as prepared, for example AI help on an issue reserved for
   newcomers or an AI-written description, don't write the submission. Tell
   the user which rule applies and what the policy allows instead: another
   issue, doing it without AI, or asking the maintainers.
3. **Disclose AI use exactly as the project asks.** Follow its placement (pull
   request description, commit trailer or both) and its format. Don't use a
   format it forbids, such as an `Assisted-by:` trailer. If it says nothing,
   ask the user. Never add a sign-off, DCO line or CLA statement for the
   human; they add their own.
4. **Match the project's style.** Copy the title format, sections, length and
   tone of its merged pull requests. Address the project, not one maintainer.
5. **Make the smallest change that fits its design.** Before submitting, review
   the diff against its standards, and check that every pattern you copied has
   a reason that applies here.
6. **Predict CI only by reproducing it.** Use the same workflow, platform,
   branches and job types. Name any job you didn't run.
7. **Lead with the general problem.** Then cite the project's own stated rule
   it breaks, then your case as evidence. Keep your own product's internals
   out; the reproduction must not need them.
8. **The user posts it.** The user reviews and posts, or approves, everything
   that leaves their machine.
