import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.append(str(SRC))

from corners.candidate_generation.generate_candidates import generate_all_cases

def main():
    cases = generate_all_cases(
        ROOT / "examples" / "trunk_fixtures_sample.json",
        ROOT / "examples" / "trunk_fixture_statistics_sample.json",
        ROOT / "examples" / "trunk_case_contexts.json",
    )
    summary = {"generated_cases": [], "count": 0}
    name_map = {
        "case_1_forte": "sample_output_case_1_candidate.json",
        "case_2_media": "sample_output_case_2_watchlist.json",
        "case_3_rejeitada": "sample_output_case_3_rejected.json",
    }
    for adapted, engine_output, candidate in cases:
        cid = adapted["case_id"]
        summary["generated_cases"].append({
            "case_id": cid,
            "score": candidate["score_raw"],
            "candidate_status": candidate["module_specific_payload"]["candidate_status"],
            "band": candidate["module_specific_payload"]["band"],
            "selection": candidate["selection"],
            "confidence_raw": candidate["confidence_raw"],
            "risk_raw": candidate["risk_raw"],
        })
        (ROOT / "examples" / name_map[cid]).write_text(json.dumps(candidate, ensure_ascii=False, indent=2), encoding="utf-8")
    summary["count"] = len(summary["generated_cases"])
    (ROOT / "examples" / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary

if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=2))
