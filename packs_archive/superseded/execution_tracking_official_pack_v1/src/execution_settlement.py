def summarize_ledger(ledger):
    settled = [x for x in ledger if x.get('settlement_status') in ('won', 'lost')]
    pending = [x for x in ledger if x.get('settlement_status') == 'pending']
    won = [x for x in ledger if x.get('settlement_status') == 'won']
    lost = [x for x in ledger if x.get('settlement_status') == 'lost']
    total_stake = round(sum(x.get('stake_units', 0.0) for x in ledger), 2)
    resolved_stake = round(sum(x.get('stake_units', 0.0) for x in settled), 2)
    return {
        'ledger_count': len(ledger),
        'settled_count': len(settled),
        'pending_count': len(pending),
        'won_count': len(won),
        'lost_count': len(lost),
        'analytics_audit_output': {
            'total_stake_units': total_stake,
            'resolved_stake_units': resolved_stake,
            'status_breakdown': {
                'won': len(won),
                'lost': len(lost),
                'pending': len(pending),
            }
        }
    }
