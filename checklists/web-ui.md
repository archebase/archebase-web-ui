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
