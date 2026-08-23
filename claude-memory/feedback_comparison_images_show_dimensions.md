---
name: feedback-comparison-images-show-dimensions
description: "Conventions for scan-vs-SVG preview/comparison images in model-masks: dimension lines, numbered vertices, legend placement, before/after diffing"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ee072010-f7b7-48e5-a550-d7cdb0e4bf76
  modified: 2026-08-22T23:39:18.742Z
---

When producing a preview/comparison image overlaying a traced/generated SVG
outline on the reference photo/scan (e.g. [[model-masks]] decal tracing
work), apply all of the following:

1. **Dimension line for the calibration measurement.** Show the actual
   real-world measurement the user gave (e.g. a measured height/width in mm)
   as a dimension line/callout — end-ticks/arrowheads, dashed extension
   lines from the two measured points, label text (e.g. "10.6 mm
   (measured)") — placed in a dedicated canvas margin outside the artwork,
   not overlapping it.
2. **Number every vertex** on the traced outline with a small numbered
   circle marker (leader line from the actual point to the number bubble if
   space is tight), so the user can reference "vertex 4" etc. in feedback
   without needing screenshots or coordinates.
3. **Legend/key below the dimension line and its label**, not top-left
   overlapping the image — user explicitly corrected this placement
   (2026-08-23) after an early version put the key top-left over the
   artwork. One line per vertex number explaining what it is.
4. **When revising a shape after feedback, show old vs new** in the same
   image: previous outline as a gray dashed line, new/corrected outline as
   a bold solid green line, so the change is visible at a glance rather than
   requiring a side-by-side diff.
5. Add extra canvas margin (top/bottom/left/right as needed) whenever the
   corrected shape or its annotations extend beyond the original photo
   bounds (e.g. after adding overlap/extension margins) — labels and
   markers must never get clipped at the canvas edge.

**Why:** user explicitly said (2026-08-20, during E2-S squadron-code
tracing work) to "store for future work" that comparison images should show
given dimensions this way. During later work on the decal-nose-mask outline
(2026-08-23), the user asked for numbered vertices (to describe fitting
problems precisely — see [[feedback_pedantic_naming]] for the same
precision instinct applied to word choice) and then corrected the legend's
placement to below the dimension label rather than top-left. A plain
undimensioned/unnumbered comparison isn't needed once the annotated version
exists.

**How to apply:** for future letter/marking/shape tracing work in this
project, go straight to producing a preview image with all of the above —
numbered vertices + legend below the dimension callout — rather than a bare
outline overlay, and re-show it (with old-vs-new diffing) after every
correction round before moving on.
