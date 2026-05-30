---
name: hackclub-brand-tokens
description: Official Hackclub color palette, typography, and design tokens from hackclub.com/brand and github.com/hackclub/theme
metadata:
  type: reference
  source: factory-archivist
  date: 2026-05-30
tags:
  - factory
  - source
  - hackclub
  - design-tokens
---

# Hackclub Brand Tokens

## Accent Colors
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

## Dark/Neutral Palette
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

## Typography
- **Primary font**: Phantom Sans — Hackclub's custom typeface, served from `assets.hackclub.com`
- **Weights**: Regular (400), Italic, Bold (700)
- **System fallback**: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
- **Monospace**: `"SF Mono", "Roboto Mono", Menlo, Consolas, monospace`
- **Font size scale** (px): 12, 16, 20, 24, 32, 48, 64, 96, 128, 160, 192
- **Line heights**: limit 0.875 → title 1.0 → heading 1.125 → body 1.5

## Design Tokens
```
Border radius: 4px / 8px / 12px / 16px / 99999px (pill)
Spacing scale: 0, 4, 8, 16, 32, 64, 128, 256, 512
Shadows: card = 0 4px 8px rgba(0,0,0,0.125), elevated = 0 8px 12px rgba(0,0,0,0.125)
Max widths: layout=1024px, layoutPlus=1200px, wide=1536px
Breakpoints: xs=32em, s=48em, m=64em, l=96em
```

## CDN Links
```html
<!-- Hackclub fonts (Phantom Sans) -->
<link rel="stylesheet" href="https://css.hackclub.com/fonts.css">
<!-- Hackclub base theme (CSS variables) -->
<link rel="stylesheet" href="https://css.hackclub.com/theme.css">
<!-- Minified versions -->
<link rel="stylesheet" href="https://css.hackclub.com/theme.min.css">
<link rel="stylesheet" href="https://css.hackclub.com/fonts.min.css">
```

## Sources
- https://hackclub.com/brand
- https://github.com/hackclub/theme/blob/main/packages/theme/src/index.ts
- https://github.com/hackclub/css
