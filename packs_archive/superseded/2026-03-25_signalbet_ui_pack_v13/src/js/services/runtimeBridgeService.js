import { getPipelineStatus } from './pipelineStatusService.js';

export async function getControlledRuntimeBridge(mode) {
  try {
    const snapshot = await getPipelineStatus(mode);
    return {
      source_mode: snapshot.source_mode,
      source_ok: true,
      degraded: snapshot.source_mode === 'placeholder_live',
      snapshot
    };
  } catch (error) {
    return {
      source_mode: mode,
      source_ok: false,
      degraded: true,
      snapshot: {
        cta_state: 'error',
        readiness_level: 'low',
        project_feed_coverage_ratio: 0,
        pipeline_state: 'error',
        current_stage: 'bridge_error',
        button_context: { label: 'Erro', enabled: false, note: 'Falha ao ler runtime bridge.' },
        summary: {}, module_overview: [], pipeline_steps: [], issues: [{ code: 'bridge_error', severity: 'critical', message: error.message }], final_result: null
      }
    };
  }
}
