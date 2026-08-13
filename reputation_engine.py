#!/usr/bin/env python3
"""
Review Reputation Engine
A lightweight review reputation engine designed to organize, analyze, and
monitor online review signals across business and review platforms.

Focuses on review visibility, reputation insights, customer feedback patterns,
and maintaining a structured view of a brand's online presence.

https://buypositivereview.online
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "review_visibility": "Review Visibility",
        "reputation_health": "Reputation Health",
        "feedback_pattern": "Feedback Pattern",
        "platform_coverage": "Platform Coverage",
        "response_rate": "Response Rate",
        "brand_presence": "Brand Presence",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_review_platforms(visibility: int, health: int, coverage: int, brand: int) -> dict:
    return {
        "Google": min(100, round(visibility * 1.0)),
        "Trustpilot": min(100, round(health * 1.0)),
        "Yelp": min(100, round(coverage * 1.0)),
        "App Stores": min(100, round(brand * 1.0)),
    }


def run_reputation_engine(
    brand: str,
    platform: str = "google",
    review_visibility: int = 88,
    reputation_health: int = 82,
    feedback_pattern: int = 85,
    platform_coverage: int = 78,
    response_rate: int = 90,
    brand_presence: int = 84,
) -> dict:
    """
    Run the review reputation engine across review monitoring signals.

    Args:
        brand: Brand name or identifier
        platform: Primary review platform
        review_visibility: Review visibility score (0-100)
        reputation_health: Reputation health score (0-100)
        feedback_pattern: Feedback pattern score (0-100)
        platform_coverage: Platform coverage score (0-100)
        response_rate: Response rate score (0-100)
        brand_presence: Brand presence score (0-100)

    Returns:
        dict with individual signal scores, overall reputation index,
        and review platform breakdown
    """
    scores = {
        "review_visibility": review_visibility,
        "reputation_health": reputation_health,
        "feedback_pattern": feedback_pattern,
        "platform_coverage": platform_coverage,
        "response_rate": response_rate,
        "brand_presence": brand_presence,
    }
    overall_reputation_index = round(sum(scores.values()) / 6)

    return {
        "brand": brand,
        "platform": platform.capitalize(),
        "review_visibility_score": review_visibility,
        "reputation_health_score": reputation_health,
        "feedback_pattern_score": feedback_pattern,
        "platform_coverage_score": platform_coverage,
        "response_rate_score": response_rate,
        "brand_presence_score": brand_presence,
        "overall_reputation_index": overall_reputation_index,
        "priority_action": get_priority_action(scores),
        "review_platforms": get_review_platforms(review_visibility, reputation_health, platform_coverage, brand_presence),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    brand = args[0] if len(args) > 0 else "brand-name"
    platform = args[1] if len(args) > 1 else "google"
    review_visibility = int(args[2]) if len(args) > 2 else 88
    reputation_health = int(args[3]) if len(args) > 3 else 82
    feedback_pattern = int(args[4]) if len(args) > 4 else 85
    platform_coverage = int(args[5]) if len(args) > 5 else 78
    response_rate = int(args[6]) if len(args) > 6 else 90
    brand_presence = int(args[7]) if len(args) > 7 else 84

    result = run_reputation_engine(
        brand, platform, review_visibility, reputation_health,
        feedback_pattern, platform_coverage, response_rate, brand_presence
    )

    print(f"Brand: {result['brand']}")
    print(f"Platform: {result['platform']}")
    print("=" * 45)
    print(f"Review Visibility Score:       {result['review_visibility_score']}/100  [{get_status(result['review_visibility_score'])}]")
    print(f"Reputation Health Score:       {result['reputation_health_score']}/100  [{get_status(result['reputation_health_score'])}]")
    print(f"Feedback Pattern Score:        {result['feedback_pattern_score']}/100  [{get_status(result['feedback_pattern_score'])}]")
    print(f"Platform Coverage Score:       {result['platform_coverage_score']}/100  [{get_status(result['platform_coverage_score'])}]")
    print(f"Response Rate Score:           {result['response_rate_score']}/100  [{get_status(result['response_rate_score'])}]")
    print(f"Brand Presence Score:          {result['brand_presence_score']}/100  [{get_status(result['brand_presence_score'])}]")
    print("=" * 45)
    print(f"Overall Reputation Index:      {result['overall_reputation_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nReview Platforms:")
    for platform, score in result['review_platforms'].items():
        print(f"  {platform:<24} {score}/100")


if __name__ == "__main__":
    main()
