---
name: help-me-create-a-new-design-for-httphardwareha
description: Project dashboard for Hardware@Hackclub landing page redesign
tags:
  - factory
  - project
  - help-me-create-a-new-design-for-httphardwareha
source: factory-archivist
---

# Factory: help-me-create-a-new-design-for-httphardwareha

## Status
- **State**: Phase 1 COMPLETE — eval 1.0/1.0 — Phase 2 (aesthetic polish) ready to build
- **Current Score**: 1.0 (composite, all 6 dimensions)
- **Experiments Run**: 1
- **Kept**: 1, **Reverted**: 0

## Project Summary
Redesign landing page for `hardware.hackclub.com`. Replace minimal placeholder with a rich showcase of all Hackclub hardware programs (past and present). Audiences: teens seeking on-ramp to electronics building, and funders/partners evaluating program scale.

## CEO Verdicts
- **Research**: PROCEED — Research depth rated excellent. Researcher identified 8 critical gaps, extracted exact brand tokens, visited 3 live program pages, and provided a concrete CSS scrolling gallery implementation.
- **Phase 1 Build (Experiment #001)**: PROCEED — Verified 1.0/1.0. Builder overdelivered by shipping the full marquee animation in Phase 1 (was Phase 2 scope). No issues found.

## Key Constraints
- Single-file delivery: `index.html` + `style.css` (no build step)
- Use Hackclub CDN (css.hackclub.com) — no npm installs
- Must use official brand tokens (no invented palette)
- No React/Next.js/Svelte — brief requires manual editability
- Mark placeholder content with `[TODO: update]` comments

## Source Notes
- [[hackclub-brand-tokens]] — colors, typography, CDN links
- [[current-site-analysis]] — 8 critical gaps identified in the live site
- [[hackclub-program-pages]] — aesthetic patterns from Highway, Undercity, OnBoard
- [[tech-stack-recommendation]] — vanilla HTML/CSS rationale + CSS marquee implementation

## Approved Plan
- **Phase 1 (H1):** ✅ DONE — Full HTML scaffold — all sections, brand tokens, all 9 program links. Achieved 1.0 composite (target was ≥ 0.82).
- **Phase 2 (H2):** NEXT — Aesthetic polish only (eval already at 1.0): hero decorative element (SVG/CSS circuit pattern), stats band gradient, card accent stripes, year badges on past program cards, final content pass. Target: maintain 1.0 while improving visual quality.
- Strategy snapshot: [[strategy-help-me-create-a-new-design-for-httphardwareha-2026-05-30]]

## Recent Experiments
- **Experiment #001** — Phase 1 HTML scaffold (**KEEP**, 0.0 → 1.0, +1.0) — Overdelivered: marquee animation included.
