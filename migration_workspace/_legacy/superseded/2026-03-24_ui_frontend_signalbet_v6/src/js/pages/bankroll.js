import { bankrollData } from '../../data/mock-data.js';
import { alertItem, detailKV, kpiTile, scoreBadge, statusChip } from '../components/ui.js';
import { withPageState } from './helpers.js';

export function renderBankroll(state) {
  return withPageState(state, () => `
    <section class="kpi-grid">${bankrollData.summary.map(([a,b]) => kpiTile(a,b)).join('')}</section>
    <section class="stack-2">
      <div class="section-card">
        <div class="section-head"><h3 class="section-title">Decision queue</h3><span class="chip cyan">approved / reduced / blocked / reserve</span></div>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Pick</th><th>Module</th><th>Score</th><th>Conf</th><th>Edge</th><th>Risk</th><th>Decision</th><th>Stake</th><th>Exposure</th><th>Readiness</th></tr></thead>
            <tbody>
              ${bankrollData.decisions.map(r => `<tr><td><strong>${r[0]}</strong></td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td><td>${r[4]}</td><td>${r[5]}</td><td>${statusChip(r[6])}</td><td class="mono">${r[7]}</td><td>${statusChip(r[8])}</td><td>${statusChip(r[10])}</td></tr>`).join('')}
            </tbody>
          </table>
        </div>
      </div>
      <div class="section-card detail-panel">
        <div class="section-head"><h3 class="section-title">Decision detail</h3></div>
        ${detailKV([
          ['Selected pick', bankrollData.decisions[0][0]], ['Decision', bankrollData.decisions[0][6]], ['Stake', bankrollData.decisions[0][7]], ['Exposure', bankrollData.decisions[0][8]], ['Readiness', bankrollData.decisions[0][10]], ['Remaining cap.', '€220']
        ])}
        <div class="detail-box"><strong>Racional operacional</strong><div class="small">Approved por combinação forte de score, edge e risco baixo, sem conflito relevante na exposição corrente.</div></div>
        <div class="section-head" style="margin-top:8px;"><h3 class="section-title">Exposure mix</h3></div>
        ${bankrollData.exposure.map(([name,val]) => `<div style="margin-bottom:10px;"><div class="row" style="justify-content:space-between;"><span>${name}</span><span class="small">${val}%</span></div><div class="progress"><span style="width:${val}%"></span></div></div>`).join('')}
      </div>
    </section>
    <section class="section-card"><div class="section-head"><h3 class="section-title">Alertas de risco / conflito</h3></div><div class="alert-list">${bankrollData.alerts.map(alertItem).join('')}</div></section>
  `);
}
