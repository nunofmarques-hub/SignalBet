from __future__ import annotations

def build_shortlist(ranked_picks):
    shortlisted=[]; used=set()
    for pick in sorted(ranked_picks,key=lambda x:x['global_score'],reverse=True):
        if pick['priority_tier'] not in {'Best','Top','Actionable'}:
            pick['selection_status']='watch'; pick['shortlist_bucket']='watch'; continue
        if pick['event_id'] in used:
            pick['selection_status']='excluded_duplicate_fixture'; pick['shortlist_bucket']='watch'; continue
        pick['rank_position']=len(shortlisted)+1
        pick['selection_status']='selected'
        pick['shortlist_bucket']='core' if pick['priority_tier'] in {'Best','Top'} else 'support'
        pick['pool_status']='shortlisted'
        shortlisted.append(pick); used.add(pick['event_id'])
    return shortlisted
