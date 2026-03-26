import { chip } from './ui.js';
export function poolTable(items) {
  const rows = items.map(i => `<tr><td>${i.fixture}</td><td>${i.market}</td><td>${i.module_source}</td><td>${i.global_score}</td><td>${i.confidence_norm}</td><td>${i.edge_norm}</td><td>${i.risk_norm}</td><td>${chip(i.decision_status, i.decision_status==='approved'?'green':'amber')}</td></tr>`).join('');
  return `<table class="table"><thead><tr><th>Fixture</th><th>Market</th><th>Module</th><th>Score</th><th>Conf.</th><th>Edge</th><th>Risk</th><th>Decision</th></tr></thead><tbody>${rows}</tbody></table>`;
}
export function historyTable(items) {
  const rows = items.map(i => `<tr><td>${i.date}</td><td>${i.fixture}</td><td>${i.market}</td><td>${i.module_source}</td><td>${i.global_score}</td><td>${chip(i.result, i.result==='win'?'green':'red')}</td><td>${i.roi}</td></tr>`).join('');
  return `<table class="table"><thead><tr><th>Date</th><th>Fixture</th><th>Market</th><th>Module</th><th>Score</th><th>Result</th><th>ROI</th></tr></thead><tbody>${rows}</tbody></table>`;
}
