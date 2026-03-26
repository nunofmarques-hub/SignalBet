import { runScenario } from './runtimeBridgeService.js';
export async function getTestMatrix(){
  const scenarios=['fresh_reuse','fresh_reuse','stale_refresh_success','stale_refresh_failed_reuse','fallback_mock','force_refresh','mode_transition','explicit_invalidation','repeat_scenario'];
  const labels={fresh_reuse:'snapshot fresco reutilizado',stale_refresh_success:'snapshot stale com refresh bem-sucedido',stale_refresh_failed_reuse:'snapshot stale com refresh falhado e reuso controlado',fallback_mock:'fallback para orchestrator_mock',force_refresh:'forceRefresh',mode_transition:'transição entre requested_mode e observed_mode',explicit_invalidation:'invalidação explícita',repeat_scenario:'repetição do mesmo cenário'};
  const out=[];
  for(const s of scenarios){ const r=await runScenario(s); out.push({scenario:labels[s], pass:r.pass, observed:r.observed, note:r.note}); }
  return out;
}
