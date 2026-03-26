
import { badge } from './ui.js';
function kindFromValue(v=''){
  const s=String(v).toUpperCase();
  if (['APPROVED','READY','GREEN','WIN'].includes(s)) return 'green';
  if (['REDUCED','AMBER','RESERVE','PENDING','ELIGIBLE'].includes(s)) return 'amber';
  if (['BLOCKED','ERROR','RED','LOSS'].includes(s)) return 'red';
  return 'cyan';
}
export function poolTable(rows=[]) {
  const body = rows.map(r => `<tr>
    <td>${r.fixture}</td><td>${r.market}</td><td>${r.module_source}</td><td>${r.global_score}</td>
    <td>${r.confidence_norm}</td><td>${r.edge_norm}</td><td>${r.risk_norm}</td>
    <td>${badge(r.priority_tier,'cyan')}</td>
    <td>${badge(r.eligibility, kindFromValue(r.eligibility))}</td>
    <td>${badge(r.decision_status, kindFromValue(r.decision_status))}</td>
    <td>${badge(r.execution_status, kindFromValue(r.execution_status))}</td>
    <td>${badge(r.data_quality_flag, kindFromValue(r.data_quality_flag))}</td>
  </tr>`).join('');
  return `<div class="table-wrap"><table>
    <thead><tr><th>Fixture</th><th>Market</th><th>Module</th><th>Score</th><th>Conf.</th><th>Edge</th><th>Risk</th><th>Tier</th><th>Eligibility</th><th>Decision</th><th>Execution</th><th>Quality</th></tr></thead>
    <tbody>${body}</tbody>
  </table></div>`;
}
