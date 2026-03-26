
function ensureArray(value){ return Array.isArray(value) ? value : []; }
export function validateRealRuntimeShape(raw = {}) {
  const required = ['cta_state','readiness_level','project_feed_coverage_ratio','pipeline_state','current_stage','summary','module_overview','pipeline_steps'];
  const missing = required.filter(k => !(k in raw));
  return { valid: missing.length === 0, missing };
}
export function normalizeOrchestratorSnapshot(raw = {}, sourceMode = 'unknown') {
  return {
    source_mode_observed: sourceMode,
    cta_state: raw.cta_state ?? 'disabled',
    readiness_level: raw.readiness_level ?? 'unknown',
    project_feed_coverage_ratio: Number(raw.project_feed_coverage_ratio ?? 0),
    pipeline_state: raw.pipeline_state ?? 'idle',
    current_stage: raw.current_stage ?? 'unknown',
    summary: {
      modules_available: Number(raw.summary?.modules_available ?? 0),
      modules_ready: Number(raw.summary?.modules_ready ?? 0),
      opportunities: Number(raw.summary?.opportunities ?? 0),
      approved: Number(raw.summary?.approved ?? 0),
      execution_open: Number(raw.summary?.execution_open ?? 0)
    },
    module_overview: ensureArray(raw.module_overview).map(item => ({
      module: item.module ?? 'Unknown',
      status: item.status ?? 'unknown',
      coverage: Number(item.coverage ?? 0),
      count: Number(item.count ?? 0)
    })),
    pipeline_steps: ensureArray(raw.pipeline_steps).map(step => ({
      name: step.name ?? 'Unknown',
      status: step.status ?? 'unknown'
    })),
    issues: ensureArray(raw.issues).map(issue => String(issue)),
    final_result: raw.final_result ?? 'unknown',
    run_id: raw.run_id ?? null
  };
}
