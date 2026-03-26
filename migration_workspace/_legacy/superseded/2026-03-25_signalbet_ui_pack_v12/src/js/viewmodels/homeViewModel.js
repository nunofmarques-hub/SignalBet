export function buildHomeViewModel(bridge) {
  const s = bridge.snapshot;
  return {
    title: 'Home / Dashboard',
    cta: s.buttonContext,
    summary: s.summary,
    coverageLabel: `${Math.round(s.coverageRatio * 100)}%`,
    readinessLabel: s.readinessLevel,
    pipelineState: s.pipelineState,
    moduleOverview: s.moduleOverview,
    steps: s.pipelineSteps,
    issues: s.issues,
  };
}
