# Web UI release checklist

## Brief and scope
- [ ] Route and mode selected.
- [ ] One primary judgment per screen.
- [ ] Design Read and three exploration controls recorded.
- [ ] Viewports, breakpoints, theme and localization scope recorded.

## Brand and evidence
- [ ] VI Guide identity and commit verified.
- [ ] Logo resolved from approved assets; no generated or redrawn mark.
- [ ] Colors, type and public name follow the upstream source.
- [ ] Claims, metrics, customer material and third-party assets have owners and sources.
- [ ] Unknowns are `待确认`, not silently invented.

## Logo surfaces (route to upstream operating rules)
- [ ] Page lockup keeps the delivered spacing and wordmark alignment; the mark is not redrawn, re-tinted, stretched or masked.
- [ ] Favicon, app icon and touch icon use the icon-safe family — `方形` has no built-in safe margin and was not used directly as an icon; no round version was produced by masking or scaling `方形`; circular avatars use `方圆通用`.
- [ ] Sizes meet the upstream size floors, or use the delivered small-size classes below them, instead of scaling the standard mark.
- [ ] Dark-mode headers and dark grounds use only the white families; no black-family mark (including `黑色渐变`) appears on a dark ground.
- [ ] Large sizes render from the SVG via `scripts/render_logo.sh`; no `png-hires` bitmap was upscaled, and a missing hires file was not treated as a missing asset.
- [ ] Logo blue maps to the upstream token `AB_BLUE_1`; no hardcoded historical logo blue was reintroduced.
- [ ] Every Logo size, clear-space or spacing value cites an upstream operating-rule document (`references/logo-usage-rules.md` / `references/logo-combination-matrix.md`), not a Guide page, and is not restated as a Guide fact.
- [ ] Logo rules for any hand-off print collateral were routed to the upstream operating rules.

## Implementation
- [ ] Existing framework and dependencies inspected.
- [ ] No unnecessary framework or component-system migration.
- [ ] All new imports exist in the dependency manifest.
- [ ] Components have semantic structure and stable boundaries.
- [ ] No fake dashboards, fake terminals or decorative AI motifs without an evidence role.

## States and behavior
- [ ] Default, hover, active, focus-visible, disabled, loading, empty and error states defined.
- [ ] Product UI permission, validation and offline states handled when relevant.
- [ ] Keyboard path and visible focus checked.
- [ ] Reduced-motion path checked.
- [ ] Dark mode checked when in scope.

## Rendered QA
- [ ] Rendered at every brief viewport.
- [ ] No overflow, accidental clipping, unstable wrapping or broken crops.
- [ ] Grayscale and media-removed checks preserve hierarchy.
- [ ] Text and controls meet the project's declared contrast target.
- [ ] Longest supplied copy and bilingual variants tested.
- [ ] Performance regressions reviewed.

## Release
- [ ] Human owner reviewed the intended mode and deviations.
- [ ] Decision trace completed.
- [ ] One verdict returned: `可发布`, `修复后复审`, or `阻塞，待确认`.
