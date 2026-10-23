# fflib code skeletons

These are **starting points**. Before using one, read the installed `fflib_*` classes in the project and adjust to its version, its naming and its `Application` class. Replace `Account` / `Accounts` with the object.

## Trigger

```apex
trigger AccountTrigger on Account (
    before insert, before update, before delete,
    after insert, after update, after delete, after undelete
) {
    fflib_SObjectDomain.triggerHandler(Accounts.class);
}
```

## Domain

```apex
public with sharing class Accounts extends fflib_SObjectDomain implements IAccounts {

    public Accounts(List<Account> records) {
        super(records);
    }

    public override void onApplyDefaults() {
        for (Account a : (List<Account>) Records) {
            if (a.Industry == null) {
                a.Industry = 'Other';
            }
        }
    }

    public override void onValidate() {
        for (Account a : (List<Account>) Records) {
            if (String.isBlank(a.Name)) {
                a.Name.addError('Name is required.');
            }
        }
    }

    public class Constructor implements fflib_SObjectDomain.IConstructable {
        public fflib_SObjectDomain construct(List<SObject> sObjectList) {
            return new Accounts(sObjectList);
        }
    }
}
```

## Selector

```apex
public inherited sharing class AccountsSelector extends fflib_SObjectSelector implements IAccountsSelector {

    public Schema.SObjectType getSObjectType() {
        return Account.SObjectType;
    }

    public List<Schema.SObjectField> getSObjectFieldList() {
        return new List<Schema.SObjectField>{
            Account.Id,
            Account.Name,
            Account.Industry,
            Account.OwnerId
        };
    }

    public List<Account> selectById(Set<Id> ids) {
        return (List<Account>) selectSObjectsById(ids);
    }
}
```

## Service

```apex
public interface IAccountsService {
    void reassignAccounts(Set<Id> accountIds, Id newOwnerId);
}
```

```apex
public with sharing class AccountsService {
    public static void reassignAccounts(Set<Id> accountIds, Id newOwnerId) {
        service().reassignAccounts(accountIds, newOwnerId);
    }

    private static IAccountsService service() {
        return (IAccountsService) Application.Service.newInstance(IAccountsService.class);
    }
}
```

```apex
public with sharing class AccountsServiceImpl implements IAccountsService {

    public void reassignAccounts(Set<Id> accountIds, Id newOwnerId) {
        fflib_ISObjectUnitOfWork uow = Application.UnitOfWork.newInstance();
        List<Account> accounts =
            ((IAccountsSelector) Application.Selector.newInstance(Account.SObjectType)).selectById(accountIds);

        for (Account a : accounts) {
            a.OwnerId = newOwnerId;
            uow.registerDirty(a);
        }
        uow.commitWork();
    }
}
```

## Application

```apex
public class Application {

    public static final fflib_Application.UnitOfWorkFactory UnitOfWork =
        new fflib_Application.UnitOfWorkFactory(
            new List<SObjectType>{ Account.SObjectType, Contact.SObjectType }   // parents before children
        );

    public static final fflib_Application.ServiceFactory Service =
        new fflib_Application.ServiceFactory(
            new Map<Type, Type>{ IAccountsService.class => AccountsServiceImpl.class }
        );

    public static final fflib_Application.SelectorFactory Selector =
        new fflib_Application.SelectorFactory(
            new Map<SObjectType, Type>{ Account.SObjectType => AccountsSelector.class }
        );

    public static final fflib_Application.DomainFactory Domain =
        new fflib_Application.DomainFactory(
            Application.Selector,
            new Map<SObjectType, Type>{ Account.SObjectType => Accounts.Constructor.class }
        );
}
```

## Service unit test with ApexMocks

```apex
@IsTest
private class AccountsServiceTest {

    @IsTest
    static void reassignAccountsRegistersEachAccountAsDirty() {
        fflib_ApexMocks mocks = new fflib_ApexMocks();
        fflib_ISObjectUnitOfWork uowMock = (fflib_ISObjectUnitOfWork) mocks.mock(fflib_SObjectUnitOfWork.class);
        IAccountsSelector selectorMock = (IAccountsSelector) mocks.mock(AccountsSelector.class);

        Id accountId = fflib_IDGenerator.generate(Account.SObjectType);
        Id newOwnerId = fflib_IDGenerator.generate(User.SObjectType);
        List<Account> accounts = new List<Account>{ new Account(Id = accountId, Name = 'Test') };

        mocks.startStubbing();
        mocks.when(selectorMock.sObjectType()).thenReturn(Account.SObjectType);
        mocks.when(selectorMock.selectById(new Set<Id>{ accountId })).thenReturn(accounts);
        mocks.stopStubbing();

        Application.UnitOfWork.setMock(uowMock);
        Application.Selector.setMock(selectorMock);

        Test.startTest();
        AccountsService.reassignAccounts(new Set<Id>{ accountId }, newOwnerId);
        Test.stopTest();

        ((fflib_ISObjectUnitOfWork) mocks.verify(uowMock, 1)).registerDirty(accounts[0]);
        ((fflib_ISObjectUnitOfWork) mocks.verify(uowMock, 1)).commitWork();
        System.assertEquals(newOwnerId, accounts[0].OwnerId, 'The owner should have been changed.');
    }
}
```

Interfaces `IAccounts` and `IAccountsSelector` (declaring the methods other classes use, and for the selector extending `fflib_ISObjectSelector`) are needed for the code above; generate them with the classes.
