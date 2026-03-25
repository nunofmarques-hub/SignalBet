from __future__ import annotations

from typing import Any


def _clamp_probability(probability: float) -> float:
    return round(max(0.08, min(0.93, probability)), 4)


def _score_to_probability(score: float, low: float, high: float) -> float:
    return _clamp_probability(low + (score / 10.0) * (high - low))


def prob_over_15_game(indicators: dict[str, Any]) -> float:
    probability = _score_to_probability(indicators['over_game_strength'], 0.43, 0.76)
    if indicators.get('mtd', 0.0) >= 4.5:
        probability -= 0.018
    if indicators.get('risk_balance', 0.0) >= 0.95:
        probability -= 0.012
    return _clamp_probability(probability)


def prob_under_35(indicators: dict[str, Any]) -> float:
    score = indicators['uli'] * 0.60 + indicators['ltr'] * 0.40
    probability = _score_to_probability(score, 0.47, 0.81)
    if indicators.get('over_game_strength', 0.0) >= 6.9:
        probability -= 0.018
    if indicators.get('uli', 0.0) >= 5.7 and indicators.get('ltr', 0.0) >= 4.8:
        probability += 0.014
    return _clamp_probability(probability)


def prob_favorite_over_15(indicators: dict[str, Any]) -> float:
    if not indicators.get('favorite_team'):
        return 0.08
    probability = _score_to_probability(indicators['fdi'], 0.39, 0.80)
    if abs(indicators.get('favorite_margin', 0.0)) < 0.35:
        probability -= 0.012
    if indicators.get('fdi', 0.0) >= 6.5:
        probability += 0.012
    cap = max(prob_over_15_game(indicators) + 0.06, 0.55)
    return _clamp_probability(min(probability, cap))


def build_market_probabilities(indicators: dict[str, Any], context: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    rows = [
        {
            'market': 'Over 1.5 jogo',
            'probability': prob_over_15_game(indicators),
            'engine': 'O15_GAME',
            'engine_score': indicators.get('over_game_strength', 0.0),
        },
        {
            'market': 'Under 3.5',
            'probability': prob_under_35(indicators),
            'engine': 'U35',
            'engine_score': round(indicators.get('uli', 0.0) * 0.60 + indicators.get('ltr', 0.0) * 0.40, 2),
        },
    ]
    favorite_team = indicators.get('favorite_team')
    if favorite_team:
        rows.append({
            'market': f'{favorite_team} Over 1.5',
            'probability': prob_favorite_over_15(indicators),
            'engine': 'O15_TEAM',
            'engine_score': indicators.get('fdi', 0.0),
        })
    return rows
