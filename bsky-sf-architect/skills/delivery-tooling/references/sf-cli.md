# sf CLI cheat sheet

The Salesforce CLI (`sf`, v2) is the current tool. Commands and flags change between releases: when unsure, run `sf <command> --help` and use what it says. Update with `sf update`.

`$ORG` is the alias or username. Use `--target-org "$ORG"` explicitly so a command never runs against the wrong default org.

## Orgs

```bash
sf org list                                   # authenticated orgs (alias, username, type, status)
sf org login web --alias MyOrg                # log in with the browser
sf org login web --alias MyOrg --instance-url https://test.salesforce.com   # sandbox
sf org display --target-org MyOrg             # details; NOT --verbose (it prints an access token)
sf org list limits --target-org MyOrg         # API and storage limits in use
sf config set target-org MyOrg                # set the default; still pass --target-org in scripts
```

## Source: retrieve and preview

```bash
sf project retrieve preview --target-org MyOrg            # what differs between org and source (changes nothing)
sf project retrieve start --target-org MyOrg --metadata "ApexClass:AccountService"
sf project retrieve start --target-org MyOrg --manifest manifest/package.xml
sf project generate manifest --source-dir force-app --name manifest/package.xml
```

Retrieve a temporary copy to diff without touching the project:

```bash
sf project retrieve start --target-org MyOrg --manifest manifest/package.xml --target-metadata-dir ./.tmp/org-copy --unzip
```

## Deploy

```bash
sf project deploy preview --target-org MyOrg --source-dir force-app            # what would change
sf project deploy validate --target-org MyOrg --source-dir force-app --test-level RunLocalTests   # validate only
sf project deploy start --target-org MyOrg --source-dir force-app --dry-run --test-level RunLocalTests
sf project deploy start --target-org MyOrg --source-dir force-app --test-level RunLocalTests       # a real deploy: needs the user's go-ahead
sf project deploy quick --target-org MyOrg --job-id 0Af...                      # deploy a validated package without re-running tests
sf project deploy report --target-org MyOrg --job-id 0Af...
sf project deploy cancel --job-id 0Af...
```

Test levels: `NoTestRun` (not allowed for production deploys that include Apex), `RunSpecifiedTests` (with `--tests ClassA --tests ClassB`), `RunLocalTests`, `RunAllTestsInOrg`. Production deployments containing Apex need 75% overall coverage and every trigger covered.

Destructive changes use `--post-destructive-changes` / `--pre-destructive-changes` with a `destructiveChanges.xml`. **Treat as a separate approved step** (see the skill rules).

## Tests

```bash
sf apex run test --target-org MyOrg --test-level RunLocalTests --code-coverage --result-format human --wait 20
sf apex run test --target-org MyOrg --class-names AccountServiceTest --code-coverage --result-format human --wait 10
sf apex get test --test-run-id 707... --target-org MyOrg
```

LWC unit tests run locally: `npm run test:unit` (Jest, `@salesforce/sfdx-lwc-jest`).

## Static analysis

```bash
sf plugins install code-analyzer           # once
sf code-analyzer run --workspace force-app --severity-threshold 2
npm run lint                               # ESLint for LWC, if the project defines it
```

## Data (read; writes need approval)

```bash
sf data query --target-org MyOrg --query "SELECT Id, Name FROM Account LIMIT 5"
sf data query --target-org MyOrg --use-tooling-api --query "SELECT Name, ApiVersion FROM ApexClass"
```

Writes (`sf data create|update|delete|upsert|import`) and anonymous Apex (`sf apex run`) change an org: ask first.

## Scratch orgs and packaging

```bash
sf org create scratch --definition-file config/project-scratch-def.json --alias MyScratch --duration-days 7 --set-default
sf project deploy start --target-org MyScratch
sf org assign permset --name MyPermSet --target-org MyScratch
sf org open --target-org MyScratch --path /lightning/setup/SetupOneHome/home
sf org delete scratch --target-org MyScratch        # destructive: ask first
```

Unlocked packages: `sf package create`, `sf package version create`, `sf package install`. Use them when the org is large enough to need modules with declared dependencies.

## Git for release work

```bash
git status --short
git diff --name-status origin/main...HEAD -- force-app    # changed source on this branch
git log --oneline origin/main..HEAD                       # commits to be released
```

## Reading a deploy result

- `status: Succeeded` but check `numberComponentsDeployed` against what you expected; a deploy can succeed and skip things you thought were included.
- Read `componentFailures` and `runTestResult.failures` in full, not only the summary.
- Check coverage per class in the test result, not just the overall number.
