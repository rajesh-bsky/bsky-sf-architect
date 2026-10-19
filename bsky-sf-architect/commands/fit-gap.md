---
description: Fit-gap analysis and estimate for a set of Salesforce requirements. Classifies each as standard, configuration, low code, custom code, ISV, process change or out of scope, with effort ranges, assumptions and risks. Gives the basis for a price; doesn't commit to one.
argument-hint: "[requirements file or list] [--estimate]"
---

Run a fit-gap, and optionally an estimate.

Arguments: $ARGUMENTS

1. Load the `bsky-sf-architect:consultant-toolkit` skill with the Skill tool and follow it, using `references/fit-gap-and-estimation.md`.
2. Read the requirements the user points at. If they're vague or can't be tested, say so and ask, or list them as open questions. Don't invent volumes, licences or systems.
3. Classify each requirement with the simplest category that meets it. For every item that isn't Standard or Configuration, record why the simpler option doesn't work.
4. With `--estimate`: break the work into items (include migration, integration testing, security setup, training, UAT support, deployment, hypercare and management), give low / expected / high days for each, show overheads and contingency as visible lines, list the assumptions each figure depends on, and show the total as a range with the team shape.
5. Present the fit-gap table, the estimate (if requested), the risks, and the decisions needed from the client.
6. Say clearly that this is a basis for the consultant's estimate. Don't state a price or a delivery date as a commitment.
7. Save to `estimates/<project>-fit-gap.md` unless told otherwise, and tell the user the path.
