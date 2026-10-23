# Apex standards

## Limits to design against (per transaction)

Check current values in the Salesforce documentation; these are the commonly cited synchronous / asynchronous figures.

| Limit | Synchronous | Asynchronous |
|---|---|---|
| SOQL queries | 100 | 200 |
| Records returned by SOQL | 50,000 | 50,000 |
| DML statements | 150 | 150 |
| Records processed by DML | 10,000 | 10,000 |
| CPU time | 10,000 ms | 60,000 ms |
| Heap | 6 MB | 12 MB |
| Callouts | 100 (120 s cumulative) | 100 (120 s cumulative) |

## Triggers

- **One trigger per object**, no logic in the trigger body: delegate to a handler class or (with fflib) a domain class.
- The trigger handles all contexts it needs in one place, so the order is explicit.
- Never assume one record: `Trigger.new` holds up to 200 records per chunk.
- Guard against recursion by design (compare old and new values, or track processed IDs). Avoid static boolean "ran once" flags that block legitimate later runs in the same transaction.

## SOQL and DML

- **No SOQL or DML inside loops.** Collect IDs into a `Set`, query once into a `Map<Id, SObject>`, loop over the map, and DML once on a list.
- Select **only the fields used**, with a selective `WHERE`. Add `LIMIT` where a bounded result is correct.
- Use **bind variables**, not string concatenation. If dynamic SOQL is unavoidable, use `String.escapeSingleQuotes()` and allow-list field and object names.
- Use `Database.insert(list, false)` / `Database.SaveResult` when partial success is intended, and **handle the results**: log failures, don't discard them.
- Use `WITH USER_MODE` (or `WITH SECURITY_ENFORCED`) for queries that serve users, and `AccessLevel.USER_MODE` on `Database` DML, unless the code intentionally runs in system mode and says why.
- Use `FOR UPDATE` only when you need a lock, and keep the locked section short.
- Avoid querying inside a `for` loop over a SOQL result of a large set; use a SOQL for-loop (`for (Account a : [SELECT ...])`) for big results to avoid heap issues.

## Classes and design

- **Sharing is explicit:** declare `with sharing` by default. Use `inherited sharing` for utility and selector classes meant to adopt the caller's mode. `without sharing` needs a comment with the reason and should be isolated in a small class.
- Keep methods short and single-purpose. Separate **data access, business logic and presentation** (fflib formalises this: see the `fflib` skill).
- No hard-coded IDs, URLs, usernames or record type IDs. Look up record types by `DeveloperName`; put endpoints in Named Credentials; put tunable values in Custom Metadata or Custom Labels.
- Prefer **constants and enums** over magic strings.
- Use **custom exceptions** for domain errors, and catch the narrowest type. Never leave an empty `catch`. Either handle it (retry, compensate, tell the user) or let it propagate.
- Prefer `Map` and `Set` for lookups over nested loops.
- Use **`Limits` class** sparingly for diagnostics, not as control flow.
- `@AuraEnabled(cacheable=true)` methods are read-only: no DML, no callouts that change data.

## Asynchronous Apex

| Use | When |
|---|---|
| **Queueable** | The default for async work after a transaction, chaining, passing complex types, callouts. `Database.AllowsCallouts` for callouts. Use `System.Finalizer` for cleanup and retry logic. |
| **Batch Apex** | Processing more than a few thousand records. Choose the scope size (default 200) for the work per record, and implement `Database.Stateful` only when you must. |
| **Schedulable** | Time-based trigger. Keep `execute` thin: enqueue a batch or queueable. |
| **`@future`** | Legacy. Prefer Queueable. |
| **Platform Event / CDC trigger** | Decoupled, event-driven processing. |

- Don't enqueue async work from a loop. Bundle records into one job.
- Check `System.isBatch()` / `System.isFuture()` before enqueueing from code that can run in those contexts.
- Make jobs **idempotent**: a retry must be safe.

## Naming and layout

Follow the client's standard if there is one. Defaults:

| Thing | Convention | Example |
|---|---|---|
| Class | PascalCase, noun | `AccountService`, `OpportunitySelector` |
| Test class | `<Class>Test` | `AccountServiceTest` |
| Trigger | `<Object>Trigger` | `AccountTrigger` |
| Method | camelCase, verb | `calculateDiscount` |
| Variable | camelCase | `openCases` |
| Constant | UPPER_SNAKE_CASE | `MAX_RETRIES` |
| Batch / Queueable / Schedulable | suffix with the type | `InvoiceSyncBatch`, `SyncQueueable` |

- Use a recent API version consistent with the project; don't mix versions without a reason.
- Comment the **why**, not the what. ApexDoc on public methods of a service layer.

## Review smells

- DML or SOQL in a loop, or in a method called from a loop.
- `Trigger.new[0]`, or code that only handles a single record.
- `SeeAllData=true`, `System.debug` left as the only logging, empty catch blocks.
- `without sharing` with no comment.
- `Database.query` with concatenated user input.
- Hard-coded IDs, URLs or credentials.
- A callout after DML in the same transaction without async separation.
- A test with no assertions.
- A utility class that grows without a clear owner or purpose.
