export function executionViewModel(page, pipeline){ return { ...page, currentStage: pipeline.currentStage }; }
