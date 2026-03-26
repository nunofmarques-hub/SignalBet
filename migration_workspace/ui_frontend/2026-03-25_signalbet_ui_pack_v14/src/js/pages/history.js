
export function renderHistory(vm){
  return `<div class="panel"><h3>Histórico / Validação</h3><table style="width:100%"><thead><tr><th>Date</th><th>Fixture</th><th>Result</th><th>Decision</th></tr></thead><tbody>${vm.rows.map(r=>`<tr><td>${r.date}</td><td>${r.fixture}</td><td>${r.result}</td><td>${r.decision_status}</td></tr>`).join('')}</tbody></table></div>`;
}
