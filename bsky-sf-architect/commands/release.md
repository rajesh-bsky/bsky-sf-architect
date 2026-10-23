---
description: Prepare a Salesforce release with the sf CLI: confirm the target org, preview, validate with tests, and write release notes. Validation changes nothing. A real deploy only happens after you give an explicit go-ahead for that org.
argument-hint: "<target-org alias> [--source-dir path] [--tests ClassA,ClassB] [--notes-only]"
---

Prepare a release.

Arguments: $ARGUMENTS

1. Load the `bsky-sf-architect:delivery-tooling` skill with the Skill tool and follow it, using `references/sf-cli.md` for the commands.
2. Confirm the target. Run `sf org list` and `sf org display --target-org <alias>` (never `--verbose`), and tell the user the alias, username and whether it is production, a sandbox or a scratch org. If no org was given, ask which one.
3. Confirm the branch and working tree (`git status --short`, `git branch --show-current`) and say what's uncommitted.
4. With `--notes-only`, skip to step 8.
5. Run `sf project deploy preview`, then **validate** with `sf project deploy validate` (or `deploy start --dry-run`), using `--tests` if given and otherwise `RunLocalTests`. Fix nothing silently: report failures in full (`componentFailures`, test failures, coverage per class).
6. Show the user the components, tests run, coverage, failures and warnings, and ask for a go-ahead to deploy **to this org**. For production, say so plainly, ask for the rollback plan, and prefer a quick deploy of the validated package.
7. Only after an explicit yes: deploy, then verify with the deploy report and a check in the org. A success message isn't proof; compare the components deployed with what you expected.
8. Write release notes (summary, changes by area, actions required after deploy, known issues, rollback, and a technical section) from the diff. Say what the diff doesn't show. Save to `release-notes/<date>-<target>.md` unless told otherwise.
9. Never include destructive changes unless the user asked to remove specific, named components, approved each, and a backup exists.
