---
name: tech-stack-recommendation
description: Researcher's tech stack recommendation — vanilla HTML+CSS with Hackclub CDN, rationale, and scrolling gallery implementation
metadata:
  type: reference
  source: factory-archivist
  date: 2026-05-30
tags:
  - factory
  - source
  - tech-stack
---

# Tech Stack Recommendation

## Chosen: Vanilla HTML + CSS (Hackclub CDN) + minimal vanilla JS

### Rationale
1. Brief explicitly asks for *"easy to modify either manually or using your help or both"* — no build step is most editable
2. Hackclub provides production-ready CSS via CDN (`css.hackclub.com/theme.css`) with full token access
3. All other Hackclub program pages are either Next.js (complex) or plain HTML
4. Vanilla JS is sufficient for the scrolling gallery (CSS animation + optional JS for pause-on-hover)
5. Zero configuration, zero dependencies, instant preview with a browser

### Alternative Rejected: Next.js + @hackclub/theme
- Pro: React components, easy to grow into dynamic features later
- Con: Requires Node.js, npm, build step — much harder to hand-edit without dev environment
- Verdict: Overkill for a static landing page with no dynamic data requirements

## File Structure
```
index.html      ← single-file delivery (can split if desired)
style.css       ← custom overrides on top of Hackclub CDN
assets/
  images/       ← project photos, program logos
  icons/        ← any local SVGs
```

## Scrolling Gallery: Pure CSS Infinite Marquee

```css
.marquee-track {
  display: flex;
  width: max-content;
  animation: marquee 30s linear infinite;
}
.marquee-track:hover {
  animation-play-state: paused;
}
@keyframes marquee {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}
.marquee-wrap {
  overflow: hidden;
  mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
}
@media (prefers-reduced-motion: reduce) {
  .marquee-track { animation: none; }
}
```

Key technique: duplicate all items twice inside `.marquee-track`. At 50% translation content repeats seamlessly.

## Page Section Order
```
1. [Sticky Nav]         Logo + Docs + Gallery + Leaderboard + Slack CTA
2. [Hero]               "Hardware@Hackclub!" + tagline + stats + primary CTA
3. [Scrolling Gallery]  Infinite auto-scroll project photos
4. [Current Programs]   Cards for Fallout, Stasis, Hackpad (with descriptions)
5. [Past Programs]      Grid of 6 past programs with year badges
6. [Stats Section]      "6000+ hackers · $4M+ raised · 3 years" visual block
7. [Get Help]           Docs/Jams/tutorials links
8. [Community]          #electronics Slack channel CTA
9. [Footer]             Links, Hackclub branding, "new programs" note
```

## Assets Available
| Asset | URL |
|---|---|
| Phantom Sans font | `https://css.hackclub.com/fonts.css` |
| Hackclub theme CSS | `https://css.hackclub.com/theme.css` |
| Brand page + downloads | `https://hackclub.com/brand` |
| Icon explorer | `https://icons.hackclub.com` |
| Highway projects | `https://highway.hackclub.com/projects` |
| Blueprint explore | `https://blueprint.hackclub.com/explore` |
| Hack Club Magazine | `https://magazine.hackclub.com` |
