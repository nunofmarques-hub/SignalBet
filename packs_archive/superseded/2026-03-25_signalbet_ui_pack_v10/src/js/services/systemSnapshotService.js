import { getProvider } from '../providers/providerRegistry.js';
export function getSystemSnapshot(providerName='contract_mock'){
  return getProvider(providerName).getSystemSnapshot();
}
