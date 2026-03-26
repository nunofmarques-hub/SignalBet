"""End-to-end orchestration for a single cards pick generation."""

from __future__ import annotations

from typing import Any, Dict, Tuple

from cards_module.core.eligibility import evaluate_eligibility
from cards_module.core.indicators import compute_indicators
from cards_module.core.mapper import map_to_contract
from cards_module.core.scoring import compute_score, derive_confidence, derive_edge, derive_risk
from cards_module.core.validator import validate_payload
from cards_module.types import RawAssessment


def build_drivers(indicators: Dict[str, float]) -> list[str]:
    drivers = []
    if indicators.get("projection_total_cards", 0.0) >= 5.0:
        drivers.append(f"match_cards_projection={indicators['projection_total_cards']}")
    if indicators.get("competitive_context", 0.0) >= 60:
        drivers.append("match_tension=high")
    if indicators.get("referee", 0.0) >= 60:
        drivers.append("referee_bias=over_support")
    if indicators.get("recent_trend", 0.0) >= 55:
        drivers.append("recent_intensity_signal=positive")
    return drivers


def build_penalties(indicators: Dict[str, float], odds_input: Dict[str, Any]) -> list[str]:
    penalties = []
    if odds_input.get("market", {}).get("line", 0) and odds_input["market"]["line"] >= 5.5:
        penalties.append("line_already_high")
    if indicators.get("tactical_asymmetry", 0.0) >= 70:
        penalties.append("asymmetry_elevated")
    return penalties


def run(match_input: Dict[str, Any], odds_input: Dict[str, Any]) -> Tuple[Dict[str, Any], list[str]]:
    indicators = compute_indicators(match_input, odds_input)
    data_quality_flag = match_input.get("data_quality_flag", "clean")
    score_raw = compute_score(indicators)
    confidence_raw = derive_confidence(score_raw, data_quality_flag)
    risk_raw = derive_risk(indicators, data_quality_flag)
    edge_raw = derive_edge(indicators.get("projection_total_cards", 0.0), odds_input.get("market", {}).get("line"))

    drivers = build_drivers(indicators)
    penalties = build_penalties(indicators, odds_input)
    eligibility, reason = evaluate_eligibility(score_raw, confidence_raw, risk_raw, drivers, data_quality_flag)
    if not eligibility:
        penalties.append(reason)

    rationale_summary = (
        "Jogo com contexto disciplinar favorável ao mercado, suportado por perfil combinado, "
        "intensidade competitiva e leitura arbitral."
        if eligibility else
        "Leitura disciplinar insuficiente para pick elegível no estado atual dos dados."
    )

    market = odds_input.get("market", {}).get("market", "match_cards_over")
    selection = odds_input.get("market", {}).get("selection", "Over 4.5 Cards")
    line = odds_input.get("market", {}).get("line")
    odds = odds_input.get("market", {}).get("odds")

    assessment = RawAssessment(
        market=market,
        selection=selection,
        line=line,
        odds=odds,
        score_raw=score_raw,
        confidence_raw=confidence_raw,
        risk_raw=risk_raw,
        edge_raw=edge_raw,
        eligibility=eligibility,
        rationale_summary=rationale_summary,
        main_drivers=drivers,
        penalties=penalties,
        data_quality_flag=data_quality_flag,
        module_rank_internal=1,
        expiry_context="refresh_if_odds_move_5pct_or_referee_changes",
        module_specific_payload={
            "discipline_profile": "hot" if indicators.get("projection_total_cards", 0) >= 5.0 else "balanced",
            "match_cards_projection": indicators.get("projection_total_cards"),
            "home_cards_projection": indicators.get("projection_home_cards"),
            "away_cards_projection": indicators.get("projection_away_cards"),
            "match_tension_flag": "high" if indicators.get("competitive_context", 0) >= 60 else "medium",
            "competitive_pressure": "high" if indicators.get("competitive_context", 0) >= 60 else "normal",
            "referee_used": bool(match_input.get("referee")),
            "referee_bias": "over_support" if indicators.get("referee", 0) >= 60 else "neutral",
            "referee_confidence": "medium",
            "home_away_asymmetry": "elevated" if indicators.get("tactical_asymmetry", 0) >= 60 else "balanced",
            "recent_intensity_signal": "positive_for_over" if indicators.get("recent_trend", 0) >= 55 else "neutral",
            "structural_bias": "over" if indicators.get("projection_total_cards", 0) > (line or 0) else "neutral",
            "signal_consistency": "medium_high" if score_raw >= 75 else "medium",
            "sample_depth_flag": match_input.get("sample_depth_flag", "medium"),
        },
    )

    payload = map_to_contract(match_input, assessment)
    errors = validate_payload(payload)
    return payload, errors
