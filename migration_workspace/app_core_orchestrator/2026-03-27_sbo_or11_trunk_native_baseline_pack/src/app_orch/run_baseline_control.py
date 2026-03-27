from pathlib import Path
import json
from app_orch.intake.baseline_intake import load_baseline_state
from app_orch.state.state_mapper import map_operational_state
from app_orch.ui_bridge.ui_safe_bridge import build_ui_safe_status

def run(project_root: str | None = None, baseline_path: str | None = None, out_dir: str = "runtime_outputs") -> dict:
    pr = Path(project_root) if project_root else None
    baseline, source_mode = load_baseline_state(project_root=pr, explicit_path=baseline_path)
    summary = map_operational_state(baseline, source_mode=source_mode)
    ui_status = build_ui_safe_status(summary)

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "baseline_operational_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "ui_safe_status.json").write_text(json.dumps(ui_status, indent=2, ensure_ascii=False), encoding="utf-8")
    return {"summary": summary, "ui_status": ui_status}
