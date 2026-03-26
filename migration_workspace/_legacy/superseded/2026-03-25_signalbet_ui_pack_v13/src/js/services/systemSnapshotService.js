import { providerRegistry } from '../providers/providerRegistry.js';
import { adaptContractSnapshot } from '../adapters/contractAdapters.js';

export async function getSystemSnapshot(mode) {
  const entry = providerRegistry[mode] || providerRegistry.orchestrator_mock;
  const raw = await entry.contract.getContractSnapshot();
  return adaptContractSnapshot(raw);
}
