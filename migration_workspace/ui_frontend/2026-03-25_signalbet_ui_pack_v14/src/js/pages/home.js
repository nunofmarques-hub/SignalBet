
import { tile } from '../components/ui.js';
import { topOpportunityCard } from '../components/cards.js';
function sourceBadge(metadata){
  const observed = metadata.observed_mode || 'unknown';
  const cls = observed.includes('fallback') ? 'source-fallback' : (observed.includes('real') ? 'source-real' : 'source-mock');
  return `<span class="${cls}">${observed}</span>`;
}
export function renderHome(vm) {
  const kpis = vm.kpis.map(([l,v]) => tile(l,v)).join('');
  const modules = vm.orchestrator.module_overview.map(m => `<div class="step"><span>${m.module}</span><span>${m.status} · ${(m.coverage*100).toFixed(0)}% · ${m.count}</span></div>`).join('');
  const steps = vm.orchestrator.pipeline_steps.map(s => `<div class="step"><span>${s.name}</span><span>${s.status}</span></div>`).join('');
  const issues = vm.orchestrator.issues.length ? vm.orchestrator.issues.map(i=>`<li>${i}</li>`).join('') : '<li>Sem issues críticas</li>';
  const progressPct = Math.round(vm.orchestrator.project_feed_coverage_ratio * 100);
  return `
    <div class="layout-split">
      <div class="grid" style="gap:16px">
        <div class="hero">
          ${topOpportunityCard(vm.hero)}
          <div class="orchestrator-panel">
            <div class="head">
              <h3 style="margin:0">Pôr tudo a correr</h3>
              <span class="small">Modo observado: ${sourceBadge(vm.metadata)}</span>
            </div>
            <div class="badges">
              <span class="badge lime">cta_state: ${vm.orchestrator.cta_state}</span>
              <span class="badge cyan">readiness: ${vm.orchestrator.readiness_level}</span>
              <span class="badge amber">pipeline: ${vm.orchestrator.pipeline_state}</span>
            </div>
            <div style="margin:14px 0" class="small">Cobertura de feeds do projeto</div>
            <div class="progress"><span style="width:${progressPct}%"></span></div>
            <div class="small" style="margin-top:6px">${progressPct}% · stage: ${vm.orchestrator.current_stage}</div>
            <div class="file-row" style="margin-top:14px">
              <input type="file" id="real-snapshot-file" accept="application/json,.json" />
              <button class="btn btn-secondary" id="btn-import-real">Ler snapshot real</button>
              <button class="btn btn-secondary" id="btn-clear-real">Limpar</button>
            </div>
            <div class="notice" style="margin-top:10px">
              real_read_status: ${vm.metadata.real_read_status || 'none'} · imported_file: ${vm.metadata.imported_file_name || '—'}
            </div>
            <div class="grid" style="grid-template-columns:repeat(2,minmax(0,1fr));margin-top:14px">
              <div class="panel"><div class="small">Modules ready</div><strong>${vm.orchestrator.summary.modules_ready}/${vm.orchestrator.summary.modules_available}</strong></div>
              <div class="panel"><div class="small">Approved</div><strong>${vm.orchestrator.summary.approved}</strong></div>
              <div class="panel"><div class="small">Opportunities</div><strong>${vm.orchestrator.summary.opportunities}</strong></div>
              <div class="panel"><div class="small">Execution open</div><strong>${vm.orchestrator.summary.execution_open}</strong></div>
            </div>
          </div>
        </div>
        <div class="grid kpis">${kpis}</div>
      </div>
      <div class="grid">
        <div class="panel"><h3>Module overview</h3><div class="steps">${modules}</div></div>
        <div class="panel"><h3>Pipeline steps</h3><div class="steps">${steps}</div></div>
        <div class="panel"><h3>Issues</h3><ul>${issues}</ul></div>
      </div>
    </div>
  `;
}
