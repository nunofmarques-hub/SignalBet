import { createProvider } from './providerInterfaces.js';
import { orchestratorMockSnapshot } from '../data/mock-data.js';
export const orchestratorMockProvider = createProvider('orchestratorMockProvider', 'orchestrator_mock', async () => orchestratorMockSnapshot);
