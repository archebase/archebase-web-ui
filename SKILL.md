---
name: archebase-web-ui
description: "Use whenever an ArcheBase / 智域基石 website, landing page, product UI, frontend redesign, component system, or web visual review is requested. This skill is the web implementation layer between archebase-vi-guide and archebase-visual-design: it converts approved brand evidence and visual direction into a coherent, accessible, responsive interface without generic AI-front-end patterns. Trigger even when the user asks only for a homepage, redesign, interaction, responsive behavior, or frontend polish, provided the work is ArcheBase-branded."
license: "Private internal use only. Do not redistribute."
metadata:
  version: "0.1.1"
  status: "experimental"
  dependencies: "skill-dependencies.json"
compatibility: "Requires a filesystem-capable skill loader. A package manager, browser renderer, or screenshot tool may be needed for implementation QA; Python 3 runs the bundled static checks."
core_max_lines: 320
---

# ArcheBase Web UI

This skill is the web implementation layer for ArcheBase. It does not replace the official VI Guide or the visual-design method layer.

## Ownership boundary

Load and obey these siblings before making brand decisions:

1. `archebase-vi-guide` owns brand facts, approved assets, evidence, modes, route selection and release gates. Its evidence has two layers that must not be conflated: Guide page evidence, and the asset-derived Logo operating rules in `references/logo-usage-rules.md` / `references/logo-combination-matrix.md`; cite the rule file for a Logo size, clear-space or spacing value, never a Guide page.
2. `archebase-visual-design` owns content contracts, visual propositions, hierarchy, composition, typography, imagery, accessibility, Gate A–G critique checklists and production methods.
3. This skill owns web-specific execution: design read, system selection, component contracts, responsive behavior, interaction states, motion, implementation constraints and browser QA.

Before brand-sensitive work, verify the pinned dependency identity from `skill-dependencies.json` (tag `v3.5.10`, commit `16b6e361fcd760bb8dc2c9b72e39debddaeecf54`). A local checkout is only a cache.

If the three layers disagree, brand facts from `archebase-vi-guide` win; visual method from `archebase-visual-design` wins over this skill's preferences; this skill wins only on web implementation detail. Never average conflicting rules. Record the conflict and stop the affected release route when the conflict is material.

## When it applies

Use for ArcheBase websites, landing pages, product UI, web components, frontend redesigns, responsive layouts, interaction polish, design-system mapping, browser rendering, or web UI review. If the artifact is not ArcheBase-branded, use the ordinary web workflow instead. If the request is a deck, print poster, WeChat article, event screen or image-only asset with no web delivery, do not use this skill as the primary skill.

When a web deliverable hands off Logo-bearing print collateral, route its Logo rules to the upstream `references/logo-usage-rules.md` and hand the print method to `archebase-visual-design`; this skill does not own print.

## Operating modes and routes

Read the upstream mode first: `strict`, `guided`, `creative`, or `off`.

Choose one route:

- `marketing-web`: public website, campaign page, landing page, case study or press page.
- `product-ui`: authenticated product screens, console, workflow, data-heavy UI or component system.
- `redesign`: an existing web property where preservation and change scope must be explicit.
- `review`: visual, brand, accessibility or implementation audit without building.

`off` means do not issue a VI verdict. In every other mode, hard brand, claim, privacy, rights and accessibility failures block release. Soft style findings block only in `strict`; in `guided` and `creative`, they need an owner and a recorded disposition.

## Non-negotiable boundaries

- Use the official Logo asset resolved by `archebase-vi-guide`; never generate, redraw, trace, recolor, stretch, mask or bake a Logo into an AI image.
- Route Logo size, clear space, lockup spacing and icon rules to the upstream operating-rule documents (`references/logo-usage-rules.md`, `references/logo-combination-matrix.md` at the pinned baseline). Never restate their numbers here, and never present them as VI Guide facts or attribute them to a Guide page.
- On web surfaces, the `方形` graphic mark carries no built-in safe margin and cannot be used directly as an icon; use the `方圆通用` family for icons and circular avatars, and the delivered small-size classes below the upstream size floor. Dark-mode headers and dark grounds use only the white families. Large sizes render from the SVG via the upstream `scripts/render_logo.sh`, never by upscaling `png-hires`.
- Logo blue is the brand token `AB_BLUE_1` resolved from upstream tokens. A hardcoded historical logo blue that survives only as a gradient interpolation value is wrong, is treated as `待换版`, and must never be reintroduced.
- Do not invent brand tokens, type rules, claims, metrics, customers, product capabilities or public names. If an official answer is absent, write `待确认`.
- Do not introduce a new accent, theme, component behavior or naming rule as if it were official VI. Mark any creative extension as a route-specific proposal.
- Do not migrate frameworks, styling systems or component libraries merely to make the work easier. Inspect the existing project first.
- Do not use generic fake dashboards, fake terminals, random node graphs, decorative status dots, filler gradients, or stock “AI” imagery unless they explain a verified product claim.
- Do not call a page complete while default, hover, active, focus-visible, disabled, loading, empty and error states are undefined for the in-scope components.

