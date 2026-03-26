import { badge } from './ui.js';
export function poolCard(row){
  const tone = row.decision_status === 'approved' ? 'green' : row.decision_status === 'reserve' ? 'amber' : 'cyan';
  return `<div class="card"><div class="section-head"><strong>${row.fixture}</strong>${badge(row.decision_status,tone)}</div><div class="muted small">${row.market} · ${row.module_source}</div><div class="hero-title">Score ${row.global_score}</div><div class="pill-row">${badge('conf '+row.confidence_norm,'cyan')}${badge('edge '+row.edge_norm,'lime')}${badge('risk '+row.risk_norm,'amber')}</div></div>`;
}
