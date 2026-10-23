#!/usr/bin/env python3
"""CI check: a pull request that changes the plugin must bump its version and add a changelog entry.

    python3 tests/check_version_bump.py origin/main

Changes to bsky-sf-architect/README.md alone, and changes outside bsky-sf-architect/ (tests, CI, the repo README), need neither.
"""
import json
import re
import subprocess
import sys

PLUGIN = "bsky-sf-architect/.claude-plugin/plugin.json"
CHANGELOG = "CHANGELOG.md"
SOURCE = "bsky-sf-architect/"
EXEMPT = {"bsky-sf-architect/README.md"}


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def version_at(ref):
    try:
        v = json.loads(git("show", f"{ref}:{PLUGIN}"))["version"]
        return tuple(int(x) for x in re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", v).groups())
    except (subprocess.CalledProcessError, ValueError, KeyError, AttributeError):
        return None


def main(base):
    mb = git("merge-base", base, "HEAD").strip()
    changed = git("diff", "--name-only", mb, "HEAD").split("\n")
    relevant = sorted(f for f in changed if f.startswith(SOURCE) and f not in EXEMPT)
    if not relevant:
        print("No plugin files changed: no version bump needed.")
        return 0
    old, new = version_at(mb) or (0, 0, 0), version_at("HEAD")
    problems = []
    if new is None:
        problems.append(f"{PLUGIN} has no valid version (x.y.z)")
    elif new <= old:
        problems.append(f"the plugin changed but its version did not go up (was {'.'.join(map(str, old))}, now {'.'.join(map(str, new))}): bump it in {PLUGIN}")
    if CHANGELOG not in changed:
        problems.append(f"the plugin changed but {CHANGELOG} did not: add an entry for the new version")
    if problems:
        print("This pull request changes the plugin (for example " + ", ".join(relevant[:3]) + ") so:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"Version bumped to {'.'.join(map(str, new))} and the changelog was updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "origin/main"))
