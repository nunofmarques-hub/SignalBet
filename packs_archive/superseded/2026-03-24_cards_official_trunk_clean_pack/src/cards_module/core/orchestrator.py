from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict

from providers.mappers import map_context_to_engine_input
from providers.official_live_provider import load_cards_context
from cards_module.core.eligibility import evaluate_eligibility
from cards_module.core.scoring import build_score


def run_cards_pipeline(league_id: int, season: int) -> Dict:
    context = load_cards_context(league_id, season)
    engine_input = map_context_to_engine_input(context)
    eligibility = evaluate_eligibility(engine_input)
    scoring = build_score(engine_input)

    top_fixture = engine_input['top_fixture']
    payload = {
        'schema_version': 'market_pick.v1.1',
        'pick_id': f"cards_{league_id}_{season}_{top_fixture.get('fixture_id', 'na')}",
        'created_at': datetime.now(timezone.utc).isoformat(),
        'module_id': 'cards',
        'module_version': 'cards.1.1.0',
        'event_id': top_fixture.get('fixture_id'),
        'match_label': top_fixture.get('match_label'),
        'competition': top_fixture.get('competition'),
        'market_family': 'cards',
        'market': 'match_cards_over',
        'selection': 'Over 3.5 Cards',
        'line': 3.5,
        'odds': 1.80,
        'eligibility': eligibility['eligibility'],
        'score_raw': scoring['score_raw'],
        'confidence_raw': scoring['confidence_raw'],
        'risk_raw': scoring['risk_raw'],
        'edge_raw': scoring['edge_raw'],
        'rationale_summary': 'Leitura oficial do tronco baseada em fixtures e card events por fixture, com shortlist pelo maior contexto disciplinar observado.',
        'main_drivers': [
            f"source={engine_input.get('source')}",
            f"official_object={engine_input.get('official_object')}",
            f"provider={engine_input.get('official_provider')}",
            f"avg_cards={engine_input.get('avg_cards')}",
            f"sample_size={engine_input.get('sample_size')}",
            f"top_fixture_cards={top_fixture.get('cards_count', 0)}",
        ],
        'penalties': eligibility['penalties'],
        'data_quality_flag': 'clean' if engine_input.get('sample_size', 0) >= 3 else 'partial',
        'module_rank_internal': 1,
        'module_specific_payload': {
            'provider_official': engine_input.get('official_provider'),
            'official_object_consumed': engine_input.get('official_object'),
            'sample_size': engine_input.get('sample_size'),
            'avg_cards': engine_input.get('avg_cards'),
            'top_fixture_cards': top_fixture.get('cards_count', 0),
            'eligibility_gate': 'avg_cards>=4.0 and sample_size>=3 and top_fixture_cards>=5',
        },
    }
    return payload
