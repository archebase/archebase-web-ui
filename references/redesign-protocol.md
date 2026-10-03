# Redesign protocol

Read before changing an existing web property. The goal is to improve the
interface without silently breaking user expectations or operational hooks.

## Classify the change

- `preserve`: keep information architecture, URLs, navigation labels and interaction model; polish hierarchy and implementation.
- `guided-overhaul`: retain brand, legal and content contracts while changing layout families and component composition.
- `greenfield`: no compatibility promise beyond the approved brief.

## Audit before editing

Capture screenshots and a route/screen inventory. Record current URLs,
analytics hooks, form field names, SEO metadata, legal links, permissions,
empty/error states, mobile behavior and known user pain points.

## Never change silently

- URL structure and redirects;
- navigation labels or form field names;
- legal, privacy or consent copy;
- Logo/wordmark and public brand name;
- data semantics, permission boundaries or customer-facing claims;
- analytics and experiment identifiers.

Any intentional change needs an owner, migration or rollback note, and a new
rendered QA pass at the affected routes.
