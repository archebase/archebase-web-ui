# Architecture and ownership

## Dependency order

```text
brand strategy → VI evidence → visual concept → web component contract → frontend implementation → browser QA → release gate
```

Two upstream evidence layers must stay separate. Guide page evidence (PDF page + evidence id) and the asset-derived Logo operating rules (`references/logo-usage-rules.md`, `references/logo-combination-matrix.md`, machine-readable `assets/logo-combination-matrix.json`) are not interchangeable: cite the rule file for a Logo size, clear-space or spacing value, and never attribute an operating rule to a Guide page.

## What this skill may decide

- web route and screen inventory;
- implementation foundation within the existing project;
- component boundaries and content budgets;
- responsive rules, interaction states, motion bands and browser checks;
- web-specific findings and remediation order.

## What this skill may not decide

- official brand colors, typography, Logo geometry, public name, or Logo operating-rule values (size floors, clear space, lockup spacing and print limits), which this skill routes to the upstream `references/logo-usage-rules.md` / `references/logo-combination-matrix.md` instead of restating;
- new product capabilities, customer claims, metrics or customer-data permissions;
- whether a campaign deviation becomes an official brand rule;
- release approval owned by a brand or product owner.

## Missing dependency behavior

Resolve the pinned repositories in `skill-dependencies.json`. If identity or
commit cannot be verified, mark the affected evidence as `待确认`. Do not
silently fall back to memory or a similarly named local folder. A candidate
`archebase-vi-guide` must carry `references/logo-usage-rules.md` and
`references/logo-combination-matrix.md`; a copy without them is not the pinned
baseline. Non-brand implementation work may continue only when it does not
depend on the missing source.
