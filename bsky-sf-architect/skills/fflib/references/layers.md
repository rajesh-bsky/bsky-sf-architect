# The fflib layers

Calls go downward only: **Trigger / Controller / Batch → Service → (Domain, Selector, Unit of Work)**.

```text
Trigger ─▶ Domain ─────────┐
LWC / REST / Batch ─▶ Service ─▶ Domain, Selector, Unit of Work
                              all created through Application (the factory)
```

## Domain (`fflib_SObjectDomain`)

The logic that belongs to **one object's records**: defaults, validation, calculations on the records themselves, reactions to changes.

- Extends `fflib_SObjectDomain`, takes `List<SObject>` in the constructor, and has an inner `Constructor` class implementing `fflib_SObjectDomain.IConstructable`.
- The trigger is one line: `fflib_SObjectDomain.triggerHandler(Accounts.class);`
- Override the context methods you need: `onApplyDefaults`, `onValidate`, `onBeforeInsert`, `onBeforeUpdate(Map<Id, SObject>)`, `onAfterInsert`, `onAfterUpdate(Map<Id, SObject>)`, `onBeforeDelete`, `onAfterDelete`.
- Works on `Records` (the records in this domain) so it is bulk by construction.
- Can also hold **custom domain methods** called by services (`new Accounts(records).applyDiscount()`).
- Don't query in a domain (ask a selector via the service, or use data already on the records).

## Selector (`fflib_SObjectSelector`)

The **only place that queries** an object.

- Implements `getSObjectType()` and `getSObjectFieldList()`, then provides methods such as `selectById(Set<Id>)`.
- Centralises the field list and default ordering, so a new field is added once.
- Enforces object and field security according to the constructor options of the installed version.
- Build related-object queries with `fflib_QueryFactory` through the selector's `newQueryFactory()` rather than hand-written strings.
- Return `List<SObject>` (or typed lists) and accept `Set<Id>` for bulk. Methods take collections, never single IDs in a loop.

## Service (a class with static methods, usually behind an interface)

The **use cases**: one method per business operation, bulk by signature (`Set<Id>` or `List<...>`).

- Typically `AccountsService` (static facade) → `IAccountsService` (interface) → `AccountsServiceImpl` (implementation), resolved through `Application.Service.newInstance(IAccountsService.class)`. This is what lets you mock the service.
- Creates a unit of work, calls selectors and domain classes, and **commits once**.
- Owns the transaction boundary: if it throws, nothing is committed.
- Called by triggers' domain, LWC controllers, REST resources, invocable methods, batch and queueable classes: those stay thin.
- Takes simple parameters. It doesn't know about the UI or `Trigger.new`.

## Unit of Work (`fflib_SObjectUnitOfWork`)

Collects inserts, updates, deletes and relationships (`registerNew`, `registerDirty`, `registerDeleted`, and `registerNew(child, field, parent)` to wire a relationship before IDs exist), orders DML by the object types you list, and commits in **one `commitWork()`** with a savepoint, so a failure rolls back everything.

- Created through `Application.UnitOfWork.newInstance()`.
- The list of SObject types **in dependency order** (parents first) is given in the `Application` class.
- Reduces DML statements, enforces order, and makes the transaction visible in one place.

## Application (`fflib_Application`)

One class that declares the factories:

- `UnitOfWork`: `fflib_Application.UnitOfWorkFactory`, given the SObject types in dependency order.
- `Service`: `fflib_Application.ServiceFactory`, mapping interface → implementation.
- `Selector`: `fflib_Application.SelectorFactory`, mapping SObject type → selector.
- `Domain`: `fflib_Application.DomainFactory`, mapping SObject type → domain constructor.

Tests replace entries with mocks: `Application.Service.setMock(IAccountsService.class, mockService)`.

## ApexMocks (`fflib_ApexMocks`)

Unit tests without the database or the platform's automation.

```apex
fflib_ApexMocks mocks = new fflib_ApexMocks();
IAccountsSelector selectorMock = (IAccountsSelector) mocks.mock(AccountsSelector.class);

mocks.startStubbing();
mocks.when(selectorMock.sObjectType()).thenReturn(Account.SObjectType);
mocks.when(selectorMock.selectById(ids)).thenReturn(accounts);
mocks.stopStubbing();

Application.Selector.setMock(selectorMock);
// ... call the service ...
((fflib_ISObjectUnitOfWork) mocks.verify(uowMock, 1)).registerDirty(accounts[0]);
```

- Stub (`when ... thenReturn`) what the code under test reads. Verify (`mocks.verify`) what it does.
- Use `fflib_Match` for argument matching and `fflib_InOrder` to check call order.
- The **fake `Id` helper** (`fflib_IDGenerator.generate(Account.SObjectType)`) gives valid IDs without inserting.

## Tests in layers

| Layer | Test with |
|---|---|
| Domain | Pass in-memory records, no DML: assert the changes made. |
| Service | Mock the selector and unit of work: assert what was registered. |
| Selector | A real query against test data: assert the fields, order and security. |
| Wiring | A few integration tests through the trigger or the entry point, with real data. |

## Common mistakes

- SOQL in a service or domain "because it's quicker".
- DML outside the unit of work, or more than one `commitWork()` per operation.
- Services that accept `Trigger.new` or an LWC wrapper class.
- Not registering in `Application`, so tests can't mock.
- Treating fflib as a code generator: the value is the discipline, not the file count.
- Copying code written for a different `apex-common` version without checking the installed one.
