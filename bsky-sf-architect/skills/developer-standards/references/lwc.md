# Lightning Web Components (and Aura)

## Components

- **Small and single-purpose.** One component, one job. Compose with child components rather than growing a large one.
- **Data down, events up.** Parents pass data through `@api` properties; children tell parents through `CustomEvent`. Don't reach into another component's DOM.
- `@api` properties are **read-only to the component that receives them**: copy before changing (`{...obj}`, `[...arr]`).
- Use **Lightning Data Service** (`lightning-record-form`, `lightning-record-edit-form`, `lightning-record-view-form`, `getRecord`, `updateRecord`, `createRecord`) before writing Apex. It handles CRUD, FLS and caching for you.
- Use **`@wire`** for reads, and imperative Apex for actions and for calls that need parameters at a moment you choose. Handle both `data` and `error`.
- Use **Lightning Message Service** for communication between components that aren't in the same hierarchy, and Platform Events through `lightning/empApi` for server-pushed updates.
- Use base components (`lightning-*`) and **SLDS** classes and design tokens. Don't hard-code colours or spacing that fight the theme.

## Apex called from LWC

- `@AuraEnabled(cacheable=true)` for read-only methods used with `@wire`. Refresh with `refreshApex`.
- Return the **minimum data** the component needs, not whole SObjects with every field.
- Enforce **CRUD, FLS and sharing** in the Apex method. The client can be bypassed, so never rely on the component to hide a field.
- Throw `AuraHandledException` with a useful message; show it in the component. Log the detail server-side.

## Security

- No `innerHTML`, `eval`, or dynamically built script URLs. Use `lwc:dom="manual"` only with sanitised content.
- Don't load third-party libraries from a CDN. Use **static resources** and `loadScript` / `loadStyle` after reviewing the library.
- Respect **Lightning Web Security**: don't depend on DOM access outside your namespace.
- Don't put secrets or tokens in component code or in `@api` properties that are exposed in the page metadata.

## Performance

- Keep the number of **wire and Apex calls per page** low. Combine calls; cache with `cacheable=true`.
- Avoid rendering large lists without pagination or `lightning-datatable` infinite loading.
- Don't set state in `renderedCallback` without a guard: it re-renders in a loop.
- Use `if:true` / `lwc:if` to skip rendering what isn't needed. Prefer `lwc:if`, `lwc:elseif` and `lwc:else` in current API versions.

## Accessibility

- Every input has a label. Use `aria-*` attributes where a base component doesn't supply them. Keyboard operation for every action. Don't convey meaning by colour alone.
- Test with the keyboard and a screen reader on the main flow.

## Testing

- **Jest** tests with `@salesforce/sfdx-lwc-jest`. Test rendered output and events, mock `@wire` adapters and Apex imports, and reset the DOM between tests.
- Test the **error path** as well as the happy path.
- Run `npm run test:unit` (or the project's script) and `npm run lint`.

## Aura

- Don't start new work in Aura unless a feature requires it. When maintaining Aura, keep it thin and move logic into LWC and Apex services.
- Aura components that wrap LWC need explicit event bridging; check events cross the boundary as intended.

## Review smells

- Direct DOM manipulation instead of template bindings.
- Apex called in a loop or in `connectedCallback` on every render with no caching.
- A component that does data access, business rules and presentation all at once.
- No error handling on wire or imperative calls.
- Hard-coded record IDs, URLs or object names that should be imported from `@salesforce/schema`.
