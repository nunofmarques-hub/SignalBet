import json
from pathlib import Path
from bankroll_allocator import allocate_shortlist

def main():
    base = Path(__file__).resolve().parent.parent
    input_path = base / 'examples' / 'gps_shortlist_input.json'
    payload = json.loads(input_path.read_text(encoding='utf-8'))
    shortlist = payload.get('shortlist', [])
    allocated, used = allocate_shortlist(shortlist, max_total_units=10.0)
    approved_count = len([x for x in allocated if x.get('approved')])
    rejected_count = len([x for x in allocated if not x.get('approved')])
    result = {
        'bankroll_version': '1.0.0',
        'max_total_units': 10.0,
        'approved_count': approved_count,
        'rejected_count': rejected_count,
        'total_allocated_units': used,
        'execution_payload': allocated,
        'result': 'green' if approved_count > 0 and used > 0 else 'red'
    }
    out_path = base / 'examples' / 'bankroll_smoke_output_generated.json'
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result['result'] != 'green':
        raise SystemExit(1)

if __name__ == '__main__':
    main()
