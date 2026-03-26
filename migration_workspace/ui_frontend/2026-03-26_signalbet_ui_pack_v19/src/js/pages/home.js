import { shell } from '../components/layout.js';
import { chip, kpi } from '../components/ui.js';
import { panel } from '../components/cards.js';
import { stepsTable } from '../components/tables.js';

function toneForFreshness(value){
  if(value === 'fresh') return 'green';
  if(value === 'stale') return 'amber';
  if(value === 'invalidated') return 'red';
  return 'cyan';
}

export function renderHome(vm){
  const top = `<div class="topbar">
    <h1>Home / Dashboard</h1>
    <div class="row">
      <button class="button">Pôr tudo a correr</button>
      <button class="button secondary">Nova leitura protegida</button>
    </div>
  </div>`;

  const bridgeMeta = `
    <div class="row orchestrator">
      ${chip(`requested_mode: ${vm.requested_mode}`,'cyan')}
      ${chip(`observed_mode: ${vm.observed_mode}`, vm.observed_mode==='real_read_protected'?'green':'amber')}
      ${chip(`fallback_used: ${vm.fallback_used}`, vm.fallback_used?'amber':'green')}
      ${chip(`bridge_status: ${vm.bridge_status}`, vm.bridge_status==='ok' || vm.bridge_status==='refresh_ok' || vm.bridge_status==='reuse_ok' ?'green':'amber')}
      ${chip(`bridge_scope: ${vm.bridge_scope}`,'lime')}
      ${chip(`degraded_mode: ${vm.degraded_mode}`, vm.degraded_mode?'amber':'green')}
      ${chip(`read_attempt: ${vm.read_attempt}`,'cyan')}
    </div>
    <div class="row orchestrator">
      ${chip(`snapshot_persisted: ${vm.snapshot_persisted}`, vm.snapshot_persisted?'green':'amber')}
      ${chip(`snapshot_reused: ${vm.snapshot_reused}`, vm.snapshot_reused?'amber':'green')}
      ${chip(`freshness_state: ${vm.freshness_state}`, toneForFreshness(vm.freshness_state))}
      ${chip(`snapshot_invalidated: ${vm.snapshot_invalidated}`, vm.snapshot_invalidated?'red':'green')}
      ${chip(`reuse_allowed: ${vm.reuse_allowed}`, vm.reuse_allowed?'green':'amber')}
      ${chip(`new_read_attempted: ${vm.new_read_attempted}`, vm.new_read_attempted?'cyan':'amber')}
    </div>
    <div class="row orchestrator">
      ${chip(`refresh_attempted: ${vm.refresh_attempted}`, vm.refresh_attempted?'cyan':'amber')}
      ${chip(`refresh_succeeded: ${vm.refresh_succeeded}`, vm.refresh_succeeded?'green':'amber')}
      ${chip(`reuse_preferred: ${vm.reuse_preferred}`, vm.reuse_preferred?'green':'amber')}
      ${chip(`reuse_blocked: ${vm.reuse_blocked}`, vm.reuse_blocked?'red':'green')}
      ${chip(`invalidation_trigger: ${vm.invalidation_trigger}`,'amber')}
    </div>`;

  const metaPanels = `
    <div class="two-col">
      ${panel('Bridge Meta', `
        <div class="small"><strong>Source line:</strong> ${vm.source_line}</div>
        <div class="small"><strong>Source transition:</strong> ${vm.source_transition}</div>
        <div class="small"><strong>Reuse reason:</strong> ${vm.reuse_reason}</div>
        <div class="small"><strong>Decision reason:</strong> ${vm.bridge_decision_reason}</div>
        <div class="small"><strong>Preference reason:</strong> ${vm.read_preference_reason}</div>
        <div class="small"><strong>Captured at:</strong> ${vm.captured_at || 'n/a'}</div>
        <div class="small"><strong>Persisted at:</strong> ${vm.persisted_at || 'n/a'}</div>
      `)}
      ${panel('Runtime Issues', vm.issues.length
        ? vm.issues.map(i=>`<div class='small'>• ${i}</div>`).join('')
        : `<div class='small muted'>Sem issues críticas</div>`)}
    </div>`;

  const orch = panel('Orchestrator / Runtime Bridge', `
    ${bridgeMeta}
    <div class="grid kpis">
      ${kpi('CTA State', vm.cta_state)}
      ${kpi('Readiness', vm.readiness_level)}
      ${kpi('Coverage', Math.round(vm.project_feed_coverage_ratio*100)+'%')}
      ${kpi('Current Stage', vm.current_stage)}
      ${kpi('Pipeline', vm.pipeline_state)}
      ${kpi('Final Result', vm.final_result)}
      ${kpi('Freshness', vm.freshness_state)}
      ${kpi('Observed', vm.observed_mode)}
    </div>
    <div class="row summary-strip">
      ${kpi('Opportunities', vm.summary.opportunities)}
      ${kpi('Eligible', vm.summary.eligible)}
      ${kpi('Approved', vm.summary.approved)}
      ${kpi('Executed', vm.summary.executed)}
    </div>
    ${metaPanels}
    <div style="margin-top:16px">${panel('Pipeline Steps', stepsTable(vm.pipeline_steps))}</div>
  `);

  return shell(top + orch);
}
