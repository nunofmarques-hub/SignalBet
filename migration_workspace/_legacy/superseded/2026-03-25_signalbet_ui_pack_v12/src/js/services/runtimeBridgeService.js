import { getSystemSnapshot } from './systemSnapshotService.js';
import { buildPipelineStatus } from './pipelineStatusService.js';

export function getRuntimeBridge(providerMode) {
  const snapshot = getSystemSnapshot(providerMode);
  return {
    snapshot,
    pipeline: buildPipelineStatus(snapshot),
    sourceMode: providerMode,
  };
}