## Workflow

### 1. Inspect the project before designing

Check the existing repository, `package.json` or equivalent dependency manifest, routing, CSS strategy, font loading, component library, test commands and current screenshots. Preserve working conventions. If no frontend project exists, state the proposed stack rather than silently creating one.

### 2. Write the web brief and design read

Use `templates/web-ui-brief.md`. State:

- audience, primary judgment and intended action;
- route and mode;
- viewport sizes and breakpoints being judged;
- current brand assets and approved evidence;
- Logo surfaces in scope — page lockup, favicon/app icon/touch icon, circular avatar, dark-mode header, print handoff — and the upstream operating-rule document each routes to;
- content and claim boundaries;
- existing-vs-new surface decision;
- one-line Design Read: page kind + audience + visual language + implementation foundation.

If the brief genuinely permits two incompatible directions, ask one focused question. Otherwise infer and proceed.

### 3. Set exploration controls

Record these as implementation controls, not brand tokens:

- `COMPOSITION_VARIANCE` 1–10: symmetry to deliberate asymmetry;
- `MOTION_INTENSITY` 1–10: static to scroll/physics-led;
- `INFORMATION_DENSITY` 1–10: gallery-like to operational cockpit.

Recommended guardrails: `strict` 2–5 / 1–4 / 3–7; `guided` 4–7 / 2–6 / 3–8; `creative` 5–9 / 3–8 / 2–8. Override only with a recorded reason. These values must never override official colors, fonts, assets or evidence.

### 4. Choose the implementation foundation

Read `references/system-selection.md`. Use the existing official system when the project already has one. When the brief maps to a known public design system, prefer its maintained package; when it maps only to an aesthetic, use the project's native CSS and label the result as an approximation. Verify every import against the dependency manifest before writing it.

### 5. Convert the concept into a component contract

Use `templates/component-contract.yaml` and `references/component-contract.md`. Every screen and reusable block needs:

- one primary audience judgment;
- semantic content roles and claim/evidence IDs where applicable;
- desktop, tablet and mobile behavior;
- content length budget and overflow fallback;
- interaction-state matrix;
- motion and reduced-motion behavior;
- accessibility semantics and alternative paths;
- asset/source/provenance record.

Prefer ArcheBase-specific evidence structures over generic marketing blocks: system statement, observation-to-task-state transformation, data lineage, QC/failure library, scene authorization, case study and proof-led CTA.

When a block carries the Logo, record the upstream operating-rule source (`references/logo-usage-rules.md` / `references/logo-combination-matrix.md`) in the asset/provenance record. Never restate a Logo metric as a brand fact, and never attribute one to a Guide page.

### 6. Implement with restraint

Read `references/anti-slop.md`, `references/motion-and-accessibility.md` and `references/content-and-localization.md` when their triggers apply. Use one coherent page theme and shape language unless the existing product system says otherwise. Let evidence, hierarchy and task completion carry the page; use motion and decoration only when they clarify change, focus or causality.

For redesigns, read `references/redesign-protocol.md` before changing navigation, URLs, form names, analytics hooks, legal copy or brand assets.

### 7. Render and pre-flight

Render at every viewport in the brief and inspect the rendered output, not only source code. Run `checklists/web-ui.md`; use `scripts/validate_skill_bundle.py` for this skill repository and the upstream validators for the pinned VI Guide. Check overflow, wrapping, contrast, focus, keyboard path, state completeness, reduced motion, dark mode if in scope, image crops, loading behavior and performance regressions. Check every in-scope Logo surface against the upstream operating rules and confirm that no Logo metric is presented as a Guide fact.

### 8. Return one verdict

Use `templates/decision-trace.md` and return exactly one: `可发布`, `修复后复审`, or `阻塞，待确认`. A route is not `可发布` if a required source, asset, claim, state, viewport, accessibility check or human approval is unresolved.

## Output contract

Every invocation returns:

1. route, mode and Design Read;
2. project/viewport/screen inventory;
3. selected source evidence, assets, tokens and implementation foundation;
4. component and state decisions;
5. responsive, motion, accessibility and localization decisions;
6. build/review result and rendered surfaces inspected;
7. findings with severity, owner and release impact;
8. unresolved approvals;
9. one release verdict.

## References

- Read `references/architecture.md` for the dependency and ownership model.
- Read `references/system-selection.md` before choosing or adding a UI foundation.
- Read `references/component-contract.md` before creating reusable blocks.
- Read `references/anti-slop.md` for marketing/web visual traps.
- Read `references/motion-and-accessibility.md` before adding motion or interaction.
- Read `references/content-and-localization.md` for Chinese/Latin mixed interfaces.
- Read `references/redesign-protocol.md` for existing-site changes.
- Read `references/evidence-and-provenance.md` when claims, customer data or external assets appear.
- Read `references/logo-operating-rules.md` before placing, sizing, cropping or handing off the Logo on a web surface.
- Read `checklists/web-ui.md` before the release verdict.
