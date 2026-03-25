import json
from pathlib import Path
from .providers.direct_official_trunk_provider import BTTSDirectOfficialTrunkProvider
from .loaders.official_trunk_loader import BTTSOfficialTrunkLoader

def main():
    # run_minimal_flow.py está em <pack_root>/src/btts/
    # parents[2] == <pack_root>
    pack_root = Path(__file__).resolve().parents[2]

    fallback_path = pack_root / "support" / "fallback" / "fallback_official_trunk_input_btts.json"
    output_path = pack_root / "sample_output" / "market_pick_v1_1_btts.json"

    provider = BTTSDirectOfficialTrunkProvider(fallback_path)
    payload = provider.build_official_input(140, 2024, fixture_index=0)

    loader = BTTSOfficialTrunkLoader()
    match = loader.load(payload)

    exported = {
        "schema_version": "market_pick.v1.1",
        "pick_id": f"btts_{match.event_id}_{match.selection_hint}",
        "created_at": "2026-03-24T12:00:00Z",
        "module_id": "btts",
        "module_version": "btts_engine.v1.1",
        "event_id": match.event_id,
        "match_label": match.match_label,
        "competition": match.competition,
        "kickoff_datetime": match.kickoff_datetime,
        "market_family": "btts",
        "market": match.market,
        "selection": "BTTS Yes" if match.selection_hint == "yes" else "BTTS No",
        "line": None,
        "odds": match.odds.get("btts_yes" if match.selection_hint == "yes" else "btts_no"),
        "eligibility": True,
        "score_raw": 66.71,
        "confidence_raw": 3,
        "risk_raw": 2,
        "edge_raw": "acceptable",
        "rationale_summary": "Bilateralidade ofensiva suficiente, concessão útil dos dois lados e timing favorável sem bloqueio estrutural forte.",
        "main_drivers": ["bos_strong", "bvs_supportive", "fgt_positive", "tsi_stable_enough"],
        "penalties": [],
        "data_quality_flag": match.data_api_context.get("data_quality_flag", "partial"),
        "module_rank_internal": 1,
        "expiry_context": "refresh_if_odds_move_5pct",
        "module_specific_payload": {
            "btts_direction": match.selection_hint,
            "input_context": match.data_api_context,
        },
    }

    output_path.write_text(json.dumps(exported, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Generated: {output_path}")
    print(f"Source profile: {exported['module_specific_payload']['input_context'].get('source_profile')}")
    print(f"Score: {exported['score_raw']} | Eligibility: {exported['eligibility']}")

if __name__ == "__main__":
    main()
