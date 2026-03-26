
export function shellTemplate(activePage, content) {
  const items = [['home','Home'],['pool','Opportunity Pool'],['bankroll','Banca'],['execution','Execution'],['history','Histórico']];
  const nav = items.map(([key,label]) => `<a href="#${key}" class="${activePage===key?'active':''}" data-page="${key}">${label}</a>`).join('');
  return `
  <div class="app-shell">
    <aside class="sidebar">
      <div class="logo-wrap"><img src="./assets/logo-signalbet-radar-focus.svg" alt="SignalBet" /></div>
      <nav class="nav">${nav}</nav>
      <div class="footer-meta">Frontend UI v14<br/>SignalBet / ABC PRO</div>
    </aside>
    <div class="main">
      <div class="topbar">
        <div><strong>SignalBet</strong> <span class="small">UI v14 — First Real Read Pack</span></div>
        <div class="top-actions">
          <select id="runtime-mode-select">
            <option value="orchestrator_mock">orchestrator_mock</option>
            <option value="real_read_protected">real_read_protected</option>
            <option value="placeholder_live">placeholder_live</option>
          </select>
          <button class="btn btn-primary" id="btn-refresh">Atualizar</button>
        </div>
      </div>
      <div class="page">${content}</div>
    </div>
  </div>`;
}
