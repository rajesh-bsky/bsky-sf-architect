"""Structural checks on the plugin: manifests, frontmatter, links between files, and that the docs match the content.

    python3 -m unittest discover -s tests -v

These catch what a read-through misses: a command or skill without a description (it won't load), a skill whose name
doesn't match its folder, an instruction that points at a reference file that doesn't exist, and a README that has
fallen behind the commands and skills.
"""
import json
import os
import re
import shutil
import subprocess
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PLUGIN = os.path.join(ROOT, "bsky-sf-architect")
NAME = "bsky-sf-architect"


def read(*parts):
    with open(os.path.join(*parts), encoding="utf-8") as fh:
        return fh.read()


def frontmatter(path):
    m = re.match(r"---\n(.*?)\n---\n", read(path), re.S)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        k, sep, v = line.partition(":")
        if sep and not line.startswith(" "):
            out[k.strip()] = v.strip().strip('"')
    return out


def files(sub, suffix):
    base = os.path.join(PLUGIN, sub)
    return sorted(os.path.join(dp, f) for dp, _, fs in os.walk(base) for f in fs if f.endswith(suffix))


def skill_dirs():
    base = os.path.join(PLUGIN, "skills")
    return sorted(d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d)))


class Manifests(unittest.TestCase):
    def test_plugin_and_marketplace_agree(self):
        plugin = json.loads(read(PLUGIN, ".claude-plugin", "plugin.json"))
        market = json.loads(read(ROOT, ".claude-plugin", "marketplace.json"))
        self.assertEqual(plugin["name"], NAME)
        self.assertRegex(plugin["version"], r"^\d+\.\d+\.\d+$")
        self.assertTrue(plugin["description"].strip())
        entry = next(p for p in market["plugins"] if p["name"] == plugin["name"])
        self.assertTrue(os.path.isdir(os.path.join(ROOT, entry["source"])), "the marketplace entry points at a folder that exists")

    def test_newest_changelog_entry_is_the_plugin_version(self):
        version = json.loads(read(PLUGIN, ".claude-plugin", "plugin.json"))["version"]
        first = re.search(r"^## (\d+\.\d+\.\d+)", read(ROOT, "CHANGELOG.md"), re.M)
        self.assertTrue(first, "the changelog has no entries")
        self.assertEqual(first.group(1), version, "the newest changelog entry must be the plugin's version")


class Frontmatter(unittest.TestCase):
    """Claude Code won't load a command, skill or agent without these fields."""

    def test_commands(self):
        paths = files("commands", ".md")
        self.assertTrue(paths)
        for p in paths:
            fm = frontmatter(p)
            self.assertTrue(fm and fm.get("description"), f"{os.path.basename(p)} needs a description")

    def test_agents(self):
        for p in files("agents", ".md"):
            fm = frontmatter(p)
            self.assertTrue(fm and fm.get("description"), p)
            self.assertEqual(fm.get("name"), os.path.splitext(os.path.basename(p))[0], "an agent's name is its file name")

    def test_skills(self):
        self.assertGreaterEqual(len(skill_dirs()), 6)
        for d in skill_dirs():
            p = os.path.join(PLUGIN, "skills", d, "SKILL.md")
            self.assertTrue(os.path.exists(p), f"skill folder '{d}' has no SKILL.md")
            fm = frontmatter(p)
            self.assertTrue(fm and fm.get("description"), p)
            self.assertEqual(fm.get("name"), d, "a skill's name is its folder name")


class Links(unittest.TestCase):
    def test_references_that_a_skill_points_to_exist(self):
        for d in skill_dirs():
            base = os.path.join(PLUGIN, "skills", d)
            for p in files(os.path.join("skills", d), ".md"):
                for ref in re.findall(r"references/([A-Za-z0-9_-]+\.md)", read(p)):
                    self.assertTrue(os.path.exists(os.path.join(base, "references", ref)),
                                    f"{os.path.relpath(p, ROOT)} points at missing references/{ref}")

    def test_every_reference_is_used_by_its_skill(self):
        for d in skill_dirs():
            refs_dir = os.path.join(PLUGIN, "skills", d, "references")
            skill = read(PLUGIN, "skills", d, "SKILL.md")
            for f in sorted(os.listdir(refs_dir)) if os.path.isdir(refs_dir) else []:
                self.assertIn(f, skill, f"references/{f} is never mentioned in the {d} skill, so Claude will not know to read it")

    def test_skills_named_in_commands_and_agents_exist(self):
        for p in files("commands", ".md") + files("agents", ".md"):
            # a skill is named `bsky-sf-architect:skill`; a slash command is /bsky-sf-architect:command, which is not one
            for skill in re.findall(r"(?<!/)" + re.escape(NAME) + r":([a-z-]+)`", read(p)):
                self.assertIn(skill, skill_dirs(), f"{os.path.relpath(p, ROOT)} names a skill that does not exist: {skill}")


class DocsMatchTheContent(unittest.TestCase):
    def test_every_command_is_in_the_readme(self):
        readme = read(PLUGIN, "README.md")
        for p in files("commands", ".md"):
            name = os.path.splitext(os.path.basename(p))[0]
            self.assertIn(f"/{NAME}:{name}", readme, f"command '{name}' is not in the plugin README")

    def test_every_skill_and_agent_is_in_the_readme(self):
        readme = read(PLUGIN, "README.md")
        for d in skill_dirs():
            self.assertIn(f"`{d}`", readme, f"skill '{d}' is not in the plugin README")
        for p in files("agents", ".md"):
            name = os.path.splitext(os.path.basename(p))[0]
            self.assertIn(f"`{name}`", readme, f"agent '{name}' is not in the plugin README")


class NothingClientSpecific(unittest.TestCase):
    def test_no_client_output_is_committed(self):
        if not shutil.which("git") or not os.path.isdir(os.path.join(ROOT, ".git")):
            self.skipTest("needs a git checkout")
        tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.splitlines()
        for path in tracked:
            self.assertFalse(re.search(r"(^|/)(architect-output|\.sf|\.sfdx|__pycache__)(/|$)", path),
                             f"{path} must not be committed: client output and caches stay out of the repo")


if __name__ == "__main__":
    unittest.main()
