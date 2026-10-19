---
name: consultant-toolkit
description: Salesforce consulting work: discovery workshops and question sets, turning requirements into user stories with acceptance criteria, fit-gap analysis, estimation, and client-ready write-ups. Use when a Consultant or Architect is preparing or running discovery, capturing requirements, deciding what is standard versus custom, sizing work, or writing something a client will read. Triggers on "discovery", "workshop", "requirements", "user stories", "acceptance criteria", "fit-gap", "estimate", "sizing", "scope", "client summary", "proposal".
---

# Consultant toolkit

Four jobs, each with a reference file:

| Job | Read |
|---|---|
| Prepare or run discovery; sort what's answered from what's open | [references/discovery-questions.md](references/discovery-questions.md) |
| Turn requirements into stories with acceptance criteria | [references/user-stories.md](references/user-stories.md) |
| Fit-gap analysis and estimation | [references/fit-gap-and-estimation.md](references/fit-gap-and-estimation.md) |
| Write something for a client | the rules below |

## Rules

1. **The client's words first.** Capture requirements as the business said them, then translate. Keep a trace from each story back to the source (a workshop, an email, a person).
2. **Separate fact, assumption and decision.** Mark each. An unconfirmed assumption in an estimate is a risk, and the document says so.
3. **Don't invent facts about the client.** Volumes, licences, systems and policies come from the client or the org. If you don't have a number, the number is an open question, not a guess.
4. **Standard before custom.** In every fit-gap, show the standard option first and the cost of going custom, so the client decides with the trade-off visible.
5. **Estimates are ranges with assumptions.** Give a low, expected and high figure, what's in and out, and what would move the number. Never present a single figure as certain. Don't commit the user to a price or date: you provide the basis, they decide.
6. **Nothing leaves the building unreviewed.** You draft; the consultant reviews before anything is sent. Never send an email, message or document to a client yourself.
7. **Protect client data.** Don't paste client data, names, or credentials into outputs meant for other clients, into public tools, or into this plugin's repository. When you reuse an example, anonymise it.

## Writing for the client

When the output will be read by a client (a summary, a proposal, a workshop playback, a status note):

- Say who it is for in the first line of your hand-over message so the consultant can correct it.
- **Lead with the outcome and the decision needed**, then the detail. Put the ask at the top.
- Plain language. Define a Salesforce term the first time or avoid it. Describe what the user will be able to do, not the feature name.
- Short sentences, short paragraphs. Tables for comparisons and options. No filler or hedging.
- State what's decided, what's open, who owns each open item, and by when.
- Use the client's brand and terminology if they have them, not internal shorthand.

## Workflows

**Discovery prep** (`/bsky-sf-architect:discover`): gather what exists (briefs, emails, an org if connected, earlier answers), sort it into answered / partly answered / open using the question bank, produce a workshop plan and the questions to ask, tailored to the cloud and the stakeholders.

**Requirements to stories**: take notes, a transcript or a brief; extract needs; write stories and acceptance criteria; flag gaps, conflicts and non-functional needs; list open questions.

**Fit-gap and estimate** (`/bsky-sf-architect:fit-gap`): for each requirement classify as standard, configuration, low code, custom code, ISV, or out of scope; add effort ranges and assumptions; roll up with risks.
