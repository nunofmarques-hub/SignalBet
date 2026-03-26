export function historyViewModel(page, pipeline){ return { ...page, finalResult: pipeline.finalResult || 'pending' }; }
