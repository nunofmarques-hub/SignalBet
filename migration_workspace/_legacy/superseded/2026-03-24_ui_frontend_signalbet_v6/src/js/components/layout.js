import { appState } from '../../data/mock-data.js';

export function sidebar(active) {
  const items = [
    ['home', 'Home', 'Cockpit'],
    ['pool', 'Opportunity Pool', 'GPS'],
    ['bankroll', 'Banca', 'Risk'],
    ['execution', 'Execution', 'Ops'],
    ['history', 'Histórico', 'Audit']
  ];
  return `
    <div class="brand"><img src="assets/logo-signalbet-radar-focus.svg" alt="SignalBet" /></div>
    <div class="brand-note">Produto visível: <strong>SignalBet</strong><br>Backbone interno: ABC PRO</div>
    <div class="nav-title">Navegação principal</div>
    <div class="nav-group">
      ${items.map(([key, label, tag]) => `<div class="nav-item ${active===key?'active':''}" data-page="${key}"><span>${label}</span><span class="tag">${tag}</span></div>`).join('')}
    </div>
    <div class="sidebar-footer">
      <button class="orchestrator-btn" id="openOrchestrator">Pôr tudo a correr</button>
      <div class="side-card">
        <div class="tile-label">Readiness do sistema</div>
        <div class="row" style="margin-top:10px;">${badge('Data/API', appState.readiness.data_api)} ${badge('GPS', appState.readiness.gps)} ${badge('Banca', appState.readiness.bankroll)}</div>
        <div class="small" style="margin-top:10px;">Módulos disponíveis: ${appState.readiness.modules} · Execution: ${appState.readiness.execution}</div>
      </div>
    </div>
  `;
}

function badge(label, value){
  const ok = value === 'ready';
  return `<span class="chip ${ok?'green':'amber'}">${label}: ${value}</span>`;
}

export function topbar(title, pageState, pageKey) {
  const states = ['success','loading','empty','error'];
  return `
    <div class="topbar-left">
      <div>
        <div class="breadcrumb">SignalBet / App principal</div>
        <div class="page-title">${title}</div>
      </div>
    </div>
    <div class="topbar-actions">
      <input class="search" placeholder="Pesquisar picks, módulos, jogos..." />
      <select class="select"><option>Hoje</option><option>7 dias</option><option>30 dias</option></select>
      <div class="page-states" data-state-group="${pageKey}">
        ${states.map(s => `<button class="state-switch ${pageState===s?'active':''}" data-state="${s}">${s}</button>`).join('')}
      </div>
    </div>
  `;
}

export function orchestratorDrawer() {
  return `
    <div class="drawer-head">
      <div>
        <div class="small">Entrada visual do App Core / Orchestrator</div>
        <div class="drawer-title">Pôr tudo a correr</div>
      </div>
      <button class="close-drawer" id="closeOrchestrator">Fechar</button>
    </div>
    <div class="success-banner"><div><span class="badge-dot"></span> Readiness global validada em staging forte</div><div class="small">UI não coordena a corrida</div></div>
    <div class="section-card" style="margin-top:14px;">
      <div class="section-head"><h3 class="section-title">Readiness do sistema</h3></div>
      <div class="kv">
        <div class="kv-item"><div class="kv-label">Data/API</div><div class="kv-value">READY</div></div>
        <div class="kv-item"><div class="kv-label">Módulos disponíveis</div><div class="kv-value">4</div></div>
        <div class="kv-item"><div class="kv-label">GPS</div><div class="kv-value">READY</div></div>
        <div class="kv-item"><div class="kv-label">Execution</div><div class="kv-value">READY</div></div>
      </div>
    </div>
    <div class="section-card" style="margin-top:14px;">
      <div class="section-head"><h3 class="section-title">Progresso da corrida</h3><span class="chip cyan">mock visual</span></div>
      <div class="progress"><span style="width:72%"></span></div>
      <div class="small" style="margin-top:10px;">72% — Data/API ok · módulos recolhidos · GPS consolidado · banca em decisão · execution a receber</div>
      <div class="timeline" style="margin-top:16px;">
        ${[
          ['Data/API', 'Providers oficiais verificados e estrutura pronta a consumo.'],
          ['Módulos', 'v12, Corners, BTTS e Cards disponíveis para corrida.'],
          ['GPS', 'Normalização multi-módulo e shortlist central gerada.'],
          ['Banca', 'Approved / Reduced / Blocked / Reserve aplicados.'],
          ['Execution', 'Intake real pronto a receber a shortlist final.']
        ].map(([t, d]) => `<div class="timeline-item"><div class="timeline-bullet"></div><div class="timeline-body"><strong>${t}</strong><div class="small">${d}</div></div></div>`).join('')}
      </div>
    </div>
    <div class="section-card" style="margin-top:14px;">
      <div class="section-head"><h3 class="section-title">Resumo final esperado</h3></div>
      <div class="kv">
        <div class="kv-item"><div class="kv-label">Oportunidades</div><div class="kv-value">18</div></div>
        <div class="kv-item"><div class="kv-label">Elegíveis</div><div class="kv-value">9</div></div>
        <div class="kv-item"><div class="kv-label">Approved</div><div class="kv-value">4</div></div>
        <div class="kv-item"><div class="kv-label">Pending execution</div><div class="kv-value">2</div></div>
      </div>
    </div>
  `;
}
