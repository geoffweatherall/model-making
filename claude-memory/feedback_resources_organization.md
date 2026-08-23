---
name: feedback-resources-organization
description: "model-masks resources/ folder layout: one subfolder per decal/marking, and the -for-cutting suffix naming convention for SVGs meant to be cut"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2f1e65a0-4cf1-4bda-a283-bf67bb525b2a
  modified: 2026-08-22T23:43:34.473Z
---

In each project's `resources/` folder (e.g.
`masks/projects/bottisham-four/E2-S/resources/`), organize files into one
subfolder per decal/marking rather than a flat list or a separate top-level
`svg/` folder. As of 2026-08-23 the subfolders in the E2-S example are:
`nose/`, `walkway/`, `E2-S/`, `tail-serial/` — named after the marking they
belong to, not the file type. Each subfolder holds everything for that
marking together: the source scan/reference image, the preview/comparison
PNG, and the cutting SVG(s). Loose top-level files that aren't specific to
one marking (e.g. `SCALE.md`) and unrelated asset dirs (e.g.
`imodeler-build-photos/`) stay at the top level.

**Naming convention — SVGs meant to be cut get a `-for-cutting` suffix**
(e.g. `decal-nose-mask-outline-for-cutting.svg`,
`tail-serial-413926-font-for-cutting.svg`). This distinguishes the actual
cut file from preview/comparison PNGs and from any intermediate/working
SVGs in the same folder. Style-wise, cutting SVGs built in this project use
`fill="none" stroke="#000000" stroke-width="0.1"` (see
[[feedback_comparison_images_show_dimensions]] for the matching preview-image
conventions) — some older files predating this convention (e.g.
`e2-regularized-for-cutting.svg`, `s-regularized-for-cutting.svg`,
`tail-serial-413926-font-for-cutting.svg`) still use solid `fill="#000000"`
instead; that still cuts fine (Silhouette Studio reads the path geometry
regardless of fill) but is inconsistent — worth normalizing to stroke-only
next time those files are touched, rather than a dedicated cleanup pass.

**Why:** user asked (2026-08-23) to reorganize what had become a flat
`resources/` folder into per-marking subfolders, and separately pointed out
that a legacy `svg/` folder held files that belonged in the new structure
too — asked explicitly to remember the `-for-cutting` naming convention for
both that move and all future cutting-SVG work in this project.

**How to apply:** when adding a new decal/marking to a project, create (or
reuse) a subfolder named after the marking under `resources/`, put the
source scan + preview + cutting SVG(s) there together, and give any SVG
intended for the cutter a `-for-cutting` suffix — never leave a bare
`something.svg` ambiguous between "cut file" and "working/intermediate
file."
