from __future__ import annotations

from typing import Dict


def build_score(engine_input: Dict) -> Dict:
    sample_size = int(engine_input.get('sample_size', 0))
    avg_cards = float(engine_input.get('avg_cards', 0.0))
    top_fixture_cards = int(engine_input.get('top_fixture', {}).get('cards_count', 0))

    score = min(100, round((avg_cards * 10) + (top_fixture_cards * 4) + (sample_size * 2)))
    confidence = 4 if score >= 80 else 3 if score >= 65 else 2
    risk = 2 if score >= 80 else 3 if score >= 60 else 4
    edge = f"{max(0.0, round((avg_cards - 3.5) * 4.5, 1))}%"
    return {
        'score_raw': score,
        'confidence_raw': confidence,
        'risk_raw': risk,
        'edge_raw': edge,
    }
