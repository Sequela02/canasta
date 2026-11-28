"""Check that each skill's description routes the prompts it should, and only those.

A deterministic, lexical proxy for skill routing, with Python's standard library
only. Each skill's name (weighted twice) and description form a document; a
prompt is ranked against every document by TF-IDF cosine similarity.

- A positive prompt in ``evals/<skill>.json`` must rank its skill within
  ``top_k`` (3 by default).
- A negative prompt must not rank its skill first; with an ``owner``, the owner
  must also outrank it.
- No two descriptions may be near-duplicates (cosine at or above 0.75 fails,
  0.5 warns).

It cannot judge meaning. It catches the two common routing bugs: a description
missing the words users say, and one so broad it outranks the right skill. A
failure usually means fixing the description, not the case.

Ported from the deterministic tier of addyosmani/agent-skills
``scripts/run-evals.js`` (MIT, Copyright (c) Addy Osmani), at commit
``e997ac5``; see ``evals/README.md``. Local change: ``pr``/``prs`` alias to
``pull``.
"""

import argparse
import json
import math
from pathlib import Path
import re
import sys

MIN_POSITIVE = 3
MIN_NEGATIVE = 2
COLLISION_WARN = 0.5
COLLISION_ERROR = 0.75

STOP = {
    "a", "an", "and", "any", "are", "as", "at", "be", "before", "by", "for",
    "from", "in", "into", "is", "it", "its", "my", "need", "needs", "of", "on",
    "or", "our", "so", "that", "the", "them", "this", "to", "use", "want",
    "we", "when", "with", "you", "your", "help", "me", "i",
}

TOKEN_ALIASES = {
    "doc": "document", "docs": "document",
    "config": "configuration", "configs": "configuration",
    "auth": "authenticate", "authentication": "authenticate",
    "repo": "repository", "repos": "repository",
    "dep": "dependency", "deps": "dependency",
    "pr": "pull", "prs": "pull",
}


def stem(t: str) -> str:
    """Light suffix stripping, not a real stemmer (same rules as the original)."""
    if len(t) > 10 and re.search(r"ifications?$", t):
        t = re.sub(r"ications?$", "i", t)
    for suf in ("ally", "ing", "ations", "ation", "ed", "es", "al"):
        if len(t) > len(suf) + 3 and t.endswith(suf):
            t = t[: -len(suf)]
            break
    if len(t) > 3 and t.endswith("s") and not t.endswith("ss"):
        t = t[:-1]
    if len(t) > 4 and t.endswith("e"):
        t = t[:-1]
    if len(t) > 4 and t[-1] == t[-2] and t[-1] not in "aeiou":
        t = t[:-1]
    if len(t) > 3 and t.endswith("y"):
        t = t[:-1] + "i"
    return t


def tokenize(text: str) -> list[str]:
    words = re.split(r"[\s-]+", re.sub(r"[^a-z0-9\s-]", " ", text.lower()))
    return [stem(TOKEN_ALIASES.get(w, w)) for w in words if len(w) > 2 and w not in STOP]


def term_freq(tokens: list[str]) -> dict[str, int]:
    tf: dict[str, int] = {}
    for t in tokens:
        tf[t] = tf.get(t, 0) + 1
    return tf


def description(text: str) -> str | None:
    header = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not header:
        return None
    m = re.search(r"^description: *(.*(?:\n  .*)*)", header[1], re.M)
    if not m:
        return None
    value = " ".join(line.strip() for line in m[1].splitlines())
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value


def load_skills(root: Path) -> dict[str, str]:
    skills = {}
    for entry in sorted((root / "skills").glob("*/*/SKILL.md")):
        desc = description(entry.read_text(encoding="utf-8"))
        if desc:
            skills[entry.parent.name] = desc
    return skills


