export function adaptSnapshot(raw, meta={}) {
  return {
    requested_mode: meta.requested_mode || 'real_read_protected',
    observed_mode: meta.observed_mode || 'real_read_protected',
    fallback_used: !!meta.fallback_used,
    bridge_status: meta.bridge_status || 'ok',
    bridge_scope: meta.bridge_scope || 'protected_partial',
    degraded_mode: !!meta.degraded_mode,
    read_attempt: meta.read_attempt || 1,
    snapshot_persisted: !!meta.snapshot_persisted,
    snapshot_reused: !!meta.snapshot_reused,
    snapshot_freshness: meta.snapshot_freshness || 'fresh',
    freshness_state: meta.freshness_state || 'fresh',
    snapshot_invalidated: !!meta.snapshot_invalidated,
    reuse_allowed: meta.reuse_allowed !== false,
    reuse_reason: meta.reuse_reason || 'fresh_snapshot',
    new_read_attempted: !!meta.new_read_attempted,
    refresh_attempted: !!meta.refresh_attempted,
    refresh_succeeded: !!meta.refresh_succeeded,
    reuse_preferred: !!meta.reuse_preferred,
    reuse_blocked: !!meta.reuse_blocked,
    invalidation_trigger: meta.invalidation_trigger || null,
    read_preference_reason: meta.read_preference_reason || 'prefer_reuse_when_fresh',
    source_transition: meta.source_transition || 'protected->protected',
    bridge_decision_reason: meta.bridge_decision_reason || 'stable_reuse',
    ...raw
  };
}
