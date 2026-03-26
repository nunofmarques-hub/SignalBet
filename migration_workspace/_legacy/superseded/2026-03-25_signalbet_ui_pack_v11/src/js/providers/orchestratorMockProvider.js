import { orchestratorSnapshot } from '../../data/mock-data.js';
export const orchestratorMockProvider = {
  getSystemSnapshot(){ return orchestratorSnapshot; },
  getPipelineSnapshot(){ return orchestratorSnapshot; }
};
