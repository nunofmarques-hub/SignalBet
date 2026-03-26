import { badge, chip, progress } from './ui.js';

export function heroOpportunityCard(item) {
  return `<div class="card hero stack">
    <div class="row"><div>${badge('Best of the Day','lime')}</div><div>${chip(item.decision_status, item.decision_status==='approved'?'green':'amber')}</div></div>
    <div><h2>${item.fixture}</h2><div class="muted">${item.market} · ${item.module_source}</div></div>
    <div class="grid-4">
      <div><small>Global Score</small><div class="kpi">${item.global_score}</div></div>
      <div><small>Confidence</small><div class="kpi">${item.confidence_norm}</div></div>
      <div><small>Edge</small><div class="kpi">${item.edge_norm}</div></div>
      <div><small>Risk</small><div class="kpi">${item.risk_norm}</div></div>
    </div>
  </div>`;
}

export function orchestratorPanel(runtime, bridge) {
  const steps = runtime.pipeline_steps.map(s => `<div class="list-item row"><strong>${s.label}</strong>${chip(s.status, s.status==='ready'||s.status==='done'?'green':s.status==='running'?'cyan':s.status==='waiting'?'amber':'red')}</div>`).join('');
  const modules = runtime.module_overview.map(m => `<div class="list-item row"><span>${m.module}</span><span>${chip(m.status, m.status==='ready'||m.status==='done'?'green':'amber')} <small>${m.picks ?? '-'} picks</small></span></div>`).join('');
  const issues = runtime.issues.length ? runtime.issues.map(i => `<div class="list-item">${chip(i.severity, i.severity==='critical'?'red':'amber')} ${i.message}</div>`).join('') : '<div class="list-item">Sem issues ativas.</div>';
  return `<div class="card stack">
    <div class="row"><h3>Pôr tudo a correr</h3>${chip(runtime.cta_state, runtime.cta_state==='ready'?'green':runtime.cta_state==='running'?'cyan':runtime.cta_state==='error'?'red':'amber')}</div>
    <div class="row"><div><small>Readiness</small><div class="kpi">${runtime.readiness_level}</div></div><div><small>Coverage</small>${progress(runtime.project_feed_coverage_ratio)}<div class="muted">${Math.round(runtime.project_feed_coverage_ratio*100)}%</div></div></div>
    <div class="card" style="padding:12px"><div class="row"><strong>${runtime.button_context.label}</strong><span class="muted">${runtime.button_context.note}</span></div></div>
    <div class="grid-2">
      <div class="stack"><div class="section-title"><strong>Pipeline steps</strong><small class="muted">${runtime.pipeline_state} · ${runtime.current_stage}</small></div><div class="list">${steps}</div></div>
      <div class="stack"><div class="section-title"><strong>Module overview</strong><small class="muted">source: ${bridge.source_mode}${bridge.degraded ? ' · protected' : ''}</small></div><div class="list">${modules}</div></div>
    </div>
    <div class="stack"><div class="section-title"><strong>Issues</strong><small class="muted">run_id: ${runtime.run_id || 'n/a'}</small></div><div class="list">${issues}</div></div>
  </div>`;
}
