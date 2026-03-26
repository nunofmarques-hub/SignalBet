
export function renderBankroll(vm){
  const row = (title, list) => `<div class="panel"><h3>${title}</h3><div class="small">${list.length} picks</div><ul>${list.map(x=>`<li>${x.fixture} · ${x.decision_status}</li>`).join('') || '<li>Sem itens</li>'}</ul></div>`;
  return `<div class="grid" style="grid-template-columns:repeat(3,minmax(0,1fr))">${row('Approved', vm.approved)}${row('Reduced', vm.reduced)}${row('Reserve', vm.reserve)}</div>`;
}
