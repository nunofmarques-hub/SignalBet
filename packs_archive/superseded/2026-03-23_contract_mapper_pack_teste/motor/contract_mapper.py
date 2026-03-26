from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def parse_market_label(label: str) -> tuple[str, float | None]:
    parts = (label or "").strip().split()
    direction = parts[0] if parts else "Unknown"
    line = None
    for token in parts:
        try:
            line = float(token)
            break
        except ValueError:
            continue
    return direction, line


def normalize_line(line: float | None) -> str:
    if line is None:
        return "na"
    return str(line).replace(".", "_")


def map_market_and_selection(direction: str, line: float | None) -> tuple[str, str]:
    if direction == "Over":
        return "match_corners_over", f"Over {line} Corners"
    if direction == "Under":
        return "match_corners_under", f"Under {line} Corners"
    return "match_corners_unknown", f"{direction} {line} Corners"


def build_data_quality_flag(eligibility: bool, alerts: list[str]) -> str:
    lowered = " | ".join(a.lower() for a in alerts)
    if not eligibility:
        return "invalid"
    if "qualidade" in lowered or "low data" in lowered:
        return "fragile"
    if "contradit" in lowered:
        return "fragile"
    if "fronteira" in lowered or "borderline" in lowered:
        return "partial"
    return "clean"


def build_context_flags(alerts: list[str]) -> dict[str, bool]:
    lowered = [a.lower() for a in alerts]
    return {
        "contradictory_read": any("contradit" in a for a in lowered),
        "borderline_market": any("fronteira" in a or "borderline" in a for a in lowered),
        "low_data_quality": any("qualidade" in a or "low data" in a for a in lowered),
    }


def map_team_scores(team_scores: dict[str, Any]) -> dict[str, float | None]:
    if "home" in team_scores or "away" in team_scores:
        return {"home": team_scores.get("home"), "away": team_scores.get("away")}
    values = list(team_scores.values())
    return {
        "home": values[0] if len(values) > 0 else None,
        "away": values[1] if len(values) > 1 else None,
    }


def build_pick_id(event_id: int, direction: str, line: float | None) -> str:
    return f"corners_{event_id}_{direction.lower()}_{normalize_line(line)}"


def map_corners_output_to_market_pick(
    corners_output: dict[str, Any],
    *,
    module_version: str,
    created_at: str | None = None,
    kickoff_datetime: str | None = None,
    odds: float | None = None,
    edge_raw: float | str | None = None,
    module_rank_internal: int | None = None,
    expiry_context: str | None = None,
) -> dict[str, Any]:
    event_id = int(corners_output["fixture_id"])
    market_label = str(corners_output["market"])
    direction, line = parse_market_label(market_label)
    market, selection = map_market_and_selection(direction, line)

    alerts = list(corners_output.get("alerts", []))
    eligibility = bool(corners_output.get("eligible", False))
    created_at = created_at or now_utc_iso()

    return {
        "schema_version": "market_pick.v1.1",
        "pick_id": build_pick_id(event_id, direction, line),
        "created_at": created_at,
        "module_id": "corners",
        "module_version": module_version,
        "event_id": event_id,
        "match_label": corners_output.get("game"),
        "competition": corners_output.get("competition"),
        "kickoff_datetime": kickoff_datetime,
        "market_family": "corners",
        "market": market,
        "selection": selection,
        "line": line,
        "odds": odds,
        "eligibility": eligibility,
        "score_raw": corners_output.get("score"),
        "confidence_raw": corners_output.get("confidence"),
        "risk_raw": corners_output.get("risk"),
        "edge_raw": edge_raw,
        "rationale_summary": corners_output.get("operational_conclusion"),
        "main_drivers": list(corners_output.get("main_drivers", [])),
        "penalties": alerts,
        "data_quality_flag": build_data_quality_flag(eligibility, alerts),
        "module_rank_internal": module_rank_internal,
        "expiry_context": expiry_context,
        "module_specific_payload": {
            "corner_projection": corners_output.get("estimated_total_corners"),
            "match_corner_bias": corners_output.get("market_bias"),
            "tempo_profile": corners_output.get("game_profile"),
            "team_scores": map_team_scores(corners_output.get("team_scores", {})),
            "line_grid": list(corners_output.get("line_grid", [])),
            "alerts": alerts,
            "context_flags": build_context_flags(alerts),
        },
    }
