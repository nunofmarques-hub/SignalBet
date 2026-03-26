import { getSystemSnapshot } from './systemSnapshotService.js';
export function getPipelineStatus(mode='orchestrator_mock'){
  const snap = getSystemSnapshot(mode);
  return {
    ctaState: snap.ctaState,
    readinessLevel: snap.readinessLevel,
    projectFeedCoverageRatio: snap.coverageRatio,
    pipelineState: snap.pipelineState,
    currentStage: snap.currentStage,
    finalResult: snap.finalResult,
    pipelineSteps: snap.pipelineSteps,
    moduleOverview: snap.moduleOverview,
    buttonContext: snap.buttonContext,
    summary: snap.summary,
    issues: snap.issues
  };
}
