import { chip, kpi } from './ui.js';
export function orchestratorPanel(vm) {
  const steps = vm.steps.map(s => chip(s.step, s.status)).join('');
  const modules = vm.moduleOverview.map(m => `<tr><td>${m.module}</td><td>${chip(m.status, m.status)}</td><td>${m.count}</td></tr>`).join('');
  return `
    <section class="orchestrator">
      <div class="card hero">
        <div class="muted">Pôr tudo a correr</div>
        <h2 style="margin:8px 0 6px">${vm.cta.ctaLabel}</h2>
        <div class="small">Readiness: ${chip(vm.readinessLabel, vm.readinessLabel === 'high' ? 'success' : vm.readinessLabel === 'medium' ? 'warning' : 'error')} · Cobertura: ${vm.coverageLabel} · Pipeline: ${chip(vm.pipelineState, vm.pipelineState)}</div>
        <div class="steps">${steps}</div>
      </div>
      <div class="panel">
        <div class="muted">Resumo da corrida</div>
        <div class="kpi-grid" style="grid-template-columns:1fr 1fr; margin-top:10px;">
          ${kpi('Opportunities', vm.summary.opportunities)}
          ${kpi('Eligible', vm.summary.eligible)}
          ${kpi('Approved', vm.summary.approved)}
          ${kpi('To Execution', vm.summary.sentToExecution)}
        </div>
      </div>
    </section>
    <section class="split">
      <div class="card"><div class="muted">Module overview</div><table class="table"><thead><tr><th>Módulo</th><th>Estado</th><th>Count</th></tr></thead><tbody>${modules}</tbody></table></div>
      <div class="panel" id="issues-panel"><div class="muted">Issues</div></div>
    </section>`;
}
