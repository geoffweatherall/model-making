#!/usr/bin/env python3
"""Assemble the combined Silhouette cut sheet for the Bottisham Four E2-S
project: one SVG containing every mask/marking for this aircraft, laid out
with gaps between items so they're easy to select individually in Silhouette
Studio. Re-run this after changing any ITEM below (sizes, gaps, which source
files are included) rather than hand-editing the generated SVG.

Output: masks/projects/bottisham-four/E2-S/cut-sheet-for-cutting.svg

Items on the sheet (edit the constants below to tweak):
  - walkway guide (left; mirror it in Silhouette Studio for the right one)
  - nose mask
  - E2-S serial (E2 + S, baseline-aligned with a small gap between them)
  - two "stars and bars" roundels at different widths
  - two masking rings (draw a strip of tape around a small round item)
  - one tail serial number

All source SVGs are expected to already be real-world mm size and to use
the project's cutting convention: fill="none" stroke="#000000"
stroke-width="0.1" (see model-masks/CLAUDE.md and the
feedback-resources-organization / feedback-comparison-images-show-dimensions
/ feedback-insignia-cutline-method memory notes for the conventions this
script follows).
"""
import re

REPO = "/home/geoff/Projects/model-masks-workspace/model-masks"
BASE = f"{REPO}/masks/projects/bottisham-four/E2-S/resources"
ROUNDEL_MASTER = (f"{REPO}/masks/common/insignia/us-roundel-b-1943-1947/"
                   "us-roundel-b-1943-1947-for-cutting.svg")
OUT_PATH = f"{REPO}/masks/projects/bottisham-four/E2-S/cut-sheet-for-cutting.svg"

# ---------------------------------------------------------------------------
# Tweakable parameters
# ---------------------------------------------------------------------------
GAP = 6.0        # mm between items, both directions - keep generous enough
                 # to click individual items apart in Silhouette Studio
MARGIN = 4.0     # mm border around the whole sheet
TARGET_STROKE_MM = 0.1   # real-world cut line thickness for scaled items

LETTER_GAP = 4.0          # mm gap between the "E2" block and the "S"
ROUNDEL_WIDTHS_MM = [38.6, 32.6]  # bar-to-bar width of each roundel copy wanted
RING_INNER_DIAMETERS_MM = [1.2, 1.3]       # one ring per listed inner diameter
RING_BAND_THICKNESS_MM = 2.0               # width of the tape/ring band

CUT_STYLE = 'fill="none" stroke="#000000" stroke-width="0.1"'

# ---------------------------------------------------------------------------
# Load source SVGs
# ---------------------------------------------------------------------------
def read(path):
    with open(path) as f:
        return f.read()

def get_paths(svg_text):
    return re.findall(r'<path[^>]*/?>', svg_text)

def get_wh(svg_text):
    w = float(re.search(r'width="([\d.]+)mm"', svg_text).group(1))
    h = float(re.search(r'height="([\d.]+)mm"', svg_text).group(1))
    vb = [float(x) for x in re.search(r'viewBox="([\-\d. ]+)"', svg_text).group(1).split()]
    return w, h, vb  # vb = [minx, miny, width, height]

def strip_fill_add_cutstyle(path_tag):
    """Normalize any path's fill/stroke attrs to the project cut-line style."""
    tag = re.sub(r'\s*(fill|stroke|stroke-width)="[^"]*"', '', path_tag)
    tag = re.sub(r'/?>$', '', tag).rstrip()
    return tag + f' {CUT_STYLE}/>'

walkway_svg = read(f"{BASE}/walkway/decal-walkway-guide-left-outline-for-cutting.svg")
nose_svg = read(f"{BASE}/nose/decal-nose-mask-outline-for-cutting.svg")
e2_svg = read(f"{BASE}/E2-S/e2-regularized-for-cutting.svg")
s_svg = read(f"{BASE}/E2-S/s-regularized-for-cutting.svg")
tail_svg = read(f"{BASE}/tail-serial/tail-serial-413926-font-for-cutting.svg")
roundel_svg = read(ROUNDEL_MASTER)

walkway_paths = [strip_fill_add_cutstyle(p) for p in get_paths(walkway_svg)]
nose_paths = [strip_fill_add_cutstyle(p) for p in get_paths(nose_svg)]
e2_paths = [strip_fill_add_cutstyle(p) for p in get_paths(e2_svg)]
s_paths = [strip_fill_add_cutstyle(p) for p in get_paths(s_svg)]
tail_paths = [strip_fill_add_cutstyle(p) for p in get_paths(tail_svg)]
roundel_d = re.search(r'<path[^>]*\sd="([^"]*)"', roundel_svg).group(1)

WALKWAY_W, WALKWAY_H, _ = get_wh(walkway_svg)
NOSE_W, NOSE_H, _ = get_wh(nose_svg)
E2_W, E2_H, _ = get_wh(e2_svg)
S_W, S_H, _ = get_wh(s_svg)
TAIL_W, TAIL_H, tail_vb = get_wh(tail_svg)
TAIL_OX, TAIL_OY = tail_vb[0], tail_vb[1]   # tail-serial's viewBox has a small negative origin

# Baseline (bottom edge, in each file's own coords) of the E2 and S glyphs -
# their source files disagree by ~0.2mm; align on E2's baseline so the two
# pieces read as one line of text. Re-check these if the source SVGs change.
E2_BASELINE = 13.077
S_BASELINE = 12.877
S_DY = E2_BASELINE - S_BASELINE

