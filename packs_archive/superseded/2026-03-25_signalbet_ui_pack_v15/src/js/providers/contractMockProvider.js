import { createProvider } from './providerInterfaces.js';
import { contractMockSnapshot } from '../data/mock-data.js';
export const contractMockProvider = createProvider('contractMockProvider', 'contract_mock', async () => contractMockSnapshot);
