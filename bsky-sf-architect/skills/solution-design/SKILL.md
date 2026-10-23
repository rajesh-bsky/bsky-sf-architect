---
name: solution-design
description: Design a Salesforce solution from a requirement. Use when an Architect, Developer or Consultant asks to design, architect, spec or choose between approaches in Salesforce: data model, security model, automation approach (Flow vs Apex), integration pattern, or an architecture decision record (ADR). Produces a design document with options, a recommendation and the reasons, or a decision record. Triggers on "design this", "how should we architect", "which approach", "ADR", "integration pattern", "data model for", "declarative or code".
---

# Solution design

A design is a set of decisions with reasons, written so that someone who wasn't in the room can build from it and challenge it. Your job is to make the decisions visible, not to produce a long document.

## Rules

1. **Requirement before solution.** Restate the requirement in one or two sentences, list what you assume, and ask about anything that would change the design. Don't design against a guess about volumes, users, or who owns the data.
2. **Options, then a recommendation.** For each significant decision give at least two real options, the trade-off in a line each, and one recommendation with the reason. A decision with a single option isn't a decision. Say plainly when the choice is close.
3. **Prefer the platform.** Standard feature, then configuration, then Flow, then Apex, then external. Move down the list only for a stated reason (volume, complexity, performance, testability, a capability the platform lacks). Record that reason.
4. **Numbers, not adjectives.** "Large" and "high volume" are not requirements. Get record counts, peak transactions, number of users per persona, and data growth per year. Check them against limits before recommending.
5. **Check the current platform.** Limits, licences and features change by release. Don't quote a limit or an edition entitlement from memory as fact: say what you believe, and tell the user to confirm against the current Salesforce documentation or the client's org (`sf org list limits`).
6. **Use the client's org when there is one.** If the user has an org authenticated, look at what exists (objects, automation, existing integrations) before proposing new things. Read only; follow `delivery-tooling` for how.
7. **Name the risks and what you did not cover.** Every design ends with open questions, risks and out-of-scope items.

## Workflow

1. **Frame.** Requirement, personas, volumes, constraints (licences, edition, existing automation, compliance, timelines), assumptions.
2. **Decide the hard parts first**, in this order, because each constrains the next:
   - Data model and ownership: [references/data-model.md](references/data-model.md)
   - Security and sharing: object access, field access, the sharing model, who sees what
   - Automation approach: Flow, Apex, or both, and where the logic lives. If Apex, consider the `fflib` skill.
   - Integration: pattern, mechanism, direction, failure handling: [references/integration-patterns.md](references/integration-patterns.md)
   - UI: standard page, Lightning page, LWC, Screen Flow, Experience Cloud
   - Reporting: what must be measured, and whether the model supports it
3. **Review** the draft with the `well-architected` skill and fix what it finds before presenting.
4. **Write it up** using the structure below. Use the ADR template in [references/adr-template.md](references/adr-template.md) for each decision that is costly to reverse.
5. **Present and stop.** Show the design and the open questions. Don't start building, and don't treat silence as approval.

## Design document structure

1. Summary: the requirement and the recommended solution in a paragraph.
2. Assumptions and constraints.
3. Data model: objects, key fields, relationships, record types, and why. A diagram if it helps.
4. Security and sharing.
5. Automation and logic: what runs when, in which order, and where.
6. Integration: systems, direction, pattern, volumes, error handling, retries.
7. UI and user experience.
8. Decisions: a table of decision, options considered, choice, reason (link to ADRs).
9. Non-functional: limits and volumes, performance, availability, data retention, audit.
10. Testing approach and deployment approach.
11. Risks, open questions, out of scope.

Keep it as short as the problem allows. A small change gets a page, not twenty.

## Output

Save the design as markdown in the working folder (for example `design/<topic>.md`) unless the user names a place. Tell the user the path and list the open questions. If the document is for a client, say so before writing it and write it for the client's reader: plain language, no internal shorthand.
