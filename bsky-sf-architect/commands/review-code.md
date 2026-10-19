---
description: Review Salesforce code and configuration (Apex, LWC, Flow, tests) against developer standards: security, governor limits, bulk safety, error handling and maintainability. Reviews a diff, branch or folder and reports Blocker, Major and Minor findings with file and line. Read-only.
argument-hint: "[branch | PR diff | path] [--base main] [--run-checks]"
---

Review code against the developer standards.

Arguments: $ARGUMENTS

1. Load the `bsky-sf-architect:developer-standards` skill with the Skill tool and follow it. If the code uses fflib (a `fflib_` class, an `Application` class, or `*Selector` and `*Service` classes), also load `bsky-sf-architect:fflib` and check the layers.
2. Work out the scope. For a branch or pull request, use `git diff --name-status <base>...HEAD` (base defaults to `main`) and review the changed files. For a path, review that path. Say which files and revision you read.
3. Read the changed code and enough of its surroundings to understand callers and the object's other automation.
4. Check in order: security, bulk and limits, correctness and error handling, tests, maintainability.
5. With `--run-checks`, run the project's own static checks and tests (lint, Jest, Code Analyzer) and report their output. Apex tests need an org: only run them with the user's go-ahead, against a named sandbox or scratch org. Never claim code compiles or tests pass if you didn't run them: say "not run".
6. Report a verdict, then findings grouped Blocker, Major and Minor, each with `file:line`, the problem, what it costs and the smallest fix. Then list what was checked and what wasn't.
7. Don't edit the code unless the user asks you to apply fixes.
