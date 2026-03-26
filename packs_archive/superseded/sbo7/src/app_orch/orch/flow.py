from __future__ import annotations

def collect(run_id: str, mod_results: list[dict]):
    cands = []
    sources = {}
    for r in mod_results:
        sources[r['module_id']] = {'source_type': r.get('source_type',''), 'source_path': r.get('source_path','')}
        if r.get('status') != 'PASS':
            continue
        for c in r.get('candidates', []):
            item = dict(c)
            item['source_module'] = r['module_id']
            cands.append(item)
    return {'run_id': run_id, 'candidate_count': len(cands), 'candidates': cands, 'sources': sources}

def gps(pool: dict):
    ordered = sorted(pool['candidates'], key=lambda x: x.get('confidence', 0), reverse=True)
    return {'status': 'PASS', 'shortlist': ordered[:5], 'selected_count': min(5, len(ordered)), 'pool_size': pool['candidate_count']}

def bank(gps_out: dict):
    approved, reduced, blocked = [], [], []
    for item in gps_out['shortlist']:
        conf = item.get('confidence', 0)
        if conf >= 0.80:
            approved.append(item)
        elif conf >= 0.70:
            reduced.append(item)
        else:
            blocked.append(item)
    return {'status': 'PASS', 'approved': approved, 'reduced': reduced, 'blocked': blocked, 'reserve': []}

def exec_reg(bank_out: dict, dry_run: bool):
    if dry_run:
        return {'status': 'SKIPPED', 'message': 'validation_run sem execution real'}
    return {'status': 'PASS', 'message': 'execution registada em draft'}
