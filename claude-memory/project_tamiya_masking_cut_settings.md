---
name: project-tamiya-masking-cut-settings
description: "Confirmed Silhouette Portrait 3 / AutoBlade cut settings for Tamiya yellow masking sheet"
metadata:
  type: project
---

For cutting Tamiya (yellow) masking sheet on a Silhouette Portrait 3 with the
standard AutoBlade, use: **blade depth = 2 (max), force = 3, speed = 1** (Silhouette
Studio Cut Settings). Applied uniformly across the whole cut sheet — not
split into different settings per object/group.

**Why:** user was seeing the cutter pull up/lift small fine-detail cut
pieces (e.g. the tail serial number lettering) while larger simple shapes
(roundels, rings) cut fine. Prior to landing on this, we'd discussed a
lower physical blade depth (over-extension was suspected as a cause of the
lifting) and running the whole job at slow speed (no real quality downside
since force, not speed, mainly governs whether a shape fully cuts through).
User confirmed depth=2 (max)/force=3/speed=1 works well via test cut on the
actual sheet (2026-08-23, first real cut of
`masks/projects/bottisham-four/E2-S/cut-sheet-for-cutting.svg`).

**How to apply:** default to depth=2 (max)/force=3/speed=1 as the starting point
for any future Tamiya masking-sheet cut on this hardware (Portrait 3 +
AutoBlade), rather than re-deriving settings from scratch. Still worth a
quick Test Cut on scrap before a full sheet — this is a known-good setting
for this material/blade combo, not a guaranteed-universal spec (blade wear,
material batch variation, etc. could shift it slightly over time).
