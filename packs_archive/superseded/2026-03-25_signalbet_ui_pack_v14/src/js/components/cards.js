
import { badge, metric } from './ui.js';
export function topOpportunityCard(hero) {
  if (!hero) return `<div class="card"><h3>Sem top opportunity</h3></div>`;
  return `
  <div class="card">
    <div class="badges">${badge('Best of the Day','lime')}${badge(hero.module_source,'cyan')}${badge(hero.decision_status,'green')}</div>
    <h3>${hero.fixture}</h3>
    <div class="small">${hero.market}</div>
    <div class="grid" style="grid-template-columns:repeat(2,minmax(0,1fr));margin-top:12px">
      ${metric('Global Score', hero.global_score)}
      ${metric('Confidence', hero.confidence_norm)}
      ${metric('Edge', hero.edge_norm)}
      ${metric('Risk', hero.risk_norm)}
    </div>
  </div>`;
}
