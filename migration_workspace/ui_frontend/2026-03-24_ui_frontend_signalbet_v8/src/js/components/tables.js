
import { statusChip, tableCellScore } from './ui.js';

export function poolTable(rows, selectedIndex=0){
  return `
  <table>
    <thead><tr><th>Fixture / Pick</th><th>Market</th><th>Module</th><th>Score</th><th>Confidence</th><th>Edge</th><th>Risk</th><th>Tier</th><th>Eligibility</th><th>Decision</th><th>Execution</th><th>Quality</th></tr></thead>
    <tbody>
      ${rows.map((r,i) => `<tr class="${i===selectedIndex?'selected':''}" data-select-row="pool" data-index="${i}"><td><strong>${r.fixture}</strong></td><td>${r.market}</td><td>${r.module_source}</td><td>${tableCellScore(r.global_score)}</td><td>${r.confidence_norm}</td><td>${r.edge_norm}</td><td>${r.risk_norm}</td><td>${statusChip(r.priority_tier)}</td><td>${statusChip(r.eligibility)}</td><td>${statusChip(r.decision_status)}</td><td>${statusChip(r.execution_status)}</td><td>${statusChip(r.data_quality_flag)}</td></tr>`).join('')}
    </tbody>
  </table>`;
}

export function bankrollTable(rows, selectedIndex=0){
  return `<table><thead><tr><th>Pick</th><th>Module</th><th>Score</th><th>Conf</th><th>Edge</th><th>Risk</th><th>Decision</th><th>Stake</th><th>Exposure</th><th>Readiness</th></tr></thead><tbody>${rows.map((r,i)=>`<tr class="${i===selectedIndex?'selected':''}" data-select-row="bankroll" data-index="${i}"><td><strong>${r.fixture}</strong></td><td>${r.module_source}</td><td>${r.global_score}</td><td>${r.confidence_norm}</td><td>${r.edge_norm}</td><td>${r.risk_norm}</td><td>${statusChip(r.decision_status)}</td><td class="mono">${r.stake}</td><td>${statusChip(r.exposure_impact)}</td><td>${statusChip(r.execution_readiness)}</td></tr>`).join('')}</tbody></table>`;
}

export function executionIntakeTable(rows, selectedIndex=0){
  return `<table><thead><tr><th>Pick</th><th>Module</th><th>Decision</th><th>Stake</th><th>Readiness</th><th>Intake</th><th>Created</th><th>Queue age</th></tr></thead><tbody>${rows.map((r,i)=>`<tr class="${i===selectedIndex?'selected':''}" data-select-row="executionIntake" data-index="${i}"><td><strong>${r.fixture}</strong></td><td>${r.module_source}</td><td>${statusChip(r.decision_status)}</td><td>${r.stake}</td><td>${statusChip(r.execution_readiness)}</td><td>${statusChip(r.intake_status)}</td><td>${r.created_at}</td><td>${r.queue_age}</td></tr>`).join('')}</tbody></table>`;
}

export function executionLiveTable(rows){
  return `<table><thead><tr><th>Pick</th><th>Market</th><th>Placed</th><th>Status</th><th>Live</th><th>Stake</th><th>Return</th><th>Flag</th></tr></thead><tbody>${rows.map(r=>`<tr><td><strong>${r.fixture}</strong></td><td>${r.market}</td><td>${r.placed_at}</td><td>${statusChip(r.execution_status)}</td><td>${statusChip(r.live_status)}</td><td>${r.stake}</td><td>${r.potential_return}</td><td>${statusChip(r.tracking_flag)}</td></tr>`).join('')}</tbody></table>`;
}

export function historyTable(rows, selectedIndex=0){
  return `<table><thead><tr><th>Date</th><th>Pick</th><th>Market</th><th>Module</th><th>Score</th><th>Conf</th><th>Edge</th><th>Risk</th><th>Decision</th><th>Execution</th><th>Result</th><th>Return</th><th>Quality</th></tr></thead><tbody>${rows.map((r,i)=>`<tr class="${i===selectedIndex?'selected':''}" data-select-row="history" data-index="${i}"><td>${r.date}</td><td><strong>${r.fixture}</strong></td><td>${r.market}</td><td>${r.module_source}</td><td>${r.global_score}</td><td>${r.confidence_norm}</td><td>${r.edge_norm}</td><td>${r.risk_norm}</td><td>${statusChip(r.decision_status)}</td><td>${statusChip(r.execution_status)}</td><td>${statusChip(r.result)}</td><td>${r.roi}</td><td>${statusChip(r.data_quality_flag)}</td></tr>`).join('')}</tbody></table>`;
}
