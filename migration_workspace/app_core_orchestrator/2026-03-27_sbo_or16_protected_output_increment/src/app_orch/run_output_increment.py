from pathlib import Path
import json
from app_orch.intake.central_intake import load_central_corridor
from app_orch.state.output_increment import build_semantic_center
from app_orch.ui_bridge.protected_output import build_protected_output

def run(project_root: str | None = None, out_dir: str = "runtime_outputs") -> dict:
    pr = Path(project_root) if project_root else None
    corridor, source_mode = load_central_corridor(project_root=pr)
    state = build_semantic_center(corridor, source_mode=source_mode)
    protected = build_protected_output(state)

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "central_corridor_semantic_state.json").write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "central_corridor_protected_output_increment.json").write_text(json.dumps(protected, indent=2, ensure_ascii=False), encoding="utf-8")
    return {"state": state, "protected": protected}
