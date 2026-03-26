from __future__ import annotations

def to_num(v):
    if isinstance(v,(int,float)): return float(v)
    return float(str(v).replace('%','').replace(',','.'))

def build_normalized_fields(payload: dict) -> dict:
    score=to_num(payload['score_raw'])
    if payload['module_id']=='btts' and score<=10: score*=10
    def level(x):
        if isinstance(x,int): return max(1,min(5,x))
        s=str(x).lower()
        mp={'muito baixa':1,'baixa':2,'média':3,'media':3,'alta':4,'muito alta':5,'muito baixo':1,'baixo':2,'moderado':3,'alto':4,'muito alto':5}
        return mp.get(s,3)
    edge=to_num(payload.get('edge_raw',0) or 0)
    edge_norm='weak' if edge<3 else 'acceptable' if edge<6 else 'strong' if edge<10 else 'very_strong'
    return {'score_norm_base':max(0,min(100,score)),'confidence_norm':level(payload['confidence_raw']),'risk_norm':level(payload['risk_raw']),'edge_norm':edge_norm}
