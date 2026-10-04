# ArcheBase Web UI Skill

ArcheBase / 智域基石 web implementation skill. It sits between the authoritative VI system and the visual-design application layer:

- `archebase-vi-guide`: brand facts, approved assets, evidence, modes, release gates, and the asset-derived Logo operating rules (`references/logo-usage-rules.md`, `references/logo-combination-matrix.md`) this skill routes to but never restates.
- `archebase-visual-design`: content contract, visual proposition, hierarchy, composition, accessibility, Gate A–G critique checklists and production methods.
- `archebase-web-ui`: web-specific implementation, component contracts, responsive behavior, states, motion and browser QA.

This repository is private and contains no copied VI PDF, Logo bundle or Design IR. Resolve those from the pinned dependencies when the task requires them.

Pinned baseline: `archebase-vi-guide` tag `v3.5.10`, commit `16b6e361fcd760bb8dc2c9b72e39debddaeecf54`. That baseline signs the Logo operating rules and the combination matrix that govern web Logo surfaces — favicon/app-icon/touch-icon and avatar sizing, header/hero/footer lockups, dark-mode headers and print handoff. Those values are measured from the approved assets, not defined by the VI Guide, so this skill routes to the upstream rule documents and never presents them as Guide facts.

## Status

Experimental `0.1.1`. The skill is intended for internal ArcheBase use and should be evaluated against real website and product UI tasks before a stable release.

## Layout

```text
SKILL.md                         agent-facing workflow
references/                      progressive-disclosure web methods
templates/                       briefs, component contracts, decision traces
checklists/                      release checks
evals/                           test prompts and static checks
scripts/                         deterministic repository checks
skill-dependencies.json          pinned upstream skill identities
LICENSE                          private internal-use notice
NOTICE.md                        provenance and non-redistribution notes
```

## Checks

```bash
python3 scripts/validate_skill_bundle.py
```

`scripts/validate_skill_bundle.py` also requires `references/logo-operating-rules.md` and fails when a live file states a Logo size or clear-space metric without routing it to the upstream rule documents (or marking it `待确认`), so an asset-derived rule cannot be reintroduced as an unattributed brand fact.

`references/` includes `logo-operating-rules.md`, the single routing point for every web Logo surface; it points at the upstream rule documents instead of copying their numbers.

## Feedback

Record methodology issues as GitHub issues in this private repository. Changes that affect official brand facts belong in `archebase-vi-guide`; changes to visual method belong in `archebase-visual-design`.
