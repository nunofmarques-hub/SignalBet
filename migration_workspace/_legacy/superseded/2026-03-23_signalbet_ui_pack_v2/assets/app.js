const app = document.getElementById('app');
const state = { screen: 'home' };

function logoSVG() {
  return `
  <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="SignalBet logo">
    <circle cx="30" cy="34" r="18" stroke="#F5F7FA" stroke-width="5" stroke-dasharray="82 36" stroke-linecap="round"/>
    <circle cx="30" cy="34" r="5" fill="#B8FF3B"/>
    <path d="M34 28L53 22L47 33L34 28Z" fill="#B8FF3B"/>
  </svg>`;
}

function chip(value) {
  const cls = String(value).toLowerCase().replace(/\s+/g, '_');
  return `<span class="chip ${cls}">${String(value).replace(/_/g,' ')}</span>`;
}
function scorePill(label, value) {
  const display = typeof value === 'number' ? (value <= 1 ? Math.round(value*100)+'%' : value) : value;
  return `<span class="pill score">${label} ${display}</span>`;
}
function kpiGrid(items) {
  return `<div class="kpi-grid">${items.map(([label,val])=>`<div class="kpi"><div class="label">${label}</div><div class="value">${val}</div></div>`).join('')}</div>`;
}

function sidebar() {
  const items = [
    ['home','Home'],['pool','Opportunity Pool'],['banca','Banca / Decisão'],['execution','Execution'],['historico','Histórico']
  ];
  return `
  <aside class="sidebar">
    <div class="brand">
      ${logoSVG()}
      <div>
        <div class="brand-name">Signal<span class="bet">Bet</span></div>
        <div class="brand-sub">Menos ruído. Mais sinal.</div>
      </div>
    </div>
    <nav class="nav">
      ${items.map(([key,label])=>`<button class="${state.screen===key?'active':''}" data-screen="${key}">${label}</button>`).join('')}
    </nav>
    <div class="sidebar-footer">
      <div style="font-weight:700;margin-bottom:6px">Pôr tudo a correr</div>
      <div class="footer-note">Entrada visual pronta. Fluxo real pertence ao App Core / Orchestrator.</div>
      <button class="button primary" style="width:100%;margin-top:12px">Abrir launcher</button>
    </div>
  </aside>`;
}

function topbar() {
  return `<header class="topbar">
    <div class="muted">UI staging pack v2 · frontend implementável</div>
    <div class="top-actions">
      <button class="ghost small">Hoje</button>
      <button class="ghost small">Todos os mercados</button>
      <button class="ghost small">Online</button>
    </div>
  </header>`;
}

function heroHome() {
  const h = SignalBetMock.home.hero;
  return `<section class="hero">
    <div>
      <div class="muted">Best of the Day</div>
      <h2>${h.fixture}</h2>
      <div class="muted">${h.market} · ${h.module_source}</div>
      <div class="meta">
        ${scorePill('GS', h.global_score)}
        ${scorePill('Conf', h.confidence_norm)}
        ${scorePill('Edge', h.edge_norm)}
        ${scorePill('Risk', h.risk_norm)}
        ${chip(h.priority_tier)}
        ${chip(h.decision_status)}
        ${chip(h.execution_status)}
        ${chip(h.data_quality_flag)}
      </div>
    </div>
    <div class="actions"><button class="button primary">Abrir pick</button><button class="ghost">Ver na pool</button></div>
  </section>`;
}

function renderHome() {
  return `
    <div class="page-title"><div><h1>Home / Dashboard</h1><p>Cockpit operacional do sistema SignalBet.</p></div><button class="button primary">Pôr tudo a correr</button></div>
    ${heroHome()}
    ${kpiGrid(SignalBetMock.home.kpis)}
    <div class="grid-2">
      <section class="panel"><h3>Destaques do dia</h3><div class="list">${SignalBetMock.home.highlights.map(x=>`<div class="list-item"><strong>${x.fixture}</strong><small>${x.market} · ${x.decision_status}</small><div class="meta">${scorePill('GS',x.global_score)} ${scorePill('Conf',x.confidence_norm)} ${scorePill('Edge',x.edge_norm)}</div></div>`).join('')}</div></section>
      <section class="right-stack">
        <div class="panel"><h3>Snapshot da banca</h3><div class="metric-line"><span>Approved today</span><strong>5 picks</strong></div><div class="metric-line"><span>Allocated stake</span><strong>4.75u</strong></div><div class="metric-line"><span>Remaining capacity</span><strong>24.3u</strong></div></div>
        <div class="panel"><h3>Execution snapshot</h3><div class="metric-line"><span>Pending intake</span><strong>2</strong></div><div class="metric-line"><span>Live</span><strong>1</strong></div><div class="metric-line"><span>Settled today</span><strong>8</strong></div></div>
        ${SignalBetMock.home.alerts.map(a=>`<div class="alert ${a.level}">${a.text}</div>`).join('')}
      </section>
    </div>`;
}

