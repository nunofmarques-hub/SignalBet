
from __future__ import annotations

from typing import Any, Dict, Tuple

from cards_module.io.data_layer_adapter import adapt_payload
from cards_module.core.scoring import compute_scores
from cards_module.core.eligibility import decide_eligibility
from cards_module.io.exporter import build_output
from cards_module.io.validator import validate_output


def run(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], list[str]]:
    internal = adapt_payload(payload)
    scores = compute_scores(internal)
    decision = decide_eligibility(internal, scores)
    output = build_output(internal, scores, decision)
    errors = validate_output(output)
    return output, errors
