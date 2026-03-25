import { alertItem } from './ui.js';

export function sidebar(active, app){
  const items = [
    ['home', 'Home', 'Cockpit'],
    ['pool', 'Opportunity Pool', 'GPS'],
    ['bankroll', 'Banca', 'Risk'],
    ['execution', 'Execution', 'Ops'],
    ['history', 'Histórico', 'Audit']
  ];
  return `
    <div class="brand"><img src="assets/logo-signalbet-radar-focus.svg" alt="SignalBet" /></div>
    <div class="brand-note">Produto visível: <strong>${app.brand}</strong><br>Backbone interno: ${app.backbone}</div>
    <div class="nav-title">Navegação principal</div>
    <div class="nav-group">
      ${items.map(([key, label, tag]) => `<div class="nav-item ${active===key?'active':''}" data-page="${key}"><span>${label}</span><span class="tag">${tag}</span></div>`).join('')}
    </div>
    <div class="sidebar-footer">
      <button class="orchestrator-btn" id="openOrchestrator">Pôr tudo a correr</button>
      <div class="side-card">
        <div class="tile-label">Readiness do sistema</div>
        <div class="row" style="margin-top:10px; gap:8px; flex-wrap:wrap;">${miniBadge('Data/API', app.readiness.data_api)} ${miniBadge('GPS', app.readiness.gps)} ${miniBadge('Banca', app.readiness.bankroll)} ${miniBadge('Execution', app.readiness.execution)}</div>
        <div class="small" style="margin-top:10px;">Módulos disponíveis: ${app.readiness.modules} · estado global: ${app.readiness.orchestrator}</div>
      </div>
    </div>
  `;
}

function miniBadge(label, value){
  const cls = value === 'ready' ? 'green' : value === 'staged' || value === 'warning' ? 'amber' : 'red';
  return `<span class="chip ${cls}">${label}: ${String(value).replace(/_/g,' ')}</span>`;
}

export function topbar(title, pageState){
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
      <div class="page-states">
        ${states.map(s => `<button class="state-switch ${pageState===s?'active':''}" data-state="${s}">${s}</button>`).join('')}
      </div>
    </div>
  `;
}

function bannerByStatus(run){
  if(run.status === 'running') return `<div class="warn-banner"><div><span class="badge-dot" style="background:var(--amber)"></span> ${run.title}</div><button class="btn ghost" id="cycleRunState">Mudar estado</button></div>`;
  if(run.status === 'partial') return `<div class="warn-banner"><div><span class="badge-dot" style="background:var(--amber)"></span> ${run.title}</div><button class="btn ghost" id="cycleRunState">Mudar estado</button></div>`;
  if(run.status === 'error') return `<div class="alert critical"><div><strong>${run.title}</strong><div class="small">${run.message}</div></div><button class="btn ghost" id="cycleRunState">Mudar estado</button></div>`;
  if(run.status === 'success') return `<div class="success-banner"><div><span class="badge-dot"></span> ${run.title}</div><button class="btn ghost" id="cycleRunState">Mudar estado</button></div>`;
  return `<div class="section-card"><div class="small">${run.message}</div><button class="btn ghost" id="cycleRunState" style="margin-top:12px;">Mudar estado</button></div>`;
}

function stageChip(status){
  const map = { done: 'green', active: 'cyan', ready: 'lime', queued: 'gray', warning: 'amber', blocked: 'red', error: 'red' };
  const cls = map[status] || 'gray';
  return `<span class="chip ${cls}">${String(status).replace(/_/g,' ')}</span>`;
}

export function orchestratorDrawer(run){
  return `
    <div class="drawer-head">
      <div>
        <div class="small">Entrada visual do App Core / Orchestrator</div>
        <div class="drawer-title">Pôr tudo a correr</div>
      </div>
      <button class="close-drawer" id="closeOrchestrator">Fechar</button>
    </div>
    ${bannerByStatus(run)}
    <div class="section-card" style="margin-top:14px;">
      <div class="section-head"><h3 class="section-title">Readiness do sistema</h3><span class="chip cyan">integration-ready staging</span></div>
      <div class="domain-grid">
        ${run.checks.map(check => `<div class="domain-card"><div class="tile-label">${check.label}</div><div class="tile-value mono" style="font-size:18px;">${String(check.status).toUpperCase()}</div><div class="small">${check.detail}</div></div>`).join('')}
      </div>
    </div>
    <div class="section-card" style="margin-top:14px;">
      <div class="section-head"><h3 class="section-title">Fases da corrida</h3><span class="small">${run.progress}% concluído</span></div>
      <div class="progress"><span style="width:${run.progress}%"></span></div>
      <div class="timeline" style="margin-top:16px;">
        ${run.stages.map(step => `<div class="timeline-item"><div class="timeline-bullet ${step.status==='warning'?'warn':step.status==='error' || step.status==='blocked'?'fail':''}"></div><div class="timeline-body"><div class="row" style="justify-content:space-between;"><strong>${step.index}. ${step.title}</strong>${stageChip(step.status)}</div><div class="small">${step.detail}</div></div></div>`).join('')}
      </div>
    </div>
    <div class="section-card" style="margin-top:14px;">
      <div class="section-head"><h3 class="section-title">Resumo da corrida</h3></div>
      <div class="kv">
        <div class="kv-item"><div class="kv-label">Oportunidades</div><div class="kv-value">${run.summary.opportunities}</div></div>
        <div class="kv-item"><div class="kv-label">Elegíveis</div><div class="kv-value">${run.summary.eligible}</div></div>
        <div class="kv-item"><div class="kv-label">Approved</div><div class="kv-value">${run.summary.approved}</div></div>
        <div class="kv-item"><div class="kv-label">Pending execution</div><div class="kv-value">${run.summary.pending_execution}</div></div>
        <div class="kv-item"><div class="kv-label">Reserve</div><div class="kv-value">${run.summary.reserve}</div></div>
        <div class="kv-item"><div class="kv-label">Blocked</div><div class="kv-value">${run.summary.blocked}</div></div>
      </div>
    </div>
    ${run.issues?.length ? `<div class="section-card" style="margin-top:14px;"><div class="section-head"><h3 class="section-title">Issues / exceções</h3></div><div class="alert-list">${run.issues.map(alertItem).join('')}</div></div>` : ''}
  `;
}
