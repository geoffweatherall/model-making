# US national aircraft insignia — "star and bars", blue outline (Aug 1943 – Jan 1947)

The "star and bars" national insignia carried by US military aircraft from
**14 August 1943 to 14 January 1947** — the version seen on [the Bottisham
Four](../../../../projects/bottisham-four/) and all other US military aircraft of
the period. US-specific: other Allied air forces (RAF, etc.) used their own
national markings, not this one.

## Two versions, easy to mix up

Defined by **Army-Navy Aeronautical Specification AN-I-9**, amended twice:

- **AN-I-9a** (29 June 1943) — white bars added either side of the star
  circle, outlined in **insignia red**. Short-lived — about six weeks.
- **AN-I-9b** (14 August 1943) — the red outline replaced with **insignia
  blue**. This is the version in this folder, worn until 14 January 1947,
  when Amendment 2 added a red stripe bisecting each bar (a distinct,
  later variant — not this one, and not correct for WWII-era aircraft).

## Not branch-specific

The "AN" in the spec name stands for **Army-Navy** — this was a joint
standard, not a USAAF-only marking. Army Air Forces, Navy, and Marine Corps
aircraft all carried the same insignia during this period. (The source SVG
below even cites the Navy F6F Hellcat and USMC F4U Corsair as reference
aircraft for its proportions.)

## Files

`us-roundel-b-1943-1947-wikimedia.svg` — unmodified download from Wikimedia
Commons: [File:Roundel of the United States
(1943–1947).svg](https://commons.wikimedia.org/wiki/File:Roundel_of_the_United_States_(1943%E2%80%931947).svg).
Public domain. Named with the `-wikimedia` suffix to distinguish it from a
second SVG (different source) expected to join this folder later.

Careful: Wikimedia Commons also hosts a plain **"Roundel of the USAF.svg"**
— that one is the **post-1947** variant (red stripe, Amendment 2) and is
the wrong file for WWII work. Only the one in this folder, with the
1943–1947 date range in its title, is correct for this period.

`us-roundel-b-1943-1947-for-cutting.svg` — derived from the file above for
single-sheet paint masking: cut this once, then peel individual regions to
spray each color in turn, leaving the rest of the mask in place — rather
than cutting a separate mask per color layer. It's a single `<path>` whose
lines are *only* the overall outer edge (background/navy) and actual color
changes (navy/white) — computed as exact boolean geometry (Shapely) on the
final flattened artwork: `(outer_disk ∪ outer_bar) − (white_bar − inner_disk)
− star`, giving one outer boundary plus three holes (the two white
bar-remainder pieces either side of the disk, and the star). Deliberately
**not** built by just keeping each of the master file's 5 overlapping shapes'
raw outlines — that leaves the bar/disk edges cutting straight through the
middle of the star and other single-color regions, which is wrong for this
technique. No enclosing margin rectangle baked in (cut lines should only be
color changes and the outer edge — add any margin you want as a separate
rectangle at use time). Has no inherent real-world size (same as the master
file) — when embedding at a target width, scale by `target_width_mm / 1245`
(1245 = the bar width in source units, the usual "how wide is this
insignia" reference dimension) and recompute `stroke-width` for that scale
so the cut line ends up a consistent real-world thickness (this project
uses ~0.1mm).
