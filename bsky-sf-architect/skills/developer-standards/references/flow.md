# Flow standards

Workflow Rules and Process Builder are retired by Salesforce. Anything still on them should be migrated to Flow (or Apex where Flow is the wrong tool).

## Choosing the Flow type

| Need | Use |
|---|---|
| Change fields on the **same record** as it is saved | **Record-triggered flow, before-save** (fast, no extra DML) |
| Create or update **other records**, send emails, call actions | **Record-triggered flow, after-save** |
| Guide a user through steps | **Screen flow** |
| Run on a schedule | **Scheduled flow** (or Batch Apex for large volumes) |
| React to a Platform Event | **Platform-event-triggered flow** |
| Reusable logic called by other flows | **Autolaunched flow / subflow** |
| Logic Flow can't do well (complex loops, heavy computation, large volumes) | **Apex invocable action** called from Flow |

## Design rules

1. **One record-triggered flow per object per timing (before-save, after-save)**, or a clearly justified set with entry conditions that never overlap. Overlapping flows on one object have no guaranteed order between them (use **Flow Trigger Explorer** to set the order when you must have several).
2. **Entry conditions** narrow the trigger as far as possible, using "only when a record is updated to meet the conditions" so it doesn't run on every save.
3. **No Get Records, Create, Update or Delete elements inside a loop.** Collect into a collection variable, then do one operation after the loop.
4. **Every DML and action element has a fault path** that does something useful: log the error, tell the user in a screen flow, or roll back. A fault path that does nothing hides failures.
5. **Don't hard-code IDs.** Look up by developer name, use custom metadata, custom labels or custom permissions.
6. **Use subflows** for logic repeated in more than one flow.
7. **Name everything** with a convention (`Object_Trigger_Purpose` for flows; `get_`, `upd_`, `dec_`, `loop_` prefixes for elements) and fill in descriptions on the flow and on non-obvious elements.
8. **Version control.** Keep flows in source; deactivate old versions deliberately and delete versions that are no longer needed.
9. **Asynchronous paths** for callouts and slow work in record-triggered flows, so the user's save isn't blocked.
10. **Bulk-safe by default.** Flow batches records in a transaction. Test with 200 records.

## What to leave to Apex

- Complex transformations over large collections, recursion, or anything near CPU limits.
- Reusable business logic shared by Flow, LWC, APIs and batch (put it in a service class and expose an invocable method).
- Callouts needing custom auth, retries or response handling beyond External Services.

## Testing

- **Flow tests** (the built-in test feature) for record-triggered flows, covering positive, negative and bulk cases.
- Debug runs for screen flows, and a manual test as each persona.
- Test the **interaction** with other automation on the object, not the flow alone.

## Review smells

- DML or Get Records in a loop.
- Missing fault paths, or fault paths that end with no action.
- Several record-triggered flows on one object with overlapping entry conditions.
- No entry conditions, so the flow runs on every save.
- Hard-coded record IDs, usernames or email addresses.
- Flow does what a validation rule, formula or roll-up would do more simply.
- Large flows with no subflows, no names and no descriptions.
