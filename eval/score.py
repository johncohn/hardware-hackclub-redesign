#!/usr/bin/env python3
"""Eval scorer for hardware.hackclub.com landing page redesign."""

import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_FILE = os.path.join(ROOT, "index.html")


def read_html() -> str:
    try:
        with open(HTML_FILE) as f:
            return f.read()
    except FileNotFoundError:
        return ""


def score_required_sections(html: str) -> float:
    """Check that all 6 required sections are present."""
    required = [
        # hero / splash
        r'id=["\']hero["\']|class=["\'][^"\']*hero[^"\']*["\']|Hardware.*[Hh]ackclub|hackclubbers|6000',
        # current programs section
        r'fallout\.hackclub\.com|stasis\.hackclub\.com|hackpad\.hackclub\.com',
        # past programs section
        r'blueprint\.hackclub\.com|undercity\.hackclub\.com|highway\.hackclub\.com',
        # gallery / scrolling showcase
        r'gallery|marquee|scroll.*project|project.*scroll',
        # help / docs section
        r'[Dd]ocs|[Jj]ams|[Tt]utorial|[Gg]et.*[Ss]tarted|[Hh]elp.*[Ss]tarted',
        # community / slack section
        r'#electronics|slack\.hackclub\.com|[Ss]lack.*channel|[Cc]ommunity',
    ]
    found = sum(1 for pattern in required if re.search(pattern, html, re.IGNORECASE))
    return round(found / len(required), 3)


def score_brand_compliance(html: str) -> float:
    """Check use of Hackclub brand colors and Phantom Sans font."""
    checks = [
        r'Phantom Sans|phantom-sans|phantomsans',           # font family
        r'css\.hackclub\.com/fonts|fonts\.css',             # font CDN
        r'css\.hackclub\.com/theme|theme\.css',             # theme CDN
        r'#ec3750|ec3750|var\(--color-red\)',                # hackclub red
        r'#121217|#17171d|#252429|var\(--color-dark',       # dark backgrounds
    ]
    found = sum(1 for pattern in checks if re.search(pattern, html, re.IGNORECASE))
    return round(found / len(checks), 3)


def score_program_links(html: str) -> float:
    """Check all 9 program URLs are linked."""
    programs = [
        "fallout.hackclub.com",
        "stasis.hackclub.com",
        "hackpad.hackclub.com",
        "blueprint.hackclub.com",
        "undercity.hackclub.com",
        "highway.hackclub.com",
        "solder.hackclub.com",
        "v3.hackclub.com/bin",
        "v3.hackclub.com/onboard",
    ]
    found = sum(1 for p in programs if p in html)
    return round(found / len(programs), 3)


def score_mobile_responsive(html: str) -> float:
    """Check for viewport meta tag and media queries."""
    checks = [
        r'<meta[^>]+viewport',
        r'@media\s*\(',
        r'max-width|min-width',
    ]
    found = sum(1 for pattern in checks if re.search(pattern, html, re.IGNORECASE))
    return round(found / len(checks), 3)


def score_scrolling_gallery(html: str) -> float:
    """Check for scrolling gallery / marquee animation."""
    checks = [
        r'@keyframes\s+(?:marquee|scroll|slide)',
        r'animation.*(?:marquee|scroll|infinite)',
        r'class=["\'][^"\']*marquee[^"\']*["\']|id=["\'][^"\']*marquee[^"\']*["\']',
    ]
    found = sum(1 for pattern in checks if re.search(pattern, html, re.IGNORECASE))
    return round(min(found / len(checks), 1.0), 3)


DIMENSIONS = {
    "required_sections": score_required_sections,
    "brand_compliance": score_brand_compliance,
    "program_links": score_program_links,
    "mobile_responsive": score_mobile_responsive,
    "scrolling_gallery": score_scrolling_gallery,
}


def run_all(html: str) -> dict:
    results = {}
    total_weight = 0.0
    weighted_score = 0.0
    weights = {
        "required_sections": 0.30,
        "brand_compliance": 0.20,
        "program_links": 0.20,
        "mobile_responsive": 0.10,
        "scrolling_gallery": 0.05,
        "html_validity": 0.15,
    }

    for name, fn in DIMENSIONS.items():
        score = fn(html)
        results[name] = score
        w = weights.get(name, 0.0)
        weighted_score += score * w
        total_weight += w

    # html_validity: if index.html exists and parses, count it
    if html:
        try:
            from html.parser import HTMLParser
            HTMLParser().feed(html)
            results["html_validity"] = 1.0
        except Exception:
            results["html_validity"] = 0.0
    else:
        results["html_validity"] = 0.0

    weighted_score += results["html_validity"] * weights["html_validity"]
    total_weight += weights["html_validity"]

    results["total"] = round(weighted_score, 3)
    return results


def main():
    parser = argparse.ArgumentParser(description="Score hardware.hackclub.com landing page")
    parser.add_argument("--dimension", help="Run a single dimension only")
    args = parser.parse_args()

    html = read_html()

    if args.dimension:
        if args.dimension not in DIMENSIONS:
            print(json.dumps({"error": f"Unknown dimension: {args.dimension}", "score": 0.0}))
            sys.exit(1)
        score = DIMENSIONS[args.dimension](html)
        print(json.dumps({"score": score, "dimension": args.dimension}))
    else:
        results = run_all(html)
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
