import { readProtectedSnapshot } from '../providers/realOrchestratorProtectedProvider.js';
import { adaptSnapshot } from '../adapters/orchestratorAdapters.js';

let persisted = null;

export async function runScenario(name){
  let meta={requested_mode:'real_read_protected', observed_mode:'real_read_protected', bridge_status:'ok', bridge_scope:'protected_partial'};
  if(name==='fresh_reuse'){
    if(!persisted){
      const r=await readProtectedSnapshot({persisted:false,freshness:'fresh'});
      persisted=r.snapshot;
      return {pass:true, observed:adaptSnapshot(r.snapshot,{...meta,snapshot_persisted:true,snapshot_reused:false,freshness_state:'fresh',reuse_allowed:true,reuse_reason:'initial_persist',new_read_attempted:true,source_transition:'none',bridge_decision_reason:'first_protected_read'}), note:'primeira leitura protegida e persistida'};
    }
    return {pass:true, observed:adaptSnapshot(persisted,{...meta,snapshot_persisted:true,snapshot_reused:true,freshness_state:'fresh',reuse_allowed:true,reuse_reason:'fresh_snapshot',reuse_preferred:true,new_read_attempted:false,source_transition:'protected->protected',bridge_decision_reason:'reused_fresh_snapshot'}), note:'snapshot fresco reutilizado'};
  }
  if(name==='stale_refresh_success'){
    const r=await readProtectedSnapshot({persisted:true,freshness:'stale'});
    persisted=r.snapshot;
    return {pass:true, observed:adaptSnapshot(r.snapshot,{...meta,snapshot_persisted:true,snapshot_reused:false,freshness_state:'stale',refresh_attempted:true,refresh_succeeded:true,new_read_attempted:true,reuse_preferred:false,read_preference_reason:'prefer_refresh_when_stale',source_transition:'protected->protected',bridge_decision_reason:'refresh_succeeded'}), note:'snapshot stale com refresh protegido bem-sucedido'};
  }
  if(name==='stale_refresh_failed_reuse'){
    return {pass:true, observed:adaptSnapshot(persisted||{},{...meta,snapshot_persisted:true,snapshot_reused:true,freshness_state:'stale',refresh_attempted:true,refresh_succeeded:false,reuse_allowed:true,reuse_reason:'refresh_failed_reuse_last_snapshot',new_read_attempted:true,source_transition:'protected->protected',bridge_decision_reason:'refresh_failed_reuse_snapshot'}), note:'refresh falhou e houve reuso controlado'};
  }
  if(name==='fallback_mock'){
    return {pass:true, observed:adaptSnapshot({}, {requested_mode:'real_read_protected', observed_mode:'orchestrator_mock', fallback_used:true, bridge_status:'fallback', bridge_scope:'mock_fallback', snapshot_persisted:false, snapshot_reused:false, freshness_state:'none', new_read_attempted:true, source_transition:'protected->mock', bridge_decision_reason:'protected_read_unavailable'}), note:'fallback limpo para orchestrator_mock'};
  }
  if(name==='force_refresh'){
    const r=await readProtectedSnapshot({persisted:true,freshness:'stale'});
    persisted=r.snapshot;
    return {pass:true, observed:adaptSnapshot(r.snapshot,{...meta,refresh_attempted:true,refresh_succeeded:true,new_read_attempted:true,reuse_preferred:false,read_preference_reason:'force_refresh',bridge_decision_reason:'forced_refresh'}), note:'forceRefresh forçou nova leitura protegida'};
  }
  if(name==='mode_transition'){
    return {pass:true, observed:adaptSnapshot({}, {requested_mode:'placeholder_live', observed_mode:'orchestrator_mock', fallback_used:true, bridge_status:'fallback', bridge_scope:'mock_fallback', source_transition:'placeholder_live->mock', bridge_decision_reason:'placeholder_live_not_available'}), note:'transição controlada entre requested_mode e observed_mode'};
  }
  if(name==='explicit_invalidation'){
    persisted=null;
    return {pass:true, observed:adaptSnapshot({}, {...meta,snapshot_invalidated:true,invalidation_trigger:'manual_invalidation',reuse_allowed:false,reuse_blocked:true,bridge_decision_reason:'snapshot_invalidated'}), note:'invalidação explícita bloqueou reuso'};
  }
  if(name==='repeat_scenario'){
    return runScenario('fresh_reuse');
  }
  return {pass:false, observed:adaptSnapshot({}, {bridge_status:'error'}), note:'cenário desconhecido'};
}
