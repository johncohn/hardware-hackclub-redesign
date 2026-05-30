---
tags:
  - factory
  - patterns
source: factory-archivist
---

# Cross-Project Patterns

## Over-scope in Phase 1 pays dividends
Discovered in help-me-create-a-new-design-for-httphardwareha experiment #001.
When a builder includes a higher-risk Phase 2 deliverable (the CSS marquee animation) in Phase 1, Phase 2 becomes pure aesthetic polish — no risk of missing the eval gate on the high-weight dimension. If Phase 1 can safely deliver everything needed for max eval score, do it.

## Vanilla HTML+CSS beats frameworks for brief-mandated manual editability
Discovered in help-me-create-a-new-design-for-httphardwareha research/strategy phases.
When a brief explicitly requires the result to be "manually editable," using a framework (React, Next.js, Svelte) violates the spirit of the constraint even if it produces a working site. Vanilla HTML+CSS with a CDN for fonts/tokens is the correct choice — it satisfies the editability brief, has no build step, and still achieves 1.0/1.0 on structural evals.

## CSS @keyframes marquee > JS for scrolling galleries
Discovered in help-me-create-a-new-design-for-httphardwareha experiment #001.
Implementing a scrolling program gallery with pure CSS `@keyframes` (translate animation, duplicate set for seamless loop) requires zero JS and satisfies the `scrolling_gallery` eval dimension. Simpler, more accessible, and no JS library dependency.
