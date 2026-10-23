# Discovery question bank

Use it to plan a workshop and to sort what the client has already answered from what is open. Pick the sections that apply; don't read the whole list aloud. For each question note: **answered** (with the source), **partly answered**, or **open** (with who can answer).

## Business and goals

- What outcome should this change deliver, and how will you measure it? What's the number today?
- Who sponsors it, who decides, and who will use it every day?
- What happens if nothing changes? What's the cost of the current way of working?
- What is the deadline and what drives it (a contract, a season, a regulation, a launch)?
- What has been tried before and why did it fail or stall?
- What is explicitly out of scope?

## People and process

- Walk me through the process today, from trigger to outcome. Where does it hurt?
- Who does each step? In which system? How many people, in how many teams and locations?
- What are the personas and what must each be able to do? How many of each?
- What exceptions and edge cases happen weekly?
- What approvals exist, who gives them, and what are the thresholds?
- How are people trained today, and what is their appetite for change?

## Data

- What are the main records (accounts, products, cases ...) and where do they live today?
- How many records, how fast do they grow, and how old is the oldest you must keep?
- What is the quality of the data today? Duplicates, missing fields, free-text where there should be lists?
- Who owns each data set? Who is allowed to change it?
- What needs migrating, from where, and what can be left behind or archived?
- What are the reporting needs? Which questions must the business be able to answer, and how often?

## Systems and integrations

- Which systems must Salesforce talk to? For each: direction, what data, how often, how many records, who owns it?
- Is there an existing middleware or integration platform? Who runs it?
- What is the system of record for each data set?
- What authentication and network constraints exist (SSO, VPN, IP allow lists)?
- What happens when a system is down?

## Security and compliance

- Which obligations apply (POPIA, GDPR, HIPAA, PCI DSS, sector rules)? Who is the data protection or compliance owner?
- Which data is personal or sensitive? Where does it go, and who may see it?
- How is consent captured and honoured? What are the retention and deletion rules?
- Who must **not** see which records? (This sets the sharing model.)
- Are there audit requirements: who changed what, and when?
- Any data-residency restriction on where data or integrations are hosted?

## Salesforce estate (when there is one)

- Which edition, clouds and licences? How many of each licence type? What's the renewal date?
- Which managed packages are installed and who supports them?
- How many sandboxes and what is the release process? Is there source control and a pipeline?
- Who administers the org? How many admins and developers? Any known technical debt?
- What customisation exists (Apex, Flow, LWC) and who understands it?
- Which features are used, and which were bought and aren't?

## Delivery and adoption

- Who is on the client team and how much time can they give? Who has the authority to decide quickly?
- What are the environments, access arrangements and security reviews that take time?
- What does success look like at go-live and at three months?
- How will users be trained and supported? Who owns the system after go-live?
- What is the budget range and the appetite for phasing?

## Marketing, service, sales, and industry add-ons

Add a focused set when the scope includes:
- **Sales**: lead sources and routing, qualification stages, forecasting method, quoting and pricing rules, territories.
- **Service**: channels, case categories, SLAs and entitlements, escalations, knowledge ownership, self-service goals.
- **Marketing**: consent model, channels, segmentation data, journey owners, attribution, send volumes.
- **Experience Cloud**: audience and numbers, authentication, branding, guest access, content ownership.
- **Data / AI**: data readiness, where the data lives, who may use it for what, how outputs are checked.

## Closing a workshop

- Read back decisions, open items, owners and dates.
- Agree the next session and what each side will bring.
- Send a short summary within a day (a draft for the consultant to review and send).
