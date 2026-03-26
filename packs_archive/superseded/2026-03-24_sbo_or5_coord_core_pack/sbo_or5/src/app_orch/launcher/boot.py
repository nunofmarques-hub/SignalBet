from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import uuid
from app_orch.util.paths import resolve_project_root

def run_id():
    ts = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    return f'RUN-{ts}-{uuid.uuid4().hex[:6].upper()}'

def boot(req: dict, pack_root: Path):
    project_root, mode, checked = resolve_project_root(req, pack_root)
    return {
        'run_id': run_id(),
        'run_profile': req.get('run_profile', 'validation_run'),
        'initiated_by': req.get('initiated_by', 'system'),
        'dry_run': bool(req.get('dry_run', False)),
        'forced_modules': req.get('forced_modules', []),
        'started_at': datetime.now(timezone.utc).isoformat(),
        'pack_root': str(pack_root),
        'project_root': str(project_root),
        'project_mode': mode,
        'checked_paths': checked,
    }
