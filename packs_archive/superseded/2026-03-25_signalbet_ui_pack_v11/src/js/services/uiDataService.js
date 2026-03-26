import { providerRegistry } from '../providers/providerRegistry.js';
import { adaptPageData } from '../adapters/contractAdapters.js';
import { getPipelineStatus } from './pipelineStatusService.js';
export const uiDataService = {
  bootstrap(){ return getPipelineStatus(); },
  getPage(page){ return adaptPageData(page, providerRegistry.contract_mock.getPageData(page)); },
  getProviderStatus(){ return { contract:'mock', orchestrator:'mock', real:'placeholder' }; }
};
