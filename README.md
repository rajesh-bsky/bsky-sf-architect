# BlueSky Salesforce Architect plugins

A private Claude Code plugin marketplace (`bsky-architects`) for BlueSky's Salesforce Architects, Developers and Consultants.

| Plugin | What it does |
|---|---|
| [bsky-sf-architect](bsky-sf-architect/) | Solution design, Well-Architected review, Apex/LWC/Flow standards, fflib patterns, a consultant toolkit and gated sf CLI delivery tooling |

## Quick start

```text
/plugin marketplace add rajesh-bsky/bsky-sf-architect
/plugin install bsky-sf-architect@bsky-architects
```

The plugin's own [README](bsky-sf-architect/README.md) has the full reference.

## Repository layout

```text
.claude-plugin/marketplace.json     the bsky-architects marketplace listing
bsky-sf-architect/
├── .claude-plugin/plugin.json      plugin manifest
├── commands/                       /bsky-sf-architect:design, :review-design, :review-code, :fflib, :discover, :fit-gap, :release
└── skills/                         solution-design, well-architected, developer-standards, fflib,
                                    consultant-toolkit, delivery-tooling (each with references/)
tests/                              structural checks and the CI version-bump check
```

## Contributing

Make every change on a branch and open a pull request against `main`; don't push to `main` directly.

- Run the tests: `python3 -W error::ResourceWarning -m unittest discover -s tests`. They check manifests, frontmatter, links between files and that the README covers every command and skill.
- **Version and changelog:** any change to the plugin's files (other than its README) bumps the version in `bsky-sf-architect/.claude-plugin/plugin.json` and adds an entry at the top of [CHANGELOG.md](CHANGELOG.md). CI fails the pull request if either is missing.
- Keep advice and review **read-only**. A change that lets the plugin modify an org without an explicit go-ahead won't be merged.
- Never commit client data, org metadata, usernames or tokens.
- Check a Salesforce fact (a limit, a command flag) against the current documentation before putting it in a reference file.
