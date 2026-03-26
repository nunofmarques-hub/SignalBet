
export function renderExecution(vm){
  return `<div class="grid"><div class="panel"><h3>Execution / Tracking</h3><div class="small">Pipeline: ${vm.pipeline_state} · Stage: ${vm.current_stage}</div><ul>${vm.pending.map(x=>`<li>${x.fixture} · ${x.execution_status}</li>`).join('') || '<li>Sem pendentes</li>'}</ul></div></div>`;
}
