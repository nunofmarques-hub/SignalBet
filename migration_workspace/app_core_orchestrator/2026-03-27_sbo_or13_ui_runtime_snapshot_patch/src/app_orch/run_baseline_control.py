from pathlib import Path
import json
from app_orch.intake.baseline_intake import load_demo_baseline
from app_orch.state.state_mapper import map_operational_state
from app_orch.ui_bridge.ui_payloads import build_ui_payloads

def run(out_dir: str = "runtime_outputs") -> dict:
    baseline, source_mode = load_demo_baseline()
    summary = map_operational_state(baseline, source_mode=source_mode)
    ui = build_ui_payloads(summary)

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "baseline_operational_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "ui_button_payload.json").write_text(json.dumps(ui["button_payload"], indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "ui_panel_payload.json").write_text(json.dumps(ui["panel_payload"], indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "ui_runtime_snapshot.json").write_text(json.dumps(ui["runtime_snapshot"], indent=2, ensure_ascii=False), encoding="utf-8")
    return {"summary": summary, **ui}
