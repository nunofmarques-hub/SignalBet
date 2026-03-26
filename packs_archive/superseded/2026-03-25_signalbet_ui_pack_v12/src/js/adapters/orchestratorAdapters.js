const norm = (v, fb = 'unknown') => v ?? fb;

export function adaptRuntimeSnapshot(snapshot) {
  return {
    runId: norm(snapshot.run_id, 'no-run'),
    ctaState: norm(snapshot.cta_state, 'idle'),
    readinessLevel: norm(snapshot.readiness_level, 'low'),
    coverageRatio: Number(snapshot.project_feed_coverage_ratio ?? 0),
    pipelineState: norm(snapshot.pipeline_state, 'idle'),
    currentStage: norm(snapshot.current_stage, 'preflight'),
    finalResult: snapshot.final_result ?? null,
    summary: adaptSummary(snapshot.summary),
    moduleOverview: adaptModuleOverview(snapshot.module_overview),
    pipelineSteps: adaptPipelineSteps(snapshot.pipeline_steps),
    issues: adaptIssues(snapshot.issues),
    buttonContext: adaptButtonContext(snapshot),
  };
}

export function adaptSummary(summary = {}) {
  return {
    opportunities: Number(summary.opportunities ?? 0),
    eligible: Number(summary.eligible ?? 0),
    approved: Number(summary.approved ?? 0),
    sentToExecution: Number(summary.sent_to_execution ?? 0),
  };
}

export function adaptModuleOverview(items = []) {
  return items.map((item) => ({
    module: norm(item.module),
    status: norm(item.status),
    count: Number(item.count ?? 0),
  }));
}

export function adaptPipelineSteps(steps = []) {
  return steps.map((step) => ({
    step: norm(step.step),
    status: norm(step.status),
  }));
}

export function adaptIssues(issues = []) {
  return issues.map((issue) => ({
    severity: norm(issue.severity, 'info'),
    message: norm(issue.message, 'No detail'),
  }));
}

export function adaptButtonContext(snapshot) {
  const cta = norm(snapshot.cta_state, 'idle');
  const readiness = norm(snapshot.readiness_level, 'low');
  return {
    ctaState: cta,
    readinessLevel: readiness,
    ctaLabel: cta === 'running' ? 'Corrida em curso' : 'Pôr tudo a correr',
    disabled: cta === 'blocked',
  };
}
