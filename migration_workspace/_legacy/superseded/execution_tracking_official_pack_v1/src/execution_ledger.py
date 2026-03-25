def build_ledger(execution_payload):
    ledger = []
    for idx, item in enumerate(execution_payload, start=1):
        ledger.append({
            'ledger_id': idx,
            'match_id': item.get('match_id'),
            'source_module': item.get('source_module'),
            'market': item.get('market'),
            'stake_units': item.get('stake_units', 0.0),
            'risk_level': item.get('risk_level'),
            'approved': bool(item.get('approved', False)),
            'settlement_status': item.get('settlement_status', 'pending'),
            'notes': item.get('notes', ''),
        })
    return ledger
