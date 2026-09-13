# CLAUDE.md

Notes for Claude working in this repo. Content here is at Claude's discretion —
project context, conventions, and decisions worth remembering across sessions
and across machines (this repo is git-synced between two of the user's machines).

## Documentation split

- **CLAUDE.md** (this file): Claude-maintained. Working notes, conventions,
  decisions, and context that help future sessions pick up work correctly.
  Not primarily written for human reading, though humans can read it.
- **README.md** and other topic-specific markdown files: human-readable
  project documentation, written for people. Claude should read these for
  context too, but they are not where Claude records its own notes.

## Project

Scale-model building reference and tooling generally. Currently centered on
producing SVG files for a Silhouette Portrait 3 cutter, used to cut masks for
painting scale models (see `masks/`), with other model-making project types
expected under `projects/` over time.

## Why Claude Code (not browser Claude)

Working in Claude Code rather than claude.ai's browser sandbox specifically so
that locally-installed software (e.g. Inkscape for path/boolean-ops/font-to-path
work) and system fonts are available to Claude via the Bash tool. Browser
Claude's sandbox is a fixed pre-built container — installed packages/fonts
don't persist or become available to it. Claude Code shells out directly on
the user's real machine, so anything installed there (apt packages, fonts via
`fc-cache`) is usable immediately.

## Environment gotchas (both machines are Ubuntu, similar versions)

- **No root access for Claude.** `sudo` requires interactive password auth,
  which Claude's Bash tool can't provide. Anything needing `sudo apt install`
  must be installed manually by the user — see README's software table.
  Don't keep re-attempting sudo; just tell the user the exact command to
  run. **Whenever new software gets installed for this project (by either
  of us), add/update its row in README's software table** — that table is
  the source of truth for what a fresh machine needs, and Claude should
  proactively suggest tools that would help (better Python, useful CLI
  utilities, etc.) rather than waiting to be asked.
- **Inkscape** (installed 2026-08-20, v1.4.3) works both headful (normal GUI,
  picks up fonts via the `~/.local/share/fonts/model-fonts-proprietary` (and,
  once it exists, `model-making`) symlink(s) — see Fonts section) and
  headless via CLI (`inkscape in.svg --export-type=png
  --export-filename=out.png`, or `--actions=...` for scripted path ops) —
  confirmed working even with `DISPLAY`/`WAYLAND_DISPLAY` unset, no Xvfb
  needed.
- **System Python has no `ensurepip`/`pip3`, and is a PEP 668
  externally-managed-environment** — `python3 -m venv` reports failure and
  `pip install --user` is refused. Workaround (no root needed): create the
  venv anyway (the directory structure is created even though the command
  reports an ensurepip error), then bootstrap pip into it manually via
  `get-pip.py`. This is encoded in `scripts/setup-venv.sh` — use that rather
  than rediscovering the trick.
- Project Python deps go in `requirements.txt`, installed into `.venv`
  (gitignored, per-machine, recreate via the setup script rather than syncing).
- The Windows partition is dual-boot on this machine and mounts automatically
  at `/run/media/geoff/9A8832FE8832D909` when booted into Linux (NTFS,
  read-write). Useful for pulling reference material/fonts across.

## Fonts (split across two repos — read this before adding or looking for any font)

**model-making will go public; a sibling repo, `model-fonts`, stays private.**
Font files are split between them by license status, so no copyrighted font
software ends up in the public repo:

