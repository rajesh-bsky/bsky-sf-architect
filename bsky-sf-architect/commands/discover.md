---
description: Prepare or run Salesforce discovery. Sorts what the client has already answered from what is still open, and produces a workshop plan and a tailored question set. Can also turn notes or a transcript into user stories with acceptance criteria. Drafts only; never sends anything to a client.
argument-hint: "[client or project] [notes / brief / transcript path] [--stories]"
---

Prepare discovery, or turn notes into requirements.

Arguments: $ARGUMENTS

1. Load the `bsky-sf-architect:consultant-toolkit` skill with the Skill tool and follow it.
2. Gather what exists: the files or text the user points at (briefs, emails, notes, a transcript), and an org if one is connected (read-only, following `bsky-sf-architect:delivery-tooling`). Don't invent facts about the client.
3. Without `--stories`: use `references/discovery-questions.md` in the skill to sort the questions into answered (with source), partly answered and open (with who can answer). Produce a workshop plan (objective, attendees, agenda with timings, questions per session) tailored to the clouds and stakeholders.
4. With `--stories`: extract the needs, write user stories with Given/When/Then acceptance criteria using `references/user-stories.md`, capture non-functional needs, and list conflicts, gaps and open questions, each traceable to its source.
5. If anything you write will be read by the client, say who it is written for in the first line of your reply, and write it in plain language.
6. Save to `discovery/<client>-<topic>.md` unless told otherwise, and tell the user the path. You draft; the consultant reviews and sends. Never send an email or message yourself.
