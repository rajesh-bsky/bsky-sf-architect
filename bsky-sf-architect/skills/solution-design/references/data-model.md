# Data model guidance

## Start from the business, then the standard model

1. List the nouns the business talks about and who owns each.
2. Map each to a standard object first (Account, Contact, Lead, Opportunity, Case, Product, Quote, Order, Contract, Campaign, Asset, Entitlement, Work Order and the industry objects of the licensed cloud). A custom object needs a reason the standard one can't serve.
3. Decide relationships, then sharing, then fields. Changing a relationship later is the most expensive change.

## Choosing a relationship

| Need | Use | Watch for |
|---|---|---|
| Child can't exist without the parent; child inherits parent's sharing and is deleted with it; roll-up summaries | **Master-detail** | Up to 2 master-detail relationships per object. The child's owner and sharing come from the parent. Converting later has rules about existing data. |
| Child is independent, may have no parent | **Lookup** | Optional by default. Decide what happens on parent delete (clear, restrict, or cascade where allowed). |
| Many-to-many | **Junction object** with two master-detail relationships | Roll-ups can sit on both parents. The junction's sharing follows the primary master. |
| Link to an external system's record | **External lookup / indirect lookup** with an external ID | Needs Salesforce Connect or an external ID field. |
| Hierarchy within one object | **Hierarchical relationship** (User) or a self-lookup | Depth and query cost. Plan reporting on the hierarchy. |

## Fields

- **Types matter.** Store dates as Date or DateTime, numbers as Number or Currency, flags as Checkbox, and fixed lists as Picklist. Text fields that hold dates or Yes/No values are defects.
- **Picklist or lookup.** A short, stable list owned by admins is a picklist (use a global value set when several objects share it). A list with its own attributes, or that changes often, or is maintained by the business, is an object.
- **External IDs** on anything that integrations upsert on. Mark them unique and case-insensitive deliberately.
- **Formula fields** are free to store but add to query and report cost. A formula that crosses many objects can hit the cross-object limit.
- **Roll-up summary** needs master-detail. Without it use Flow, Apex, or Declarative Lookup Rollup Summaries, and say which.
- **Encryption.** Platform Encryption or Classic Encryption removes some features (filtering, sorting, some formulas). Decide per field, not per object, and check the effect on search and reporting.
- **Naming.** Label for the user, API name for the developer. Keep the API name aligned with the label, and use the client's naming standard if there is one. Descriptions on every custom object and field.

## Record types, page layouts and Lightning pages

- Use a record type when the **business process or picklist values differ**. Don't use one to hide fields: that is what Lightning page visibility and field-level security are for.
- Fewer record types is better. Each one multiplies layouts, picklist values and testing.

## Volume

- Over about a million records on an object, plan for **selective queries**, indexes (standard, external ID, custom index by request), and avoid reports and list views that filter on unindexed fields.
- Over several million, consider **skinny tables** (by request to Salesforce Support), **Big Objects**, archiving, or an external store with Salesforce Connect.
- **Data skew**: more than about 10,000 child records under one parent (account skew), one owner (ownership skew), or one lookup value (lookup skew) causes lock contention and slow sharing recalculation. Spread children across parents and avoid a single integration user owning millions of records.
- Check storage: data and file storage are allocated per licence. Estimate growth per year.

These thresholds are guidance, not hard limits. Confirm limits that matter to the design against the current Salesforce documentation.

## Security and the model

- Start from **Private** organisation-wide defaults for anything sensitive and open up with the role hierarchy, sharing rules, teams and manual sharing. Opening up is easy; closing down breaks things.
- Object and field access through **permission sets and permission set groups**, with profiles kept minimal. Don't give "Modify All" or "View All" to non-admins to solve a visibility problem.
- Think about **who owns the record**, because ownership drives visibility in a private model and is the root of ownership skew.
