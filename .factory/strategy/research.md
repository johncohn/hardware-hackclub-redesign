# Research — Hardware@Hackclub Landing Page

## Project Summary

Build a redesigned landing page for `hardware.hackclub.com` that replaces the current minimal stub
with a rich, fun showcase of all Hackclub hardware programs (past and present). The audience is two
groups: (1) teens who want to build electronics and need an on-ramp, and (2) funders/partners who
want a compelling overview of the program's scale and creativity. The page must match Hackclub's
eclectic, youth-centric aesthetic.

---

## Current Site Analysis

**URL**: http://hardware.hackclub.com

### What Exists
The current page is a bare-minimum placeholder:
- Nav header: "Sign in" + three links: Docs, Gallery, Leaderboard
- Three horizontal program tiles: Hackpad, Stasis, Fallout (no descriptions, just external links with arrows)
- Tagline: "View your hardware projects." — generic, says nothing about community or scale
- No footer, no hero, no CTAs, no social proof, no history

### Critical Gaps vs. Brief
| Missing Element | Impact |
|---|---|
| Hero / splash section with stats | First impression — no hook for newcomers or funders |
| Program descriptions | Visitors don't know what any program is |
| Past programs section | History of $4M+ investment invisible |
| Community link (#electronics Slack) | No way to join the community |
| Projects gallery / scrolling showcase | Nothing showing the work that has been done |
| Mobile responsiveness signals | Unclear if the current page works on phones |
| Footer | No copyright, contact, or secondary nav |
| "New programs starting" signal | No reason to return |

---

## Hackclub Brand & Aesthetic Findings

### Official Color Palette
Sourced from `hackclub.com/brand` and `github.com/hackclub/theme`:

**Accent colors:**
| Name | Hex | Use |
|---|---|---|
| Red (primary) | `#ec3750` | Brand hero color, primary CTAs |
| Orange | `#ff8c37` | Highlights, warm accents |
| Yellow | `#f1c40f` | Stats, callouts |
| Green | `#33d6a6` | Success states, secondary CTAs |
| Cyan | `#5bc0de` | Links, cool accents |
| Blue | `#338eda` | Informational, links |
| Purple | `#a633d6` | Creative, gradient endpoints |
| Muted | `#8492a6` | Captions, secondary text |

**Dark/neutral palette:**
| Name | Hex | Use |
|---|---|---|
| darker | `#121217` | Hero backgrounds, darkest surfaces |
| dark | `#17171d` | Card backgrounds on dark sections |
| darkless | `#252429` | Slightly elevated dark surfaces |
| black | `#1f2d3d` | Body text, dark on light |
| steel | `#273444` | Borders on dark |
| slate | `#3c4858` | Secondary text on dark |
| smoke | `#e0e6ed` | Light section backgrounds |
| snow | `#f9fafc` | Near-white backgrounds |
| white | `#ffffff` | Pure white |

### Typography
- **Primary font**: Phantom Sans — Hackclub's custom typeface, served from `assets.hackclub.com`
- **Weights**: Regular (400), Italic, Bold (700)
- **System fallback stack**: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
- **Monospace**: `"SF Mono", "Roboto Mono", Menlo, Consolas, monospace`
- **Font size scale** (px): 12, 16, 20, 24, 32, 48, 64, 96, 128, 160, 192
- **Line heights**: limit 0.875 → title 1.0 → heading 1.125 → body 1.5

### Design Token Summary
```
Border radius: 4px / 8px / 12px / 16px / 99999px (pill)
Spacing scale: 0, 4, 8, 16, 32, 64, 128, 256, 512
Shadows: card = 0 4px 8px rgba(0,0,0,0.125), elevated = 0 8px 12px rgba(0,0,0,0.125)
Max widths: layout=1024px, layoutPlus=1200px, wide=1536px
Breakpoints: xs=32em, s=48em, m=64em, l=96em
```

### Visual Style Patterns (from program pages)

**Highway** (`highway.hackclub.com`):
- Dark navy/charcoal background
- Neon lime/green primary CTA accent
- Purple + pink + cyan gradient decorative elements
- Bold headline: *"Design any hardware project. Get a grant to make it real."*
- Racing track illustrations + Cerberus mascot character
- Stats pattern: "Design. Share. Build. Repeat."
- Real teen project photos in grid

**Undercity** (`undercity.hackclub.com`):
- Cyberpunk aesthetic — pure black + neon cyan/electric blue
- Gate-themed background imagery
- Polaroid-style photo grids
- Prominent stats banner: *"166 teen makers · 75 total projects · 19 countries · 72 hours of magic"*
- Conversational, humorous project names reflecting teen voices

**OnBoard** (`v3.hackclub.com/onboard`):
- Light/white background (contrast to others)
- Bold headline: *"Circuit boards are magical"*
- Fun PCB shapes as hero imagery (dinosaurs, flowers, fidget spinners)
- Steve Wozniak testimonial for social proof
- Card-based showcase of student work
- Dual CTAs: "Learn PCB Design Now!" + "Get a Grant"

**Common patterns across all programs:**
- Full-width hero with strong headline + stat/proof
- Card-based program/project showcases
- Real photos of teen makers and their work
- Playful typography mixing weights dramatically
- Dark-first aesthetic (most programs), occasional light variants
- Custom mascot/character illustrations (Orpheus the dinosaur, Cerberus, etc.)
- Sticker-style decorative elements scattered around
- Prominent grant/CTA buttons throughout, not just hero

---

## Tech Stack Recommendation

### Recommendation: Vanilla HTML + CSS (with Hackclub CDN) + minimal vanilla JS

**Rationale:**
1. The brief explicitly says *"easy to modify either manually or using your help or both"* — no build step is the most editable format
2. Hackclub provides a production-ready CSS system via CDN (`css.hackclub.com/theme.css`) that gives full access to all tokens
3. All other Hackclub program pages are either Next.js apps (complex) or plain HTML — the landing page is a one-file deliverable
4. Vanilla JS is sufficient for the scrolling gallery (CSS animation + optional JS for pause-on-hover)
5. Zero configuration, zero dependencies, instant preview with a browser

**Alternative considered: Next.js + @hackclub/theme**
- Pro: React components, easy to grow into dynamic features later
- Con: Requires Node.js, npm, build step — significantly harder to hand-edit without dev environment
- Verdict: Overkill for a static landing page with no dynamic data requirements

**File structure:**
```
index.html          ← single-file delivery (can split if desired)
style.css           ← custom overrides on top of Hackclub CDN
assets/
  images/           ← project photos, program logos
  icons/            ← any local SVGs
```

**CDN dependencies (no npm install):**
```html
<!-- Hackclub fonts (Phantom Sans) -->
<link rel="stylesheet" href="https://css.hackclub.com/fonts.css">
<!-- Hackclub base theme (CSS variables) -->
<link rel="stylesheet" href="https://css.hackclub.com/theme.css">
```

---

## Architecture Patterns

### Page Section Order
```
1. [Sticky Nav]          Logo + Docs + Gallery + Leaderboard + Slack CTA
2. [Hero]                "Hardware@Hackclub!" + tagline + stats counter + primary CTA
3. [Scrolling Gallery]   Infinite auto-scroll showcase of project photos
4. [Current Programs]    Cards for Fallout, Stasis, Hackpad (with descriptions)
5. [Past Programs]       Grid/carousel of 6 past programs with year badges
6. [Stats Section]       "6000+ hackers · $4M+ raised · 3 years" visual block
7. [Get Help]            Docs/Jams/tutorials links
8. [Community]           #electronics Slack channel CTA
9. [Footer]              Links, Hackclub branding, "new programs" note
```

### Section Design Patterns

**Hero section:**
- Full-viewport dark background (`#121217` or gradient → `#17171d`)
- Large Phantom Sans headline (64px+), Hackclub Red `#ec3750` accent on "Hardware"
- 3 inline stats (6000+ hackers, since 2023, anything goes)
- "Anything goes" tagline with breadboard/PCB/FPGA examples
- Single primary CTA button (red, pill-shaped)
- Decorative circuit board pattern or Orpheus character as background element

**Program cards (current programs):**
- Dark card surface (`#252429`), 12-16px radius
- Program name large, brief 1-2 sentence description
- External link with arrow → program site
- Colored top border or left accent stripe in program's own color
- "Active" badge in green `#33d6a6`

**Past programs grid:**
- Slightly muted styling vs current — `opacity: 0.85` or `--color-muted` text
- Year badge on each card
- Hover state reveals brief description

**Stats section:**
- Full-width colored band (red or gradient from red → orange)
- 3-4 large numbers with labels
- High contrast white text

---

## Scrolling Gallery Implementation

### Recommended: Pure CSS Infinite Marquee

The most performant, no-JS implementation:

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
```

**Key technique**: Duplicate all items twice inside `.marquee-track`. At 50% translation the content
seamlessly repeats, creating an infinite loop without JavaScript.

**Items to show**: Project photos from the hardware gallery with project name + creator name overlay.
Source images from:
- Highway gallery: `https://highway.hackclub.com/projects`
- Hackclub Magazine: `https://magazine.hackclub.com`
- Undercity gallery photos

**Accessibility**: Add `prefers-reduced-motion` media query to stop animation for users who have
that OS setting enabled.

```css
@media (prefers-reduced-motion: reduce) {
  .marquee-track { animation: none; }
}
```

### Alternative: Intersection Observer JS (for lazy-load + speed control)
A lightweight vanilla JS enhancement if scroll speed needs dynamic control or images should
lazy-load. ~30 lines of JS, no library required.

---

## Assets & Resources Available

### CDN-hosted (use directly)
| Asset | URL |
|---|---|
| Phantom Sans font | `https://css.hackclub.com/fonts.css` |
| Hackclub theme CSS | `https://css.hackclub.com/theme.css` |
| Theme (minified) | `https://css.hackclub.com/theme.min.css` |
| Fonts (minified) | `https://css.hackclub.com/fonts.min.css` |
| Brand page + downloads | `https://hackclub.com/brand` |
| Icon explorer | `https://icons.hackclub.com` |

### Logo assets (from hackclub.com/brand)
- Orpheus Flag (SVG, PNG, PDF) — top and left orientations
- Flag Standalone, Icon Rounded, Icon Square
- All available as ZIP download from brand page

### Icon pack
- `@hackclub/icons` — React package, but icons are also browseable at `icons.hackclub.com`
- Many icons are simple SVGs that can be inlined directly

### Project images
- Highway project gallery: `https://highway.hackclub.com/projects`
- Blueprint explore: `https://blueprint.hackclub.com/explore`
- Hack Club Magazine 2025: `https://magazine.hackclub.com`
- Undercity projects showcased at `undercity.hackclub.com`

---

## Prior Knowledge (Archive)

No factory archive exists yet for this project directory. This is a greenfield build.

---

## Recommended Focus Areas

### 1. Hero Section — Highest Impact
The jump from the current "View your hardware projects." to a proper hero with stats and personality
is the single largest UX improvement. Use dark background + Hackclub red headline + real project
photo backdrop or Orpheus illustration. Add the 6000+ stat prominently.

### 2. Scrolling Gallery — Most Distinctive Element
The auto-scrolling project showcase is what differentiates this from a plain link list. Implement
as pure CSS marquee. Source 10-20 project thumbnail images from the existing galleries.

### 3. Program Cards with Descriptions
Current programs need 1-2 sentence descriptions so visitors understand what they're clicking into.
Past programs need brief "what was this?" descriptions for funders/newcomers.

### 4. Stats & Social Proof
Funders respond to numbers. A "6000+ hackers · $4M+ raised · 3 years" band is a fast credibility
builder. Mirrors what Undercity does with "166 teen makers · 19 countries."

### 5. Community CTA
The #electronics Slack link is buried in hardware.md but is a key conversion action for teens.
Should be a prominent section, not a footer link.

### 6. Single-file Deliverability
The whole page should be deliverable as a single `index.html` with an inline `<style>` block (or
one companion `style.css`). This makes it trivially easy for the Hackclub team to pick up, modify,
or deploy without any tooling.

---

## Constraint Notes

- **No framework dependency**: Avoid React/Next.js/Svelte — the brief asks for manual editability
- **No external JS libraries**: jQuery, GSAP, etc. add friction; vanilla CSS + JS only
- **Must use Hackclub brand colors**: Do not invent a new palette; use the official tokens
- **Content is placeholder-friendly**: Mark stats and project images with `[TODO: update]` comments
  so the team knows exactly what to fill in
- **Links to program pages**: All 9 program URLs are confirmed working from hardware.md; use them

---

## Sources

- [Hack Club Brand](https://hackclub.com/brand)
- [hackclub/theme — design tokens](https://github.com/hackclub/theme/blob/main/packages/theme/src/index.ts)
- [hackclub/css — CDN links](https://github.com/hackclub/css)
- [Highway — program page](https://highway.hackclub.com)
- [Undercity — program page](https://undercity.hackclub.com)
- [OnBoard — program page](https://v3.hackclub.com/onboard)
- [Highway projects gallery](https://highway.hackclub.com/projects)
- [Hack Club Magazine](https://magazine.hackclub.com)
- [Hackclub design system (old)](https://github.com/hackclub/design-system)
- [Scrolling design patterns](https://lovable.dev/guides/scrolling-designs-patterns-when-to-use)
- [Landing page best practices 2025](https://www.softriver.co/blog/8-landing-page-design-best-practices-for-2025)
