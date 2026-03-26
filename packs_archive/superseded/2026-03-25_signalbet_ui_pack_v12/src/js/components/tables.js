export function simpleTable(title, snapshot) {
  return `
    <div class="card">
      <div class="muted">${title}</div>
      <table class="table">
        <thead><tr><th>Campo</th><th>Valor</th></tr></thead>
        <tbody>
          <tr><td>run_id</td><td>${snapshot.runId}</td></tr>
          <tr><td>cta_state</td><td>${snapshot.ctaState}</td></tr>
          <tr><td>readiness_level</td><td>${snapshot.readinessLevel}</td></tr>
          <tr><td>project_feed_coverage_ratio</td><td>${Math.round(snapshot.coverageRatio*100)}%</td></tr>
          <tr><td>current_stage</td><td>${snapshot.currentStage}</td></tr>
        </tbody>
      </table>
    </div>`;
}
