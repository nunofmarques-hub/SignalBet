import { historyData } from '../../data/mock-data.js';
import { alertItem, detailKV, kpiTile, statusChip } from '../components/ui.js';
import { withPageState } from './helpers.js';

export function renderHistory(state) {
  return withPageState(state, () => `
    <section class="kpi-grid">${historyData.summary.map(([a,b]) => kpiTile(a,b)).join('')}</section>
    <section class="stack-2">
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Historical ledger</h3><div class="filters"><span class="filter-chip active">7D</span><span class="filter-chip">30D</span><span class="filter-chip">Approved</span><span class="filter-chip">Wins</span></div></div>
        <div class="table-wrap"><table><thead><tr><th>Date</th><th>Pick</th><th>Market</th><th>Module</th><th>Score</th><th>Conf</th><th>Edge</th><th>Risk</th><th>Decision</th><th>Execution</th><th>Result</th><th>Return</th><th>Quality</th></tr></thead><tbody>${historyData.ledger.map(r=>`<tr><td>${r[0]}</td><td><strong>${r[1]}</strong></td><td>${r[2]}</td><td>${r[3]}</td><td>${r[4]}</td><td>${r[5]}</td><td>${r[6]}</td><td>${r[7]}</td><td>${statusChip(r[8])}</td><td>${statusChip(r[9])}</td><td>${statusChip(r[10])}</td><td>${r[11]}</td><td>${statusChip(r[12])}</td></tr>`).join('')}</tbody></table></div>
      </div>
      <div class="section-card detail-panel">
        <div class="section-head"><h3 class="section-title">Validation panel</h3></div>
        ${detailKV([
          ['Selected pick', historyData.ledger[0][1]], ['Result', historyData.ledger[0][10]], ['Return', historyData.ledger[0][11]], ['Decision', historyData.ledger[0][8]], ['Execution', historyData.ledger[0][9]], ['Quality', historyData.ledger[0][12]]
        ])}
        <div class="detail-box"><strong>Trail resumido</strong><div class="small">Generated → entered pool → approved by bankroll → executed → settled.</div></div>
        <div class="section-head" style="margin-top:8px;"><h3 class="section-title">Insights</h3></div>
        <div class="alert-list">${historyData.insights.map(alertItem).join('')}</div>
      </div>
    </section>
  `);
}
