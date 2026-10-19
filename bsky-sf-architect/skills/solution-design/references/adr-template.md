# Architecture decision record (ADR) template

Write one ADR for each decision that is costly to reverse: the data model, the sharing model, an integration pattern, Flow versus Apex for a core process, a managed package versus a build, a framework such as fflib.

Number them in the order they are made (`ADR-001`) and never rewrite an accepted one. If the decision changes, write a new ADR and mark the old one "Superseded by ADR-nnn".

```markdown
# ADR-000: <short title of the decision>

- **Status:** Proposed | Accepted | Superseded by ADR-nnn | Rejected
- **Date:** YYYY-MM-DD
- **Decided by:** <names or roles>

## Context
What is the situation and what forces are at play? Requirement, constraints, volumes, deadlines,
licences, existing systems. Facts, not opinions.

## Options considered
### Option A: <name>
How it works in a line or two.
- Good: ...
- Bad: ...
### Option B: <name>
- Good: ...
- Bad: ...

## Decision
We will <option>, because <the reasons that outweighed the others>.

## Consequences
- What becomes easier.
- What becomes harder, or what we are now committed to.
- What we will need to watch (a limit, a cost, a dependency), and the trigger for revisiting this.

## Open questions
Anything that could change the decision.
```

## Writing a good one

- The context must hold up on its own: someone who joins in a year should understand why this was reasonable.
- Include the option you rejected most easily if people will keep proposing it.
- State the consequences you don't like. An ADR with only upsides isn't believed.
- Keep it to one page.
