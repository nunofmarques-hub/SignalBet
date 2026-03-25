import json
from pathlib import Path
from execution_ledger import build_ledger
from execution_settlement import summarize_ledger

def main():
    base = Path(__file__).resolve().parent.parent
    input_path = base / 'examples' / 'bankroll_execution_input.json'
    payload = json.loads(input_path.read_text(encoding='utf-8'))
    execution_payload = payload.get('execution_payload', [])
    ledger = build_ledger(execution_payload)
    summary = summarize_ledger(ledger)
    result = {
        'execution_version': '1.0.0',
        **summary,
        'ledger': ledger,
        'result': 'green' if len(ledger) > 0 and summary['settled_count'] > 0 else 'red'
    }
    out_path = base / 'examples' / 'execution_smoke_output_generated.json'
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result['result'] != 'green':
        raise SystemExit(1)

if __name__ == '__main__':
    main()
