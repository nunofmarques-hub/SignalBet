export function renderRunPanel(p){
  const issues = p.issues.map(i => `<div class="chip ${i.level==='warning'?'warn':'bad'}">${i.text}</div>`).join('');
  const steps = p.pipelineSteps.map(s => `<div class="stage ${s.status==='done'?'done':s.status==='ready'?'active':''}"><div>${s.label}</div><div class="small muted">${s.status}</div></div>`).join('');
  return `<div><div style="display:flex;justify-content:space-between;align-items:center"><div><div class="label">Orchestrator</div><div class="value" style="font-size:20px">${p.buttonContext.label}</div></div><button class="cta" ${p.buttonContext.enabled?'':'disabled'}>${p.buttonContext.label}</button></div><div class="small muted" style="margin-top:8px">readiness=${p.readinessLevel} · coverage=${Math.round(p.projectFeedCoverageRatio*100)}% · pipeline=${p.pipelineState}</div><div class="run-stages">${steps}</div><div>${issues}</div></div>`;
}
export function renderBasicState(type, text){ return `<div class="screen-section"><div class="chip ${type==='error'?'bad':type==='empty'?'warn':'live'}">${type}</div><p>${text}</p></div>`; }
