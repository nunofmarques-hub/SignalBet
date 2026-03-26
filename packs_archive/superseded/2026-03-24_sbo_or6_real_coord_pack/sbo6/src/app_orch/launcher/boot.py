from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
from app_orch.util.paths import resolve_project_root

def bootstrap(run_request: dict, pack_root: Path):
    project_root, project_mode, checked_paths = resolve_project_root(run_request, pack_root)
    return {
        'run_id': datetime.now(timezone.utc).strftime('RUN-%Y%m%d-%H%M%S'),
        'run_profile': run_request.get('run_profile', 'validation_run'),
        'started_at': datetime.now(timezone.utc).isoformat(),
        'pack_root': str(pack_root),
        'project_root': str(project_root),
        'project_mode': project_mode,
        'checked_paths': checked_paths,
        'forced_modules': run_request.get('forced_modules', []),
    }
