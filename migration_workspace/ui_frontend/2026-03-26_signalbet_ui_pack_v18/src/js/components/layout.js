export function shell(content){
  return `<div class="app">
    <aside class="sidebar">
      <div class="brand"><img src="assets/logo-signalbet-radar-focus.svg" alt="logo"/><span>SignalBet</span></div>
      <nav class="nav">
        <a class="active">Home</a><a>Opportunity Pool</a><a>Banca</a><a>Execution</a><a>Histórico</a>
      </nav>
      <div class="small muted sidebar-note">UI v18 · Protected Real Consumption</div>
    </aside>
    <main class="main">${content}</main>
  </div>`;
}
