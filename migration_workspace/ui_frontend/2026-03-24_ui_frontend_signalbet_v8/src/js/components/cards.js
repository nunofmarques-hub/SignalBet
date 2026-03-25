
import { scoreBadge, statusChip } from './ui.js';

export function compactOpportunityCard(h) {
  return `<div class="list-item"><div class="row" style="justify-content:space-between;"><strong>${h.fixture}</strong>${statusChip(h.decision_status)}</div><div class="small">${h.market} · ${h.module_source}</div><div class="row" style="margin-top:10px;">${scoreBadge('Score', h.global_score)}${scoreBadge('Conf', h.confidence_norm)}${scoreBadge('Edge', h.edge_norm)}</div></div>`;
}

export function moduleCard(m){
  return `<div class="list-item"><div class="row" style="justify-content:space-between;"><strong>${m.name}</strong>${statusChip(m.health)}</div><div class="small">${m.picks} picks hoje</div></div>`;
}
