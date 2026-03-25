from __future__ import annotations
from pathlib import Path
from app_orch.util.io import read_json

def discover(pack_root: str, profile: str, forced_modules=None):
    root = Path(pack_root)
    mods = read_json(root / 'src' / 'app_orch' / 'man' / 'modules.json')['modules']
    prof = read_json(root / 'src' / 'app_orch' / 'man' / 'profiles.json')['profiles'][profile]
    subset = forced_modules or prof.get('module_subset', [])
    eligible, skipped = [], []
    for m in sorted(mods, key=lambda x: x['run_order']):
        mid = m['module_id']
        if not m.get('enabled'):
            skipped.append({'module_id': mid, 'reason': 'disabled_registry'})
            continue
        if subset and mid not in subset:
            skipped.append({'module_id': mid, 'reason': 'outside_profile_subset'})
            continue
        eligible.append(m)
    return eligible, skipped


def _candidate_paths(project_root: Path, module_id: str):
    return [
        (project_root / 'integration_feeds' / module_id / 'latest.json', 'project_integration_feed'),
        (project_root / 'runtime' / 'mod_out' / f'{module_id}_output.json', 'project_runtime_mod_out'),
        (project_root / 'mod_out' / f'{module_id}_output.json', 'project_mod_out_root'),
    ]


def run_modules(project_root: str, modules: list[dict]):
    root = Path(project_root)
    results, run, failed = [], [], []
    for m in modules:
        mid = m['module_id']
        found = None
        src = ''
        for candidate, source in _candidate_paths(root, mid):
            if candidate.exists():
                found = candidate
                src = source
                break
        if found is None:
            results.append({'module_id': mid, 'status': 'FAIL', 'warnings': ['Feed não encontrado.'], 'errors': ['module_output_missing'], 'candidates_count': 0, 'candidates': [], 'source_type': 'missing', 'source_path': ''})
            failed.append({'module_id': mid, 'reason': 'output_missing'})
            continue
        payload = read_json(found)
        if not isinstance(payload, dict) or 'candidates' not in payload:
            results.append({'module_id': mid, 'status': 'FAIL', 'warnings': ['Payload inválido.'], 'errors': ['module_output_invalid'], 'candidates_count': 0, 'candidates': [], 'source_type': src, 'source_path': str(found)})
            failed.append({'module_id': mid, 'reason': 'output_invalid'})
            continue
        payload['source_type'] = src
        payload['source_path'] = str(found)
        results.append(payload)
        if payload.get('status') == 'PASS':
            run.append(mid)
        else:
            failed.append({'module_id': mid, 'reason': payload.get('status','WARN').lower()})
    return results, run, failed