function renderPool() {
  const top = SignalBetMock.pool[0];
  return `
    <div class="page-title"><div><h1>Opportunity Pool</h1><p>Ranking global de oportunidades do sistema.</p></div><div class="actions"><button class="ghost">Filtros</button><button class="button primary">Saved view</button></div></div>
    ${kpiGrid([['Total Opportunities','23'],['Eligible','18'],['Approved','6'],['Reserve','4'],['Blocked','2'],['Avg Global Score','78']])}
    <section class="hero"><div><div class="muted">Top Opportunity</div><h2>${top.fixture}</h2><div class="muted">${top.market} · odd ${top.odd} · ${top.module_source}</div><div class="meta">${scorePill('GS',top.global_score)} ${scorePill('Conf',top.confidence_norm)} ${scorePill('Edge',top.edge_norm)} ${scorePill('Risk',top.risk_norm)} ${chip(top.priority_tier)} ${chip(top.eligibility)}</div></div><button class="button primary">Abrir pick</button></section>
    <div class="grid-2">
      <section class="table-card rows-3">
        <div class="table-head"><div>Pick</div><div>Módulo</div><div>GS</div><div>Conf</div><div>Edge</div><div>Decision</div><div>Execution</div><div>Quality</div></div>
        ${SignalBetMock.pool.map(r=>`<div class="table-row"><div><strong>${r.fixture}</strong><small>${r.market} · odd ${r.odd}</small></div><div>${r.module_source}<small>${r.priority_tier}</small></div><div>${r.global_score}</div><div>${Math.round(r.confidence_norm*100)}%</div><div>${Math.round(r.edge_norm*100)}%</div><div>${chip(r.decision_status)}</div><div>${chip(r.execution_status)}</div><div>${chip(r.data_quality_flag)}</div></div>`).join('')}
      </section>
      <section class="panel"><h3>Inspector</h3><div class="panel-sub">Detalhe rápido da pick selecionada.</div><div class="metric-line"><span>Fixture</span><strong>${top.fixture}</strong></div><div class="metric-line"><span>Market</span><strong>${top.market}</strong></div><div class="metric-line"><span>Eligibility</span><span>${chip(top.eligibility)}</span></div><div class="metric-line"><span>Decision</span><span>${chip(top.decision_status)}</span></div><div class="metric-line"><span>Execution</span><span>${chip(top.execution_status)}</span></div><div class="metric-line"><span>Data quality</span><span>${chip(top.data_quality_flag)}</span></div><div class="actions" style="margin-top:14px"><button class="button primary">Abrir detalhe</button><button class="ghost">Abrir banca</button></div></section>
    </div>`;
}

function renderBanca() {
  const q = SignalBetMock.banca.queue;
  return `
    <div class="page-title"><div><h1>Banca / Decision View</h1><p>Decisão operacional, sizing e controlo de exposição.</p></div><button class="button primary">Executar picks aprovadas</button></div>
    ${kpiGrid([['Bankroll Base',SignalBetMock.banca.summary.bankroll_base],['Available Exposure',SignalBetMock.banca.summary.available_exposure],['Allocated Stake',SignalBetMock.banca.summary.allocated_stake],['Remaining Capacity',SignalBetMock.banca.summary.remaining_capacity],['Approved Today','2'],['Blocked','1']])}
    <div class="grid-2">
      <section class="table-card rows-2">
        <div class="table-head"><div>Pick</div><div>Scores</div><div>Decisão</div><div>Stake</div><div>Impacto</div><div>Ação</div></div>
        ${q.map(r=>`<div class="table-row"><div><strong>${r.fixture}</strong><small>${r.market} · ${r.module_source}</small></div><div>${scorePill('GS',r.global_score)} ${scorePill('Conf',r.confidence_norm)} ${scorePill('Edge',r.edge_norm)} ${scorePill('Risk',r.risk_norm)}</div><div>${chip(r.decision_status)}<small>${r.reason_code}</small></div><div><strong>${r.stake}</strong><small>${r.execution_readiness}</small></div><div>${r.exposure_impact}</div><div>${r.decision_status==='blocked'?'<button class="ghost small">Bloqueado</button>':'<button class="button small primary">Confirmar</button>'}</div></div>`).join('')}
      </section>
      <section class="right-stack">
        <div class="panel"><h3>Resumo de decisão</h3><div class="metric-line"><span>Approved</span><strong>2 · 4.75u</strong></div><div class="metric-line"><span>Reduced</span><strong>1 · 1.00u</strong></div><div class="metric-line"><span>Blocked</span><strong>1 · 0u</strong></div></div>
        <div class="panel"><h3>Capacidade pós-decisão</h3><div class="progress"><span style="width:79%"></span></div><div class="metric-line"><span>Disponível</span><strong>23.4u</strong></div><div class="metric-line"><span>Dentro dos limites</span><strong>Sim</strong></div></div>
        <div class="panel"><h3>Regras ativas</h3><div class="metric-line"><span>Máx. por pick</span><strong>3u</strong></div><div class="metric-line"><span>Exposição total</span><strong>&lt; 6%</strong></div><div class="metric-line"><span>Mín. global score</span><strong>70</strong></div></div>
      </section>
    </div>`;
}

