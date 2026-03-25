
import { getBankrollModel } from '../services/uiDataService.js';
import { alertItem, detailKV, kpiTile } from '../components/ui.js';
import { bankrollTable } from '../components/tables.js';
import { withPageState } from '../components/stateView.js';
import { getSelected } from '../core/store.js';

export function renderBankroll(state) {
  const data = getBankrollModel();
  const selected = getSelected('bankroll');
  const picked = data.decisions[selected] || data.decisions[0];
  return withPageState(state, () => `
    <section class="kpi-grid">${data.summary.map(([a,b]) => kpiTile(a,b)).join('')}</section>
    <section class="stack-2">
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Decision queue</h3><span class="chip cyan">approved / reduced / blocked / reserve</span></div>
        <div class="table-wrap">${bankrollTable(data.decisions, selected)}</div>
      </div>
      <div class="section-card detail-panel">
        <div class="section-head"><h3 class="section-title">Decision detail</h3></div>
        ${detailKV([
          ['Selected pick', picked.fixture], ['Decision', picked.decision_status], ['Stake', picked.stake], ['Exposure', picked.exposure_impact], ['Readiness', picked.execution_readiness], ['Reason code', picked.reason_code]
        ])}
        <div class="detail-box"><strong>Racional operacional</strong><div class="small">Approved por combinação forte de score, edge e risco baixo, sem conflito relevante na exposição corrente.</div></div>
        <div class="section-head" style="margin-top:8px;"><h3 class="section-title">Exposure mix</h3></div>
        ${data.exposure.map(([name,val]) => `<div style="margin-bottom:10px;"><div class="row" style="justify-content:space-between;"><span>${name}</span><span class="small">${val}%</span></div><div class="progress"><span style="width:${val}%"></span></div></div>`).join('')}
      </div>
    </section>
    <section class="section-card"><div class="section-head"><h3 class="section-title">Alertas de risco / conflito</h3></div><div class="alert-list">${data.alerts.map(alertItem).join('')}</div></section>
  `);
}
