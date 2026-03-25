from __future__ import annotations

from typing import Any, Dict, List


def evaluate_eligibility(engine_input: Dict[str, Any]) -> Dict[str, Any]:
    penalties: List[str] = []
    sample_size = int(engine_input.get('sample_size', 0))
    avg_cards = float(engine_input.get('avg_cards', 0.0))
    top_cards = int(engine_input.get('top_fixture', {}).get('cards_count', 0))

    if sample_size < 3:
        penalties.append('LOW_SAMPLE_DEPTH')
    if avg_cards < 4.0:
        penalties.append('WEAK_DISCIPLINE_SIGNAL')
    if top_cards < 5:
        penalties.append('TOP_FIXTURE_NOT_STRONG_ENOUGH')

    eligible = not penalties
    return {
        'eligibility': eligible,
        'penalties': penalties,
    }
