## Strategy — 2026-05-30

### Observations
- Current composite score: 0.0 (no index.html exists yet — baseline not set)
- Weakest eval dimension: all at 0.0 (greenfield build, no output file)
- Last 3 experiments: none (cycle 0 — first build)
- Pattern: Greenfield project. Research is complete and rated excellent by CEO. Eval harness (eval/score.py) is already scaffolded with 6 dimensions and weights. All brand tokens, program URLs, section architecture, and CSS marquee implementation are documented. Ready to build.

Eval dimensions and weights (from eval/score.py):
| Dimension | Weight | Target |
|---|---|---|
| required_sections | 0.30 | All 6 section patterns present |
| html_validity | 0.15 | index.html parses cleanly |
| brand_compliance | 0.20 | Phantom Sans + CDN + red + dark tokens |
| program_links | 0.20 | All 9 program URLs in HTML |
| mobile_responsive | 0.10 | viewport meta + @media queries |
| scrolling_gallery | 0.05 | @keyframes marquee + animation + .marquee class |

### Design Space
| Dimension | Score | Notes |
|---|---|---|
| Features | 0 | No output yet — greenfield |
| Bug fixes | 0 | N/A at this stage |
| Instrumentation | 4 | eval/score.py already scaffolded with 6 dimensions |
| Flow changes | 0 | N/A |
| New agents | 0 | N/A |
| Prompt engineering | 0 | N/A |
| Eval improvements | 4 | Harness exists; just needs review/approval |
| Knowledge management | 3 | Archive notes and research.md well-structured |
| Infrastructure | 0 | Single-file delivery, no CI needed |
| Operational execution | 0 | Nothing to run yet |
| Self-evolution | 0 | N/A |

**Underserved:** Features (output), Operational execution, Infrastructure (delivery)

---

### Hypotheses

#### H1: Build complete HTML scaffold with all sections, brand tokens, and all 9 program links
- **Category:** EXPLORE
- **Type:** code
- **New:** Greenfield Phase 1 — no prior experiments
- **Growth dimension:** capability_surface
- **What:** Create `index.html` and `style.css` from scratch with the complete page structure: sticky nav, hero section, scrolling gallery placeholder, current programs (Fallout/Stasis/Hackpad), past programs grid (Blueprint/Undercity/Highway/Solder/Bin/OnBoard), stats section, get-help section, community/Slack CTA, footer. Wire in all 9 program links (exact URLs validated in eval/score.py). Apply all Hackclub brand tokens: Phantom Sans via CDN, `#ec3750` red primary, `#121217` dark background, dark card surfaces (`#252429`). Include viewport meta tag. Add eval/score.py review to confirm harness passes on the scaffolded output.
- **Why:** The eval composite is 0.0 with no index.html. The three highest-weight dimensions — required_sections (0.30), brand_compliance (0.20), program_links (0.20) — are all blocked on the HTML scaffold. Building the structure first maxes 70% of the total score in one shot. The gallery section can use a placeholder grid; the marquee animation ships in Phase 2.
- **Expected impact:** required_sections 0.0→1.0, brand_compliance 0.0→1.0, program_links 0.0→1.0, html_validity 0.0→1.0, mobile_responsive 0.0→0.33 (viewport meta only), scrolling_gallery 0.0→0.33 (marquee class present). Composite: 0.0 → ~0.82
- **Priority:** high

**GitHub Issue — Phase 1:**

```
Title: [Phase 1] Complete HTML scaffold — all sections, brand tokens, all 9 program links

## Summary
Build index.html and style.css from scratch. This is the full structural scaffold of the
hardware.hackclub.com redesign. No placeholders for structure — everything except real project
photos ships in this issue.

## Acceptance Criteria

### index.html
- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1">` present
- [ ] Hackclub CDN links in <head>:
      `<link rel="stylesheet" href="https://css.hackclub.com/fonts.css">`
      `<link rel="stylesheet" href="https://css.hackclub.com/theme.css">`
