# Motion, interaction and accessibility

Read before introducing motion, scroll-linked behavior, modals, menus, forms,
or dense data interaction.

## Motion bands

- `1–2`: opacity/color or instant state changes; suitable for strict, trust-first UI.
- `3–5`: short transform/opacity transitions, staged entry, restrained hover feedback.
- `6–8`: scroll-linked, pinned or physics-like motion only when it explains a sequence or spatial relation.
- `9–10`: exceptional; requires a clear audience benefit, performance budget and human approval.

Always provide a reduced-motion path. Do not drive continuous interaction values
through React state when the project's motion library or CSS can avoid rerendering.
Do not animate layout geometry when transform/opacity can communicate the same change.

## Required state matrix

For each in-scope component, define default, hover, active, focus-visible,
disabled, loading, empty and error. Product UI should also define permission,
validation and offline states when applicable.

## Accessibility checks

- semantic HTML before ARIA;
- keyboard path and visible focus;
- contrast for text, controls and meaningful boundaries;
- status/error announcements where needed;
- no critical meaning conveyed by color alone;
- alt text or an explicit decorative decision for every image;
- motion and autoplay respect user preference;
- touch targets and zoom/reflow remain usable at target breakpoints.

Declare the WCAG version/level used by the project. Do not claim compliance
without checking the rendered surface.
