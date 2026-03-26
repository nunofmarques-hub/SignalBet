import data from '../data/mock-data.js';

const STORAGE_KEY = 'signalbet_protected_runtime_snapshot_v19';

function hasStorage(){
  try { return typeof window !== 'undefined' && !!window.localStorage; } catch(e){ return false; }
}

export function loadPersistedProtectedSnapshot(){
  if(!hasStorage()) return null;
  try{
    const raw = window.localStorage.getItem(STORAGE_KEY);
    if(!raw) return null;
    return JSON.parse(raw);
  }catch(e){
    return null;
  }
}

export function persistProtectedSnapshot(snapshot){
  if(!hasStorage()) return false;
  try{
    const payload = {
      ...snapshot,
      persisted_at: new Date().toISOString(),
      snapshot_persisted: true,
      source_line: snapshot.source_line || 'protected_snapshot_persisted'
    };
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(payload));
    return true;
  }catch(e){
    return false;
  }
}

export function clearPersistedProtectedSnapshot(){
  if(!hasStorage()) return false;
  try{
    window.localStorage.removeItem(STORAGE_KEY);
    return true;
  }catch(e){
    return false;
  }
}

export async function getRealProtectedSnapshot(options={}){
  const { allowReuse=true, forceRefresh=false } = options;
  const persisted = loadPersistedProtectedSnapshot();
  if(allowReuse && !forceRefresh && persisted){
    return {
      ...persisted,
      source_line: persisted.source_line || 'persisted_protected_snapshot',
      snapshot_reused: true,
      bridge_decision_reason: persisted.bridge_decision_reason || 'persisted_snapshot_reused',
      source_transition: 'real_read_protected->real_read_protected(reuse_provider)'
    };
  }
  const fresh = { ...data.realProtectedSnapshotV19 };
  persistProtectedSnapshot(fresh);
  return {
    ...fresh,
    snapshot_reused: false,
    source_transition: 'real_read_protected->real_read_protected(new_provider_read)'
  };
}
