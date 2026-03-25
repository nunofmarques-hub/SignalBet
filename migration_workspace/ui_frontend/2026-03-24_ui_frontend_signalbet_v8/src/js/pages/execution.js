
import { getExecutionModel } from '../services/uiDataService.js';
import { alertItem, detailKV, kpiTile, statusChip } from '../components/ui.js';
import { executionIntakeTable, executionLiveTable } from '../components/tables.js';
import { withPageState } from '../components/stateView.js';
import { getSelected } from '../core/store.js';

export function renderExecution(state) {
  const data = getExecutionModel();
  const selected = getSelected('executionIntake');
  const picked = data.intake[selected] || data.intake[0];
  return withPageState(state, () => `
    <section class="kpi-grid">${data.summary.map(([a,b]) => kpiTile(a,b)).join('')}</section>
    <section class="stack-2">
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Intake / queue</h3><span class="chip amber">estado operacional</span></div>
        <div class="table-wrap">${executionIntakeTable(data.intake, selected)}</div>
      </div>
      <div class="section-card detail-panel">
        <div class="section-head"><h3 class="section-title">Audit panel</h3></div>
        ${detailKV([
          ['Selected pick', picked.fixture], ['Decision', picked.decision_status], ['Intake', picked.intake_status], ['Queue age', picked.queue_age], ['Readiness', picked.execution_readiness], ['Created', picked.created_at]
        ])}
        <div class="detail-box"><strong>Trail resumido</strong><div class="small">Received from bankroll → queued for intake → awaiting placement → not yet settled.</div></div>
      </div>
    </section>
    <section class="stack-2">
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Open / live tracking</h3></div>
        <div class="table-wrap">${executionLiveTable(data.live)}</div>
      </div>
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Recent settlement</h3></div>
        <div class="list">${data.settled.map(r => `<div class="list-item"><div class="row" style="justify-content:space-between;"><strong>${r.fixture}</strong>${statusChip(r.result)}</div><div class="small">${r.settled_at} · ${r.delta}</div></div>`).join('')}</div>
      </div>
    </section>
    <section class="section-card"><div class="section-head"><h3 class="section-title">Alertas operacionais</h3></div><div class="alert-list">${data.alerts.map(alertItem).join('')}</div></section>
  `);
}
