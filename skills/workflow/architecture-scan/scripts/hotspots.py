#!/usr/bin/env python3
"""Rank a Git repository's hot spots and cross-module change coupling (read-only).

Usage: python hotspots.py [REPO] [--since "6 months ago"] [--top 15] [--min-shared 5] [--depth 2]

Hot spots: commits touching each file, times its current line count. Change
coupling: pairs of non-test files in different modules that change in the same
commits, as a share of the less-changed file's commits. Merges, bot authors,
dependency and formatting commits, lockfiles, generated files, docs and binaries
are dropped first. Standard library only.
"""

from __future__ import annotations

import argparse
import collections
import itertools
import re
import subprocess
from pathlib import Path

BOT_AUTHOR = re.compile(r"\[bot\]|\bbot\b|renovate|dependabot", re.I)
NOISE_SUBJECT = re.compile(r"^(chore|build)\(deps[^)]*\)|^style\b|^chore: (format|bump|lint)", re.I)
SKIP_FILE = re.compile(
    r"(^|/)(package-lock\.json|bun\.lockb?|yarn\.lock|pnpm-lock\.yaml|Cargo\.lock|go\.sum)$"
    r"|\.(lock|snap|svg|png|jpe?g|gif|ico|webp|woff2?|pdf|md)$|(^|/)(generated|dist|build)/|\.gen\."
)
TEST_FILE = re.compile(r"(^|/)(tests?|__tests__|spec)/|[._-](test|spec)\.[^/]+$")
LARGE_COMMIT = 25  # sweeping commits (renames, mass edits) say little about coupling


def read_commits(repo: Path, since: str) -> list[set[str]]:
    log = subprocess.run(
        ["git", "-C", str(repo), "log", f"--since={since}", "--no-merges", "--format=@@%an%x09%s", "--name-only"],
        capture_output=True, text=True, encoding="utf-8", errors="replace", check=True,
    ).stdout
    commits: list[set[str]] = []
    current: set[str] | None = None
    for line in log.splitlines():
        if line.startswith("@@"):
            author, _, subject = line[2:].partition("\t")
            noise = BOT_AUTHOR.search(author) or NOISE_SUBJECT.search(subject)
            current = None if noise else set()
            if current is not None:
                commits.append(current)
        elif line.strip() and current is not None and not SKIP_FILE.search(line.strip()):
            current.add(line.strip())
    return commits


def module(path: str, depth: int) -> str:
    parts = path.split("/")[:-1]
    return "/".join(parts[:depth]) or "."


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--since", default="6 months ago")
    parser.add_argument("--top", type=int, default=15)
    parser.add_argument("--min-shared", type=int, default=5)
    parser.add_argument("--depth", type=int, default=3, help="path segments that name a module")
    args = parser.parse_args()
    repo = Path(args.repo)

    commits = [{f for f in c if (repo / f).is_file()} for c in read_commits(repo, args.since)]
    churn = collections.Counter(f for c in commits for f in c)
    lines = {f: sum(1 for _ in open(repo / f, encoding="utf-8", errors="ignore")) for f in churn}
    print(f"{len(commits)} commits since {args.since} after filtering; {len(churn)} files still present")

    print(f"\nHot spots (commits x lines), top {args.top}:")
    for f, n in sorted(churn.items(), key=lambda kv: kv[1] * lines[kv[0]], reverse=True)[: args.top]:
        print(f"  {n:4} commits {lines[f]:6} lines  {f}")

    shared: collections.Counter[tuple[str, str]] = collections.Counter()
    for c in commits:
        code = sorted(f for f in c if not TEST_FILE.search(f))
        if len(code) > LARGE_COMMIT:
            continue
        for a, b in itertools.combinations(code, 2):
            if module(a, args.depth) != module(b, args.depth):
                shared[(a, b)] += 1
    rows = sorted(
        ((n / min(churn[a], churn[b]), n, a, b) for (a, b), n in shared.items() if n >= args.min_shared),
        reverse=True,
    )
    print(f"\nCross-module coupling (shared commits / the less-changed file's), at least {args.min_shared} shared:")
    for ratio, n, a, b in rows[: args.top]:
        print(f"  {ratio:4.0%} {n:3}  {a}  <->  {b}")
    if not rows:
        print("  none")


if __name__ == "__main__":
    main()
