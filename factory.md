# Factory Configuration

## Goal

A redesigned landing page for hardware.hackclub.com that showcases all Hackclub hardware programs (current and past), features a scrolling project gallery, and matches the fun, eclectic Hackclub aesthetic with dark theme and brand colors.

## Scope

### Modifiable

- index.html
- style.css
- assets/**

### Read-only

- eval/score.py
- factory.md

## Guards

- Do not delete or overwrite existing tests
- Do not modify files outside the declared scope
- Do not introduce secrets or credentials into the repository

## Eval

### Command

```bash
python3 eval/score.py
```

### Threshold

0.95

## Target Branch

main

## Smoke Test

```bash
python3 -c "html=open('index.html').read(); assert 'Hardware' in html; assert 'fallout.hackclub.com' in html; assert '@keyframes marquee' in html; print('smoke ok')"
```

## Constraints

- Do not use React, Vue, Next.js, or any JavaScript framework — plain HTML/CSS/JS only
- Do not use external JS libraries (jQuery, GSAP, etc.) — vanilla only
- Do not invent new brand colors — use only the official Hackclub token set (#ec3750, #121217, #252429, etc.)
- Do not change href values for any of the 9 program links
- Run python3 eval/score.py after every change — must stay at 1.0
