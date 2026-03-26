import { badge } from './ui.js';
export function runtimeStatePanel(vm){
  const r = vm.runtime;
  return `
  <div class="card">
    <div class="section-head"><strong>Pôr tudo a correr</strong>${badge(r.cta_state || 'unknown', r.cta_state==='ready'?'green':r.cta_state==='blocked'?'red':'amber')}</div>
    <div class="pill-row">
      ${badge('requested: '+vm.mode_requested,'cyan')}
      ${badge('observed: '+vm.mode_observed, vm.mode_observed==='real_read_protected'?'green':'amber')}
      ${badge('bridge: '+vm.bridge_status, vm.bridge_status.includes('real')?'green':'amber')}
      ${badge(vm.fallback_used ? 'fallback used' : 'no fallback', vm.fallback_used ? 'amber' : 'green')}
    </div>
    <div class="grid cards" style="margin-top:12px;grid-template-columns:repeat(3,minmax(0,1fr))">
      <div class="state-box"><div class="small muted">readiness_level</div><strong>${r.readiness_level}</strong></div>
      <div class="state-box"><div class="small muted">pipeline_state</div><strong>${r.pipeline_state}</strong></div>
      <div class="state-box"><div class="small muted">current_stage</div><strong>${r.current_stage}</strong></div>
    </div>
    <div style="margin-top:12px" class="small muted">project_feed_coverage_ratio</div>
    <div class="progress"><span style="width:${Math.round((r.project_feed_coverage_ratio||0)*100)}%"></span></div>
    <div class="small muted">issues: ${(r.issues||[]).length} · final_result: ${r.final_result || 'n/a'}</div>
  </div>`;
}
