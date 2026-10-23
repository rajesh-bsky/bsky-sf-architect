# Security and testing

## Security: the Apex checklist

| Concern | What good looks like |
|---|---|
| **Sharing** | Classes declare `with sharing` (or `inherited sharing` for utilities). `without sharing` has a comment saying why and is kept to a small class. |
| **CRUD and FLS** | User-facing queries use `WITH USER_MODE` (or `WITH SECURITY_ENFORCED`). DML uses `AccessLevel.USER_MODE` or checks with `Schema` describe. `Security.stripInaccessible` removes fields the user can't access before returning or saving. |
| **SOQL injection** | Bind variables. When dynamic SOQL is unavoidable: `String.escapeSingleQuotes`, and an allow-list for field, object and sort-order names. |
| **XSS** | Visualforce output escaped (`{!HTMLENCODE(x)}`, `JSENCODE`); no `escape="false"` on user data. LWC avoids `innerHTML`. |
| **Secrets** | None in code, labels, custom settings, static resources or tests. Named Credentials and External Credentials for callouts. |
| **Open redirects and CSRF** | Redirect targets validated against an allow-list. State-changing GET requests avoided. |
| **Guest and community users** | Guest user profile minimal. No object access beyond need. Sharing rules for guest users reviewed. Apex classes exposed to guests checked line by line. |
| **Logging** | No personal data, tokens or full request bodies in debug logs or custom log objects. |

## Security: configuration

- Profiles minimal; access through permission sets and groups.
- No "Modify All Data", "View All Data", "Modify Metadata" or "Author Apex" for non-admins.
- Connected apps: scoped OAuth, IP policies, refresh-token policy, admin pre-approval.
- Sharing: private defaults for sensitive data, rules reviewed, no "View All" used to paper over a sharing problem.
- Integration users dedicated, least privilege, API-only where possible.

## Testing: Apex

- **Assert behaviour.** Every test method has meaningful `Assert` / `System.assertEquals` statements with a message. Coverage without assertions is not testing.
- **Cover** the positive case, the negative case (validation fails, bad input), the **bulk case (200+ records)**, and **different users** (`System.runAs`) for security behaviour.
- **Own data.** Create data in the test (`@TestSetup`, a test data factory). Don't use `SeeAllData=true`, except where Salesforce forces it.
- **Isolate callouts** with `HttpCalloutMock` (or `Test.setMock`), and async work with `Test.startTest()` / `Test.stopTest()`.
- **Don't test the platform.** Test your logic.
- **Test the limits:** a test that inserts 200 records through your trigger catches most SOQL and DML in loops.
- With fflib: unit-test logic with **ApexMocks** (no database), and keep a few integration tests for the wiring. See the `fflib` skill.
- Deployment to production needs **75% overall coverage** from Apex tests and every trigger must have some coverage, but treat that as the floor, not the goal.

## Testing: general

- Test as each **persona** with that persona's permission sets, not as System Administrator.
- Write **UAT scripts** with Given/When/Then steps and expected results; keep them with the design.
- Test **integrations** with failure cases: timeout, 500 response, bad payload, duplicate message.
- **Regression**: keep a small suite of the critical paths that runs on every deployment.
- **Data load tests** at production-like volumes in a full or partial copy sandbox before go-live.

## Static analysis

- **Salesforce Code Analyzer** (PMD, ESLint, RetireJS and others) in the pipeline; fail the build on the high-severity rules the team agrees on.
- Agree a ruleset once and keep it in the repository.
