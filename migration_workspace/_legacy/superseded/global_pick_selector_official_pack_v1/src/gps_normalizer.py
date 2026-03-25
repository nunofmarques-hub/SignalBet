import json
from pathlib import Path

def load_module_inputs(base_dir):
    inputs_dir = Path(base_dir)
    rows = []
    for path in sorted(inputs_dir.glob('*.json')):
        payload = json.loads(path.read_text(encoding='utf-8'))
        if isinstance(payload, list):
            rows.extend(payload)
    return rows

def normalize_rows(rows):
    normalized = []
    for row in rows:
        normalized.append({
            'match_id': row.get('match_id'),
            'source_module': row.get('source_module'),
            'market': row.get('market'),
            'score': row.get('score', 0),
            'confidence': row.get('confidence', 'desconhecida'),
            'eligible': bool(row.get('eligible', False)),
            'notes': row.get('notes', ''),
        })
    return normalized
