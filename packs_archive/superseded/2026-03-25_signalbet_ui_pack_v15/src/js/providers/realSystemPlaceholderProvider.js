import { createProvider } from './providerInterfaces.js';
export const realSystemPlaceholderProvider = createProvider('realSystemPlaceholderProvider', 'placeholder_live', async () => { throw new Error('LIVE_SOURCE_NOT_AVAILABLE'); });
