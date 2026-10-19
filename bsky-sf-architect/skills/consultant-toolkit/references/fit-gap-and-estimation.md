# Fit-gap and estimation

## Fit-gap classification

For each requirement, choose the **simplest category that meets it**:

| Category | Meaning | Effort pattern |
|---|---|---|
| **Standard** | Works out of the box as it is | Training only |
| **Configuration** | Setup with clicks: fields, layouts, validation, permission sets, reports | Low |
| **Low code** | Flow, formula, approvals, dynamic forms, screen flows | Low to medium |
| **Custom code** | Apex, LWC, custom integration | Medium to high; add test and maintenance cost |
| **ISV / AppExchange** | A managed package covers it | Licence cost plus configuration; check support and fit |
| **Process change** | The business adapts to the standard way | Change management, not build |
| **Out of scope / gap** | Not met in this phase, with the reason | None, but record it |

For every item that isn't Standard or Configuration, record **why the simpler option doesn't work**. That sentence is what protects the client from paying for custom work they don't need.

## Fit-gap table

| ID | Requirement | Priority | Fit | Approach | Why not simpler | Effort (low / expected / high) | Assumptions | Risk |
|---|---|---|---|---|---|---|---|---|

## Estimation

1. **Break the work down** to items small enough to estimate in days (see user stories). Include the work that is easy to forget: data migration, integration testing, security and sharing setup, training material, UAT support, deployment and cut-over, hypercare, project management.
2. **Estimate each item as three numbers:** low, expected and high (days). The spread says how well it is understood. A wide spread is an open question to close, not a number to average away.
3. **Expected = (low + 4 × most likely + high) ÷ 6** (three-point / PERT) if the team uses it; otherwise state the method used.
4. **Add overheads explicitly**: testing, defect fixing, reviews, deployment, and management as visible lines, not hidden multipliers.
5. **Add contingency** as a stated percentage with the reason (unknown data quality, an integration partner not yet engaged, a new technology for the team). Don't bury it in the item estimates.
6. **List the assumptions** the estimate depends on (client availability, access dates, data quality, number of integrations, no scope change) and what changes if each one is wrong.
7. **Show the total as a range** and the team shape (roles and weeks) that produces it.

## What a good estimate pack contains

- Scope in and out
- Fit-gap table
- Estimate by work item, with the three figures
- Assumptions and dependencies
- Risks, with likelihood, impact and a mitigation
- Team and timeline options (for example phased versus single release)
- The decisions needed from the client, and by when

## Cautions

- Don't quote a price or promise a date. Provide the basis: the consultant decides what to commit.
- Don't use a single figure from a similar past project without saying what was different.
- An estimate made before discovery is a rough order of magnitude. Label it that way, and give the accuracy you believe it has.
- Re-estimate when assumptions change, and record the version and what changed.
