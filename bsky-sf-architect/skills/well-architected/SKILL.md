---
name: well-architected
description: Review a Salesforce design, solution, org or pull request against the Salesforce Well-Architected framework (the Trusted, Easy and Adaptable pillars). Use when asked to review a design, check an architecture, score a solution, run a well-architected review, find risks before build, or test whether something is secure, scalable and maintainable. Produces findings by pillar with severity, evidence and a fix. Triggers on "well-architected", "WAF", "review the design", "architecture review", "is this a good design", "design risks".
---

# Salesforce Well-Architected review

The Salesforce Well-Architected framework describes what a good solution looks like through three pillars, each with sub-areas:

| Pillar | Sub-areas | The question |
|---|---|---|
| **Trusted** | Secure, Compliant, Reliable | Will it protect data, meet obligations and keep working? |
| **Easy** | Intentional, Automated, Engaging | Is it clear, efficient and pleasant to use and to run? |
| **Adaptable** | Resilient, Composable | Can it change and survive change without a rewrite? |

Use the checklist in [references/review-checklist.md](references/review-checklist.md). It turns each sub-area into questions you can answer from a design document, a repository or an org.

## Rules

1. **Evidence for every finding.** Cite the document section, file and line, or the query and result. A finding without evidence is an opinion; label opinions as opinions.
2. **Ask before you assume.** If a design doesn't say how failures are handled, the finding is "not stated", not "missing". Say which, and ask.
3. **Severity is about consequence.** Use this scale and apply it consistently:
   - **High**: data exposure, data loss, a limit that will be hit in production at stated volumes, or a decision that is expensive to reverse and looks wrong.
   - **Medium**: will cause pain or rework within a release or two.
   - **Low**: hygiene, naming, documentation.
4. **Proportion.** Match the depth to the size of the thing. A single Flow doesn't need twelve findings. Prefer fewer, well-evidenced findings to a long list.
5. **Say what is good.** Note what the design does well, briefly. It tells the author what to keep.
6. **Don't claim what you didn't check.** List what was out of scope or could not be seen (no org access, no volumes, no sharing rules).
7. **Read-only.** A review reports. It doesn't change the org or the code. If the user wants fixes, that is a separate step they ask for.

## Workflow

1. **Identify the target and what you can see.** A design document, a folder of source, a pull request, a live org. Say which, and which evidence is missing.
2. **Establish context.** Edition and clouds, user count and personas, record volumes, integrations, compliance obligations (POPIA, GDPR, HIPAA, PCI). Ask for what's missing and note what you assumed.
3. **Go pillar by pillar** through the checklist. Skip questions that don't apply and say so.
4. **Rank** the findings, High first, then by effort to fix.
5. **Report** in this shape:
   - Verdict in two or three sentences: is it sound to build or release, and what must change first.
   - Table of findings: ID, pillar and sub-area, severity, finding, evidence, recommended fix, effort (S/M/L).
   - What the design does well.
   - Not assessed, and open questions.
6. **Offer next steps**: update the design, raise ADRs for decisions that need recording, or run `developer-standards` over the code.

## Pairing with other skills

- A design review before build: run after `solution-design`.
- Code in scope: apply `developer-standards` for the line-level review and keep this review at the design level.
- Apex structured with fflib: check the layers with the `fflib` skill.
