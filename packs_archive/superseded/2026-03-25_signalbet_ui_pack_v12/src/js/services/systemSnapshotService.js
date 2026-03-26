import { runtimeSourceRegistry } from '../providers/providerRegistry.js';
import { adaptRuntimeSnapshot } from '../adapters/orchestratorAdapters.js';

export function getSystemSnapshot(providerMode) {
  const provider = runtimeSourceRegistry.get(providerMode);
  return adaptRuntimeSnapshot(provider.getRuntimeSnapshot());
}
