import { getProvider } from '../providers/providerRegistry.js';
export function getPipelineSnapshot(providerName='contract_mock'){
  return getProvider(providerName).getPipelineSnapshot();
}
