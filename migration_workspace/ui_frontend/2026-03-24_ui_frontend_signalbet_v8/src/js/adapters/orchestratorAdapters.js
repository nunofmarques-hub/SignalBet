export function adaptRunState(run){
  return {
    status: run.status,
    progress: run.progress,
    title: run.title,
    message: run.message,
    checks: run.checks.map(c => ({
      key: c.key,
      label: c.label,
      status: c.status,
      detail: c.detail
    })),
    stages: run.stages.map((s, index) => ({
      ...s,
      index: index + 1
    })),
    summary: run.summary,
    issues: run.issues || []
  };
}
