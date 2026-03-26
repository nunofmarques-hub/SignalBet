import { readRuntime } from './runtimeBridgeService.js';

export async function bootstrap(mode='real_read_protected'){
  const runtime = await readRuntime(mode);
  return {
    runtime,
    source_status: {
      requested: mode,
      observed: runtime.observed_mode,
      fallback_used: runtime.fallback_used,
      bridge_status: runtime.bridge_status,
      freshness_state: runtime.freshness_state,
      snapshot_reused: runtime.snapshot_reused,
      snapshot_invalidated: runtime.snapshot_invalidated
    }
  };
}
