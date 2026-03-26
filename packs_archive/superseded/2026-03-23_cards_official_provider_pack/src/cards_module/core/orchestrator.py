from __future__ import annotations

from datetime import datetime, UTC
from hashlib import md5
from typing import Any, Dict

from cards_module.core.scoring import compute_projection, compute_score
from cards_module.core.eligibility import evaluate_eligibility


def build_pick(engine_input: Dict[str, Any]) -> Dict[str, Any]:
    fixture = engine_input["fixture"]
    market = engine_input["market"]
    projection = compute_projection(engine_input)
    score_block = compute_score(engine_input, projection)
    gate = evaluate_eligibility(engine_input, score_block, projection)

    created_at = datetime.now(UTC).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    raw_id = f'{fixture["event_id"]}|{market["market"]}|{market["selection"]}|{market["line"]}'
    pick_id = 'cards_' + md5(raw_id.encode('utf-8')).hexdigest()[:12]

    main_drivers = [
        f'match_cards_projection={projection["match_cards_projection"]}',
        f'match_tension={engine_input["discipline_profile"]["match_tension_flag"]}',
        f'competitive_pressure={engine_input["discipline_profile"]["competitive_pressure"]}',
    ]
    if engine_input["discipline_profile"].get("referee_used"):
        main_drivers.append(f'referee_cards_avg={engine_input["discipline_profile"]["referee_cards_avg"]}')

    pick = {
        "schema_version": "market_pick.v1.1",
        "pick_id": pick_id,
        "created_at": created_at,
        "module_id": "cards",
        "module_version": "cards.1.1.0-staging",
        "event_id": fixture["event_id"],
        "match_label": fixture["match_label"],
        "competition": fixture["competition"],
        "kickoff_datetime": fixture["kickoff_datetime"],
        "market_family": "cards",
        "market": market["market"],
        "selection": market["selection"],
        "line": market["line"],
        "odds": market["odds"],
        "eligibility": gate["eligibility"],
        "score_raw": score_block["score_raw"],
        "confidence_raw": score_block["confidence_raw"],
        "risk_raw": score_block["risk_raw"],
        "edge_raw": score_block["edge_raw"],
        "rationale_summary": fixture.get("rationale_summary") or (
            "Sinal disciplinar construído a partir do provider central, com projeção, contexto competitivo e filtro de elegibilidade."
        ),
        "main_drivers": main_drivers,
        "penalties": gate["penalties"],
        "data_quality_flag": engine_input["data_quality_flag"],
        "module_rank_internal": 1 if gate["eligibility"] else 9,
        "expiry_context": "refresh_if_odds_move_or_referee_changes",
        "module_specific_payload": {
            "discipline_profile": "hot" if projection["match_cards_projection"] >= market["line"] + 0.7 else "balanced",
            **projection,
            "match_tension_flag": engine_input["discipline_profile"]["match_tension_flag"],
            "competitive_pressure": engine_input["discipline_profile"]["competitive_pressure"],
            "referee_used": engine_input["discipline_profile"]["referee_used"],
            "referee_bias": "over_support" if engine_input["discipline_profile"]["referee_cards_avg"] >= 5.0 else "neutral",
            "referee_confidence": "medium" if engine_input["discipline_profile"]["referee_used"] else "low",
            "home_away_asymmetry": engine_input["discipline_profile"]["home_away_asymmetry"],
            "recent_intensity_signal": engine_input["discipline_profile"]["recent_intensity_signal"],
            "structural_bias": score_block["structural_bias"],
            "signal_consistency": "medium_high" if score_block["score_raw"] >= 75 else "medium",
            "sample_depth_flag": engine_input["sample_depth_flag"],
            "provider_name": fixture.get("provider_name", "central_cards_provider.v1"),
            "provider_status": gate["status"],
        },
    }
    return pick
