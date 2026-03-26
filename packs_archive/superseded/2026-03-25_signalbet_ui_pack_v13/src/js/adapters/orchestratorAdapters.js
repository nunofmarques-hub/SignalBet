const defaults = {
  cta_state: 'disabled', readiness_level: 'low', project_feed_coverage_ratio: 0,
  pipeline_state: 'unknown', current_stage: 'unknown', run_id: null,
  button_context: { label: 'Indisponível', enabled: false, note: 'Sem snapshot válido.' },
  summary: {}, module_overview: [], pipeline_steps: [], issues: [], final_result: null
};

export function adaptOrchestratorSnapshot(raw = {}) {
  const merged = { ...defaults, ...raw };
  return {
    source_mode: raw.source_mode || 'unknown',
    cta_state: merged.cta_state,
    readiness_level: merged.readiness_level,
    project_feed_coverage_ratio: Number(merged.project_feed_coverage_ratio || 0),
    pipeline_state: merged.pipeline_state,
    current_stage: merged.current_stage,
    run_id: merged.run_id,
    button_context: {
      label: merged.button_context?.label || defaults.button_context.label,
      enabled: Boolean(merged.button_context?.enabled),
      note: merged.button_context?.note || defaults.button_context.note
    },
    summary: merged.summary || {},
    module_overview: Array.isArray(merged.module_overview) ? merged.module_overview : [],
    pipeline_steps: Array.isArray(merged.pipeline_steps) ? merged.pipeline_steps : [],
    issues: Array.isArray(merged.issues) ? merged.issues : [],
    final_result: merged.final_result
  };
}
