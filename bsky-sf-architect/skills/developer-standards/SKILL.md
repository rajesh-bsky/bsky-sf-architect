---
name: developer-standards
description: Salesforce developer standards and code review for Apex, Lightning Web Components, Flow, security and tests. Use when writing, reviewing or refactoring Apex classes and triggers, LWC, Aura, Flows or test classes, checking governor-limit risk, CRUD/FLS and sharing, SOQL and DML patterns, or preparing a pull request. Triggers on "review this Apex", "code review", "bulkify", "governor limits", "test class", "LWC review", "Flow best practice", "is this secure", "PR review", "naming convention".
---

# Developer standards and code review

Use this when writing or reviewing Salesforce code and configuration. The standards live in the reference files; this page says how to apply them.

| Reviewing | Read |
|---|---|
| Apex classes, triggers, SOQL, DML, async | [references/apex.md](references/apex.md) |
| Lightning Web Components and Aura | [references/lwc.md](references/lwc.md) |
| Flow | [references/flow.md](references/flow.md) |
| Security (CRUD, FLS, sharing, injection) and tests | [references/security-and-testing.md](references/security-and-testing.md) |

If the client has its own standard (naming, minimum API version, banned patterns), **the client's standard wins**. Ask for it, and say where you departed from the defaults here.

## Rules

1. **Review what is there, and say what you read.** Name the files and the revision. Don't review code you haven't opened.
2. **Findings need a location and a reason.** File, line, what is wrong, what it costs (a limit hit at what volume, a data exposure, a maintenance trap), and the fix. No "consider improving".
3. **Separate must-fix from nice-to-have.** Use **Blocker** (security hole, certain limit failure, data loss, broken behaviour), **Major** (likely limit or maintainability problem), **Minor** (style, naming, small clarity). A pull request with a Blocker isn't ready.
4. **Bulk is the default.** Assume every trigger, Flow and invocable method receives 200 records or more, and that other automation runs in the same transaction.
5. **Don't rewrite what wasn't asked about.** When you write code, match the surrounding style. When you review, suggest the smallest change that fixes the problem, and show it.
6. **Run the tools the project already has.** If there is a `package.json`, `.eslintrc`, `sfdx-project.json` or a PMD ruleset, use them (see `delivery-tooling` for the commands) and report their output next to your own findings. Never claim code compiles or tests pass without running them; say "not run" if you didn't.
7. **Never put secrets, tokens or org data in code, comments, tests or commit messages.**

## Workflow for a review

1. Identify the scope: a diff, a branch, a folder. Use `git diff` against the base branch for a pull request.
2. Read the changed code, plus enough around it to understand callers and the object's other automation.
3. Check in this order: **security**, **bulk and limits**, **correctness and error handling**, **tests**, **maintainability and style**.
4. Run the available static checks and (if the user wants and an org is available) the relevant tests.
5. Report: a one-paragraph verdict, then findings grouped Blocker / Major / Minor with `file:line`, then what was checked and not checked.

## Workflow for writing

1. Check how the project is organised (packages, namespaces, existing patterns, whether fflib is in use: if so, use the `fflib` skill and follow its layers).
2. Write the code and its tests together. Tests assert behaviour, cover bulk and negative cases, and create their own data.
3. Run the tests and the linters before saying it's done.
4. Describe what you changed and how you verified it, including what you didn't verify.
