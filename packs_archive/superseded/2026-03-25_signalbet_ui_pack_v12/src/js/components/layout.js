export function shell({ active, content, providerMode }) {
  const routes = [
    ['home', 'Home'], ['pool', 'Opportunity Pool'], ['bankroll', 'Banca'], ['execution', 'Execution'], ['history', 'Histórico']
  ];
  const nav = routes.map(([key, label]) => `<a href="#${key}" class="${active===key?'active':''}">${label}</a>`).join('');
  return `
    <div class="app-shell">
      <aside class="sidebar">
        <div class="logo"><img src="assets/logo-signalbet-radar-focus.svg" alt="SignalBet"/><span>SignalBet</span></div>
        <div class="muted small" style="margin-bottom:12px">Modo fonte: ${providerMode}</div>
        <nav class="nav">${nav}</nav>
      </aside>
      <main class="main">${content}</main>
    </div>`;
}
