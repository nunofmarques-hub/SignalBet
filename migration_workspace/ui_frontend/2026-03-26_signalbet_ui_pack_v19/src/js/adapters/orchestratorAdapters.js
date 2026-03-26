export function adaptOrchestratorSnapshot(raw){
  if(!raw) return { valid:false, reason:'empty_snapshot' };
  const summary = raw.summary || {};
  const pipelineSteps = Array.isArray(raw.pipeline_steps) ? raw.pipeline_steps : [];
  const moduleOverview = Array.isArray(raw.module_overview) ? raw.module_overview : [];
  const issues = Array.isArray(raw.issues) ? raw.issues : [];
  const freshnessState = raw.freshness_state || raw.snapshot_freshness || 'unknown';

  return {
    valid: true,
    requested_mode: raw.requested_mode || 'unknown',
    observed_mode: raw.observed_mode || raw.source_mode || 'unknown',
    fallback_used: !!raw.fallback_used,
    bridge_status: raw.bridge_status || 'ok',
    bridge_scope: raw.bridge_scope || 'protected_real_partial_v19',
    degraded_mode: !!raw.degraded_mode,
    read_attempt: raw.read_attempt || 1,
    snapshot_persisted: !!raw.snapshot_persisted,
    snapshot_reused: !!raw.snapshot_reused,
    snapshot_freshness: raw.snapshot_freshness || freshnessState,
    freshness_state: freshnessState,
    snapshot_invalidated: !!raw.snapshot_invalidated,
    reuse_allowed: raw.reuse_allowed !== false,
    reuse_reason: raw.reuse_reason || 'not_set',
    new_read_attempted: !!raw.new_read_attempted,
    refresh_attempted: !!raw.refresh_attempted,
    refresh_succeeded: !!raw.refresh_succeeded,
    reuse_preferred: !!raw.reuse_preferred,
    reuse_blocked: !!raw.reuse_blocked,
    invalidation_trigger: raw.invalidation_trigger || 'none',
    read_preference_reason: raw.read_preference_reason || 'not_set',
    source_transition: raw.source_transition || `${raw.requested_mode || 'unknown'}->${raw.observed_mode || raw.source_mode || 'unknown'}`,
    bridge_decision_reason: raw.bridge_decision_reason || 'protected_read_ok',
    cta_state: raw.cta_state || 'ready',
    readiness_level: raw.readiness_level || 'unknown',
    project_feed_coverage_ratio: raw.project_feed_coverage_ratio || 0,
    pipeline_state: raw.pipeline_state || 'idle',
    current_stage: raw.current_stage || 'none',
    source_line: raw.source_line || 'unknown',
    captured_at: raw.captured_at || null,
    persisted_at: raw.persisted_at || null,
    final_result: raw.final_result || 'unknown',
    summary: {
      opportunities: summary.opportunities || 0,
      eligible: summary.eligible || 0,
      approved: summary.approved || 0,
      executed: summary.executed || 0
    },
    module_overview: moduleOverview,
    pipeline_steps: pipelineSteps,
    issues
  };
}
