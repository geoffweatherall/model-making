#!/usr/bin/env python3
"""Build a Silhouette-ready cut sheet of two families of test/masking rings,
laid out in same-size groups (adjacent copies) with gaps for easy selection
in Silhouette Studio. Re-run after changing any constant below rather than
hand-editing the generated SVG.

Output: masks/common/ring-test-sheet/ring-test-sheet-for-cutting.svg

Ring families:
  Set 1 - constant 1.0mm radial coverage band, inner diameter stepped
          0.1mm across 1.9mm +/- 0.2mm (5 sizes), 3 copies of each.
  Set 2 - constant 2.0mm inner hole diameter, outer diameter stepped
          0.1mm across 7.2mm +/- 0.2mm (5 sizes), 2 copies of each.
"""
import os

REPO = "/home/geoff/projects/model-making-workspace/model-making"
OUT_DIR = f"{REPO}/masks/common/ring-test-sheet"
OUT_PATH = f"{OUT_DIR}/ring-test-sheet-for-cutting.svg"

# ---------------------------------------------------------------------------
# Tweakable parameters
# ---------------------------------------------------------------------------
SET1_BAND_THICKNESS_MM = 1.0                 # radial wall width, constant
                                              # (1mm coverage beyond the 1.9mm circle)
SET1_INNER_DIAMETERS_MM = [1.7, 1.8, 1.9, 2.0, 2.1]  # 1.9mm +/- 0.2mm, 5 steps
SET1_COPIES = 3

SET2_INNER_DIAMETER_MM = 2.0                 # constant hole, all sizes
SET2_OUTER_CENTER_MM = 7.2
SET2_OUTER_RANGE_MM = 0.2                    # +/- range
SET2_STEP_MM = 0.1
SET2_COPIES = 2
_n = round(SET2_OUTER_RANGE_MM / SET2_STEP_MM)
SET2_OUTER_DIAMETERS_MM = [
    round(SET2_OUTER_CENTER_MM - SET2_OUTER_RANGE_MM + SET2_STEP_MM * i, 1)
    for i in range(2 * _n + 1)
]

GAP_WITHIN_GROUP_MM = 0.4     # edge-to-edge gap between same-size copies
GAP_BETWEEN_GROUPS_MM = 1.0   # gap between different-size groups, same row or next row
MARGIN_MM = 1.5
TARGET_WIDTH_MM = 40.0        # requested 4cm sheet width; height grows if needed

CUT_STYLE = 'fill="none" stroke="#000000" stroke-width="0.1"'

# ---------------------------------------------------------------------------
# Build the size-group list
# ---------------------------------------------------------------------------
groups = []
for d in SET1_INNER_DIAMETERS_MM:
    outer = round(d + 2 * SET1_BAND_THICKNESS_MM, 2)
    groups.append({"inner": d, "outer": outer, "set": 1, "copies": SET1_COPIES,
                   "label": f"S1 ID{d}mm/OD{outer}mm"})

for od in SET2_OUTER_DIAMETERS_MM:
    groups.append({"inner": SET2_INNER_DIAMETER_MM, "outer": od, "set": 2,
                   "copies": SET2_COPIES,
                   "label": f"S2 OD{od}mm/ID{SET2_INNER_DIAMETER_MM}mm"})

# ---------------------------------------------------------------------------
# Shelf-pack groups (First-Fit Decreasing Height): process groups largest-
# outer-diameter first, fill each row left-to-right until the next group
# wouldn't fit within TARGET_WIDTH_MM, then start a new (shorter) row. Groups
# from both sets can share a row - only same-size copies are kept adjacent,
# which packs tightest for a strict-fit check.
# ---------------------------------------------------------------------------
def group_width(g):
    n = g["copies"]
    return n * g["outer"] + (n - 1) * GAP_WITHIN_GROUP_MM

usable_width = TARGET_WIDTH_MM - 2 * MARGIN_MM
sorted_groups = sorted(groups, key=lambda g: g["outer"], reverse=True)

rows = []       # list of lists of groups
row_widths = [] # content width actually used per row
for g in sorted_groups:
    gw = group_width(g)
    if rows:
        cur_w = row_widths[-1] + GAP_BETWEEN_GROUPS_MM + gw
        if cur_w <= usable_width:
            rows[-1].append(g)
            row_widths[-1] = cur_w
            continue
    rows.append([g])
    row_widths.append(gw)

y = MARGIN_MM
max_right_edge = 0.0
circles = []  # (cx, cy, r_outer, r_inner, label)
for row in rows:
    row_h = max(g["outer"] for g in row)
    x = MARGIN_MM
    for g in row:
        gw = group_width(g)
        cy = y + g["outer"] / 2
        for i in range(g["copies"]):
            cx = x + g["outer"] / 2 + i * (g["outer"] + GAP_WITHIN_GROUP_MM)
            circles.append((cx, cy, g["outer"] / 2, g["inner"] / 2, g["label"]))
        x += gw + GAP_BETWEEN_GROUPS_MM
    max_right_edge = max(max_right_edge, x - GAP_BETWEEN_GROUPS_MM)
    y += row_h + GAP_BETWEEN_GROUPS_MM

total_width = round(max_right_edge + MARGIN_MM, 2)
total_height = round(y - GAP_BETWEEN_GROUPS_MM + MARGIN_MM, 2)

# ---------------------------------------------------------------------------
# Emit SVG: two concentric circles (outer, inner) per ring, cut-line style.
# ---------------------------------------------------------------------------
lines = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}mm" '
    f'height="{total_height}mm" viewBox="0 0 {total_width} {total_height}">'
]
for cx, cy, r_outer, r_inner, label in circles:
    lines.append(f'<circle cx="{cx:.3f}" cy="{cy:.3f}" r="{r_outer:.3f}" {CUT_STYLE}/>')
    lines.append(f'<circle cx="{cx:.3f}" cy="{cy:.3f}" r="{r_inner:.3f}" {CUT_STYLE}/>')
lines.append('</svg>')

os.makedirs(OUT_DIR, exist_ok=True)
with open(OUT_PATH, "w") as f:
    f.write("\n".join(lines) + "\n")

n_set1 = len(SET1_INNER_DIAMETERS_MM)
n_set2 = len(SET2_OUTER_DIAMETERS_MM)
print(f"Set 1: {n_set1} sizes x {SET1_COPIES} copies = {n_set1*SET1_COPIES} rings "
      f"(inner {SET1_INNER_DIAMETERS_MM[0]}-{SET1_INNER_DIAMETERS_MM[-1]}mm, "
      f"band {SET1_BAND_THICKNESS_MM}mm, outer "
      f"{SET1_INNER_DIAMETERS_MM[0]+2*SET1_BAND_THICKNESS_MM:.1f}-"
      f"{SET1_INNER_DIAMETERS_MM[-1]+2*SET1_BAND_THICKNESS_MM:.1f}mm)")
print(f"Set 2: {n_set2} sizes x {SET2_COPIES} copies = {n_set2*SET2_COPIES} rings "
      f"(outer {SET2_OUTER_DIAMETERS_MM[0]}-{SET2_OUTER_DIAMETERS_MM[-1]}mm, "
      f"inner {SET2_INNER_DIAMETER_MM}mm constant)")
print(f"Total rings: {n_set1*SET1_COPIES + n_set2*SET2_COPIES}")
print(f"Sheet size: {total_width}mm x {total_height}mm "
      f"(requested target: 40mm x 30mm)")
print(f"Wrote {OUT_PATH}")
