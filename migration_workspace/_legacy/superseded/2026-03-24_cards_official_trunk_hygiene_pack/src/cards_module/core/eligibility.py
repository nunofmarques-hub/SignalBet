from __future__ import annotations

from typing import Dict, List


def evaluate_eligibility(engine_input: Dict) -> Dict:
    penalties: List[str] = []
    sample_size = engine_input.get('sample_size', 0)
    avg_cards = engine_input.get('avg_cards', 0.0)
    top_fixture_cards = engine_input.get('top_fixture', {}).get('cards_count', 0)

    if sample_size < 3:
        penalties.append('low_sample_depth')
    if avg_cards < 4.0:
        penalties.append('avg_cards_below_threshold')
    if top_fixture_cards < 5:
        penalties.append('top_fixture_cards_below_threshold')

    eligibility = len(penalties) == 0
    return {
        'eligibility': eligibility,
        'penalties': penalties,
        'gate': 'avg_cards>=4.0 and sample_size>=3 and top_fixture_cards>=5',
    }
