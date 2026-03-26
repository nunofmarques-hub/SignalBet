import { SnapshotProvider } from './providerInterfaces.js';
import { contractSnapshot, orchestratorSnapshot } from '../data/mock-data.js';
export class ContractMockProvider extends SnapshotProvider {
  getSystemSnapshot(){ return contractSnapshot; }
  getPipelineSnapshot(){ return orchestratorSnapshot; }
}
