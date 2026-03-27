from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
from app_orch.util.paths import resolve_project_root
from app_orch.util.io import read_json

def bootstrap(run_request: dict, pack_root: Path):
    profiles = read_json(pack_root / 'src' / 'app_orch' / 'man' / 'profiles.json')['profiles']
    profile_name = run_request.get('run_profile', 'validation_run')
    profile = profiles.get(profile_name, profiles['validation_run'])
    project_root, project_mode, checked_paths = resolve_project_root(run_request, pack_root)
    dry_run = run_request.get('dry_run', profile.get('dry_run', True))
    strict_real_project = run_request.get('require_real_project_root', profile.get('strict_real_project', False))
    strict_real_feeds = run_request.get('require_real_module_feeds', profile.get('strict_real_feeds', False))
    target_intent = 'real_proof' if (strict_real_project or strict_real_feeds or profile_name in ('validation_run_real','validation_run_proof')) else 'staging'
    return {
        'run_id': datetime.now(timezone.utc).strftime('RUN-%Y%m%d-%H%M%S'),
        'run_profile': profile_name,
        'started_at': datetime.now(timezone.utc).isoformat(),
        'pack_root': str(pack_root),
        'project_root': str(project_root),
        'project_mode': project_mode,
        'checked_paths': checked_paths,
        'forced_modules': run_request.get('forced_modules', []),
        'dry_run': dry_run,
        'strict_real_project': strict_real_project,
        'strict_real_feeds': strict_real_feeds,
        'initiated_by': run_request.get('initiated_by', 'ui_button'),
        'target_intent': target_intent,
    }
