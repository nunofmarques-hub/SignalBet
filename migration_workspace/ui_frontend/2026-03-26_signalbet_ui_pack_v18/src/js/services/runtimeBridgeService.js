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

function invalidateIfNeeded(snapshot){
  const freshness = deriveFreshness(snapshot);
  if(freshness === 'stale'){
    return {
      ...snapshot,
      freshness_state: 'stale',
      snapshot_freshness: 'stale',
      snapshot_invalidated: false,
      reuse_allowed: true,
      reuse_reason: snapshot.snapshot_reused ? 'stale_but_reusable_until_new_read' : 'stale_from_source',
    };
  }
  return {
    ...snapshot,
    freshness_state: freshness,
    snapshot_freshness: freshness,
    snapshot_invalidated: false
  };
}

export async function readRuntime(requested='real_read_protected'){
  let observed = requested;
  let fallbackUsed = false;
  let raw = null;
  let readAttempt = 1;

  if(requested === 'real_read_protected'){
    const persisted = loadPersistedProtectedSnapshot();
    if(persisted){
      const persistedState = invalidateIfNeeded({
        ...persisted,
        requested_mode: requested,
        observed_mode: 'real_read_protected',
        snapshot_reused: true,
        source_transition: `${requested}->real_read_protected(reuse)`,
        bridge_decision_reason: 'persisted_snapshot_checked_first'
      });
      if(persistedState.freshness_state === 'fresh'){
        return adaptOrchestratorSnapshot(persistedState);
      }
      // stale snapshot: try fresh protected read, if it fails reuse stale snapshot
      try{
        readAttempt = 2;
        raw = await providerRegistry.real_read_protected({ allowReuse:false });
        const next = {
          ...raw,
          requested_mode: requested,
          observed_mode: 'real_read_protected',
          snapshot_reused: false,
          new_read_attempted: true,
          source_transition: `${requested}->real_read_protected(new_read)`,
          bridge_decision_reason: 'stale_snapshot_revalidated'
        };
        return adaptOrchestratorSnapshot(invalidateIfNeeded(next));
      }catch(e){
        return adaptOrchestratorSnapshot({
          ...persistedState,
          requested_mode: requested,
          observed_mode: 'real_read_protected',
          fallback_used: false,
          read_attempt: readAttempt,
          new_read_attempted: true,
          bridge_status: 'stale_reuse',
          bridge_decision_reason: 'reused_stale_snapshot_after_failed_new_read',
          source_transition: `${requested}->real_read_protected(reuse_after_failed_new_read)`
        });
      }
    }
  }

  try{
    raw = await providerRegistry[requested]({ allowReuse:false });
  }catch(e){
    raw = null;
  }

  if(!raw){
    observed = 'orchestrator_mock';
    fallbackUsed = true;
    raw = await providerRegistry.orchestrator_mock();
  }else{
    if(observed === 'real_read_protected'){
      persistProtectedSnapshot(raw);
    }
  }

  return adaptOrchestratorSnapshot(invalidateIfNeeded({
    ...raw,
    requested_mode: requested,
    observed_mode: observed,
    fallback_used: fallbackUsed,
    read_attempt: readAttempt,
    source_transition: raw?.source_transition || `${requested}->${observed}`,
    bridge_decision_reason: raw?.bridge_decision_reason || (fallbackUsed ? 'fallback_to_orchestrator_mock' : 'protected_read_ok')
  }));
}