- [ ] Sticky nav: Hackclub logo/wordmark + links (Docs, Gallery, Leaderboard) + Slack CTA button
- [ ] Hero section (id="hero"): large headline with "Hardware" in #ec3750 red, tagline,
      stat callouts (6000+, $4M+, since 2023), primary CTA button
- [ ] Scrolling gallery section: .marquee-wrap + .marquee-track with 8–12 placeholder
      project cards (colored backgrounds + placeholder text) — no real photos needed
- [ ] Current Programs section: cards for Fallout, Stasis, Hackpad each with:
      - 1–2 sentence description
      - External link to program URL
      - "Active" badge
- [ ] Past Programs section: grid cards for Blueprint, Undercity, Highway, Solder, Bin, OnBoard
      each with year badge and brief description
- [ ] Stats section: full-width band, 3–4 large numbers (6000+ hackers, $4M+, 3 years, 9 programs)
- [ ] Get Help section: links to Docs, Jams/tutorials, "Get Started" resources
- [ ] Community section: #electronics Slack CTA with slack.hackclub.com link
- [ ] Footer: Hackclub copyright + secondary nav links + "new programs starting" note

### style.css
- [ ] Phantom Sans declared as font-family (loaded via CDN)
- [ ] Dark base background #121217 or #17171d
- [ ] Card surfaces using #252429 (darkless)
- [ ] Primary accent color #ec3750 (red) used for CTAs and headline accents
- [ ] Border radius: 8px–16px on cards, pill (99999px) on buttons
- [ ] Max-width container: 1024px centered
- [ ] All 9 program URLs present as href values:
      fallout.hackclub.com, stasis.hackclub.com, hackpad.hackclub.com,
      blueprint.hackclub.com, undercity.hackclub.com, highway.hackclub.com,
      solder.hackclub.com, v3.hackclub.com/bin, v3.hackclub.com/onboard

### Eval harness review
- [ ] Run `python eval/score.py` — confirm composite score ≥ 0.80
- [ ] required_sections = 1.0
- [ ] brand_compliance = 1.0
- [ ] program_links = 1.0
- [ ] html_validity = 1.0

## Out of scope (Phase 2)
- CSS marquee @keyframes animation (placeholder .marquee class is fine)
- Real project photos
- Full mobile breakpoints beyond viewport meta
- Hero decorative imagery (Orpheus, circuit patterns)
- Stats counter animation
```

---

#### H2: Hero polish, scrolling gallery animation, mobile responsiveness, final content pass
- **Category:** EXPLOIT
- **Type:** code
- **New:** Phase 2 — builds directly on Phase 1 scaffold
- **Growth dimension:** capability_surface
- **What:** Add the CSS marquee animation (@keyframes marquee, animation: marquee 30s linear infinite, prefers-reduced-motion guard), complete all mobile breakpoints (@media max-width for nav collapse, card stacking, font scaling), add hero decorative elements (SVG circuit pattern or CSS-only decoration, Hackclub red gradient), finalize stats section visual treatment (full-width red/orange gradient band), add hover states on cards and nav, final content pass to remove any [TODO] markers resolvable without real photos, and verify full eval pass at ≥ 0.95.
- **Why:** Phase 1 delivers ~0.82 composite. Phase 2 pushes scrolling_gallery from 0.33→1.0, mobile_responsive from 0.33→1.0, and adds the visual polish that makes the page compelling vs. functional-but-plain. The marquee animation is the most distinctive element identified in research (differentiates from a plain link list) and has a fully specified CSS implementation ready to drop in.
- **Expected impact:** scrolling_gallery 0.33→1.0, mobile_responsive 0.33→1.0, brand_compliance maintained at 1.0. Composite: ~0.82 → ~0.97
- **Priority:** high

**GitHub Issue — Phase 2:**

```
Title: [Phase 2] Polish — scrolling gallery animation, mobile layout, hero imagery, final pass

