from bankroll_rules import base_stake_for_pick, risk_level_for_pick

def allocate_shortlist(shortlist, max_total_units=10.0):
    allocated = []
    used = 0.0
    for pick in shortlist:
        approved = bool(pick.get('eligible', False))
        stake = 0.0
        if approved:
            stake = base_stake_for_pick(pick)
            if used + stake > max_total_units:
                stake = max(0.0, round(max_total_units - used, 2))
            if stake <= 0:
                approved = False
        if approved:
            used = round(used + stake, 2)
        allocated.append({
            'match_id': pick.get('match_id'),
            'source_module': pick.get('source_module'),
            'market': pick.get('market'),
            'score': pick.get('score'),
            'rank': pick.get('rank'),
            'stake_units': stake,
            'risk_level': risk_level_for_pick(pick),
            'approved': approved,
            'notes': pick.get('notes', ''),
        })
    return allocated, used
