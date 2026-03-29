from __future__ import annotations

import json
from pathlib import Path

from input_adapter import InputContractError
from provider_bridge import build_context_or_fail


BASE_DIR = Path(__file__).resolve().parents[1]
PAYLOAD_PATH = BASE_DIR / "runtime_inputs" / "protected_runtime_payload.json"
RESULT_PATH = BASE_DIR / "examples" / "runtime_fix_summary.json"


def main() -> int:
    try:
        context = build_context_or_fail(PAYLOAD_PATH)
        normalized = context["normalized_fixture"]
        summary = {
            "v12_runtime_fix": "OK",
            "fixture_id": normalized["fixture_id"],
            "league_id": normalized["league_id"],
            "source_mode": normalized["source_mode"],
            "observed_mode": normalized["observed_mode"],
            "readiness_level": normalized["readiness_level"],
            "home": normalized["home_team_name"],
            "away": normalized["away_team_name"],
            "over_1_5_team_context": normalized["over_1_5_team_context"],
            "over_1_5_match_context": normalized["over_1_5_match_context"],
            "under_3_5_match_context": normalized["under_3_5_match_context"],
            "runtime_status": context["runtime_status"],
            "message": "v12 isolated smoke passed with normalized protected input",
        }
        RESULT_PATH.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 0
    except InputContractError as exc:
        summary = {
            "v12_runtime_fix": "HARD_FAIL",
            "runtime_status": "hard_fail",
            "message": str(exc),
        }
        RESULT_PATH.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
