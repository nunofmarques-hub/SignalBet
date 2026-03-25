
import { getHistoryModel } from '../services/uiDataService.js';
import { alertItem, detailKV, kpiTile } from '../components/ui.js';
import { historyTable } from '../components/tables.js';
import { withPageState } from '../components/stateView.js';
import { getSelected } from '../core/store.js';

export function renderHistory(state) {
  const data = getHistoryModel();
  const selected = getSelected('history');
  const picked = data.ledger[selected] || data.ledger[0];
  return withPageState(state, () => `
    <section class="kpi-grid">${data.summary.map(([a,b]) => kpiTile(a,b)).join('')}</section>
    <section class="stack-2">
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Historical ledger</h3><div class="filters"><span class="filter-chip active">7D</span><span class="filter-chip">30D</span><span class="filter-chip">Approved</span><span class="filter-chip">Wins</span></div></div>
        <div class="table-wrap">${historyTable(data.ledger, selected)}</div>
      </div>
      <div class="section-card detail-panel">
        <div class="section-head"><h3 class="section-title">Validation panel</h3></div>
        ${detailKV([
          ['Selected pick', picked.fixture], ['Result', picked.result], ['Return', picked.roi], ['Decision', picked.decision_status], ['Execution', picked.execution_status], ['Quality', picked.data_quality_flag]
        ])}
        <div class="detail-box"><strong>Trail resumido</strong><div class="small">Generated → entered pool → approved by bankroll → executed → settled.</div></div>
        <div class="section-head" style="margin-top:8px;"><h3 class="section-title">Insights</h3></div>
        <div class="alert-list">${data.insights.map(alertItem).join('')}</div>
      </div>
    </section>
  `);
}
