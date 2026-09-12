---
name: feedback-cut-results-scope-claims
description: Never record a cut setting as confirmed/successful beyond the specific elements actually observed to cut cleanly
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 56bf9d59-471d-4710-8c26-18e2db6b2ea1
  modified: 2026-09-11T23:12:36.953Z
---

When logging cutter results, scope every success claim to the exact elements
that were observed to cut cleanly. "The sheet cut OK" is not "the tail serial
cut cleanly." Don't promote a setting to recommended/confirmed for fine
detail unless the user said that fine detail specifically came out right.

**Why:** an earlier memory note recorded depth=2/force=3/speed=1 as
"confirmed working" for the whole Tamiya 87130 sheet including small
detail. The user corrected this on 2026-09-12: no setting has ever cleanly
cut the tail serial numbers on 87130. The overstatement came from treating a
generally-successful sheet cut as validation of the hardest element on it,
and it would have sent them back to a setting that never actually solved the
problem.

**How to apply:** in `masks/cut-settings.md` (and any similar test log), a
row only earns "confirmed" for the item types explicitly reported good.
Everything else stays "unresolved" or "not tested" — an honest gap is more
useful to the user than an optimistic entry, because they plan real cutting
sessions off that table. Also relates to [[feedback-pedantic-naming]]: same
underlying preference for claims being precisely true rather than
approximately right.
