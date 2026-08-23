---
name: feedback-insignia-cutline-method
description: "Standard method for converting a color-filled, multi-shape national-insignia/roundel-style SVG into cut lines for a single-sheet paint mask"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2f1e65a0-4cf1-4bda-a283-bf67bb525b2a
  modified: 2026-08-23T00:16:34.350Z
---

When converting a reference national-insignia (or similar) SVG — built as
several overlapping, solid-filled shapes composited in painter's-algorithm
order (later shapes drawn on top override earlier ones), e.g. a roundel's
outer disk + outer bar + white bar + inner disk + star — into cut lines for
a single-sheet paint mask (see [[feedback_resources_organization]] for where
these files live and how they're named), do **not** just strip each shape's
fill and keep its raw outline. Overlapping shapes' raw outlines leave lines
running straight through the middle of regions that are meant to be a
single color (e.g. the bar's rectangle edges cutting through the star) —
wrong for the "cut once, peel each region to spray its color" technique,
where every cut line must be either an actual color change or the overall
outer edge, nothing else.

**Correct method:** compute the exact boolean geometry of each final color
region from the flattened artwork, respecting paint order, using Shapely
(`shapely.geometry.Polygon`/`box`, `.union()`, `.difference()`). For the
roundel this meant, in paint order: `navy = (outer_disk ∪ outer_bar) −
(white_bar − inner_disk) − star`. The result is a single polygon with an
exterior ring (the overall outer edge) and interior rings/holes wherever a
different color shows through (each hole IS the boundary of that other
color's region too — no need to compute or draw it separately). Emit the
exterior + all interior rings as one `<path>` with multiple `M...Z`
subpaths. Approximate circles with a high-segment-count polygon (e.g.
`quad_segs=128` in Shapely, or ~500 points around) — smooth enough that the
polygon approximation is invisible at cutting scale (sub-0.001mm deviation),
far simpler than trying to preserve true circular arcs through the boolean
ops.

No separate enclosing/margin rectangle unless asked for — cut lines should
be only real color changes and the true outer edge; any margin the user
wants added is a deliberate separate choice, not baked into the derived
file by default.

**Why:** user's actual technique (2026-08-23, Bottisham Four E2-S roundel
work) is one mask sheet, cut once, then peel individual regions to spray
each color in turn, leaving the rest of the mask in place — not a separate
mask per color layer, and not a naive outline overlay. First attempt (raw
overlaid outlines, fill stripped) was rejected: "the bar lines are cutting
though the middle of the star." The Shapely boolean-geometry version fixed
it exactly, confirmed correct, and the user asked to remember this as the
**standard method for any national-insignia/similar color-filled SVG**
converted for cutting in this project, not a one-off fix.

**How to apply:** whenever asked to prepare a national-insignia, roundel,
or other multi-shape layered-color reference SVG (e.g. from
`masks/common/insignia/`) for cutting, reach for this boolean-geometry
method by default rather than a raw-outline overlay — and store the
derived `-for-cutting.svg` alongside the master reference file (same
folder), documented in that folder's README, so it's reusable across
projects rather than rebuilt per cut sheet.
