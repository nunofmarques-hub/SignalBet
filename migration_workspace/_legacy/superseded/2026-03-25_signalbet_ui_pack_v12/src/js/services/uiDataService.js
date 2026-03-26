import { getRuntimeBridge } from './runtimeBridgeService.js';

export function bootstrapUiData(providerMode) {
  return getRuntimeBridge(providerMode);
}
