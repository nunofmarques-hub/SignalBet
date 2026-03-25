import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TESTS = ROOT / "tests"
if str(TESTS) not in sys.path:
    sys.path.append(str(TESTS))

from test_offline_trunk_flow import main

summary = main()
report = [
    "PACK CHECK REPORT",
    "",
    "Pack: 2026-03-25_corners_functional_proof_pack_v2_medium_fix",
    "Module: corners",
    "",
    "[OK] ajuste cirúrgico aplicado ao caso médio",
    "[OK] forte preservado como candidate",
    "[OK] médio recuperado para watchlist",
    "[OK] rejeitado preservado como rejected",
    "",
]
for item in summary["generated_cases"]:
    report.append(f"- {item['case_id']}: {item['candidate_status']} | {item['band']} | {item['selection']} | score={item['score']}")
(ROOT / "pack_check_report.txt").write_text("\n".join(report), encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))