## Summary
Build on the Phase 1 scaffold to add all interactive and visual polish. This issue ships
the full production-ready page.

## Acceptance Criteria

### Scrolling Gallery (marquee animation)
- [ ] CSS @keyframes marquee: `from { transform: translateX(0); } to { transform: translateX(-50%); }`
- [ ] .marquee-track has `animation: marquee 30s linear infinite`
- [ ] .marquee-track items duplicated (all items appear twice) for seamless loop
- [ ] .marquee-wrap has `overflow: hidden` + fade mask:
      `mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent)`
- [ ] Pause on hover: `.marquee-track:hover { animation-play-state: paused; }`
- [ ] `@media (prefers-reduced-motion: reduce) { .marquee-track { animation: none; } }`

### Mobile Responsiveness
- [ ] Nav collapses or stacks on mobile (≤768px): hamburger or stacked links
- [ ] Hero headline font size scales down (64px desktop → 40px mobile)
- [ ] Program cards stack to single column on mobile
- [ ] Past programs grid: 3-col desktop → 2-col tablet → 1-col mobile
- [ ] Stats band numbers scale gracefully (large on desktop, medium on mobile)
- [ ] No horizontal scroll at 375px viewport width
- [ ] Gallery marquee still animates on mobile

### Hero Section Polish
- [ ] Dark gradient background (linear-gradient from #121217 → #17171d)
- [ ] Decorative element: CSS-drawn circuit dots pattern or inline SVG (no external image required)
- [ ] Stat callouts styled as distinct chips/pills (border or background highlight)
- [ ] Primary CTA button: pill shape, #ec3750 fill, hover darkens slightly
- [ ] Headline uses dramatic weight contrast (bold "Hardware" + lighter rest of line)

### Stats Section
- [ ] Full-width band with red→orange gradient background
- [ ] 3–4 numbers displayed large (48px+) in white
- [ ] Labels in smaller weight below each number
- [ ] Responsive: numbers wrap gracefully to 2×2 on mobile

### Card Polish
- [ ] Program cards: colored left border accent (each program gets own accent color)
- [ ] Hover state: subtle translateY(-2px) + elevated shadow
- [ ] Past program cards: slightly muted (opacity 0.85 or muted text color)
- [ ] Year badges on past program cards

### Final Content Pass
- [ ] All [TODO: update] comments resolved or confirmed as needing real photos
- [ ] All links verified (href not "#" except photo placeholders)
- [ ] Page title: "Hardware @ Hack Club" or "Hardware@Hackclub"
- [ ] Meta description set for SEO

### Eval harness final check
- [ ] Run `python eval/score.py` — confirm composite score ≥ 0.95
- [ ] scrolling_gallery = 1.0
- [ ] mobile_responsive = 1.0
- [ ] All other dimensions remain 1.0

## Deferred (requires human intervention — real assets)
- Real project photos for gallery cards (sourced from teen makers)
- Real gallery images for marquee (current placeholder grid is shippable)
- Program-specific hero images
```

---

### Anti-patterns to Avoid
- Do not use React, Next.js, or any framework — manual editability is a hard constraint
- Do not use external JS libraries (jQuery, GSAP, etc.) — vanilla only
- Do not invent new brand colors — use only the official Hackclub token set
- Do not skip the eval run — `python eval/score.py` must confirm scores before marking complete
- Do not defer full section structure to Phase 2 — Phase 1 must have ALL sections present (even unstyled), so the eval's section-detection regexes all pass
- Do not use `git add .` — only stage index.html and style.css

---

### Deferred Backlog Items
The following items genuinely require human intervention and cannot be built autonomously:
- **Real project photos for gallery**: Need sourcing from teen maker community (highway.hackclub.com/projects, magazine.hackclub.com)
- **Real marquee images**: Current placeholder colored-card grid is shippable; swap in when photos are available
