---
name: feedback-concise-reference-docs
description: "Reference docs in this repo: lead with key points, keep only the summary of what failed and why — not the full narrative"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 56bf9d59-471d-4710-8c26-18e2db6b2ea1
  modified: 2026-09-12T00:14:07.076Z
---

Reference documents the user consults while working (e.g.
`masks/cut-settings.md`) should open with a **key points** section — the
decision and the background needed to make it — then the tables. Failed
experiments get a compressed overview of the range that failed and why, not
a per-attempt log.

**Why:** the user asked for exactly this rewrite on 2026-09-12 after the cut
settings doc accumulated a detailed row-per-attempt failure log and lengthy
reasoning. These are documents read at the bench mid-task, so the answer
has to be findable at a glance; the full investigation narrative was noise
once it had produced a conclusion.

**How to apply:** while an investigation is live, detail is useful — record
attempts as they happen. Once it resolves, compress: keep the conclusion,
the working settings, and a short "what failed and why" so the range isn't
retried. Brief material/physical background *is* wanted where it explains
a choice (why one material over another) — this is about cutting narrative,
not cutting explanation. Relates to [[feedback-cut-results-scope-claims]].
