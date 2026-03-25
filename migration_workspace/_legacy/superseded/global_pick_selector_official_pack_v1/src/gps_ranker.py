def rank_rows(rows):
    eligible = [r for r in rows if r.get('eligible')]
    eligible.sort(key=lambda x: (x.get('score', 0), x.get('confidence') == 'alta'), reverse=True)
    ranked = []
    for idx, row in enumerate(eligible, start=1):
        item = dict(row)
        item['rank'] = idx
        ranked.append(item)
    return ranked