- **`fonts-open/`** (this repo) — fonts with a clearly open/permissive
  license (public domain, SIL OFL, explicit "free for any use including
  redistribution", etc.). Safe to be public. **Doesn't exist yet** — every
  font sourced so far turned out not to qualify (see below), so there's
  nothing to put in it. Create it (`mkdir fonts-open`) the first time a
  genuinely open-licensed font is actually added.
- **`../model-fonts/fonts-proprietary/`** (sibling repo, private, expected
  to already be cloned alongside this one at
  `/home/geoff/projects/model-making-workspace/model-fonts`) — everything
  else: shareware, "personal use only", "all rights reserved" with no
  redistribution grant, or no license info found at all. **When unsure,
  it goes here, not in `fonts-open/`** — that's a deliberate standing rule
  from the user, not a one-off judgment call.

**When looking for a font to use, check both directories.** When adding a
new font, check its license (embedded `name` table via fontTools — IDs 0
Copyright, 13 License, 14 LicenseURL are usually the most direct — plus a
web search if those are empty/ambiguous) and place it accordingly. See
`model-fonts/README.md` for the full rationale and a per-font license table.

Filenames are normalized to lowercase-hyphenated, derived from each font's
internal `family` metadata (via `fc-query`), not the original filename —
those varied wildly in case/spacing/relevance. Non-ASCII characters
transliterated (ü → ue). File permissions `644` (data, no execute bit).

**Resolved (2026-08-20): AmarilloUSAF font search.** The font wasn't
missing — it was in the user's Windows-partition `for_claude` folder all
along, saved under the unrelated filename `amarurgt.ttf`. Confirmed via
`fc-query` (family/fullname/postscriptname all "AmarilloUSAF") and by
diffing extracted glyph outlines byte-for-byte against a prior
browser-Claude session's pre-extracted `AmarilloUSAF_glyph_data.json`
(found in `Downloads/` on the Windows partition, now redundant). Turned out
to be registered shareware (see license table in `model-fonts/README.md`),
so it now lives in `model-fonts/fonts-proprietary/amarillo-usaf.ttf`, not
here.

**Installing fonts for local use (per machine, not git-synced):** registering
fonts with the OS font system is a per-machine step outside both repos, and
must be redone on each machine after a fresh clone/pull. Run, once
`model-fonts` is cloned as a sibling of this repo:

```
mkdir -p ~/.local/share/fonts
ln -sfn "$(pwd)/../model-fonts/fonts-proprietary" ~/.local/share/fonts/model-fonts-proprietary   # run from this repo's root
fc-cache -f ~/.local/share/fonts
```

(Add `ln -sfn "$(pwd)/fonts-open" ~/.local/share/fonts/model-making` too, once
`fonts-open/` actually exists and has something in it.)

Verify with `fc-list | grep -iE "amarillo|blockschrift|raf_ww2|universj|usaaf|usn_stencil"`
— should list all 8 (all currently live in the proprietary/private set).
No root needed. This makes the fonts visible both to fontconfig-based
headless tooling and to Inkscape's GUI font picker (restart Inkscape if it
was already open) — registering the proprietary fonts locally like this is
fine, since it's a private, per-machine, non-distributed use; it's
committing them into the *public* repo that must be avoided. Symlinking
rather than copying means future additions to either `fonts-open/` or
`fonts-proprietary/` are picked up with just another `fc-cache -f`.

## Bottisham Four / E2-S — cut sheet work (as of 2026-08-23)

Per-project `resources/` folders (e.g.
`projects/bottisham-four/E2-S/resources/`) are organized into one
subfolder per decal/marking (`nose/`, `walkway/`, `E2-S/`, `tail-serial/`),
each holding that marking's source scan, preview PNG, and cutting SVG(s)
together. Loose top-level files not specific to one marking (`SCALE.md`)
and unrelated asset dirs (`imodeler-build-photos/`) stay at the top level.
Any SVG meant to go to the cutter gets a `-for-cutting` suffix, styled
`fill="none" stroke="#000000" stroke-width="0.1"`, to distinguish it from
preview/comparison PNGs and older working files. Full rationale in the
`feedback-resources-organization` and `feedback-comparison-images-show-dimensions`
memory notes (see `claude-memory/` in this repo's root — auto-memory is
git-synced here, see the section below).

**`projects/bottisham-four/E2-S/cut-sheet-for-cutting.svg`** — one
combined Silhouette-ready SVG with every E2-S marking laid out with gaps for
easy selection: walkway guide (left only — mirror the other in Silhouette
Studio), nose mask, E2-S serial, two stars-and-bars roundels (38.6mm and
32.6mm), two masking rings (1.2mm and 1.3mm inner diameter, 2mm tape band),
one tail serial number. Built by **`scripts/build-e2-s-cut-sheet.py`** —
re-run that script after changing anything (item sizes, gaps, which files
are included) rather than hand-editing the generated SVG; the tweakable
constants (`GAP`, `MARGIN`, `ROUNDEL_WIDTHS_MM`,
`RING_INNER_DIAMETERS_MM`, etc.) are at the top of the script.

