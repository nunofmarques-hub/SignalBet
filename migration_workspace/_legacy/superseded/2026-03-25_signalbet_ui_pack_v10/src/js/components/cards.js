import { chip } from './ui.js';
export function heroOpportunity(hero){
  return `<div class="card"><div style="display:flex;justify-content:space-between;align-items:center"><div>${chip('Best of the Day','lime')}</div>${chip(hero.decision_status,'green')}</div>
    <h2 style="margin-top:12px">${hero.fixture}</h2><div class="muted">${hero.market} · ${hero.module_source}</div>
    <div class="grid three" style="margin-top:16px"><div><div class="muted">Global Score</div><div class="kpi-number">${hero.global_score}</div></div><div><div class="muted">Confidence</div><div class="kpi-number">${hero.confidence_norm}</div></div><div><div class="muted">Edge</div><div class="kpi-number">${hero.edge_norm}</div></div></div>
    <div style="margin-top:14px">${chip('Risk ' + hero.risk_norm,'amber')} ${chip(hero.priority_tier,'cyan')}</div>
  </div>`;
}
export function compactItem(item){ return `<div class="list-row"><strong>${item.fixture}</strong><span>${chip(item.decision_status, item.decision_status.includes('APPROVED')?'green':'amber')}</span></div>`; }