class Corpus:
    def __init__(self, skills: dict[str, str]):
        self.docs = {}
        for name, desc in skills.items():
            name_tokens = tokenize(name.replace("-", " "))
            self.docs[name] = term_freq(name_tokens + name_tokens + tokenize(desc))
        df: dict[str, int] = {}
        for tf in self.docs.values():
            for term in tf:
                df[term] = df.get(term, 0) + 1
        self.n = len(self.docs)
        self.df = df

    def idf(self, term: str) -> float:
        return math.log(1 + self.n / (1 + self.df.get(term, 0)))

    def vec(self, tf: dict[str, int]) -> dict[str, float]:
        return {t: f * self.idf(t) for t, f in tf.items()}

    def rank(self, prompt: str) -> list[tuple[str, float]]:
        pv = self.vec(term_freq(tokenize(prompt)))
        scores = [(name, cosine(pv, self.vec(tf))) for name, tf in self.docs.items()]
        return sorted(scores, key=lambda s: -s[1])


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    dot = sum(w * b.get(t, 0.0) for t, w in a.items())
    na = math.sqrt(sum(w * w for w in a.values()))
    nb = math.sqrt(sum(w * w for w in b.values()))
    return dot / (na * nb) if na and nb else 0.0


def run(root: Path, min_rank1: float | None) -> tuple[list[str], list[str], str]:
    skills = load_skills(root)
    corpus = Corpus(skills)
    errors: list[str] = []
    notes: list[str] = []
    positives = rank1 = 0

    for name in skills:
        path = root / "evals" / f"{name}.json"
        if not path.exists():
            errors.append(f"{name}: no case file (evals/{name}.json)")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"evals/{name}.json: invalid JSON: {e}")
            continue
        trigger = data.get("trigger", {})
        pos, neg = trigger.get("positive", []), trigger.get("negative", [])
        if len(pos) < MIN_POSITIVE or len(neg) < MIN_NEGATIVE:
            errors.append(f"{name}: {len(pos)} positive / {len(neg)} negative prompts; need {MIN_POSITIVE} / {MIN_NEGATIVE}")
        for case in pos:
            positives += 1
            ranking = corpus.rank(case["prompt"])
            idx = next(i for i, (n, _) in enumerate(ranking) if n == name)
            score = ranking[idx][1]
            top_k = case.get("top_k", 3)
            if idx == 0 and score > 0:
                rank1 += 1
            if score == 0:
                errors.append(f"{name}: no shared vocabulary with \"{case['prompt']}\"")
            elif idx >= top_k:
                top = ", ".join(f"{n} ({s:.2f})" for n, s in ranking[:3])
                errors.append(f"{name}: ranked #{idx + 1} for \"{case['prompt']}\" (need top {top_k}); top 3: {top}")
            elif idx > 0:
                notes.append(f"{name}: #{idx + 1} for \"{case['prompt']}\" (#1 {ranking[0][0]})")
        for case in neg:
            ranking = corpus.rank(case["prompt"])
            if ranking[0][0] == name and ranking[0][1] > 0:
                errors.append(f"{name}: ranked #1 for negative \"{case['prompt']}\" (too broad)")
            owner = case.get("owner")
            if owner:
                if owner not in skills:
                    errors.append(f"evals/{name}.json: unknown owner {owner}")
                    continue
                order = [n for n, _ in ranking]
                owner_score = dict(ranking)[owner]
                if owner_score == 0 or order.index(owner) > order.index(name):
                    errors.append(f"{name}: owner {owner} doesn't outrank it for \"{case['prompt']}\"")

    names = list(corpus.docs)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            sim = cosine(corpus.vec(corpus.docs[a]), corpus.vec(corpus.docs[b]))
            if sim >= COLLISION_ERROR:
                errors.append(f"collision: {a} and {b} descriptions {sim:.0%} similar")
            elif sim >= COLLISION_WARN:
                notes.append(f"overlap: {a} and {b} descriptions {sim:.0%} similar")

    rate = rank1 / positives * 100 if positives else 0.0
    if min_rank1 is not None and rate < min_rank1:
        errors.append(f"rank-1 rate {rate:.0f}% is below {min_rank1:.0f}%")
    summary = f"{len(skills)} skills, rank-1 rate {rate:.0f}% ({rank1}/{positives} positive prompts rank their skill first)"
    return errors, notes, summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("root", nargs="?", default=Path(__file__).resolve().parents[1], type=Path)
    parser.add_argument("--min-rank1", type=float, default=None, help="fail below this rank-1 percentage")
    args = parser.parse_args()
    errors, notes, summary = run(args.root, args.min_rank1)
    for line in notes:
        print(f"note: {line}")
    for line in errors:
        print(f"FAIL: {line}")
    print(summary)
    print("FAILED" if errors else "PASS")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
