# Changelog

## 0.1.1 — 2026-10-04

- Advanced the pinned `archebase-vi-guide` baseline to `v3.5.10` (`16b6e36`), covering the owner-signed Logo release published since the previously pinned tag, and `archebase-visual-design` to `6953733`; updated the dependency roles to name the Logo operating-rule documents and the Gate A–G checklists.
- Added `references/logo-operating-rules.md`: a routing reference for web Logo surfaces (favicon/app-icon/touch-icon and avatar sizing, header/hero/footer lockups, dark-mode headers, `png-hires` versus SVG rendering, print handoff) that points at the upstream rules instead of restating their numbers.
- Routed the new rules through the contract surface: SKILL.md boundaries and workflow, `references/architecture.md`, `references/evidence-and-provenance.md`, `references/system-selection.md`, `references/redesign-protocol.md`, `checklists/web-ui.md` and the three templates. Asset-derived operating rules are cited to the upstream rule files and never presented as VI Guide facts.
- Noted that logo blue is the token `AB_BLUE_1` and that a hardcoded historical logo blue (gradient-interpolation only) must not be reintroduced.
- `scripts/validate_skill_bundle.py`: requires the new reference and fails when a live file states a Logo size/clear-space metric without routing to an upstream rule document.

## 0.1.0 — 2026-10-03

- Initial private release.
- Adds the web implementation layer between `archebase-vi-guide` and `archebase-visual-design`.
- Adds routes for marketing web, product UI, redesign and review.
- Adds design-read controls, component contracts, state/motion/accessibility guidance, provenance checks and deterministic bundle validation.
