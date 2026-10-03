# Architecture and ownership

## Dependency order

```text
brand strategy → VI evidence → visual concept → web component contract → frontend implementation → browser QA → release gate
```

## What this skill may decide

- web route and screen inventory;
- implementation foundation within the existing project;
- component boundaries and content budgets;
- responsive rules, interaction states, motion bands and browser checks;
- web-specific findings and remediation order.

## What this skill may not decide

- official brand colors, typography, Logo geometry, public name or clear-space values;
- new product capabilities, customer claims, metrics or customer-data permissions;
- whether a campaign deviation becomes an official brand rule;
- release approval owned by a brand or product owner.

## Missing dependency behavior

Resolve the pinned repositories in `skill-dependencies.json`. If identity or
commit cannot be verified, mark the affected evidence as `待确认`. Do not
silently fall back to memory or a similarly named local folder. Non-brand
implementation work may continue only when it does not depend on the missing
source.
