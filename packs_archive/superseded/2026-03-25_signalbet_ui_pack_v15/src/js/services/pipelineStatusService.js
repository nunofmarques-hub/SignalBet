export function pipelineReadiness(rt){
  const steps = rt.pipeline_steps || [];
  const ready = steps.filter(s => s.status === 'ready').length;
  return { ready_steps: ready, total_steps: steps.length, ratio: steps.length ? ready / steps.length : 0 };
}
