---
description: Review a Salesforce design, solution or org against the Salesforce Well-Architected framework (Trusted, Easy, Adaptable). Reports findings by pillar with severity, evidence and a fix. Read-only.
argument-hint: "[path to design doc or folder | --org alias] [--pillar trusted|easy|adaptable]"
---

Run a Well-Architected review.

Arguments: $ARGUMENTS

1. Load the `bsky-sf-architect:well-architected` skill with the Skill tool and follow it.
2. Identify the target (a design document, a source folder, or a live org) and say what you can and can't see. If the user gave no target, ask for one.
3. For an org, use read-only queries only (see `bsky-sf-architect:delivery-tooling`), name the org and its type, and don't print access tokens.
4. Establish context first: edition, clouds, users, volumes, integrations, compliance. Ask for what's missing and say what you assumed.
5. With `--pillar`, review only that pillar and say the others were not reviewed.
6. Report: the verdict, a findings table (ID, pillar and sub-area, severity, finding, evidence, fix, effort), what the design does well, and what wasn't assessed. Don't change anything.
7. Offer next steps: update the design, write ADRs for the decisions found, or review the code with `/bsky-sf-architect:review-code`.
