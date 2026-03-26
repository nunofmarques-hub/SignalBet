import { providerRegistry } from '../providers/providerRegistry.js';
import { adaptOrchestratorSnapshot } from '../adapters/orchestratorAdapters.js';
import { loadPersistedProtectedSnapshot, persistProtectedSnapshot } from '../providers/realOrchestratorProtectedProvider.js';

const FRESH_MS = 15 * 60 * 1000;

function getSnapshotAgeMs(snapshot){
  const stamp = snapshot?.persisted_at || snapshot?.captured_at;
  if(!stamp) return null;
  const n = Date.parse(stamp);
  if(Number.isNaN(n)) return null;
  return Date.now() - n;
}

function deriveFreshness(snapshot){
  const age = getSnapshotAgeMs(snapshot);
  if(age == null) return 'unknown';
  if(age <= FRESH_MS) return 'fresh';
  return 'stale';
}

function withFreshness(snapshot){
  const freshness = deriveFreshness(snapshot);
  return {
    ...snapshot,
    freshness_state: freshness,
    snapshot_freshness: freshness,
    snapshot_invalidated: freshness === 'stale' && snapshot?.invalidate_on_stale === true,
  };
}

export async function readRuntime(requested='real_read_protected'){
  let observed = requested;
  let fallbackUsed = false;
  let readAttempt = 1;
  let refreshAttempted = false;
  let refreshSucceeded = false;
  let reusePreferred = false;
  let reuseBlocked = false;
  let invalidationTrigger = 'none';
  let readPreferenceReason = 'requested_mode_default';

  if(requested === 'real_read_protected'){
    const persisted = loadPersistedProtectedSnapshot();
    if(persisted){
      const persistedState = withFreshness({
        ...persisted,
        requested_mode: requested,
        observed_mode: 'real_read_protected',
        snapshot_reused: true,
        snapshot_persisted: true,
        source_transition: `${requested}->real_read_protected(reuse_candidate)`,
        bridge_decision_reason: 'persisted_snapshot_checked_first'
      });

      if(persistedState.freshness_state === 'fresh'){
        reusePreferred = true;
        readPreferenceReason = 'fresh_snapshot_reuse_preferred';
        return adaptOrchestratorSnapshot({
          ...persistedState,
          reuse_preferred: true,
          reuse_blocked: false,
          refresh_attempted: false,
          refresh_succeeded: false,
          invalidation_trigger: 'none',
          read_preference_reason: readPreferenceReason,
          source_transition: `${requested}->real_read_protected(reuse_fresh)`,
          bridge_status: persistedState.bridge_status || 'reuse_ok'
        });
      }

      // stale persisted snapshot: prefer refresh, then fallback to stale reuse
      refreshAttempted = true;
      readAttempt = 2;
      invalidationTrigger = 'stale_snapshot';
      readPreferenceReason = 'stale_snapshot_refresh_preferred';
      try {
        const raw = await providerRegistry.real_read_protected({ allowReuse:false, forceRefresh:true });
        refreshSucceeded = true;
        persistProtectedSnapshot(raw);
        return adaptOrchestratorSnapshot(withFreshness({
          ...raw,
          requested_mode: requested,
          observed_mode: 'real_read_protected',
          snapshot_reused: false,
          snapshot_persisted: true,
          new_read_attempted: true,
          refresh_attempted: true,
          refresh_succeeded: true,
          reuse_preferred: false,
          reuse_blocked: false,
          invalidation_trigger: invalidationTrigger,
          read_preference_reason: readPreferenceReason,
          source_transition: `${requested}->real_read_protected(refresh_success)`,
          bridge_decision_reason: 'stale_snapshot_refreshed_successfully',
          bridge_status: 'refresh_ok'
        }));
      } catch(e) {
        reusePreferred = false;
        reuseBlocked = false;
        return adaptOrchestratorSnapshot({
          ...persistedState,
          requested_mode: requested,
          observed_mode: 'real_read_protected',
          fallback_used: false,
          read_attempt: readAttempt,
          new_read_attempted: true,
          refresh_attempted: true,
          refresh_succeeded: false,
          reuse_preferred: false,
          reuse_blocked: false,
          invalidation_trigger: invalidationTrigger,
          read_preference_reason: 'refresh_failed_stale_reuse_used',
          bridge_status: 'stale_reuse',
          bridge_decision_reason: 'reused_stale_snapshot_after_failed_refresh',
          source_transition: `${requested}->real_read_protected(reuse_after_failed_refresh)`
        });
      }
    }
  }

  let raw = null;
  try {
    raw = await providerRegistry[requested]({ allowReuse:false, forceRefresh:false });
  } catch(e){
    raw = null;
  }

  if(!raw){
    observed = 'orchestrator_mock';
    fallbackUsed = true;
    raw = await providerRegistry.orchestrator_mock();
    readPreferenceReason = 'requested_mode_unavailable_fallback';
  } else {
    if(observed === 'real_read_protected'){
      persistProtectedSnapshot(raw);
      refreshSucceeded = true;
    }
  }

  return adaptOrchestratorSnapshot(withFreshness({
    ...raw,
    requested_mode: requested,
    observed_mode: observed,
    fallback_used: fallbackUsed,
    read_attempt: readAttempt,
    refresh_attempted: refreshAttempted,
    refresh_succeeded: refreshSucceeded,
    reuse_preferred: reusePreferred,
    reuse_blocked: reuseBlocked,
    invalidation_trigger: invalidationTrigger,
    read_preference_reason: readPreferenceReason,
    source_transition: raw?.source_transition || `${requested}->${observed}`,
    bridge_decision_reason: raw?.bridge_decision_reason || (fallbackUsed ? 'fallback_to_orchestrator_mock' : 'protected_read_ok')
  }));
}
