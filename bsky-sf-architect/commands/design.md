---
description: Design a Salesforce solution from a requirement, or record an architecture decision. Produces a design document with options, a recommendation and the reasons, or an ADR. Read-only: it designs, it doesn't build.
argument-hint: "[requirement or topic] [--adr] [--org alias]"
---

Design a solution, or write a decision record.

Arguments: $ARGUMENTS

1. Load the `bsky-sf-architect:solution-design` skill with the Skill tool and follow it.
2. If the arguments include a requirement, restate it in a sentence or two and list your assumptions. If it's missing or vague, ask for the requirement, the personas, and the volumes before designing. Don't design against a guess.
3. If `--org` names an authenticated org, look at what already exists (read-only, following `bsky-sf-architect:delivery-tooling`) before proposing anything new.
4. With `--adr`, write a single architecture decision record using `references/adr-template.md` in the skill, for the one decision named. Otherwise write the full design document structure.
5. Run the draft past the `bsky-sf-architect:well-architected` skill and fix what it finds before presenting.
6. Save to `design/<topic>.md` in the working folder unless the user names another place. Tell the user the path, and list the open questions and risks.
7. Stop there. Don't start building, and don't treat silence as approval.
