export function buildBankrollViewModel(bundle) {
  return {
    system: bundle.system,
    runtime: bundle.runtime.snapshot,
    bridge: bundle.runtime
  };
}
