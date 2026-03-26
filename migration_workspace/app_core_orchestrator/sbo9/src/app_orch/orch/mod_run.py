
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


def _official_candidates(project_root: Path, module_id: str):
    base = project_root / 'integration_feeds' / module_id
    ordered = [
        base / 'latest.json',
        base / f'{module_id}_output.json',
        base / 'module_output.json',
        base / 'output.json',
    ]
    return [(p, f'official:{p.relative_to(project_root)}') for p in ordered]


def _direct_fallback_candidates(project_root: Path, module_id: str):
    bases = [
        project_root / 'runtime' / 'mod_out' / module_id,
        project_root / 'mod_out' / module_id,
        project_root / 'migration_workspace' / module_id,
        project_root / 'modules' / module_id / 'out',
        project_root / 'modules' / module_id / 'examples',
    ]
    names = ['latest.json', f'{module_id}_output.json', 'module_output.json', 'output.json']
    out = []
    for b in bases:
        for n in names:
            out.append((b / n, f'fallback:{b.relative_to(project_root)}'))
    return out


def _recursive_fallback_candidates(project_root: Path, module_id: str):
    # examples/ is intentionally last and recursive scans are only tried after every direct path.
    bases = [
        project_root / 'runtime' / 'mod_out' / module_id,
        project_root / 'mod_out' / module_id,
        project_root / 'migration_workspace' / module_id,
        project_root / 'modules' / module_id / 'out',
        project_root / 'modules' / module_id / 'examples',
    ]
    out = []
    for b in bases:
        if b.exists():
            for p in sorted(b.rglob('*.json')):
                if any(k in p.name.lower() for k in ['candidate', 'output', 'latest']):
                    out.append((p, f'fallback_recursive:{b.relative_to(project_root)}'))
    return out


def _candidate_paths(project_root: Path, module_id: str):
    return (
        _official_candidates(project_root, module_id)
        + _direct_fallback_candidates(project_root, module_id)
        + _recursive_fallback_candidates(project_root, module_id)
    )


def _source_mode(project_root: Path, found: Path):
    root_str = str(project_root).replace("\\", "/").lower()
    if '/examples/project' in root_str or root_str.endswith('/examples/project'):
        return 'demo'
    try:
        found.relative_to(project_root)
        return 'project'
    except ValueError:
        return 'external'


def run_modules(project_root: str, modules: list[dict]):
    root = Path(project_root)
    results, run, failed = [], [], []
    feed_stats = {'project': 0, 'demo': 0, 'external': 0, 'missing': 0}
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
            feed_stats['missing'] += 1
            results.append({
                'module_id': mid,
                'status': 'FAIL',
                'warnings': ['Feed oficial não encontrado nos paths candidatos.'],
                'errors': ['output_missing'],
                'candidates_count': 0,
                'candidates': [],
                'source_type': 'missing',
                'source_mode': 'missing',
                'source_path': ''
            })
            failed.append({'module_id': mid, 'reason': 'output_missing'})
            continue
        payload = read_json(found)
        mode = _source_mode(root, found)
        feed_stats[mode] = feed_stats.get(mode, 0) + 1
        if not isinstance(payload, dict) or 'candidates' not in payload:
            results.append({
                'module_id': mid,
                'status': 'FAIL',
                'warnings': ['Feed encontrado, mas payload estruturalmente inválido.'],
                'errors': ['output_invalid'],
                'candidates_count': 0,
                'candidates': [],
                'source_type': src,
                'source_mode': mode,
                'source_path': str(found)
            })
            failed.append({'module_id': mid, 'reason': 'output_invalid'})
            continue
        result = {
            'module_id': mid,
            'status': payload.get('status', 'PASS'),
            'warnings': payload.get('warnings', []),
            'errors': payload.get('errors', []),
            'candidates_count': len(payload.get('candidates', [])),
            'candidates': payload.get('candidates', []),
            'source_type': src,
            'source_mode': mode,
            'source_path': str(found),
            'meta': payload.get('meta', {}),
        }
        results.append(result)
        if result['status'] == 'PASS':
            run.append(mid)
        else:
            failed.append({'module_id': mid, 'reason': result['status'].lower()})
    return results, run, failed, feed_stats
