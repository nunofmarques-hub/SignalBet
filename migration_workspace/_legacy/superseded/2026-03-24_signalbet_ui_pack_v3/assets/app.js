const data = window.SIGNALBET_DATA;
const routes = {
  home: renderHome,
  pool: renderPool,
  bank: renderBank,
  execution: renderExecution,
  history: renderHistory,
};
let currentRoute = 'home';

function appShell(content) {
  return `
    <aside class="sidebar">
      <div class="brand">
        <div class="logo"></div>
        <div>
          <h1>${data.app.productName}</h1>
          <small>powered by ${data.app.internalSystem}</small>
        </div>
      </div>
      <nav class="nav">
        ${navButton('home','Home')}
        ${navButton('pool','Opportunity Pool')}
        ${navButton('bank','Banca / Decisão')}
        ${navButton('execution','Execution / Tracking')}
        ${navButton('history','Histórico / Validação')}
      </nav>
      <div class="meta">
        <strong>Data/API oficial</strong>
        <span>${data.app.dataApiReference}</span>
        <div style="height:10px"></div>
        <strong>Orchestrator</strong>
        <span>Estado visual: ${data.app.orchestratorStatus}</span>
      </div>
    </aside>
    <main class="main">
      <div class="topbar">
        <div class="left">
          <h2>${topTitle()}</h2>
          <p>${topSubtitle()}</p>
        </div>
        <div class="top-actions">
          <input class="search" placeholder="Pesquisar pick, módulo ou mercado" />
          <button class="btn btn-secondary">Hoje</button>
          <button class="btn btn-primary">Pôr tudo a correr</button>
        </div>
      </div>
      <section class="content">${content}</section>
    </main>`;
}
function navButton(id,label){return `<button data-route="${id}" class="${currentRoute===id?'active':''}"><span>${label}</span><span class="dot"></span></button>`}
function topTitle(){return ({home:'Home / Dashboard',pool:'Opportunity Pool',bank:'Banca / Decision View',execution:'Execution / Tracking',history:'Histórico / Validação'})[currentRoute]}
function topSubtitle(){return ({home:'Cockpit do sistema e resumo operacional do dia',pool:'Ranking global de oportunidades do sistema',bank:'Decisão operacional, sizing e exposição',execution:'Fluxo operacional, estados e rastreabilidade',history:'Memória, validação e revisão do sistema'})[currentRoute]}
function chip(text, cls='badge-neutral'){return `<span class="badge ${cls}">${text}</span>`}
function kpi(title,value){return `<div class="card"><div class="kpi-title">${title}</div><div class="kpi-value">${value}</div></div>`}
function scoreSet(item){return `<div class="badges">${chip('Score '+item.global_score,'badge-score')}${chip('Conf. '+item.confidence_norm,'badge-blue')}${chip('Edge '+item.edge_norm,'badge-tier')}${chip('Risk '+item.risk_norm,item.risk_norm >= 40 ? 'badge-amber':'badge-neutral')}</div>`}
function statusChip(status){
  const map={approved:'badge-approved',reduced:'badge-amber',blocked:'badge-red',reserve:'badge-neutral',eligible:'badge-green',watchlist:'badge-amber',pending:'badge-blue',green:'badge-green',yellow:'badge-amber',none:'badge-neutral',ready:'badge-green',hold:'badge-amber',no:'badge-red',live:'badge-blue',settled:'badge-green',loss:'badge-red',win:'badge-green','no bet':'badge-neutral'};
  return chip(String(status).replace('_',' '), map[status]||'badge-neutral');
}
function renderHome(){
  const hero=data.home.hero;
  return `
    <div class="hero">
      <div class="card">
        ${chip('Best of the Day','badge-tier')}
        <div class="headline">${hero.pick_name}</div>
        <div class="row"><span class="muted">${hero.module_source} · ${hero.market}</span>${statusChip(hero.decision_status)}</div>
        <div style="height:12px"></div>
        ${scoreSet(hero)}
        <div style="height:16px"></div>
        <div class="row"><div class="muted">Priority Tier</div><div>${chip(hero.priority_tier,'badge-tier')}</div></div>
        <div style="height:16px"></div>
        <div class="row"><button class="btn btn-primary">Abrir Pick</button><button class="btn btn-secondary" onclick="go('pool')">Ver na Pool</button></div>
      </div>
      <div class="card side-panel">
        <h3>Resumo operacional</h3>
        <div class="subgrid">
          <div><div class="label">Decision</div><div class="value">${hero.decision_status}</div></div>
          <div><div class="label">Tier</div><div class="value">${hero.priority_tier}</div></div>
          <div><div class="label">Confidence</div><div class="value">${hero.confidence_norm}</div></div>
          <div><div class="label">Risk</div><div class="value">${hero.risk_norm}</div></div>
        </div>
        <div class="alert"><div class="icon">!</div><div><strong>Orchestrator visual pronto</strong><div class="muted">O botão “Pôr tudo a correr” já está preparado na UI. A lógica pertence ao App Core.</div></div></div>
      </div>
    </div>
    <div class="grid kpis">${data.home.kpis.map(x=>kpi(x[0],x[1])).join('')}</div>
    <div class="grid two">
      <div class="card"><h3>Opportunity highlights</h3><div class="list">${data.home.highlights.map(h=>`<div class="mini-card"><div class="row"><h4>${h.pick_name}</h4>${statusChip(h.decision_status)}</div><div class="muted">${h.module_source} · ${h.market}</div><div style="height:10px"></div>${scoreSet(h)}</div>`).join('')}</div></div>
      <div class="card"><h3>Módulos ativos</h3><div class="list"><div class="mini-card"><div class="row"><strong>v12</strong>${chip('6 picks','badge-green')}</div><div class="muted">Fonte principal do núcleo atual</div></div><div class="mini-card"><div class="row"><strong>BTTS</strong>${chip('2 picks','badge-blue')}</div><div class="muted">Em leitura oficial da base</div></div><div class="mini-card"><div class="row"><strong>Corners</strong>${chip('1 pick','badge-amber')}</div><div class="muted">Pré-integração / calibrar motor</div></div></div></div>
    </div>
  `;
}
function renderPool(){
  const top=data.pool.top;
  return `
    <div class="grid kpis">${data.pool.summary.map(x=>kpi(x[0],x[1])).join('')}</div>
    <div class="grid two">
      <div class="card"><h3>Top opportunity</h3><div class="headline" style="font-size:24px">${top.fixture} — ${top.market}</div><div class="row"><span class="muted">${top.module_source}</span>${statusChip(top.decision_status)}</div><div style="height:12px"></div>${scoreSet(top)}<div style="height:12px"></div><div class="badges">${statusChip(top.eligibility)}${statusChip(top.execution_status)}${statusChip(top.data_quality_flag)}</div></div>
      <div class="card side-panel"><h3>Resumo da pick</h3><div class="subgrid"><div><div class="label">Priority</div><div class="value">${top.priority_tier}</div></div><div><div class="label">Data Quality</div><div class="value">${top.data_quality_flag}</div></div><div><div class="label">Eligibility</div><div class="value">${top.eligibility}</div></div><div><div class="label">Execution</div><div class="value">${top.execution_status}</div></div></div><div class="muted">Pool central com ranking global, elegibilidade e transição para banca.</div></div>
    </div>
    <div class="card"><div class="filters"><span class="chip active">Todos</span><span class="chip">Over 1.5</span><span class="chip">Under 3.5</span><span class="chip">BTTS</span><span class="chip">Elegíveis</span><span class="chip">Approved</span><span class="chip">Mais filtros</span></div></div>
    <div class="grid two">
      <div class="card"><h3>Ranking global</h3><div class="table-wrap"><table><thead><tr><th>Fixture / Pick</th><th>Market</th><th>Source</th><th>Score</th><th>Conf.</th><th>Edge</th><th>Risk</th><th>Tier</th><th>Eligibility</th><th>Decision</th><th>Execution</th><th>Quality</th></tr></thead><tbody>${data.pool.rows.map(r=>`<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td><td>${r[4]}</td><td>${r[5]}</td><td>${r[6]}</td><td>${statusChip(r[7])}</td><td>${statusChip(r[8])}</td><td>${statusChip(r[9])}</td><td>${statusChip(r[10])}</td><td>${statusChip(r[11])}</td></tr>`).join('')}</tbody></table></div></div>
      <div class="card side-panel"><h3>Inspector</h3><div class="muted">Ao selecionar uma linha, o painel mostra scores, estados, racional curto e handoff para banca.</div><div class="alert"><div class="icon">i</div><div><strong>Data/API</strong><div class="muted">Mock payloads já espelham a estrutura oficial esperada da Data/API Layer.</div></div></div></div>
    </div>`;
}
function renderBank(){
  return `
    <div class="grid kpis">${data.bank.summary.map(x=>kpi(x[0],x[1])).join('')}</div>
    <div class="grid three">
      <div class="card"><h3>Approved</h3><div class="kpi-value">6</div><div class="muted">Stake alocada com readiness pronta</div></div>
      <div class="card"><h3>Reduced</h3><div class="kpi-value">2</div><div class="muted">Ajustes por exposição e correlação</div></div>
      <div class="card"><h3>Blocked / Reserve</h3><div class="kpi-value">8</div><div class="muted">Controlo disciplinar do sistema</div></div>
    </div>
    <div class="grid two">
      <div class="card"><h3>Decision queue</h3><div class="table-wrap"><table><thead><tr><th>Pick</th><th>Source</th><th>Score</th><th>Conf.</th><th>Edge</th><th>Risk</th><th>Decision</th><th>Stake</th><th>Exposure</th><th>Readiness</th></tr></thead><tbody>${data.bank.decisions.map(r=>`<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td><td>${r[4]}</td><td>${r[5]}</td><td>${statusChip(r[6])}</td><td>${r[7]}</td><td>${statusChip(r[8])}</td><td>${statusChip(r[9])}</td></tr>`).join('')}</tbody></table></div></div>
      <div class="card side-panel"><h3>Exposure panel</h3><div class="subgrid"><div><div class="label">Capacidade remanescente</div><div class="value">€140</div></div><div><div class="label">Exposição disponível</div><div class="value">€320</div></div><div><div class="label">Conflitos</div><div class="value">1</div></div><div><div class="label">Ready for execution</div><div class="value">3</div></div></div><div class="alert"><div class="icon">!</div><div><strong>Correlated picks detected</strong><div class="muted">Uma pick de corners foi reduzida por concentração no mesmo jogo.</div></div></div></div>
    </div>`;
}
function renderExecution(){
  return `
    <div class="grid kpis">${data.execution.summary.map(x=>kpi(x[0],x[1])).join('')}</div>
    <div class="grid two">
      <div class="card"><h3>Intake / queue</h3><div class="table-wrap"><table><thead><tr><th>Pick</th><th>Source</th><th>Decision</th><th>Stake</th><th>Readiness</th><th>Intake</th><th>Created</th><th>Queue age</th></tr></thead><tbody>${data.execution.queue.map(r=>`<tr><td>${r[0]}</td><td>${r[1]}</td><td>${statusChip(r[2])}</td><td>${r[3]}</td><td>${statusChip(r[4])}</td><td>${statusChip(r[5])}</td><td>${r[6]}</td><td>${r[7]}</td></tr>`).join('')}</tbody></table></div></div>
      <div class="card side-panel"><h3>Audit side panel</h3><div class="muted">Trail resumido: received from bankroll → intake → placed → live → settled.</div><div class="alert"><div class="icon">!</div><div><strong>Execution issue</strong><div class="muted">1 caso com settlement delay acima da média.</div></div></div></div>
    </div>
    <div class="card"><h3>Open / live tracking</h3><div class="table-wrap"><table><thead><tr><th>Pick</th><th>Market</th><th>Placed at</th><th>Status</th><th>Live status</th><th>Stake</th><th>Potential Return</th><th>Tracking Flag</th></tr></thead><tbody>${data.execution.live.map(r=>`<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td><td>${statusChip(r[3])}</td><td>${statusChip(r[4])}</td><td>${r[5]}</td><td>${r[6]}</td><td>${statusChip(r[7])}</td></tr>`).join('')}</tbody></table></div></div>`;
}
function renderHistory(){
  return `
    <div class="grid kpis">${data.history.summary.map(x=>kpi(x[0],x[1])).join('')}</div>
    <div class="grid two">
      <div class="card"><h3>Validation overview</h3><div class="table-wrap"><table><thead><tr><th>Grupo</th><th>Strike</th><th>ROI</th></tr></thead><tbody>${data.history.validations.map(r=>`<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join('')}</tbody></table></div></div>
      <div class="card side-panel"><h3>Insights / exceptions</h3><div class="alert"><div class="icon">i</div><div><strong>Review needed</strong><div class="muted">Picks com quality flag amarela tiveram ROI abaixo da média do período.</div></div></div><div class="mini-card"><strong>Approved picks</strong><div class="muted">Mantêm melhor consistência de strike e ROI.</div></div></div>
    </div>
    <div class="card"><h3>Historical ledger</h3><div class="table-wrap"><table><thead><tr><th>Date</th><th>Pick</th><th>Market</th><th>Source</th><th>Score</th><th>Conf.</th><th>Edge</th><th>Risk</th><th>Decision</th><th>Execution</th><th>Result</th><th>Return</th><th>Quality</th></tr></thead><tbody>${data.history.rows.map(r=>`<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td><td>${r[4]}</td><td>${r[5]}</td><td>${r[6]}</td><td>${r[7]}</td><td>${statusChip(r[8])}</td><td>${statusChip(r[9])}</td><td>${statusChip(r[10])}</td><td>${r[11]}</td><td>${statusChip(r[12])}</td></tr>`).join('')}</tbody></table></div></div>`;
}
function render(){document.getElementById('app').innerHTML = appShell(routes[currentRoute]()); bindNav();}
function bindNav(){document.querySelectorAll('[data-route]').forEach(btn=>btn.onclick=()=>go(btn.dataset.route));}
function go(route){currentRoute=route; render();}
window.go=go;
render();
