const screens = ['Home / Dashboard','Opportunity Pool','Banca / Decision View','Execution / Tracking','Histórico / Validação'];
const nav = document.getElementById('nav');
const content = document.getElementById('content');
const title = document.getElementById('page-title');
let active = screens[0];

function statusChip(v){
  const map={approved:'green',eligible:'green',pending:'warn',placed:'cyan',live:'cyan',settled:'green',reserve:'warn',reduced:'warn',blocked:'red',yellow:'warn',green:'green',none:'red',hold:'warn'};
  const cls=map[v]||'cyan';
  return `<span class="chip ${cls}">${v}</span>`;
}
function scoreChip(label,val,cls='cyan'){return `<span class="chip ${cls}">${label}: ${val}</span>`}
function renderNav(){nav.innerHTML=screens.map(s=>`<button class="nav-btn ${s===active?'active':''}" data-screen="${s}">${s}</button>`).join('');document.querySelectorAll('.nav-btn').forEach(b=>b.onclick=()=>{active=b.dataset.screen; render();});}
function renderHome(){const d=window.SignalBetData.home;return `
<div class="hero">
  <div class="hero-main">
    <span class="chip lime">Best of the Day</span>
    <h2>${d.hero.fixture}</h2>
    <p>${d.hero.market} · módulo ${d.hero.module_source}</p>
    <div class="meta">${scoreChip('Score',d.hero.global_score,'lime')}${scoreChip('Confidence',d.hero.confidence_norm)}${scoreChip('Edge',d.hero.edge_norm)}${scoreChip('Risk',d.hero.risk_norm,'warn')}${statusChip(d.hero.decision_status)}</div>
  </div>
  <div class="sidebar-panel"><div class="small">Orchestrator entry point</div><h3>Pôr tudo a correr</h3><p class="small">A UI prepara o ponto de entrada visual. A lógica pertence ao App Core / Orchestrator.</p></div>
</div>
<div class="section-title">Resumo do sistema</div>
<div class="grid kpis">${d.kpis.map(([l,v])=>`<div class="tile"><div class="label">${l}</div><div class="value">${v}</div></div>`).join('')}</div>`}
function renderPool(){const rows=window.SignalBetData.pool; const top=rows[0]; return `
<div class="hero-main"><span class="chip lime">Top Opportunity</span><h2>${top.fixture}</h2><p>${top.market} · ${top.module_source}</p><div class="meta">${scoreChip('Score',top.global_score,'lime')}${scoreChip('Conf',top.confidence_norm)}${scoreChip('Edge',top.edge_norm)}${scoreChip('Risk',top.risk_norm,'warn')}${statusChip(top.priority_tier)}${statusChip(top.eligibility)}${statusChip(top.decision_status)}</div></div>
<div class="section-title">Ranking global</div>
<table class="table"><thead><tr><th>Fixture</th><th>Market</th><th>Module</th><th>Score</th><th>Confidence</th><th>Edge</th><th>Risk</th><th>Tier</th><th>Eligibility</th><th>Decision</th><th>Execution</th><th>Quality</th></tr></thead><tbody>${rows.map(r=>`<tr><td>${r.fixture}</td><td>${r.market}</td><td>${r.module_source}</td><td>${r.global_score}</td><td>${r.confidence_norm}</td><td>${r.edge_norm}</td><td>${r.risk_norm}</td><td>${statusChip(r.priority_tier)}</td><td>${statusChip(r.eligibility)}</td><td>${statusChip(r.decision_status)}</td><td>${statusChip(r.execution_status)}</td><td>${statusChip(r.data_quality_flag)}</td></tr>`).join('')}</tbody></table>`}
function renderBanking(){const rows=window.SignalBetData.banking; return `
<div class="grid kpis">${[['Approved','2'],['Reduced','1'],['Reserve','1'],['Available Exposure','62%'],['Allocated Stake','2.25u'],['Remaining Capacity','37%']].map(([l,v])=>`<div class="tile"><div class="label">${l}</div><div class="value">${v}</div></div>`).join('')}</div>
<div class="section-title">Decision queue</div>
<div class="two-col"><table class="table"><thead><tr><th>Fixture</th><th>Decision</th><th>Stake</th><th>Exposure</th><th>Readiness</th></tr></thead><tbody>${rows.map(r=>`<tr><td>${r.fixture}</td><td>${statusChip(r.decision_status)}</td><td>${r.stake}</td><td>${r.exposure_impact}</td><td>${statusChip(r.execution_readiness)}</td></tr>`).join('')}</tbody></table><div class="sidebar-panel"><div class="small">Reason code</div><h3>${rows[0].fixture}</h3><p>${rows[0].reason}</p><div class="meta">${statusChip(rows[0].decision_status)}${statusChip(rows[0].execution_readiness)}</div></div></div>`}
function renderExecution(){const rows=window.SignalBetData.execution; return `
<div class="grid kpis">${[['Pending Intake','1'],['Placed','1'],['Live','1'],['Settled Today','1'],['Issues','0'],['Avg Delay','2m']].map(([l,v])=>`<div class="tile"><div class="label">${l}</div><div class="value">${v}</div></div>`).join('')}</div>
<div class="section-title">Execution pipeline</div>
<div class="two-col"><table class="table"><thead><tr><th>Fixture</th><th>Intake</th><th>Execution</th><th>Queue Age</th></tr></thead><tbody>${rows.map(r=>`<tr><td>${r.fixture}</td><td>${statusChip(r.intake_status)}</td><td>${statusChip(r.execution_status)}</td><td>${r.queue_age}</td></tr>`).join('')}</tbody></table><div class="sidebar-panel"><div class="small">Audit trail</div><p>received from bankroll → intake → placed → live → settled</p></div></div>`}
function renderHistory(){const rows=window.SignalBetData.history; return `
<div class="grid kpis">${[['Total Picks','12'],['Settled','10'],['Wins','7'],['Losses','3'],['Strike Rate','70%'],['ROI','+12.4%']].map(([l,v])=>`<div class="tile"><div class="label">${l}</div><div class="value">${v}</div></div>`).join('')}</div>
<div class="section-title">Historical ledger</div>
<div class="two-col"><table class="table"><thead><tr><th>Date</th><th>Fixture</th><th>Market</th><th>Module</th><th>Decision</th><th>Execution</th><th>Result</th><th>ROI</th></tr></thead><tbody>${rows.map(r=>`<tr><td>${r.date}</td><td>${r.fixture}</td><td>${r.market}</td><td>${r.module_source}</td><td>${statusChip(r.decision_status)}</td><td>${statusChip(r.execution_status)}</td><td>${statusChip(r.result)}</td><td>${r.roi}</td></tr>`).join('')}</tbody></table><div class="sidebar-panel"><div class="small">Validation</div><h3>Performance by module</h3><p>v12 está acima da média no período. BTTS ainda com amostra curta e mais volátil.</p></div></div>`}
function render(){renderNav(); title.textContent=active; content.innerHTML = active===screens[0]?renderHome():active===screens[1]?renderPool():active===screens[2]?renderBanking():active===screens[3]?renderExecution():renderHistory();}
render();
