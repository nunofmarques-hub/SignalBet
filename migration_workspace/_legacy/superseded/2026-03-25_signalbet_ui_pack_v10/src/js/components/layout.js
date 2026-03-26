export function renderLayout(active, content){
  const routes = [['home','Home'],['pool','Opportunity Pool'],['bankroll','Banca'],['execution','Execution'],['history','Histórico']];
  return `
  <aside class="sidebar">
    <div class="brand"><img src="assets/logo-signalbet-radar-focus.svg" alt="SignalBet"/><small>Camada visual principal da app</small></div>
    <nav class="nav">${routes.map(([k,v])=>`<a href="#${k}" class="${active===k?'active':''}">${v}</a>`).join('')}</nav>
    <div class="footer-note">SignalBet = marca de produto<br/>ABC PRO = backbone interno</div>
  </aside>
  <main class="main">${content}</main>`;
}
export function topbar(title, right=''){
  return `<div class="topbar"><h1>${title}</h1><div class="right">${right}</div></div>`;
}
