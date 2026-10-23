# Integration patterns

Choose the pattern from the business need (timing, direction, volume, who needs the answer), then the mechanism. Salesforce's integration pattern catalogue is the shared vocabulary.

## Patterns

| Pattern | Use when | Typical mechanism |
|---|---|---|
| **Remote Process Invocation, Request and Reply** | Salesforce calls out and needs the answer to continue (price, credit check, address validation) | Apex callout (synchronous or Continuation for long calls), External Services in Flow |
| **Remote Process Invocation, Fire and Forget** | Salesforce tells another system something happened and doesn't wait | Platform Event, Outbound Message, queueable callout with retry |
| **Batch Data Synchronization** | Moving large volumes on a schedule, either direction | Bulk API 2.0 or an ETL / iPaaS tool, scheduled Batch Apex for callouts |
| **Remote Call-In** | An external system creates, reads or updates Salesforce data | REST or SOAP API, Composite API, custom Apex REST for transactional logic, Pub/Sub API |
| **UI Update Based on Data Changes** | A user's screen should refresh when data changes elsewhere | Platform Events or Change Data Capture with `lightning/empApi` |
| **Data Virtualization** | Show external data without copying it | Salesforce Connect (OData, or a custom adapter), external objects |

## Choosing the mechanism

| Need | Mechanism | Notes |
|---|---|---|
| Event notification, loose coupling | **Platform Events** | Publish after commit or immediate; subscribers can be Apex triggers, Flow, or external clients. Replay window is limited. |
| Mirror record changes to other systems | **Change Data Capture** | Only for the objects you enable. Counts against event allocations. |
| Large volume load or extract | **Bulk API 2.0** | Not for transactional logic. |
| Many related records in one call | **Composite / sObject Collections** | Reduces round trips and API calls. |
| Server-to-server callout from Apex | **Named Credential with External Credential** | Keep endpoints and secrets out of code. Set the principal and permission set mapping. |
| Callout from Flow, low code | **External Services** (OpenAPI) | Needs a spec; check complexity limits. |
| Many systems, transformation, orchestration | **iPaaS / MuleSoft / middleware** | Justify the cost: it earns its place with three or more systems, heavy transformation, or governance needs. Two systems and a simple mapping rarely need it. |
| Real-time external data display | **Salesforce Connect** | Latency depends on the source; can't be used in every automation. |

## Decisions to make for every integration

1. **Direction and system of record.** Which system owns each field? Two-way sync without a clear owner leads to overwrite loops.
2. **Identity.** What key links the records (external ID)? How do you upsert without creating duplicates?
3. **Timing and volume.** Real-time, near real-time or batch? Peak calls per hour and per day against the **API request allocation** and callout limits.
4. **Failure.** What happens when the other side is down? Retry with backoff, a dead-letter store, an error log that someone watches, idempotent operations so a retry is safe.
5. **Security.** Authentication (OAuth flows, certificates), least-privilege integration user, IP restrictions, field-level security for the integration user, and what data leaves Salesforce.
6. **Monitoring and ownership.** Who is alerted, where do errors surface, who fixes them.
7. **Limits.** Callouts per transaction (and cumulative timeout), no callout after uncommitted DML in the same transaction, event publishing allocations, API calls per 24 hours. Check current values.

## Antipatterns

- Point-to-point sprawl with no owner or documentation.
- Callouts in a trigger on every record with no bulkification or async hand-off.
- Hard-coded endpoints, usernames or keys in Apex or custom settings.
- Polling the API on a short interval where an event would do.
- An integration user with System Administrator.
- No idempotency: a retry creates duplicates.
- Treating "it worked in the sandbox with ten records" as evidence for production volumes.
