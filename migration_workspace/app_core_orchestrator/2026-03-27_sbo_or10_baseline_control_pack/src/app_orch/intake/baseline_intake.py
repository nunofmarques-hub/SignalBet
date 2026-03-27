from pathlib import Path
import json

DEFAULT_BASELINE_PATH = "examples/demo_data_api/baselines/baseline_state_green.json"

def load_baseline_state(project_root: Path | None = None, explicit_path: str | None = None) -> tuple[dict, str]:
    if explicit_path:
        p = Path(explicit_path)
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8")), "explicit"
    if project_root:
        candidates = [
            project_root / "data_api" / "baseline_state.json",
            project_root / "runtime_outputs" / "baseline_state.json",
            project_root / "snapshots" / "baseline_state.json",
        ]
        for p in candidates:
            if p.exists():
                return json.loads(p.read_text(encoding="utf-8")), "project"
    local = Path(__file__).resolve().parents[3] / DEFAULT_BASELINE_PATH
    return json.loads(local.read_text(encoding="utf-8")), "demo"
