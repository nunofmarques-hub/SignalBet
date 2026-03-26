const required = ['cta_state','readiness_level','project_feed_coverage_ratio','pipeline_state','current_stage','summary','module_overview','pipeline_steps'];
export function validateOrchestratorSnapshot(snapshot){
  const missing = required.filter(k => !(k in snapshot));
  return { ok: missing.length === 0, missing };
}
export function adaptOrchestratorSnapshot(snapshot, sourceObserved, fallbackUsed=false){
  const validation = validateOrchestratorSnapshot(snapshot);
  return {
    source_mode_observed: sourceObserved,
    fallback_used: fallbackUsed,
    consumption_status: validation.ok ? 'ok' : 'degraded',
    bridge_status: sourceObserved === 'real_read_protected' ? 'real_partial_protected' : 'mock_runtime',
    cta_state: snapshot.cta_state || 'blocked',
    readiness_level: snapshot.readiness_level || 'low',
    project_feed_coverage_ratio: snapshot.project_feed_coverage_ratio ?? 0,
    pipeline_state: snapshot.pipeline_state || 'unknown',
    current_stage: snapshot.current_stage || 'unknown',
    summary: snapshot.summary || {},
    module_overview: snapshot.module_overview || [],
    pipeline_steps: snapshot.pipeline_steps || [],
    issues: snapshot.issues || [],
    final_result: snapshot.final_result || null,
    pool_rows: snapshot.pool_rows || [],
    history_rows: snapshot.history_rows || [],
    validation_missing: validation.missing
  };
}
