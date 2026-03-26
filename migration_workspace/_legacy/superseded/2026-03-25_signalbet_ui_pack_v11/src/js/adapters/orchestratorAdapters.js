export function adaptSystemSnapshot(raw){
  return {
    ctaState: raw.cta_state,
    readinessLevel: raw.readiness_level,
    coverageRatio: raw.project_feed_coverage_ratio,
    pipelineState: raw.pipeline_state,
    currentStage: raw.current_stage,
    finalResult: raw.final_result,
    summary: raw.summary,
    moduleOverview: raw.module_overview,
    pipelineSteps: raw.pipeline_steps,
    buttonContext: {
      enabled: raw.cta_state === 'ready' || raw.cta_state === 'idle',
      label: raw.pipeline_state === 'running' ? 'Corrida em curso' : 'Pôr tudo a correr'
    },
    issues: raw.issues || []
  };
}
