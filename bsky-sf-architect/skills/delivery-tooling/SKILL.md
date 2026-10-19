---
name: delivery-tooling
description: Salesforce DX and sf CLI delivery workflows: connect to an org safely, retrieve and diff metadata, validate before deploying, run Apex tests, deploy to a sandbox or production with the right gates, quick deploy, scratch orgs, and write release notes. Use when asked to deploy, validate, retrieve, compare orgs, run tests, create a scratch org, prepare a release, or check what changed. Triggers on "deploy", "validate", "retrieve", "sf project", "scratch org", "run tests", "release notes", "what changed", "promote to production".
---

# Delivery tooling (sf CLI)

Commands are in [references/sf-cli.md](references/sf-cli.md). This page is the discipline around them: what's safe, what needs a go-ahead, and in what order.

## Rules

1. **Know which org you're in.** Before any command that touches an org, run `sf org list` and `sf org display --target-org <alias>` (without `--verbose`), and tell the user the alias, username, instance and whether it is production, a sandbox, a scratch org or a Developer Edition. Name it in every message about what you did.
2. **Never print, log or store access tokens.** Don't use `sf org display --verbose` or `--json` output that includes a token, and don't paste one into a file, a commit, or the chat.
3. **Read-only by default.** Queries, `retrieve`, `deploy preview`, `deploy validate` and `--dry-run` change nothing. Anything else (a real deploy, `data delete`, `data upsert`, anonymous Apex, user changes, `org delete`) needs the user's explicit go-ahead **for that action, on that org, in this conversation**. Approval for one deploy isn't approval for the next.
4. **Validate before you deploy**, always, with the test level the target needs. In production, validate first, review the result with the user, then deploy (a quick deploy of the validated package where it applies).
5. **Production needs more.** Say plainly that it is production, check there is a rollback plan (the previous state in source control, or a retrieved backup), prefer a change window, and run the tests the org requires (`RunLocalTests` as a minimum unless a specified-tests run is justified). Never deploy to production on the strength of a sandbox result alone.
6. **A success message isn't proof.** After a deploy, check the result for each component (and for unexpectedly missing ones), then retrieve or query to confirm the org matches what you meant to deploy. Report component failures and test failures in full.
7. **Destructive changes are a separate decision.** A manifest with `destructiveChanges` removes metadata and the data behind it. Never include one unless the user asked for the removal of specific named components, they approved each one, and a backup exists.
8. **Don't change data in a client org** without being asked, and never run anonymous Apex that writes. Prefer a sandbox for anything experimental.
9. **Keep client output out of shared places.** Retrieved metadata, query results and logs stay in the client's project folder, not in this plugin's repository or anywhere public.

## Standard flows

**Start work on an org**: list orgs, confirm the target, `sf project retrieve preview` to see what differs from source, retrieve only what's needed.

**Release a change**
1. Confirm the branch and that the working tree is clean or that you know what's uncommitted.
2. `sf project deploy preview` against the target to see what will change.
3. `sf project deploy validate` (or `deploy start --dry-run`) with tests. Fix failures at the cause.
4. Show the user: components, tests run, coverage, failures, warnings. Ask for the go-ahead.
5. Deploy (or `sf project deploy quick` with the validated job ID).
6. Verify: deploy report, then spot-check in the org.
7. Write release notes.

**What changed** between two points: `git diff --name-status <from> <to> -- force-app` for source; for org drift, retrieve into a temporary folder and diff with source.

## Release notes

Write them from the diff and the work items, for the reader who will use them:

- **Summary** of what's new in one or two sentences, for the business.
- **Changes** grouped by area, each with what changed and why it matters. Include **new fields, objects, flows and permission sets** by name.
- **Actions required** after deploy (permission set assignments, page layout activation, data loads, configuration done by hand).
- **Known issues** and **rollback** notes.
- A separate **technical** section (components, test results, API version) for the team.

Say what the diff doesn't show (changes made directly in the org, data changes). Don't claim a feature works unless it was tested.
