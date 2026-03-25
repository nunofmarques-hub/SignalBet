from __future__ import annotations


def parse_odds_window(window: str) -> tuple[float, float]:
    left, right = window.split("-")
    return float(left), float(right)


def is_within_window(executed_odds: float, window: str) -> bool:
    min_odds, max_odds = parse_odds_window(window)
    return min_odds <= executed_odds <= max_odds
