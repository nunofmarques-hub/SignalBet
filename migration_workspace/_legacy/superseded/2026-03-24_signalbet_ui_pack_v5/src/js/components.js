export function chip(text, type='gray') {
  return `<span class="chip ${type}">${text}</span>`;
}
export function score(label, value) {
  return `<span class="pill score">${label}: <strong>${value}</strong></span>`;
}
export function tile(label, value, subtle='') {
  return `<div class="tile"><div class="tile-label">${label}</div><div class="tile-value mono">${value}</div>${subtle ? `<div class="small">${subtle}</div>`:''}</div>`;
}
export function stateBlock(title, body, cta='') {
  return `<div class="state-box"><h3>${title}</h3><p class="small">${body}</p>${cta ? `<div class="button-row" style="justify-content:center"><button class="btn secondary">${cta}</button></div>`:''}</div>`;
}
export function topbar(title) {
  return `
    <div>
      <div class="tile-label">SignalBet</div>
      <div style="font-size:24px;font-weight:800">${title}</div>
    </div>
    <div class="topbar-actions">
      <input class="search" placeholder="Pesquisar fixture, mercado ou módulo" />
      <button class="btn secondary">Hoje</button>
      <button class="btn secondary">Todos os mercados</button>
    </div>`;
}
export function sidebar(active) {
  const items = [
    ['home','Home'],
    ['pool','Opportunity Pool'],
    ['bankroll','Banca / Decision'],
    ['execution','Execution / Tracking'],
    ['history','Histórico / Validação']
  ];
  return `
    <div class="logo-wrap"><img src="assets/logo-signalbet-radar-focus.svg" alt="SignalBet" /></div>
    <div class="small" style="margin-top:8px">ABC PRO como sistema interno</div>
    <div class="nav-group">
      ${items.map(([key,label]) => `<div class="nav-item ${active===key?'active':''}" data-page="${key}">${label}</div>`).join('')}
    </div>
    <div class="sidebar-footer">
      <button class="orchestrator-btn">Pôr tudo a correr</button>
    </div>`;
}
export function table(headers, rows) {
  return `<div class="table-wrap"><table><thead><tr>${headers.map(h=>`<th>${h}</th>`).join('')}</tr></thead><tbody>${rows.join('')}</tbody></table></div>`;
}
