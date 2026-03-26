export function shell(title, subtitle, body, route, sourceMode) {
  const links = [
    ['home','Home'], ['pool','Opportunity Pool'], ['bankroll','Banca'], ['execution','Execution'], ['history','Histórico']
  ].map(([key,label]) => `<a href="#${key}" class="${route===key?'active':''}" data-route="${key}">${label}</a>`).join('');
  return `
  <div class="layout">
    <aside class="sidebar">
      <div class="brand">
        <img src="assets/logo-signalbet-radar-focus.svg" alt="SignalBet" />
        <div><strong>SignalBet</strong><div class="muted">UI v13</div></div>
      </div>
      <nav class="nav">${links}</nav>
      <div class="card" style="margin-top:18px">
        <small>Source mode</small>
        <div class="row" style="margin-top:8px"><span class="chip cyan">${sourceMode}</span></div>
      </div>
    </aside>
    <main class="main">
      <div class="topbar">
        <div class="title-wrap"><h1>${title}</h1><p>${subtitle}</p></div>
        <div class="top-actions">
          <select class="select" id="sourceModeSelect">
            <option value="orchestrator_mock">orchestrator_mock</option>
            <option value="placeholder_live">placeholder_live</option>
            <option value="contract_mock">contract_mock</option>
          </select>
          <button class="btn secondary" id="reloadBtn">Atualizar</button>
        </div>
      </div>
      <section class="content">${body}</section>
    </main>
  </div>`;
}
