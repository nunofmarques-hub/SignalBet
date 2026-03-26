from __future__ import annotations

from typing import Dict, List

from cards_module.schemas.contract import REQUIRED_KEYS


def validate_pick(payload: Dict) -> List[str]:
    errors: List[str] = []
    for key in REQUIRED_KEYS:
        if key not in payload:
            errors.append(f'MISSING:{key}')
    if payload.get('market_family') != 'cards':
        errors.append('INVALID:market_family')
    if payload.get('schema_version') != 'market_pick.v1.1':
        errors.append('INVALID:schema_version')
    if payload.get('data_quality_flag') not in {'clean', 'partial', 'fragile', 'invalid'}:
        errors.append('INVALID:data_quality_flag')
    return errors
