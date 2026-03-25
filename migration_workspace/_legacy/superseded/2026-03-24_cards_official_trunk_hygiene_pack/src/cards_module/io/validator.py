from __future__ import annotations

from typing import Dict, List

REQUIRED_FIELDS = [
    'schema_version', 'pick_id', 'created_at', 'module_id', 'module_version',
    'event_id', 'match_label', 'competition', 'market_family', 'market', 'selection',
    'line', 'odds', 'eligibility', 'score_raw', 'confidence_raw', 'risk_raw', 'edge_raw',
    'rationale_summary', 'main_drivers', 'penalties', 'data_quality_flag', 'module_rank_internal',
    'module_specific_payload'
]


def validate_pick(payload: Dict) -> List[str]:
    errors: List[str] = []
    for field in REQUIRED_FIELDS:
        if field not in payload:
            errors.append(f'missing:{field}')
    if payload.get('schema_version') != 'market_pick.v1.1':
        errors.append('invalid:schema_version')
    if payload.get('module_id') != 'cards':
        errors.append('invalid:module_id')
    if payload.get('market_family') != 'cards':
        errors.append('invalid:market_family')
    if not isinstance(payload.get('main_drivers', []), list):
        errors.append('invalid:main_drivers')
    if not isinstance(payload.get('penalties', []), list):
        errors.append('invalid:penalties')
    return errors
