# ArcheBase Web UI Skill

ArcheBase / 智域基石 web implementation skill. It sits between the authoritative VI system and the visual-design application layer:

- `archebase-vi-guide`: brand facts, approved assets, evidence, modes and release gates.
- `archebase-visual-design`: content contract, visual proposition, hierarchy, composition, accessibility and production methods.
- `archebase-web-ui`: web-specific implementation, component contracts, responsive behavior, states, motion and browser QA.

This repository is private and contains no copied VI PDF, Logo bundle or Design IR. Resolve those from the pinned dependencies when the task requires them.

## Status

Experimental `0.1.0`. The skill is intended for internal ArcheBase use and should be evaluated against real website and product UI tasks before a stable release.

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

## Feedback

Record methodology issues as GitHub issues in this private repository. Changes that affect official brand facts belong in `archebase-vi-guide`; changes to visual method belong in `archebase-visual-design`.
