export const realSystemPlaceholderProvider = {
  getSystemSnapshot(){ return { source:'real_placeholder', status:'not_connected' }; },
  getPipelineSnapshot(){ return { source:'real_placeholder', status:'not_connected' }; }
};
