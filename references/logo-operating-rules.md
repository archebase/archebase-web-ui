# Logo operating rules for web surfaces

Read this before a web surface shows, sizes, crops or hands off the ArcheBase
Logo: header/hero/footer lockups, favicon, app icon, touch icon, avatar, social
card, dark-mode headers and any print collateral a web project produces.

## Where the rules live

The values live upstream, in the pinned `archebase-vi-guide` baseline (tag
`v3.5.10`, commit `16b6e361fcd760bb8dc2c9b72e39debddaeecf54`):

- `references/logo-usage-rules.md` — asset-derived operating rules for minimum
  size and the dedicated small-size classes, clear space, horizontal and
  vertical lockup spacing and wordmark alignment, background and colour-family
  limits, `白底` versus transparent encoding, the print processes each colour
  family is allowed on with their minimum widths, and SVG rendering for large
  sizes;
- `references/logo-combination-matrix.md` and its machine-readable
  `assets/logo-combination-matrix.json` — the authorised combinations per
  colour family.

This skill routes to those documents. It does not restate their numeric values,
and it never presents them as VI Guide facts.

## Provenance

These rules are measured from the approved `智域基石 Logo V2` assets, not
defined by the VI Guide (`assets/guide-evidence.json` →
`operational_rules.must_not_claim`). Guide page evidence and asset-derived
operating rules are two different evidence layers: cite the upstream rule file
for a size, clear-space or spacing value, and cite a Guide page only for what
the Guide actually defines. Never attribute an operating rule to a Guide page,
and never claim a combination that the upstream matrix does not list — a
missing combination is the signed scope, not a gap to fill.

## Web surfaces and what to route

- **Page lockup (header, hero, footer).** Resolve the asset through the upstream
  resolver; keep the delivered lockup spacing and wordmark alignment unchanged
  and give the mark its upstream clear space. Lockup geometry is a delivery
  fact, not a design variable, and the mark is never redrawn, re-tinted,
  stretched, masked or baked into a generated image.
- **Icon surfaces (favicon, app icon, touch icon).** The `方形` graphic mark
  carries no built-in safe margin, so it cannot be used directly as an icon: use
  the `方圆通用` mark or supply the margin yourself. Below the upstream size
  floor, switch to the delivered small-size classes instead of scaling the
  standard mark.
- **Circular avatars and crops.** Use the `方圆通用` family. Never build a round
  version by masking or scaling the `方形` asset, and do not treat the family's
  built-in margin as clear space outside a circular crop.
- **Dark-mode headers and dark grounds.** Only the white families are allowed;
  the black families, including `黑色渐变`, do not hold up on dark grounds.
- **Large sizes and icons that outgrow the supplied rasters.** Render from the
  SVG with the upstream `scripts/render_logo.sh`; never upscale a `png-hires`
  bitmap. `png-hires/` covers only the combinations the upstream matrix lists,
  so a missing hires file is not a missing asset.
- **Logo blue.** The mark's blue is the brand token `AB_BLUE_1`, resolved from
  the pinned upstream tokens; map it to a semantic token rather than a literal.
  A hardcoded historical logo blue that survives only as a gradient
  interpolation value is not a spec fill, must never be reintroduced, and
  material that carries it is `待换版`.
- **Print collateral handoff.** Route to the upstream operating rules for the
  per-process minimum sizes and the processes barred from gradient families;
  hand the collateral to `archebase-visual-design` and do not copy the upstream
  numbers into the web deliverable.
