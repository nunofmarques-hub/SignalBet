import { readRuntime } from './runtimeBridgeService.js';
export async function getUiRuntime(modeRequested){
  const runtime = await readRuntime(modeRequested);
  return {
    mode_requested: modeRequested,
    mode_observed: runtime.source_mode_observed,
    fallback_used: runtime.fallback_used || false,
    bridge_status: runtime.bridge_status,
    runtime,
  };
}
