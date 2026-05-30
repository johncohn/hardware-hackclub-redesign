---
name: strategy-help-me-create-a-new-design-for-httphardwareha-2026-05-30
description: CEO-approved two-phase build plan for Hardware@Hackclub redesign — scaffold then polish
tags:
  - factory
  - strategy
  - help-me-create-a-new-design-for-httphardwareha
date: 2026-05-30
source: factory-archivist
---

# Strategy: help-me-create-a-new-design-for-httphardwareha — 2026-05-30

## CEO Verdict
**PROCEED** — Plan approved. Both hypotheses well-specified and correctly scoped. No hygiene-only work, no deferrable code pushed to backlog.

## Context
Greenfield build. Composite score: 0.0 (no index.html yet). Eval harness already scaffolded at `eval/score.py` with 6 dimensions.

## Eval Dimensions
| Dimension | Weight | Target |
|---|---|---|
| required_sections | 0.30 | All 6 section patterns present |
| html_validity | 0.15 | index.html parses cleanly |
| brand_compliance | 0.20 | Phantom Sans + CDN + red + dark tokens |
| program_links | 0.20 | All 9 program URLs in HTML |
| mobile_responsive | 0.10 | viewport meta + @media queries |
| scrolling_gallery | 0.05 | @keyframes marquee + animation + .marquee class |

## Phase 1 — H1: Full HTML Scaffold
- **Category:** EXPLORE
- **Target score:** ≥ 0.82 composite
- **Deliverables:** `index.html` + `style.css` with all 6 sections, all 9 program URLs, all brand tokens
- **Key sections:** sticky nav, hero, scrolling gallery placeholder, current programs (Fallout/Stasis/Hackpad), past programs grid (Blueprint/Undercity/Highway/Solder/Bin/OnBoard), stats, get-help, community/Slack, footer
- **Acceptance gate:** `python eval/score.py` ≥ 0.80; required_sections=1.0, brand_compliance=1.0, program_links=1.0, html_validity=1.0

## Phase 2 — H2: Polish + Animation
- **Category:** EXPLOIT (builds on Phase 1)
- **Target score:** ≥ 0.97 composite
- **Deliverables:** CSS @keyframes marquee animation, full mobile breakpoints, hero decorative elements, stats gradient band, card hover states
- **Key animation spec:** `@keyframes marquee { from { transform: translateX(0); } to { transform: translateX(-50%); } }`, 30s linear infinite, pause-on-hover, prefers-reduced-motion guard
- **Acceptance gate:** `python eval/score.py` ≥ 0.95; scrolling_gallery=1.0, mobile_responsive=1.0

## Anti-patterns
- No React/Next.js/frameworks — vanilla HTML/CSS only
- No external JS libraries (jQuery, GSAP) — vanilla only
- No invented brand colors — official Hackclub token set only
- Must run eval before marking complete
- Do not use `git add .` — stage index.html and style.css only

## Deferred (requires human)
- Real project photos for gallery cards (sourced from teen makers)
- Real marquee images (placeholder colored-card grid is shippable)
