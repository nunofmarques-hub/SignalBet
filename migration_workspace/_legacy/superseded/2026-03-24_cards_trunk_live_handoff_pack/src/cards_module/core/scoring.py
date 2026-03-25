from __future__ import annotations

from typing import Any, Dict


def build_score(engine_input: Dict[str, Any]) -> Dict[str, Any]:
    avg_cards = float(engine_input.get('avg_cards', 0.0))
    sample_size = int(engine_input.get('sample_size', 0))
    top_cards = int(engine_input.get('top_fixture', {}).get('cards_count', 0))
    score_raw = min(90, int(45 + avg_cards * 8 + min(sample_size, 5) + top_cards))
    confidence_raw = 4 if avg_cards >= 4.5 and sample_size >= 3 else 3 if avg_cards >= 3.8 else 2
    risk_raw = 2 if sample_size >= 3 and avg_cards >= 4.0 else 3
    edge_raw = f"{max(0.0, round((avg_cards - 3.5) * 6, 1))}%"
    return {
        'score_raw': score_raw,
        'confidence_raw': confidence_raw,
        'risk_raw': risk_raw,
        'edge_raw': edge_raw,
    }
