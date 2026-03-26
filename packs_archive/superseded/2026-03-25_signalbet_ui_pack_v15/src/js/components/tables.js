import { badge } from './ui.js';
export function poolTable(rows){
  const body = rows.map(r => `<tr><td>${r.fixture}</td><td>${r.market}</td><td>${r.module_source}</td><td>${r.global_score}</td><td>${badge(r.decision_status, r.decision_status==='approved'?'green':r.decision_status==='reserve'?'amber':'cyan')}</td><td>${badge(r.execution_status,'cyan')}</td><td>${badge(r.data_quality_flag, r.data_quality_flag==='green'?'green':'amber')}</td></tr>`).join('');
  return `<table class="table"><thead><tr><th>Fixture</th><th>Market</th><th>Source</th><th>Score</th><th>Decision</th><th>Execution</th><th>Quality</th></tr></thead><tbody>${body}</tbody></table>`;
}
export function historyTable(rows){
  const body = rows.map(r => `<tr><td>${r.date}</td><td>${r.fixture}</td><td>${r.market}</td><td>${r.module_source}</td><td>${r.global_score}</td><td>${badge(r.result, r.result==='win'?'green':'red')}</td><td>${r.roi}</td></tr>`).join('');
  return `<table class="table"><thead><tr><th>Date</th><th>Fixture</th><th>Market</th><th>Source</th><th>Score</th><th>Result</th><th>ROI</th></tr></thead><tbody>${body}</tbody></table>`;
}
