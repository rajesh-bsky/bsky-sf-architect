---
description: Work with the fflib Apex Enterprise Patterns: scaffold domain, selector, service and ApexMocks tests for an object, review fflib code for layering mistakes, or advise whether to adopt fflib. Matches the project's installed fflib version and conventions.
argument-hint: "[scaffold ObjectName | review path | should we adopt fflib]"
---

Apply the fflib patterns.

Arguments: $ARGUMENTS

1. Load the `bsky-sf-architect:fflib` skill with the Skill tool and follow it.
2. First inspect the project: is fflib installed (look for `fflib_` classes in `force-app`, and the version in `sfdx-project.json` or the package alias), is there an `Application` class, and what naming do the existing selector, service and domain classes use? Say what you found.
3. **scaffold**: ask which layers are needed and the first use case if the user hasn't said. Generate the files in the project's conventions, register them in the `Application` class, and write tests. Read the installed fflib classes first so method names match the installed version. List the files created.
4. **review**: check that SOQL is only in selectors, DML only through the unit of work, domain classes hold the object's logic, services are bulk and use one `commitWork()`, classes are registered in `Application`, and tests use ApexMocks where they should.
5. **adopt?**: give a recommendation with reasons using the skill's table, and offer to write an ADR (`/bsky-sf-architect:design --adr`).
6. Don't deploy or run tests against an org unless the user says so; use `bsky-sf-architect:delivery-tooling` for the commands when they do.
