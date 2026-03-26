export function adaptContract(snapshot){
  return {
    source_mode_observed: snapshot.source_mode || 'contract_mock',
    summary: { opportunities: snapshot.opportunities_today || 0, approved: snapshot.approved_today || 0, pending_execution: snapshot.pending_execution || 0 },
    bridge_status: 'mock_only'
  };
}
