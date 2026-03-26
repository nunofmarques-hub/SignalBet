
export function buildExecutionViewModel(system, orchestrator) {
  return { pending: system.pool_rows.filter(r => r.execution_status === 'PENDING'), pipeline_state: orchestrator.pipeline_state, current_stage: orchestrator.current_stage };
}
