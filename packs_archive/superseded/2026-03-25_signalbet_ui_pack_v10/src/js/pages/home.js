import { topbar } from '../components/layout.js';
import { kpi, chip } from '../components/ui.js';
import { heroOpportunity, compactItem } from '../components/cards.js';
import { renderIssue, renderStage } from '../components/stateView.js';
export function renderHome(vm){
  const readiness = Object.entries(vm.readiness.modules||{}).map(([k,v])=>`<div class="list-row"><span>${k}</span><span>${chip(v, v==='READY'?'green':'amber')}</span></div>`).join('');
  const issues = (vm.run.issues||[]).map(renderIssue).join('') || '<div class="muted">Sem issues relevantes.</div>';
  return `${topbar('Home / Dashboard', `<span class="chip cyan">Provider contract_mock</span><button class="btn" id="runBtn">Pôr tudo a correr</button>`)}
  <div class="content">
    <div class="hero"><div>${heroOpportunity(vm.hero)}</div>
      <div class="card"><h3>Pipeline Run</h3><div class="muted">run_id: ${vm.run.run_id}</div><div style="margin:10px 0">${chip(vm.run.pipeline_state, vm.run.pipeline_state==='RUNNING'?'lime':'cyan')} ${chip(vm.run.current_stage,'cyan')}</div><div class="orch-stage">${(vm.run.stages||[]).map(renderStage).join('')}</div></div></div>
    <div class="grid kpi">${kpi('Opportunities Today', vm.opportunities_today)}${kpi('Eligible', vm.eligible_today)}${kpi('Approved', vm.approved_today)}${kpi('Pending Execution', vm.pending_execution)}${kpi('Alerts', vm.alerts)}${kpi('Progress', vm.run.progress_pct + '%')}</div>
    <div class="grid two"><div class="card"><h3>Readiness do Sistema</h3><div class="list"><div class="list-row"><span>Data/API</span><span>${chip(vm.readiness.data_api, 'green')}</span></div>${readiness}<div class="list-row"><span>GPS</span><span>${chip(vm.readiness.gps,'green')}</span></div><div class="list-row"><span>Banca</span><span>${chip(vm.readiness.bankroll,'green')}</span></div><div class="list-row"><span>Execution</span><span>${chip(vm.readiness.execution,'green')}</span></div></div></div>
      <div class="card"><h3>Top Highlights</h3><div class="list">${vm.providerStatus?'<div class="list-row"><span>Provider Modes</span><span class="muted">'+Object.values(vm.providerStatus).join(' / ')+'</span></div>':''}${compactItem(vm.hero)}</div></div></div>
    <div class="card"><h3>Issues / Exceptions</h3><div class="list">${issues}</div></div>
  </div>`;
}
