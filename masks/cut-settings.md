# Cutter Settings Reference

Silhouette Portrait 3, OEM AutoBlade. Settings are Silhouette Studio "Cut
Settings" values: blade depth, force, speed, passes.

## Key points

**Use Oramask 810 for anything with fine detail. Use Tamiya 87130 where you
need conformability.**

- **Oramask 810** — polymer stencil film, made for cut-and-spray stencilling.
  Non-fibrous, so it shears to a clean edge and a small piece stays intact
  and dimensionally stable. Holds detail at sizes where paper falls apart.
  Stiffer than kabuki paper, so less willing to conform over compound curves.
- **Tamiya 87130 "Masking Sticker Sheet"** — kabuki (washi) paper with a
  low-tack adhesive on a release liner. Conforms beautifully over curves and
  releases cleanly at paint edges, which is what it's for. But it's fibrous
  and tears rather than shears, and its low tack means hold scales with
  contact area — so small pieces both lift and tear. Fine for large, simple
  shapes; unusable for small lettering (see below).
- **Don't carry settings between the two materials** — they land in quite
  different places (87130 wants more depth and less force than 810).
- **Stencil fonts are the right choice for lettering.** The runners that tie
  each piece to the surrounding sheet are what keep everything in place
  during the cut — no isolated islands to lift.
- **Clean the bottom of the AutoBlade housing before fine-detail cuts.** See
  the note at the end; it silently ruins depth.

## Settings

| Material | Item type | Depth | Force | Speed | Passes | Status |
|---|---|---|---|---|---|---|
| Oramask 810 | All — large and small | 1 | 10 | 1 | 1 | **Confirmed.** Works very well, no lifting, including small stencil-font lettering |
| Tamiya 87130 (kabuki sheet) | Large/simple (squadron codes, roundels, rings) | 2 | 6 | 1 | 1 | Confirmed. Cuts slightly into the backing liner; harmless at this size |
| Tamiya 87130 (kabuki sheet) | Small/fine detail | — | — | — | — | **Don't.** No working setting exists — use Oramask 810 |

Worth a Test Cut on scrap before a full sheet regardless; blade wear and
material batch vary.

## Cut log

**Oramask 810 — depth=1, force=10, speed=1, passes=1** (2026-09-12). Clean
cut, no lifting, small stencil-font tail serial included. Adopted as the
setting for all Oramask work, large and small.

**Tamiya 87130 — depth=2, force=6, speed=1, passes=1.** Correct for large
elements: clean edge, no standing fibers, pieces stay put.

**Tamiya 87130, small lettering — failed across the whole usable force
range** (force 3, 4 and 6 at depth 1 and 2, 2026-09-12). Two failure modes
that cause each other:

- *Too little force* scored the surface without severing, leaving standing
  fibers. A partly-severed piece is still held by those fibers, so the
  pivoting blade plucks and tears it upward instead of cutting past it —
  under-cutting causes lifting rather than preventing it.
- *Enough force to sever* still lifted small pieces immediately, with a clean
  blade, at the settings that cut large elements perfectly. The smallest
  piece (a "1") failed first — least contact area, least hold.

No cell in the range works, so it isn't a settings problem. It's the
material: paper tears where film shears, and low-tack adhesive can't hold a
piece that small.

## AutoBlade housing debris

The blade housing rides *on* the material and that contact sets how far the
tip actually reaches. Anything stuck underneath acts as a shim, reducing
effective depth — and a lifted mask piece arrives adhesive-side-up, so it
sticks readily.

This closes a loop that degrades *within a single cut*: a piece lifts →
sticks to the housing → depth drops → later cuts don't sever → partly-cut
pieces tear up → more debris. Observed directly as "first digits clean, rest
too shallow", and it makes depth behave unrepeatably between tests.

Inspect and clean the housing bottom before every fine-detail cut, and again
partway through a long one.
