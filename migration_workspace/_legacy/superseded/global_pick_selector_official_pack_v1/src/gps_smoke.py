import json
from pathlib import Path
from gps_normalizer import load_module_inputs, normalize_rows
from gps_ranker import rank_rows

def main():
    base = Path(__file__).resolve().parent.parent
    inputs_dir = base / 'examples' / 'module_inputs'
    rows = load_module_inputs(inputs_dir)
    normalized = normalize_rows(rows)
    ranked = rank_rows(normalized)
    result = {
        'gps_version': '1.0.0',
        'inputs_count': len(rows),
        'normalized_count': len(normalized),
        'generated_from_modules': sorted(list({r.get('source_module') for r in normalized if r.get('source_module')})),
        'shortlist_count': len(ranked),
        'shortlist': ranked,
        'result': 'green' if len(ranked) > 0 and len(set(r['source_module'] for r in normalized)) >= 3 else 'red'
    }
    out_path = base / 'examples' / 'gps_smoke_output_generated.json'
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result['result'] != 'green':
        raise SystemExit(1)

if __name__ == '__main__':
    main()
