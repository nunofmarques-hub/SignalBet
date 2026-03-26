export function buildPipelineStatus(snapshot) {
  return {
    state: snapshot.pipelineState,
    currentStage: snapshot.currentStage,
    steps: snapshot.pipelineSteps,
    issues: snapshot.issues,
    finalResult: snapshot.finalResult,
  };
}
