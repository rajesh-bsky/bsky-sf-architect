# BlueSky Salesforce Architect

**One Claude Code plugin for the whole arc of a Salesforce engagement: discovery, design, review, build standards and release.**

Built for BlueSky's Salesforce Architects, Developers and Consultants. It turns the checks a senior architect does from memory into commands and skills anyone on the team can run, with the evidence shown and nothing touched in an org without your say-so.

> **Private repository.** You need access to it to install the plugin.

## Why use it

- **Design with reasons.** Every design shows the options considered, a recommendation and why the simpler standard option wasn't enough.
- **Reviews you can defend.** Findings cite a file and line, a query or a document section, not a hunch.
- **One set of standards.** Apex, LWC, Flow, security, testing and fflib guidance in one place, so reviews stop depending on who is reviewing.
- **Safe by default.** Advice, design and review are read-only. A deploy, data write, anonymous Apex or destructive change needs your explicit go-ahead for that action, on that org. Access tokens are never printed.
- **Client-ready output.** Discovery notes, user stories, fit-gap and estimate ranges are written as drafts for you to send. The plugin never sends anything to a client.

## Quick start

You need [Claude Code](https://claude.com/claude-code). For work against an org, also install the [Salesforce CLI](https://developer.salesforce.com/tools/salesforcecli) (`sf`) and authenticate to the org.

```text
/plugin marketplace add rajesh-bsky/bsky-sf-architect
/plugin install bsky-sf-architect@bsky-architects
```

Then try it:

```text
/bsky-sf-architect:design "Route inbound cases by product and region, 5,000 a day" --org MySandbox
```

You get a design document saved to `design/<topic>.md`, with assumptions, options, a recommendation, open questions and risks. It is checked against the Well-Architected skill before you see it.

You don't have to use the commands. Describe the job in plain words and the matching skill loads itself.

## What's in the box

### Commands

| Command | Use it to |
|---|---|
| `/bsky-sf-architect:design` | Design a solution from a requirement, or write an architecture decision record (`--adr`) |
| `/bsky-sf-architect:review-design` | Review a design, solution or org against the Well-Architected framework |
| `/bsky-sf-architect:review-code` | Review Apex, LWC, Flow and tests against developer standards |
| `/bsky-sf-architect:fflib` | Scaffold, review or advise on fflib Apex Enterprise Patterns |
| `/bsky-sf-architect:discover` | Prepare discovery, sort answered from open questions, turn notes into user stories |
| `/bsky-sf-architect:fit-gap` | Run a fit-gap analysis and produce estimate ranges with assumptions |
| `/bsky-sf-architect:release` | Preview, validate and, with your go-ahead, deploy, then write release notes |

### Skills

| Skill | Covers |
|---|---|
| `solution-design` | Design workflow, data model guidance, integration patterns, ADR template |
| `well-architected` | Review checklist for the Trusted, Easy and Adaptable pillars |
| `developer-standards` | Apex, LWC, Flow, security and testing standards, and how to review against them |
| `fflib` | Layers, the Application factory, ApexMocks and code skeletons |
| `consultant-toolkit` | Discovery question bank, user stories, fit-gap and estimation, writing for clients |
| `delivery-tooling` | `sf` CLI cheat sheet, the rules for safe validation and deploys, release notes |

Arguments, flags and examples for every command are in the [plugin README](bsky-sf-architect/README.md).

## Typical engagement flow

```text
/bsky-sf-architect:discover AcmeCorp notes/kickoff.md --stories    # what do they need?
/bsky-sf-architect:fit-gap requirements.md --estimate              # what fits, what's custom, how big?
/bsky-sf-architect:design "Route inbound cases by product" --adr   # decide, and record why
/bsky-sf-architect:review-design design/case-routing.md            # check it before building
/bsky-sf-architect:fflib scaffold Case                             # start the build on solid layers
/bsky-sf-architect:review-code feature/case-routing --run-checks   # review before merge
/bsky-sf-architect:release MySandbox                               # validate, deploy with go-ahead, write notes
```

## Principles

1. **Evidence over opinion.** A finding without a citation isn't a finding.
2. **Current facts.** Limits and entitlements change by release, so the plugin tells you to confirm the ones that matter.
3. **Standard before custom.** The simpler option is always shown, with the reason it wasn't enough.
4. **Client standards win.** If the client has naming or version rules, they override the defaults here.
5. **Drafts, not sends.** Nothing goes to a client without you.
6. **No client data in this repository.** Output goes in the client's own project folder.

## Repository layout

```text
.claude-plugin/marketplace.json     the bsky-architects marketplace listing
bsky-sf-architect/
├── .claude-plugin/plugin.json      plugin manifest and version
├── commands/                       the seven slash commands
└── skills/                         six skills, each with a references/ folder
tests/                              structural checks and the CI version-bump check
CHANGELOG.md                        every released change, newest first
```

## Contributing

Make every change on a branch and open a pull request against `main`. Don't push to `main` directly.

1. **Run the tests** before you push:
   ```bash
   python3 -W error::ResourceWarning -m unittest discover -s tests
   ```
   They check manifests, frontmatter, links between files, and that the plugin README covers every command and skill. No Salesforce org, token or network is needed.
2. **Bump the version and the changelog.** Any change to the plugin's files, other than its README, needs a new version in `bsky-sf-architect/.claude-plugin/plugin.json` and an entry at the top of [CHANGELOG.md](CHANGELOG.md). CI fails the pull request if either is missing.
3. **Keep it read-only.** A change that lets the plugin modify an org without an explicit go-ahead won't be merged.
4. **Keep it clean.** Never commit client data, org metadata, usernames or tokens.
5. **Check the facts.** Confirm any Salesforce limit or command flag against the current documentation before you put it in a reference file.

## Notes on fflib

fflib method names and signatures differ between releases of `apex-common`. The plugin reads the project's installed fflib classes before it generates code, and the skeletons in [templates.md](bsky-sf-architect/skills/fflib/references/templates.md) are starting points, not drop-in code.

## Maintainer

Rajesh ([rajesh.y@bsky.co.za](mailto:rajesh.y@bsky.co.za)), BlueSky.
