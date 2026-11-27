# Sources for upstream-contribution

Read on 2026-11-27. Paths are inside each project's repository.

## Where the rules come from

| Rule | Evidence |
| --- | --- |
| Worth more than its review | LLVM `llvm/docs/AIToolPolicy.md`, "Extractive Contributions": "a contribution should be worth more to the project than the time it takes to review it"; "The best ways to make a change less extractive and more valuable are to reduce its size or complexity or to increase its usefulness to the community." |
| See where attention is | Observation only: in one project over three months, about half of 29 outside issues got no answer; the answered ones were short, single-point and in areas under active work, the others longer, in deprioritized areas or asking for a design decision. Length, topic and actionability varied together, so no single cause is shown. |
| Propose an answer instead of asking for a decision | Same observation; gstack `spec/SKILL.md`: "Don't leave design decisions for the implementer. Decide them in conversation." (about specs, applied here by analogy) |
| One problem, reproduced; facts before cause | Simon Tatham, [How to Report Bugs Effectively](https://www.chiark.greenend.org.uk/~sgtatham/bugs.html) (1999): "the aim of a bug report is to enable the programmer to see the program failing in front of them"; "make very clear what are actual facts ... and what are speculations" |
| Open with the short version | Daniel Stenberg, [Ignore the slop](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/) (2026-10-22): "They always use too many words. Every report is now hundreds of lines"; "In a good report, the human writes a first paragraph explaining the problem briefly and then they submit the full report." Ghostty `AI_POLICY.md`: "AI is very good at being overly verbose and including noise that distracts from the main point. Humans must do their research and trim this down." tstack `skills/file-pr/SKILL.md`: open with a simple explanation of the problem, then the solution. |
| Collapsed detail | Opinion: no primary source found; it reconciles Tatham's "Be verbose" with the requests above for a short report. |
| Disclose AI and what the human checked | Ghostty `AI_POLICY.md`: "All AI usage in any form must be disclosed"; "The human-in-the-loop must fully understand all code." LLVM `AIToolPolicy.md`: a human in the loop, and "be transparent and label contributions" that contain substantial tool-generated content. |
| Send one at a time | Same observation (five long issues filed in two days, none answered); otherwise opinion. |
| Follow up once, after two to three weeks | Linux kernel `Documentation/admin-guide/reporting-issues.rst`: "wait two (better: three) weeks before sending a friendly reminder"; "After the reminder wait three more weeks". Kernel-specific; a project's own process wins. |

## Where sources disagree

- **Length.** Tatham asks for more information rather than less; Stenberg and Ghostty ask
  for less. They agree once ordered: the short version first, the full detail after it.
- **AI-written reports.** Stenberg reports that AI-assisted security reports are now
  "typically accurate and correct, even if much too wordy", so the problem he describes
  is length and lost human voice, not correctness. Ghostty and LLVM still require a human
  who understands and has checked the content.

## Not verified

- Bettenburg, Zimmermann et al., "What Makes a Good Bug Report?" (FSE 2008): widely cited
  for developers valuing steps to reproduce, stack traces and test cases; the paper's
  text wasn't extracted here.
- Studies of first-response time on GitHub (arXiv 2304.08426, 2310.01566): the papers
  exist; the figures attributed to them weren't found in their abstracts.
