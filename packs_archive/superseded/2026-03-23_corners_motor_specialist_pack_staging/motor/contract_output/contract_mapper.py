from datetime import datetime, timezone

def now_utc_iso():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

def parse_market_label(label):
    parts = (label or "").strip().split()
    direction = parts[0] if parts else "Unknown"
    line = None
    for token in parts:
        try:
            line = float(token); break
        except ValueError:
            pass
    return direction, line

def build_data_quality_flag(eligibility, alerts):
    lowered = " | ".join(a.lower() for a in alerts)
    if not eligibility: return "invalid"
    if "contradit" in lowered: return "fragile"
    if "fronteira" in lowered: return "partial"
    return "clean"

def map_corners_output_to_market_pick(corners_output, module_version, kickoff_datetime=None, odds=None, edge_raw=None, module_rank_internal=None, expiry_context=None):
    direction, line = parse_market_label(str(corners_output["market"]))
    market = "match_corners_over" if direction == "Over" else "match_corners_under"
    selection = f"{direction} {line} Corners"
    return {
        "schema_version": "market_pick.v1.1",
        "pick_id": f"corners_{corners_output['fixture_id']}_{direction.lower()}_{str(line).replace('.', '_')}",
        "created_at": now_utc_iso(),
        "module_id": "corners",
        "module_version": module_version,
        "event_id": corners_output["fixture_id"],
        "match_label": corners_output["game"],
        "competition": corners_output["competition"],
        "kickoff_datetime": kickoff_datetime,
        "market_family": "corners",
        "market": market,
        "selection": selection,
        "line": line,
        "odds": odds,
        "eligibility": corners_output["eligible"],
        "score_raw": corners_output["score"],
        "confidence_raw": corners_output["confidence"],
        "risk_raw": corners_output["risk"],
        "edge_raw": edge_raw,
        "rationale_summary": corners_output["operational_conclusion"],
        "main_drivers": corners_output["main_drivers"],
        "penalties": corners_output["alerts"],
        "data_quality_flag": build_data_quality_flag(corners_output["eligible"], corners_output["alerts"]),
        "module_rank_internal": module_rank_internal,
        "expiry_context": expiry_context,
        "module_specific_payload": {
            "corner_projection": corners_output["estimated_total_corners"],
            "match_corner_bias": corners_output["market_bias"],
            "tempo_profile": corners_output["game_profile"],
            "team_scores": corners_output["team_scores"],
            "line_grid": corners_output["line_grid"],
            "candidate_status": corners_output.get("candidate_status"),
            "band": corners_output.get("band"),
            "rationale": corners_output.get("rationale"),
            "alerts": corners_output["alerts"],
        },
    }