**Stars-and-bars / national-insignia cutting method**: converting a
color-filled reference insignia (overlapping solid shapes, e.g.
`masks/common/insignia/us-roundel-b-1943-1947/us-roundel-b-1943-1947-wikimedia.svg`)
into cut lines for a single-sheet "cut once, peel each region to spray its
color" paint mask must NOT just strip fill and keep each shape's raw
outline — overlapping shapes leave lines cutting through the middle of
single-color regions (confirmed wrong on this project: bar lines cut
through the star). Instead compute the exact boolean geometry of each final
color region in paint order with Shapely (union/difference), giving one
outer boundary plus holes only where the color actually changes. The
derived `us-roundel-b-1943-1947-for-cutting.svg` lives alongside the
wikimedia master in the same `masks/common/insignia/` folder (documented in
that folder's README) so it's reusable across projects, not rebuilt per cut
sheet. Full method in the `feedback-insignia-cutline-method` memory note.

**Known stale reference**: `scripts/generate-e2-s-svgs.py`'s `OUT_DIR`
points at `projects/bottisham-four/E2-S/svg/`, which no longer exists
after the resources reorganization above — that script would fail if
re-run as-is. Not fixed yet since it wasn't touched this session; update
its `OUT_DIR` (and check `scripts/split-e2-s-svg.py` and
`scripts/trace-tail-serial.py` for the same issue) before relying on it
again.

**Cutting happens on Windows, not here**: Silhouette Studio only runs
booted into Windows on the dual-boot machine (see the Windows-partition
note below) — this Claude Code session only produces/edits the SVGs on the
Ubuntu side. Nothing in this repo drives the cutter directly.

## Claude Code memory syncing across machines (git-backed, 2026-08-23)

Claude Code's auto-memory (preference/feedback notes it saves across
sessions) normally lives at
`~/.claude/projects/-home-geoff-Projects-model-making-workspace/memory/` —
tied to this session's working directory (the `model-making-workspace`
folder, launched one level above this repo), and **local to whichever
machine wrote it**, not git-synced by default. Since the user works from
this same workspace path on two Ubuntu machines that aren't always on
simultaneously (so something like Syncthing doesn't fit well) and already
syncs everything else via this repo's git remote, memory is synced the
same way:

- The actual memory files live in **`claude-memory/`** in this repo (i.e.
  `model-making/claude-memory/`), git-tracked like everything else.
- `~/.claude/projects/-home-geoff-Projects-model-making-workspace/memory`
  is a **symlink** to that folder, not a real directory — so Claude's
  memory tool reads/writes the repo files directly with no extra step.
- **On a new/other machine**, after cloning this repo, recreate the
  symlink (the target directory won't exist yet until Claude Code's
  first run there creates the parent `projects/...` folder — create it
  if needed):
  ```
  mkdir -p ~/.claude/projects/-home-geoff-Projects-model-making-workspace
  rm -rf ~/.claude/projects/-home-geoff-Projects-model-making-workspace/memory   # only if it exists and is a real (non-symlink) dir - check first, don't blindly delete existing memory
  ln -s /home/geoff/Projects/model-making-workspace/model-making/claude-memory \
        ~/.claude/projects/-home-geoff-Projects-model-making-workspace/memory
  ```
- This repo is **public** (see top of this file) — `claude-memory/`
  content goes public with it. Nothing saved there so far is sensitive
  (workflow preferences, not secrets), but keep that in mind before
  saving anything there.
- No automatic committing/pushing of memory changes — same "ask before
  committing, always ask before pushing" rules apply as for the rest of
  this repo (see the `feedback-ask-before-push` memory note itself). The
  user asks for a sync the same deliberate way they ask for any other
  commit/push.

## Setup checklist for a new machine (Claude: run this at the start of a
## session if things look uninitialized — no .venv, no fonts symlink, etc.)

1. `./scripts/setup-venv.sh` — Python venv + fonttools.
2. Check `model-fonts` is cloned as a sibling repo (`../model-fonts` from
   this repo's root) — it holds the proprietary/unclear-license fonts and
   is private, so it won't come along with a public clone of this repo. If
   missing, ask the user rather than guessing a clone URL.
3. Font symlink(s) + `fc-cache -f` per the font-install steps above.
4. Inkscape — check `inkscape --version`; if missing, it needs `sudo apt
   install inkscape` (see README's software table), which needs the user to
   run it (Claude has no root — see gotcha above). Ask the user rather than
   attempting sudo.
5. Repo may have uncommitted changes carried over via git — check `git
   status` before assuming a clean tree.
6. Claude memory symlink — check whether
   `~/.claude/projects/-home-geoff-Projects-model-making-workspace/memory`
   is already a symlink to `claude-memory/` in this repo (`ls -la` on its
   parent dir). If it's missing or is a real directory instead of a
   symlink, see the "Claude Code memory syncing across machines" section
   above and set it up — don't skip this, otherwise memory silently stops
   being shared between machines and starts drifting per-machine again.
