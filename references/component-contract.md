# Component contract

Reusable blocks are communication units, not decoration. A block is ready only
when its meaning, content limits and failure behavior are explicit.

## Required fields

- `id`: stable block name;
- `primary_judgment`: the one thing the user should understand;
- `content_roles`: eyebrow, heading, body, evidence, source, CTA, etc.;
- `claim_ids`: IDs for public claims or metrics; use `待确认` when absent;
- `asset_ids`: approved assets or source records;
- `logo_rule_ref`: the upstream operating-rule document when the block shows the Logo;
- `layout`: grid, alignment, crop and reading path;
- `responsive`: behavior at each in-scope breakpoint;
- `states`: default, hover, active, focus-visible, disabled, loading, empty, error;
- `motion`: trigger, property, duration/easing family, reduced-motion fallback;
- `a11y`: semantic element, keyboard path, focus treatment, text alternatives;
- `content_budget`: longest expected heading, label and body variant;
- `fallback`: what remains when media, data or optional copy is unavailable.

## ArcheBase block families

Use these when they explain the product rather than merely decorating it:

- system statement / proof-led hero;
- observation → task-state transformation;
- task distribution or data lineage;
- QC and failure library;
- scene authorization / partner value;
- case study with evidence boundary;
- research or capability comparison;
- conversion CTA with trust and source context.

Avoid a block catalogue that only renames generic three-card marketing sections.
