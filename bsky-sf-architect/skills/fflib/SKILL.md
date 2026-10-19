---
name: fflib
description: Apex Enterprise Patterns with the fflib libraries (fflib-apex-common and fflib-apex-mocks): separation of concerns into domain, selector and service layers, the unit of work, the Application factory, and ApexMocks for unit tests. Use when designing, scaffolding, reviewing or testing Apex that uses or should use fflib, or when asked whether to adopt fflib. Triggers on "fflib", "apex enterprise patterns", "domain class", "selector class", "service layer", "unit of work", "ApexMocks", "separation of concerns in Apex".
---

# fflib: Apex Enterprise Patterns

fflib (FinancialForce, now open source: `apex-common` and `apex-mocks`) implements the Apex Enterprise Patterns described by Andrew Fawcett. It separates code into layers so that logic is bulk-safe, testable without the database, and reusable from Flow, LWC, APIs and batch jobs alike.

Read [references/layers.md](references/layers.md) for what each layer does and its rules, and [references/templates.md](references/templates.md) for code skeletons.

## First decide whether to use it

fflib is not free. It adds classes, a learning curve and a dependency. Use this to advise:

| Use fflib when | Don't when |
|---|---|
| Several developers, a long-lived codebase, much custom Apex per object | A small org with a few triggers, or mostly declarative |
| Business logic must be shared by triggers, REST, LWC, batch and Flow | One-off utilities |
| You want fast, database-free unit tests (ApexMocks) | The team can't commit to the conventions |
| Strict governor-limit and security discipline matters | Nobody on the team has used it, and there's no time to learn it |

If the project already uses fflib, **follow it exactly** (its versions, naming and `Application` class) rather than introducing a variation. If it doesn't, record the adopt-or-not decision as an ADR (`solution-design` skill). Check which version of `apex-common` the project has before generating code: method names and signatures differ between releases. Read the installed classes; don't assume.

## Rules

1. **Match the project.** Look for an existing `Application` class, existing `*Selector`, `*Service` and domain classes, and copy their conventions (naming, sharing keywords, how they register in `Application`).
2. **Respect the layers.** Triggers call domain classes. Services orchestrate and own transactions with the unit of work. Selectors are the only place that queries. Domain classes hold the logic about one object's records. Nothing calls upward.
3. **Services take and return simple types or records**, never `Trigger.new` or UI types, so any caller can use them.
4. **Register in the `Application` factory** so tests can swap real classes for mocks. Don't call `new AccountsSelector()` directly where a mock might be needed: use `Application.Selector.newInstance(Account.SObjectType)`.
5. **One unit of work per service call** and a single `commitWork()` at the end.
6. **Selectors enforce security by default**: understand the `fflib_SObjectSelector` constructor options (CRUD and FLS enforcement, and sort order) of the installed version, and say if you turn enforcement off.
7. **Tests:** unit tests with ApexMocks for service and domain logic, a small number of integration tests for the wiring. See [references/layers.md](references/layers.md).
8. **Don't invent API.** If you're unsure a method exists in the installed version, read the source in the project.

## Workflow

**Scaffold for an object** (`/bsky-sf-architect:fflib`):
1. Inspect the project: fflib present? version? existing `Application` and naming?
2. Ask which layers are needed (domain, selector, service, tests) and what the first use case is.
3. Generate files with the project's conventions, the trigger (if a domain is requested), registration in `Application`, and tests with mocks.
4. List the files, and say how to deploy and test them (see `delivery-tooling`). Run the tests if an org is available and the user agrees.

**Review fflib code:**
- Is logic in the right layer? Is any SOQL outside a selector? Any DML outside the unit of work? Any layer calling upward?
- Are classes registered in `Application`? Are the unit tests using mocks, or hitting the database unnecessarily?
- Is sharing declared deliberately (`with sharing` on services; `inherited sharing` on selectors)?
