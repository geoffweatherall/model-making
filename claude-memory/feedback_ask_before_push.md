---
name: feedback-ask-before-push
description: "Always ask before running git push, in this repo and generally"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ee072010-f7b7-48e5-a550-d7cdb0e4bf76
  modified: 2026-08-20T06:08:29.583Z
---

Never run `git push` (or any command that publishes commits to a remote)
without asking the user first, even after they've approved a commit.

**Why:** user explicitly said, right after approving a commit in
model-masks, "you should ask me before making pushes to the repo" —
approval to commit is not approval to push. This is a general collaboration
preference, not scoped to one repo.

**How to apply:** commit freely when asked to commit, but stop and ask
before `git push` in any repository, every time — don't treat a prior push
approval as standing permission for future pushes.
