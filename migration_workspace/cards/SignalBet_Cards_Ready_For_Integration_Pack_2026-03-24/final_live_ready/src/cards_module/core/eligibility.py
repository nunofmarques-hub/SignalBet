from __future__ import annotations

from typing import Dict, Tuple


def evaluate_eligibility(engine_input: Dict) -> Tuple[bool, int, int, int, str, list[str], list[str]]:
    card_events_count = int(engine_input.get("card_events_count", 0))
    data_quality_flag = engine_input.get("data_quality_flag", "invalid")
    drivers = ["official_provider_consumption", f"card_events_detected={card_events_count}"]
    penalties = []

    if data_quality_flag != "clean":
        penalties.append("data_quality_not_clean")
    if card_events_count < 2:
        penalties.append("low_card_signal")

    eligible = data_quality_flag == "clean" and card_events_count >= 2
    score_raw = min(90, 55 + card_events_count * 8)
    confidence_raw = 4 if eligible else 2
    risk_raw = 2 if eligible else 4
    edge_raw = f"{max(0.0, (card_events_count - 1) * 2.5):.1f}%"
    rationale = (
        "Input oficial do trunk com sinal disciplinar suficiente para candidate."
        if eligible
        else "Input oficial do trunk sem sinal disciplinar suficiente para candidate."
    )
    return eligible, score_raw, confidence_raw, risk_raw, edge_raw, drivers, penalties, rationale
