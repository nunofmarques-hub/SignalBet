import { providerRegistry } from '../providers/providerRegistry.js';
import { adaptOrchestratorSnapshot } from '../adapters/orchestratorAdapters.js';

export async function getPipelineStatus(mode) {
  const entry = providerRegistry[mode] || providerRegistry.orchestrator_mock;
  const raw = await entry.runtime.getRuntimeSnapshot();
  return adaptOrchestratorSnapshot(raw);
}
