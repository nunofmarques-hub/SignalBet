import { chip } from './ui.js';
export function renderPoolTable(items){
  const rows = items.map(i=>`<tr><td>${i.fixture}</td><td>${i.market}</td><td>${i.module_source}</td><td>${i.global_score}</td><td>${i.confidence_norm}</td><td>${i.edge_norm}</td><td>${i.risk_norm}</td><td>${chip(i.decision_status, i.decision_status.includes('APPROVED')?'green':'amber')}</td></tr>`).join('');
  return `<table class="table"><thead><tr><th>Fixture</th><th>Market</th><th>Module</th><th>Score</th><th>Confidence</th><th>Edge</th><th>Risk</th><th>Decision</th></tr></thead><tbody>${rows}</tbody></table>`;
}
export function renderSimpleTable(items, cols){
  const head = cols.map(c=>`<th>${c.label}</th>`).join('');
  const rows = items.map(item=>`<tr>${cols.map(c=>`<td>${item[c.key] ?? ''}</td>`).join('')}</tr>`).join('');
  return `<table class="table"><thead><tr>${head}</tr></thead><tbody>${rows}</tbody></table>`;
}
