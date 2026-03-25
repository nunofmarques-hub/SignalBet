def base_stake_for_pick(pick):
    rank = pick.get('rank', 99)
    score = pick.get('score', 0)
    if rank == 1:
        stake = 3.0
    elif rank == 2:
        stake = 2.5
    elif rank == 3:
        stake = 2.0
    elif rank == 4:
        stake = 1.5
    else:
        stake = 1.0
    if score >= 80:
        stake += 0.0
    elif score < 70:
        stake -= 0.5
    return max(stake, 0.5)

def risk_level_for_pick(pick):
    score = pick.get('score', 0)
    if score >= 80:
        return 'medium'
    if score >= 70:
        return 'medium'
    return 'low'
