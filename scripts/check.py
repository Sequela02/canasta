"""Check this documentation/skill pack with Python's standard library only."""

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote


def check(root: Path) -> list[str]:
    errors = []
    skills = {}
    for group in ("workflow", "stack"):
        base = root / "skills" / group
        entries = sorted(base.glob("*/SKILL.md"))
        skills[group] = entries
        if not entries:
            errors.append(f"No skills in {group}")
        for entry in entries:
            text = entry.read_text(encoding="utf-8")
            header = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
            if not header:
                errors.append(f"Missing frontmatter: {entry.relative_to(root)}")
                continue
            name = re.search(r"^name: (.+)$", header[1], re.M)
            if not name or name[1] != entry.parent.name:
                errors.append(f"Name mismatch: {entry.relative_to(root)}")
            if not re.search(r"^description: .+", header[1], re.M):
                errors.append(f"Missing description: {entry.relative_to(root)}")
            if re.search(r"^(tools|allowed-tools|hooks|disable-model-invocation):", header[1], re.M):
                errors.append(f"Tool-specific metadata: {entry.relative_to(root)}")
        plugin_root = root if group == "workflow" else base
        manifest_path = plugin_root / ".claude-plugin" / "plugin.json"
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            expected = ["./" + entry.parent.relative_to(plugin_root).as_posix() for entry in entries]
            if sorted(manifest["skills"]) != expected:
                errors.append(f"Plugin skill inventory mismatch: {group}")
            if manifest["name"] != "canasta-" + group:
                errors.append(f"Plugin name mismatch: {group}")
            for key in ("version", "description", "author", "license"):
                if not manifest.get(key):
                    errors.append(f"Missing plugin field {key}: {group}")
        except (OSError, ValueError, KeyError, TypeError) as error:
            errors.append(f"Invalid plugin manifest {group}: {type(error).__name__}")
    try:
        market = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        expected = {"canasta-workflow": "./", "canasta-stack": "./skills/stack"}
        entries = market["plugins"]
        if market["name"] != "canasta" or len(entries) != 2 or {p["name"]: p["source"] for p in entries} != expected:
            errors.append("Marketplace source/name mismatch")
    except (OSError, ValueError, KeyError, TypeError) as error:
        errors.append(f"Invalid marketplace: {type(error).__name__}")

    agent_names = {"advisor", "clerk", "explorer", "reviewer", "verifier", "worker"}
    agents = sorted((root / "agents").glob("*.md"))
    if {path.stem for path in agents} != agent_names:
        errors.append("Agent inventory mismatch")
    for path in agents:
        text = path.read_text(encoding="utf-8")
        header = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        label = path.relative_to(root).as_posix()
        if not header:
            errors.append(f"Missing agent frontmatter: {label}")
            continue
        name = re.search(r"^name: (.+)$", header[1], re.M)
        if not name or name[1] != path.stem:
            errors.append(f"Agent name mismatch: {label}")
        if not re.search(r"^description: .+", header[1], re.M):
            errors.append(f"Missing agent description: {label}")
        # Public templates carry only portable identity, never local model choices.
        if any(not re.match(r"^(name|description): .+", line)
               for line in header[1].splitlines()):
            errors.append(f"Nonportable agent metadata: {label}")
        if not text[header.end():].strip():
            errors.append(f"Missing agent body: {label}")

    for path in sorted(root.rglob("*.json")):
        if ".git" in path.relative_to(root).parts:
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError):
            errors.append(f"Invalid JSON: {path.relative_to(root)}")
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.relative_to(root).parts:
            continue
        text = path.read_text(encoding="utf-8")
        # Examples inside code fences are not repository links.
        prose = re.sub(r"^```.*?^```[^\n]*", "", text, flags=re.M | re.S)
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", prose):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            destination = (path.parent / unquote(target.split("#")[0])).resolve()
            if not destination.is_relative_to(root.resolve()) or not destination.exists():
                errors.append(f"Broken local link: {path.relative_to(root)} -> {target}")
    readme_path = root / "README.md"
    if readme_path.exists():
        readme = readme_path.read_text(encoding="utf-8")
        for entries in skills.values():
            for skill in entries:
                if skill.relative_to(root).as_posix() not in readme:
                    errors.append(f"Skill missing from README: {skill.parent.name}")
        for agent in agents:
            if agent.relative_to(root).as_posix() not in readme:
                errors.append(f"Agent missing from README: {agent.stem}")
    else:
        errors.append("README missing")
    method_path = root / "docs/how-i-work.md"
    if not method_path.exists() or len(method_path.read_text(encoding="utf-8").splitlines()) > 250:
        errors.append("Working method missing or over 250 lines")
    notice = root / "skills/workflow/tdd/NOTICE"
    if not notice.exists() or "Copyright (c) 2026 Matt Pocock" not in notice.read_text(encoding="utf-8"):
        errors.append("Adapted debugging reference MIT notice missing")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    findings = check(args.root)
    for finding in findings:
        print(f"FAIL: {finding}")
    if not findings:
        print("PASS: manifests, skill and agent metadata/inventory, JSON, local links, README, method length and MIT notice")
    sys.exit(bool(findings))
