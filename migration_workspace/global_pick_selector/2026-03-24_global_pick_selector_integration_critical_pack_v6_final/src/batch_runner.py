from __future__ import annotations
from schema_validator import validate_pick
from normalization import build_normalized_fields
from flags import evaluate_pick_flags, apply_theme_cluster
from ranking_breakdown import build_breakdown
from ranking import compute_final_score
from explainability import build_explainability
from shortlist import build_shortlist
from exports_to_bankroll import export_frozen_batch

def run_batch(batch_payload: dict, selector_run_id: str = 'gps_run_v6', normalization_version: str = 'norm.v1.1'):
    ranked=[]; raw=[]
    for payload in batch_payload['picks']:
        v=validate_pick(payload)
        if not v['valid']: continue
        n=build_normalized_fields(payload)
        f=evaluate_pick_flags(payload,existing_raw=raw)
        b=build_breakdown(n)
        fs=compute_final_score(payload,n,f['adjustments'],b)
        e=build_explainability(b,fs,f)
        ranked.append({'pick_id':payload['pick_id'],'module_id':payload['module_id'],'module_version':payload['module_version'],'event_id':payload['event_id'],'match_label':payload['match_label'],'market_family':payload['market_family'],'market':payload['market'],'selection':payload['selection'],'line':payload.get('line'),'odds':payload['odds'],'confidence_norm':n['confidence_norm'],'risk_norm':n['risk_norm'],'edge_norm':n['edge_norm'],'conflict_flags':f['conflict_flags'],'correlation_flags':f['correlation_flags'],**f['adjustments'],**b,**fs,'global_score':fs['global_score_final'],**e,'pool_status':'ranked','normalization_version':normalization_version})
        raw.append(payload)
    ranked=apply_theme_cluster(ranked)
    shortlisted=build_shortlist(ranked)
    exported=export_frozen_batch(shortlisted,selector_run_id,normalization_version)
    return {'ranked':ranked,'shortlisted':shortlisted,'exported':exported}
