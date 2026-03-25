from __future__ import annotations

def export_frozen_batch(shortlisted, selector_run_id: str, normalization_version: str):
    generated_at='2026-03-24T12:05:00+00:00'
    picks=[]
    for p in shortlisted:
        picks.append({'selector_schema_version':'selector_pick.v1.1','pick_id':p['pick_id'],'module_id':p['module_id'],'module_version':p['module_version'],'event_id':p['event_id'],'match_label':p['match_label'],'market_family':p['market_family'],'market':p['market'],'selection':p['selection'],'line':p.get('line'),'odds':p['odds'],'global_score':p['global_score'],'confidence_norm':p['confidence_norm'],'risk_norm':p['risk_norm'],'edge_norm':p['edge_norm'],'priority_tier':p['priority_tier'],'priority_tier_reason':p['priority_tier_reason'],'conflict_flags':p['conflict_flags'],'correlation_flags':p['correlation_flags'],'executive_rationale':p['executive_rationale'],'selector_decision_note':p['selector_decision_note'],'pool_status':'exported_to_bankroll','normalization_version':normalization_version,'rank_position':p['rank_position'],'shortlist_bucket':p['shortlist_bucket'],'selection_status':p['selection_status'],'exported_at':generated_at})
    return {'batch_schema_version':'bankroll_export_batch.frozen.v3','selector_run_id':selector_run_id,'generated_at':generated_at,'normalization_version':normalization_version,'shortlist_size':len(picks),'picks':picks}
