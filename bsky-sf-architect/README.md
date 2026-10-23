# bsky-sf-architect

BlueSky Salesforce Architect: a Claude Code plugin for **Salesforce Architects, Developers and Consultants**. It brings the design, review, coding and consulting work of a Salesforce engagement into one set of skills and commands.

Advice, review and design are **read-only**. Anything that changes an org (a deploy, a data write, anonymous Apex, destructive changes) needs your explicit go-ahead for that action, on that org, and the plugin never prints an access token.

## What's inside

| Component | Purpose |
|---|---|
| `/bsky-sf-architect:design [requirement] [--adr] [--org alias]` | Design a solution from a requirement, or write an architecture decision record |
| `/bsky-sf-architect:review-design [doc \| --org alias] [--pillar ...]` | Review a design, solution or org against the Salesforce Well-Architected framework |
| `/bsky-sf-architect:review-code [branch \| path] [--base main] [--run-checks]` | Review Apex, LWC, Flow and tests against developer standards |
| `/bsky-sf-architect:fflib [scaffold Object \| review path \| should we adopt fflib]` | Scaffold, review or advise on fflib Apex Enterprise Patterns |
| `/bsky-sf-architect:discover [client] [notes] [--stories]` | Prepare discovery, sort answered from open questions, turn notes into user stories |
| `/bsky-sf-architect:fit-gap [requirements] [--estimate]` | Fit-gap analysis and estimate ranges with assumptions |
| `/bsky-sf-architect:release <org> [--tests A,B] [--notes-only]` | Preview, validate and (with your go-ahead) deploy, then write release notes |
| `solution-design` skill | Design workflow, data model guidance, integration patterns, ADR template |
| `well-architected` skill | Review checklist for the Trusted, Easy and Adaptable pillars |
| `developer-standards` skill | Apex, LWC, Flow, security and testing standards, and how to review |
| `fflib` skill | The layers, the Application factory, ApexMocks, and code skeletons |
| `consultant-toolkit` skill | Discovery question bank, user stories, fit-gap and estimation, writing for clients |
| `delivery-tooling` skill | sf CLI cheat sheet, the rules for safe validation and deploys, release notes |

## Install

You need [Claude Code](https://claude.com/claude-code). For org work, the [Salesforce CLI](https://developer.salesforce.com/tools/salesforcecli) (`sf`) and an authenticated org. The plugin has no other dependencies.

This repository is **private**: you need access to it.

```text
/plugin marketplace add rajesh-bsky/bsky-sf-architect
/plugin install bsky-sf-architect@bsky-architects
```

From a local clone, use `/plugin marketplace add ./path/to/this/repo` instead.

## Using it

```text
/bsky-sf-architect:design "Route inbound cases by product and region, 5,000 a day" --org MySandbox
/bsky-sf-architect:review-design design/case-routing.md
/bsky-sf-architect:review-code feature/case-routing --run-checks
/bsky-sf-architect:fflib scaffold Case
/bsky-sf-architect:discover AcmeCorp notes/kickoff.md --stories
/bsky-sf-architect:fit-gap requirements.md --estimate
/bsky-sf-architect:release MySandbox
```

Or just describe the job: the skills load on their own when the request matches.

## Principles

- **Evidence over opinion.** Findings cite a file and line, a query, or a document section.
- **Current facts.** Limits and entitlements change by release; the plugin tells you to confirm the ones that matter.
- **Standard before custom.** Designs and fit-gaps show the simpler option and why it wasn't enough.
- **Client standards win.** If the client has naming or version rules, they override the defaults here.
- **Drafts, not sends.** The plugin never sends an email, message or document to a client.
- **No client data in this repository.** Output goes in the client's own project folder.

## Notes on fflib

fflib method names and signatures differ between releases of `apex-common`. The plugin reads the project's installed fflib classes before generating code, and the skeletons in `skills/fflib/references/templates.md` are starting points.
