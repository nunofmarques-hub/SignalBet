export function summarizeSnapshot(rt){
  return {
    opportunities: rt.summary?.opportunities ?? 0,
    eligible: rt.summary?.eligible ?? 0,
    approved: rt.summary?.approved ?? 0,
    executed: rt.summary?.executed ?? 0,
  };
}
