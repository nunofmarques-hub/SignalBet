
import { MOCK_SYSTEM_SNAPSHOT } from '../../data/mock-data.js';
import { SnapshotProvider } from './providerInterfaces.js';
export class ContractMockProvider extends SnapshotProvider {
  async getSystemSnapshot() { return structuredClone(MOCK_SYSTEM_SNAPSHOT); }
}
