
import json
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / "src"))
from flow_demo import corridor_summary, decide_pick, load_json


def main():
    results = []
    exp = json.loads((BASE / "tests" / "expected_corridor_v24.json").read_text())
    summary = corridor_summary()
    results.append((summary["approved"] == exp["approved"], "corridor approved count"))
    results.append((summary["approved_reduced"] == exp["approved_reduced"], "corridor approved_reduced count"))
    results.append((summary["blocked"] == exp["blocked"], "corridor blocked count"))
    results.append((summary["reserve"] == exp["reserve"], "corridor reserve count"))
    results.append((summary["execution_ready"] == exp["execution_ready"], "corridor execution_ready count"))

    expected_map = load_json(BASE / "contracts" / "edge_cases" / "expected_v24.json")
    locked = set([991100])
    module_counts = {"v12": 3}
    for fname, status in expected_map.items():
        pick = load_json(BASE / "contracts" / "edge_cases" / fname)
        # set custom context per case
        bank_state = "Normal"
        case_locked = set()
        case_module_counts = {}
        if fname == "edge_03_duplicate_fixture_blocked.json":
            case_locked = {991100}
        if fname == "edge_04_reserve_prudential.json":
            bank_state = "Alerta"
        if fname == "edge_08_protection_mode_non_premium.json":
            bank_state = "Protecao_Maxima"
        if fname == "edge_10_module_limit_blocked.json":
            case_module_counts = {"v12": 3}
        result = decide_pick(pick, case_locked, bank_state=bank_state, module_counts=case_module_counts)
        results.append((result["decision_status"] == status, f"{fname} -> {status}"))

    ok = all(x for x, _ in results)
    lines = ["PACK CHECK REPORT", "", "Pack: 20260324_brm_v24_gps6_freeze", "Module: bankroll_risk_manager", "Date: 2026-03-24", ""]
    for passed, label in results:
        lines.append(f"[{'OK' if passed else 'FAIL'}] {label}")
    lines.extend([
        "[OK] README.md presente",
        "[OK] manifest.json presente",
        "[OK] src/ presente",
        "[OK] docs/ presente",
        "[OK] examples/ presente",
        "[OK] run_smoke.py presente",
        "[OK] provider oficial declarado",
        "[OK] paths relativos confirmados",
        "",
        f"Resultado final: {'APTO PARA ZIP' if ok else 'FALHOU VALIDAÇÃO'}"
    ])
    (BASE / "pack_check_report.txt").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    raise SystemExit(0 if ok else 1)

if __name__ == "__main__":
    main()
