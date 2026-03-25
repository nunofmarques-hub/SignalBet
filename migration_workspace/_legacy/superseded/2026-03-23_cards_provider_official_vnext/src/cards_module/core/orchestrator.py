from __future__ import annotations

from typing import Any, Dict, Tuple, List

from cards_module.core.scoring import compute_score
from cards_module.core.eligibility import decide_eligibility
from cards_module.io.exporter import build_output
from cards_module.io.validator import validate_output


def run_pipeline(engine_input: Dict[str, Any]) -> Tuple[Dict[str, Any], List[str]]:
    scored = compute_score(engine_input)
    decision = decide_eligibility(engine_input, scored)
    payload = build_output(engine_input, scored, decision)
    errors = validate_output(payload)
    return payload, errors
