---
tags:
  - factory
  - experiment
  - help-me-create-a-new-design-for-httphardwareha
project: help-me-create-a-new-design-for-httphardwareha
experiment_id: "001"
verdict: KEEP
score_delta: +1.0
date: 2026-05-30
source: factory-archivist
---

# Experiment #001: Complete HTML scaffold with all sections, brand tokens, and all 9 program links

## Hypothesis
Build `index.html` and `style.css` from scratch with the full page structure: sticky nav, hero, scrolling gallery, current programs, past programs grid, stats section, get-help, community/Slack CTA, footer. Wire in all 9 program links. Apply all Hackclub brand tokens (Phantom Sans, #ec3750, #121217, #252429). Include viewport meta tag.

## Result
**KEEP** — composite score changed from 0.0 to **1.0** (+1.0)

| Dimension | Before | After | Delta |
|---|---|---|---|
| required_sections (0.30) | 0.0 | 1.0 | +1.0 |
| brand_compliance (0.20) | 0.0 | 1.0 | +1.0 |
| program_links (0.20) | 0.0 | 1.0 | +1.0 |
| html_validity (0.15) | 0.0 | 1.0 | +1.0 |
| mobile_responsive (0.10) | 0.0 | 1.0 | +1.0 |
| scrolling_gallery (0.05) | 0.0 | 1.0 | +1.0 |
| **TOTAL** | **0.0** | **1.0** | **+1.0** |

## What Changed
- Created `index.html` with all 8 required sections: nav, hero, gallery, current-programs, past-programs, stats, get-help, community + footer
- Created `style.css` with Phantom Sans font family, dark base (#121217), card surfaces (#252429), #ec3750 red accent
- Wired in all 9 program links: fallout.hackclub.com, stasis.hackclub.com, hackpad.hackclub.com, blueprint.hackclub.com, undercity.hackclub.com, highway.hackclub.com, solder.hackclub.com, v3.hackclub.com/bin, v3.hackclub.com/onboard
- **Overdelivered**: Full CSS marquee @keyframes animation included in Phase 1 (was scoped to Phase 2). `scrolling_gallery` scored 1.0 immediately.
- Commit: `cd49383` — "feat: Phase 1 complete HTML scaffold with all sections and brand tokens"

## CEO Verdict
**PROCEED** — CEO independently verified 1.0/1.0 score. No issues found. Builder exceeded Phase 1 scope by including the marquee animation, which was the highest-risk Phase 2 item. Phase 2 is now pure aesthetic polish (hero decorative element, stats band gradient, card accent stripes, year badges) since eval is already at 1.0.

## Links
- Project: help-me-create-a-new-design-for-httphardwareha
- Commit: cd49383