serial_w = E2_W + LETTER_GAP + S_W
serial_h = E2_H

# roundel master's own coordinate system: 1270x700, bar width 1245 units -
# "38.6mm wide" etc. means that bar-to-bar width, not the full canvas width
BAR_W_UNITS = 1245.0
CANVAS_W_UNITS = 1270.0
CANVAS_H_UNITS = 700.0

def roundel_size(width_mm):
    s = width_mm / BAR_W_UNITS
    return CANVAS_W_UNITS * s, CANVAS_H_UNITS * s, s

def ring_size(inner_d_mm, band_t_mm):
    r_in = inner_d_mm / 2.0
    r_out = r_in + band_t_mm
    return r_out * 2, r_out, r_in

# ---------------------------------------------------------------------------
# Build the item list (grouped into rows; each row lays out left-to-right)
# ---------------------------------------------------------------------------
row1 = [("walkway", walkway_paths, WALKWAY_W, WALKWAY_H, "path"),
        ("nose", nose_paths, NOSE_W, NOSE_H, "path"),
        ("e2-s-serial", None, serial_w, serial_h, "serial")]

row2 = []
for w_mm in ROUNDEL_WIDTHS_MM:
    w, h, _ = roundel_size(w_mm)
    row2.append((f"stars-and-bars-{w_mm:g}mm", None, w, h, "roundel", w_mm))

row3 = []
for d_mm in RING_INNER_DIAMETERS_MM:
    od, r_out, r_in = ring_size(d_mm, RING_BAND_THICKNESS_MM)
    row3.append((f"ring-inner-{d_mm:g}mm", None, od, od, "ring", d_mm, r_out, r_in))
row3.append(("tail-serial-413926", tail_paths, TAIL_W, TAIL_H, "tail"))

# ---------------------------------------------------------------------------
# Layout: flow each row left-to-right with GAP between items, rows stacked
# top-to-bottom with GAP between rows, MARGIN around the whole sheet
# ---------------------------------------------------------------------------
def row_layout(items, y0):
    x = MARGIN
    placed = []
    max_h = 0
    for it in items:
        w, h = it[2], it[3]
        placed.append((it, x, y0))
        x += w + GAP
        max_h = max(max_h, h)
    row_w = x - GAP + MARGIN
    return placed, max_h, row_w

y = MARGIN
placed1, h1, w1 = row_layout(row1, y); y += h1 + GAP
placed2, h2, w2 = row_layout(row2, y); y += h2 + GAP
placed3, h3, w3 = row_layout(row3, y); y += h3 + MARGIN

total_w = max(w1, w2, w3)
total_h = y

# ---------------------------------------------------------------------------
# Emit SVG
# ---------------------------------------------------------------------------
svg_body = []

def emit_item(it, tx, ty):
    kind = it[4]
    if kind == "path":
        name, paths = it[0], it[1]
        svg_body.append(f'<g transform="translate({tx:.4f},{ty:.4f})" id="{name}">')
        svg_body.extend(paths)
        svg_body.append('</g>')
    elif kind == "serial":
        svg_body.append('<g id="e2-s-serial">')
        svg_body.append(f'<g transform="translate({tx:.4f},{ty:.4f})" id="e2">')
        svg_body.extend(e2_paths)
        svg_body.append('</g>')
        sx, sy = tx + E2_W + LETTER_GAP, ty + S_DY
        svg_body.append(f'<g transform="translate({sx:.4f},{sy:.4f})" id="s">')
        svg_body.extend(s_paths)
        svg_body.append('</g>')
        svg_body.append('</g>')
    elif kind == "roundel":
        name, width_mm = it[0], it[5]
        s = width_mm / BAR_W_UNITS
        local_stroke = TARGET_STROKE_MM / s
        svg_body.append(f'<g transform="translate({tx:.4f},{ty:.4f}) scale({s:.6f})" id="{name}">')
        svg_body.append(f'<path fill="none" stroke="#000000" stroke-width="{local_stroke:.4f}" d="{roundel_d}"/>')
        svg_body.append('</g>')
    elif kind == "ring":
        name, r_out, r_in = it[0], it[6], it[7]
        cx, cy = tx + r_out, ty + r_out
        svg_body.append(f'<g id="{name}">')
        svg_body.append(f'<circle cx="{cx:.4f}" cy="{cy:.4f}" r="{r_out:.4f}" {CUT_STYLE}/>')
        svg_body.append(f'<circle cx="{cx:.4f}" cy="{cy:.4f}" r="{r_in:.4f}" {CUT_STYLE}/>')
        svg_body.append('</g>')
    elif kind == "tail":
        name = it[0]
        gx, gy = tx - TAIL_OX, ty - TAIL_OY
        svg_body.append(f'<g transform="translate({gx:.4f},{gy:.4f})" id="{name}">')
        svg_body.extend(tail_paths)
        svg_body.append('</g>')

for placed in (placed1, placed2, placed3):
    for it, tx, ty in placed:
        emit_item(it, tx, ty)
        print(f"  {it[0]}: {it[2]:.3f} x {it[3]:.3f} mm  at ({tx:.2f},{ty:.2f})")

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_w:.4f}mm" height="{total_h:.4f}mm" '
       f'viewBox="0 0 {total_w:.4f} {total_h:.4f}">\n' + "\n".join(svg_body) + "\n</svg>\n")

with open(OUT_PATH, "w") as f:
    f.write(svg)
print(f"\nwrote {OUT_PATH}  ({total_w:.2f} x {total_h:.2f} mm)")
