# System selection

Read this before adding a UI library, changing the styling foundation, or
creating a new component family.

## Decision order

1. Preserve the project's existing framework, routing, CSS strategy and component library when they are healthy.
2. If the brief clearly belongs to an official external system, use that system's maintained package instead of recreating its tokens.
3. If the brief is an aesthetic rather than a system, implement it with the project's native primitives and label the result as an approximation.
4. If no project exists, propose a stack in the brief and wait for approval before installing dependencies.

## Safety checks

- Inspect `package.json`, lockfiles and build scripts before imports.
- Use one component-system foundation per surface. Do not mix multiple competing token systems in one tree without a documented adapter.
- Keep brand tokens semantic. The upstream VI Guide is the authority for their values and roles.
- The asset-derived Logo operating rules (upstream `references/logo-usage-rules.md`) are not tokens: route to that file for a Logo size, clear space or lockup value, and never mint a token from one.
- A web implementation preference is not permission to alter the official VI system.
- When a new dependency is justified, record its purpose, version, license and rollback path in the decision trace.

## Foundation record

```yaml
foundation:
  framework: existing | proposed
  styling: existing | proposed
  components: existing | official-package | native-primitives
  motion: none | css | existing-library | proposed-library
  reason: "why this foundation fits the current project"
  dependency_checks: pass | fail |待确认
```
