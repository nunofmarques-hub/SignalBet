import { getTestMatrix } from './services/uiDataService.js';
const matrix = await getTestMatrix();
const latest = matrix[matrix.length-1].observed;
document.getElementById('requested').textContent = latest.requested_mode;
document.getElementById('observed').textContent = latest.observed_mode;
document.getElementById('status').textContent = latest.bridge_status;
const rows = matrix.map(m=>`<tr><td>${m.scenario}</td><td class="${m.pass?'ok':'bad'}">${m.pass?'PASS':'FAIL'}</td><td>${m.observed.observed_mode||'-'}</td><td>${m.observed.bridge_status||'-'}</td><td>${m.note}</td></tr>`).join('');
document.getElementById('matrix').innerHTML = `<table><thead><tr><th>Cenário</th><th>Resultado</th><th>Observed mode</th><th>Bridge status</th><th>Nota</th></tr></thead><tbody>${rows}</tbody></table>`;
document.getElementById('meta').textContent = JSON.stringify(latest,null,2);
