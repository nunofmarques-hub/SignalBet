from __future__ import annotations
from collections import Counter

def evaluate_pick_flags(payload: dict, existing_raw=None):
    existing_raw=existing_raw or []
    conflict_flags=[]; correlation_flags=[]
    qa=ca=cora=ra=coa=0
    if payload.get('data_quality_flag')=='partial': correlation_flags.append('GOV_DATA_PARTIAL'); qa=-4
    same=[p for p in existing_raw if p.get('event_id')==payload.get('event_id')]
    if same: correlation_flags.append('DUP_SAME_FIXTURE'); cora-=2
    return {'conflict_flags':conflict_flags,'correlation_flags':correlation_flags,'adjustments':{'quality_adjustment':qa,'conflict_adjustment':ca,'correlation_adjustment':cora,'rationale_adjustment':ra,'completeness_adjustment':coa}}

def apply_theme_cluster(ranked_picks):
    return ranked_picks
