---
name: feedback-pedantic-naming
description: "User wants precise, historically/technically accurate naming for files and directories, not just convenient labels"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ee072010-f7b7-48e5-a550-d7cdb0e4bf76
  modified: 2026-08-21T00:38:00.183Z
---

Get naming precisely correct, especially where a convenient/common label
could be technically wrong. When a name implies scope, ownership, or a
specific historical/technical identity, verify that before naming a
file/folder/variable after it — don't default to the colloquial or
first-guess name.

**Why:** user said explicitly (2026-08-21, [[model-making]] insignia work)
"I like to be pedantic and get naming correct." Concretely: they caught
themselves about to name a WWII US national aircraft insignia folder
`usaaf-1943`, then asked for research first — turned out the insignia
(AN-I-9b) was a joint Army-Navy specification used across Army Air Forces,
Navy, and Marine Corps alike, not Army-Air-Forces-specific, so `usaaf-*`
would have been a real inaccuracy, not just an informal shorthand.

**How to apply:** when naming something after a historical period, spec,
organization, or scope, do a quick check of whether that name is actually
correct/precise before proposing or creating it, and surface ambiguity
(e.g. a bare year that covers multiple distinct variants) rather than
picking the first reasonable-sounding label. Offer the precise option
alongside the convenient one and explain the difference, matching how this
user likes to make the final naming call themselves.
