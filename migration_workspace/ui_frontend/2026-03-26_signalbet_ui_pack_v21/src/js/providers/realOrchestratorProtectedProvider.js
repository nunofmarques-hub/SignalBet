import { MOCK_DATA } from '../../data/mock-data.js';
export async function readProtectedSnapshot(options={}) {
  const mode = options.forceFailure ? 'mock' : 'real_read_protected';
  const snapshot = structuredClone(MOCK_DATA.runtime_snapshot);
  return { mode, snapshot, persisted: !!options.persisted, freshness: options.freshness || 'fresh' };
}
