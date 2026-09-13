---
name: feedback-prefer-real-fonts-over-handbuilt-curves
description: "When regularizing traced lettering/digits with real curves, check for a matching font file before hand-designing geometry"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ee072010-f7b7-48e5-a550-d7cdb0e4bf76
  modified: 2026-08-20T19:48:14.875Z
---

When a traced letterform needs regularizing and has genuine curves (not just
straight-line chamfers), check whether a font file already matches the
style before hand-building centerline geometry (bezier/spline waypoints,
arc parameters, etc.) from visual judgement.

**Why:** for the E2-S tail serial digits ([[model-making]] project,
2026-08-20/21), hand-building each digit's curves from scratch (two
different approaches: full parametric redesign, and a targeted hybrid) took
substantial iteration and both were explicitly rejected by the user as "a
poor match, worse than earlier attempts." Switching to rendering the actual
`usaaf-serial-stencil.ttf` font file (already installed in the project,
just scaled/spaced to match the measured calibration) produced a
near-perfect match on the first attempt. Hand-tracing curves by eye is
unreliable even with careful reference-image comparison at every step;
fonts encode correct, designed proportions directly.

**How to apply:** before reaching for spline/arc-based hand-reconstruction
of curved lettering, ask/check whether a font matching the style is
available (in this project: `fonts/*.ttf`) and try rendering from it first,
matching size/spacing to the independently-measured calibration. Reserve
hand-built geometry for shapes that are genuinely custom (no font matches)
or are simple enough to get right in one or two iterations (e.g. the E2-S
fuselage code's straight-chamfer letters, which worked fine hand-built).
Also: when parsing font glyph path data, always handle multiple subpaths
per glyph (M...Z M...Z...) - stencil-style and hollow-counter glyphs (3, 9,
6, 8, 0, etc.) are frequently multiple disconnected pieces, and flattening
them into one continuous polygon draws a spurious line across the shape.
