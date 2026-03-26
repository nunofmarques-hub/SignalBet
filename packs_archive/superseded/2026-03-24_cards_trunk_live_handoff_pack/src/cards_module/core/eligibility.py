from __future__ import annotations

from typing import Any, Dict, List


def evaluate_eligibility(engine_input: Dict[str, Any]) -> Dict[str, Any]:
    penalties: List[str] = []
    if engine_input.get('sample_size', 0) < 2:
        penalties.append('LOW_SAMPLE_DEPTH')
    if engine_input.get('avg_cards', 0.0) < 3.5:
        penalties.append('WEAK_DISCIPLINE_SIGNAL')

    eligible = not penalties and engine_input.get('top_fixture', {}).get('cards_count', 0) >= 4
    return {
        'eligibility': eligible,
        'penalties': penalties,
    }