function renderExecution() {
  return `
    <div class="page-title"><div><h1>Execution / Tracking</h1><p>Pipeline operacional do intake ao settlement.</p></div><button class="ghost">Ver audit trail</button></div>
    ${kpiGrid(SignalBetMock.execution.summary)}
    <div class="grid-2">
      <section class="table-card rows-2">
        <div class="table-head"><div>Pending / Queue</div><div>Módulo</div><div>Status</div><div>Queue age</div><div>Readiness</div><div>Ação</div></div>
        ${SignalBetMock.execution.queue.map(r=>`<div class="table-row"><div><strong>${r.fixture}</strong><small>${r.market} · ${r.created_at}</small></div><div>${r.module_source}</div><div>${chip(r.execution_status)} ${chip(r.intake_status)}</div><div>${r.queue_age}</div><div>${chip(r.decision_status)}</div><div><button class="button small primary">Tracking</button></div></div>`).join('')}
      </section>
      <section class="panel"><h3>Fluxo de execução</h3><div class="panel-sub">Approved → Intake → Placed → Live → Settled</div><div class="metric-line"><span>Taxa de sucesso</span><strong>98%</strong></div><div class="metric-line"><span>Últimos 30 dias</span><strong>186/190 execuções</strong></div></section>
    </div>
    <section class="table-card rows-2">
      <div class="table-head"><div>Open / Live</div><div>Placed at</div><div>Status</div><div>Stake</div><div>Potential Return</div><div>Ação</div></div>
      ${SignalBetMock.execution.live.map(r=>`<div class="table-row"><div><strong>${r.fixture}</strong><small>${r.market}</small></div><div>${r.placed_at}</div><div>${chip(r.execution_status)} ${chip(r.live_status)}</div><div>${r.stake}</div><div>${r.potential_return}</div><div><button class="ghost small">Abrir</button></div></div>`).join('')}
    </section>`;
}

function renderHistorico() {
  const h = SignalBetMock.history;
  return `
    <div class="page-title"><div><h1>Histórico / Validação</h1><p>Memória, performance e validação retrospetiva do sistema.</p></div><button class="ghost">Últimos 30 dias</button></div>
    ${kpiGrid(h.summary)}
    <div class="grid-2">
      <section class="table-card rows-4">
        <div class="table-head"><div>Data</div><div>Pick</div><div>Módulo</div><div>GS</div><div>Conf</div><div>Decisão</div><div>Resultado</div><div>ROI</div><div>Quality</div></div>
        ${h.ledger.map(r=>`<div class="table-row"><div>${r.date}</div><div><strong>${r.fixture}</strong><small>${r.market}</small></div><div>${r.module_source}</div><div>${r.global_score}</div><div>${Math.round(r.confidence_norm*100)}%</div><div>${chip(r.decision_status)}</div><div>${chip(r.result)}</div><div>${r.roi}</div><div>${chip(r.data_quality_flag)}</div></div>`).join('')}
      </section>
      <section class="right-stack">
        <div class="panel"><h3>Performance por módulo</h3><div class="metric-line"><span>Over 1.5 Equipa</span><strong>+6.40u</strong></div><div class="metric-line"><span>Over 1.5 Jogo</span><strong>+4.85u</strong></div><div class="metric-line"><span>Under 3.5</span><strong>+1.50u</strong></div></div>
        <div class="panel"><h3>Impacto da decisão</h3><div class="metric-line"><span>Approved</span><strong>+26.2%</strong></div><div class="metric-line"><span>Reduced</span><strong>+9.8%</strong></div><div class="metric-line"><span>Blocked</span><strong>0u</strong></div></div>
        <div class="panel"><h3>Validação</h3><div class="metric-line"><span>Baseline v11.5</span><strong>Validada</strong></div><div class="metric-line"><span>Profit factor</span><strong>1.53</strong></div><div class="metric-line"><span>Max drawdown</span><strong>6u</strong></div></div>
      </section>
    </div>`;
}

function renderScreen() {
  switch(state.screen){
    case 'pool': return renderPool();
    case 'banca': return renderBanca();
    case 'execution': return renderExecution();
    case 'historico': return renderHistorico();
    default: return renderHome();
  }
}

function mount() {
  app.innerHTML = `<div class="app-shell">${sidebar()}<div class="main">${topbar()}<main class="content">${renderScreen()}</main></div></div>`;
  app.querySelectorAll('[data-screen]').forEach(btn => btn.addEventListener('click', () => {
    state.screen = btn.getAttribute('data-screen');
    mount();
  }));
}
mount();
