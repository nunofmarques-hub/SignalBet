import { providerRegistry } from '../providers/providerRegistry.js';
import { adaptSystemSnapshot } from '../adapters/orchestratorAdapters.js';
export function getSystemSnapshot(mode='orchestrator_mock'){
  return adaptSystemSnapshot(providerRegistry[mode].getSystemSnapshot());
}
