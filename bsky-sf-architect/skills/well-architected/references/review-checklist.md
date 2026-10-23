# Well-Architected review checklist

Questions for each sub-area, with what to look for as evidence. Skip what doesn't apply and say so.

## Trusted

### Secure
- Is the sharing model **Private or Public Read Only** for sensitive objects, with access opened deliberately? (org-wide defaults, roles, sharing rules)
- Are **object and field permissions** granted through permission sets and groups, with minimal profiles? Any "Modify All Data", "View All Data", "Modify Metadata" or "Author Apex" on non-admins?
- Does Apex enforce **CRUD, FLS and sharing**? Look for `with sharing` (or an explicit reason for `without` / `inherited`), `WITH USER_MODE` or `WITH SECURITY_ENFORCED`, `Security.stripInaccessible`, and `AccessLevel.USER_MODE` on DML.
- Any **injection** risk: dynamic SOQL built by concatenation (use bind variables or `String.escapeSingleQuotes`), unescaped output in Visualforce, `innerHTML` in LWC, `lwc:dom="manual"`.
- **Secrets**: none in code, custom labels, custom settings or static resources. Named Credentials and External Credentials used for callouts.
- **Integration users**: dedicated, least privilege, restricted by IP or connected-app policy, not System Administrator.
- **Authentication**: SSO, MFA, session settings, connected-app OAuth scopes and policies, community / Experience Cloud guest user access reviewed.
- Aura / LWC **Lightning Locker or Lightning Web Security** respected; no third-party scripts without review.

### Compliant
- Which obligations apply (POPIA, GDPR, HIPAA, PCI DSS, industry rules)? Is **personal data** identified, and is there a lawful basis, a retention rule and a deletion process?
- Is **consent** captured and honoured? Are opt-out flags used by the automation and integrations?
- Is there an **audit trail**: field history tracking, Field Audit Trail, Setup Audit Trail export, event monitoring where needed?
- **Data residency** and cross-border transfer: where does data go through integrations and AI features?
- Is Shield or Platform Encryption needed for specific fields, and the impact on features understood?

### Reliable
- What happens when an **integration is down**? Retries, backoff, a dead-letter or error log, alerting.
- Are operations **idempotent** (safe to repeat) and keyed by external ID?
- **Governor limits** at stated volumes: queries and DML in loops, CPU in triggers, row counts, callouts, heap. Bulk behaviour tested with 200+ records.
- **Error handling**: Flow fault paths, Apex try/catch with a meaningful action (log, retry, tell the user), no swallowed exceptions.
- **Backup and recovery**: data export, a restore approach, the recycle bin window understood, a sandbox refresh plan.
- **Monitoring**: who sees failed jobs, failed flows, limit warnings, event delivery failures?
- Scheduled and asynchronous work: are there **concurrent-run and row-lock** risks, data skew?

## Easy

### Intentional
- Does each component have **one clear purpose**? Is there overlapping automation on the same object (Flow, trigger, Process Builder, Workflow Rule)?
- Is the **order of execution** understood where several automations fire on one object? Is there one record-triggered flow per object and context (or a justified set)?
- Naming convention followed; descriptions on objects, fields, flows, classes.
- Are there **duplicate fields**, unused fields, or fields of the wrong type? Is the data model aligned with how the business talks?
- Documentation: a design document, ADRs for the costly decisions, a data dictionary.
- Are legacy automations (Workflow Rules, Process Builder) still present? They are retired by Salesforce and should be migrated.

### Automated
- Is the right tool used: **declarative first** (validation, Flow), code where there is a reason?
- Is there a **CI/CD pipeline** with validation on pull requests, test runs and a promotion path (sandbox to production)? Source tracking and source control as the source of truth.
- **Tests**: meaningful assertions (not coverage for its own sake), bulk tests, negative tests, tests that use their own data (`@TestSetup`, factories), not `SeeAllData=true`.
- Static analysis (PMD, ESLint, Code Analyzer) in the pipeline.
- Data and config deployment: reference data, custom metadata, permission sets are deployed, not hand-clicked.

### Engaging
- Does the user experience fit the **persona and device**? Screens, steps and fields per task kept small.
- Are **page layouts, Lightning pages and dynamic forms** used to show only what's relevant? Compact layouts, highlights panel, related lists pruned.
- **Performance** the user feels: page load, component count, wire and Apex calls per page, list view and report filters on indexed fields.
- Accessibility (WCAG) in custom components; labels and error messages written for the user.
- Feedback on actions: success and error messages that say what to do next.

## Adaptable

### Resilient
- Can the solution **absorb growth** in users, records and transactions? Volumes projected over 3 years, indexes and selective queries, archiving plan.
- Are **limits** treated as design inputs, with headroom? (custom fields per object, flows, API calls, storage, platform events)
- **Dependencies on managed packages and third parties**: version pinned, support status, exit plan.
- Is the solution **tolerant of metadata change**, for example fields not hard-coded by ID, record types looked up by developer name, custom metadata or custom labels for configuration?
- Release readiness: feature flags (custom permissions or custom metadata), rollback approach, sandbox strategy.

### Composable
- Is logic **modular**: Apex separated into layers (domain, service, selector), reusable invocable actions and subflows, LWC split into small components with clear events and properties?
- Are **interfaces stable**: public service methods, Apex REST contracts and platform event schemas versioned deliberately?
- Can parts be **replaced** (a mock, a different provider) behind an interface? Is configuration separated from code?
- Packaging: unlocked packages or a clear module structure in source, with dependencies declared and acyclic.
- Reuse of standard features and **AppExchange** before building custom, with the build-or-buy reasoning recorded.
