
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict
import uuid

def generate_run_id() -> str:
    ts = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    return f'RUN-{ts}-{uuid.uuid4().hex[:6].upper()}'

def bootstrap(run_request: Dict[str, Any], pack_root: Path) -> Dict[str, Any]:
    project_root = run_request.get('project_root', 'examples/demo_data_api')
    project_root_path = (pack_root / project_root).resolve() if not Path(project_root).is_absolute() else Path(project_root)
    return {
        'run_id': generate_run_id(),
        'run_profile': run_request.get('run_profile', 'validation_run'),
        'initiated_by': run_request.get('initiated_by', 'system'),
        'dry_run': bool(run_request.get('dry_run', False)),
        'forced_modules': run_request.get('forced_modules', []),
        'data_snapshot_tag': run_request.get('data_snapshot_tag', 'latest'),
        'correlation_id': run_request.get('correlation_id', uuid.uuid4().hex),
        'started_at': datetime.now(timezone.utc).isoformat(),
        'pack_root': str(pack_root),
        'project_root': str(project_root_path),
    }
