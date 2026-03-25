import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
REQUIRED = [
    'README.md', 'manifest.json', 'run_smoke.py', 'src', 'docs', 'examples', 'contracts'
]


def load_json(rel: str):
    return json.loads((BASE / rel).read_text(encoding='utf-8'))


def check_exists():
    out = []
    ok = True
    for item in REQUIRED:
        exists = (BASE / item).exists()
        out.append(f"[{'OK' if exists else 'FAIL'}] {item} presente")
        ok &= exists
    return ok, out


def check_manifest():
    m = load_json('manifest.json')
    needed = [
        'pack_name', 'module_name', 'pack_version', 'status', 'entrypoint',
        'provider_type', 'provider_name', 'provider_object', 'contract_version'
    ]
    missing = [k for k in needed if k not in m]
    return (not missing), [f"[{'OK' if not missing else 'FAIL'}] manifest campos mínimos"]


def check_examples():
    lines = []
    ok = True
    gps = load_json('examples/gps_batch_in_v22.json')
    bank = load_json('examples/bank_resp_batch_v22.json')
    exe = load_json('examples/exec_payload_v22.json')
    ok &= gps.get('selector_schema_version') == 'selector_pick_batch.v1.1'
    lines.append(f"[{'OK' if gps.get('selector_schema_version') == 'selector_pick_batch.v1.1' else 'FAIL'}] schema batch GPS")
    ok &= bank.get('bank_schema_version') == 'bank_decision_batch.v2.2'
    lines.append(f"[{'OK' if bank.get('bank_schema_version') == 'bank_decision_batch.v2.2' else 'FAIL'}] schema batch banca")
    ok &= exe.get('execution_schema_version') == 'execution_intake.v2.2'
    lines.append(f"[{'OK' if exe.get('execution_schema_version') == 'execution_intake.v2.2' else 'FAIL'}] schema execution")
    statuses = [
        load_json('examples/approved_v22.json').get('decision_status'),
        load_json('examples/approved_reduced_v22.json').get('decision_status'),
        load_json('examples/blocked_v22.json').get('decision_status'),
        load_json('examples/reserve_v22.json').get('decision_status'),
    ]
    ok &= statuses == ['APPROVED', 'APPROVED_REDUCED', 'BLOCKED', 'RESERVE']
    lines.append(f"[{'OK' if statuses == ['APPROVED', 'APPROVED_REDUCED', 'BLOCKED', 'RESERVE'] else 'FAIL'}] exemplos finais dos 4 estados")
    return ok, lines


def check_edge_cases():
    exp = load_json('contracts/edge_cases/expected_v22.json')
    ok = len(exp) >= 10
    return ok, [f"[{'OK' if ok else 'FAIL'}] edge cases >= 10"]


def main():
    checks = []
    overall = True
    for fn in [check_exists, check_manifest, check_examples, check_edge_cases]:
        ok, lines = fn()
        overall &= ok
        checks.extend(lines)
    report = [
        'PACK CHECK REPORT',
        '',
        'Pack: 20260324_brm_v22_official',
        f"Result: {'PASS' if overall else 'FAIL'}",
        '',
        *checks,
        ''
    ]
    text = '\n'.join(report)
    (BASE / 'pack_check_report.txt').write_text(text, encoding='utf-8')
    print(text)
    raise SystemExit(0 if overall else 1)


if __name__ == '__main__':
    main()
