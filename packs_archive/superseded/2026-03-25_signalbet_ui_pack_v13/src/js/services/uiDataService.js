import { getSystemSnapshot } from './systemSnapshotService.js';
import { getControlledRuntimeBridge } from './runtimeBridgeService.js';

export async function bootstrapUiData(mode) {
  const [system, runtime] = await Promise.all([
    getSystemSnapshot(mode),
    getControlledRuntimeBridge(mode)
  ]);
  return { system, runtime };
}
