export function buildPoolViewModel(payload){
  return {
    mode_requested: payload.mode_requested,
    mode_observed: payload.mode_observed,
    fallback_used: payload.fallback_used,
    bridge_status: payload.bridge_status,
    runtime: payload.runtime,
  };
}
