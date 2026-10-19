# User stories and acceptance criteria

## Story format

```text
As a <persona>
I want to <do something>
So that <the business outcome>
```

The persona is a real role from discovery, not "the user". The outcome is the reason, so that a smaller or different solution can still satisfy it.

## Acceptance criteria

Write them as examples a tester can run, in Given / When / Then form:

```text
Given a sales rep who owns an open opportunity worth over R500,000
When they move it to "Negotiation"
Then the sales manager receives an approval request
 And the opportunity can't be moved to "Closed Won" until it is approved
```

Rules:

- One behaviour per criterion. Include the **negative** case (what must be blocked or rejected) and at least one **edge** case.
- Use concrete values and the client's terms.
- Say **who** (the persona or permission) so the security model is testable.
- Don't describe the implementation ("create a Flow that ..."). Describe the observable outcome.

## Good stories are INVEST

**I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall, **T**estable. If you can't test it, it isn't ready. If it can't be estimated, there's an open question. If it's larger than a few days of work, split it (by step in the process, by persona, by data variation, or by happy path first).

## Add the non-functional needs

For each epic, record the ones that apply, with a number where you can:

- Volume and performance (records, concurrent users, response time)
- Security and sharing (who must not see what)
- Audit and retention
- Availability and recovery
- Accessibility and devices
- Integration timing and failure behaviour
- Data migration and cut-over

## Story table

| ID | Epic | Persona | Story | Acceptance criteria | Priority (MoSCoW) | Source | Open question |
|---|---|---|---|---|---|---|---|

Keep the **source** (who said it, where) so any story can be traced and challenged. List **conflicts** between stakeholders and **gaps** explicitly: don't resolve them silently.

## Review checklist

- Does each story name a real persona and a reason?
- Can each acceptance criterion be tested as written?
- Are negative and edge cases covered?
- Are non-functional needs captured?
- Is every story traceable to a source?
- Are conflicts and open questions listed, with owners?
