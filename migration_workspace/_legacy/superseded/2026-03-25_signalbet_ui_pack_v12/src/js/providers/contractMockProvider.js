import { runtimeSnapshots } from '../../data/mock-data.js';
import { RuntimeProvider } from './providerInterfaces.js';

export class ContractMockProvider extends RuntimeProvider {
  getRuntimeSnapshot() { return structuredClone(runtimeSnapshots.contract_mock); }
}
