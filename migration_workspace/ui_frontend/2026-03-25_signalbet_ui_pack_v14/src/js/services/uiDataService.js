
export class UIDataService {
  constructor(systemSnapshotService, pipelineStatusService, runtimeBridgeService, store) {
    this.systemSnapshotService = systemSnapshotService;
    this.pipelineStatusService = pipelineStatusService;
    this.runtimeBridgeService = runtimeBridgeService;
    this.store = store;
  }
  async bootstrap(runtimeMode = 'orchestrator_mock') {
    this.store.runtimeMode = runtimeMode;
    const system = await this.systemSnapshotService.getSnapshot('contract_mock');
    let orchestrator; let fallbackUsed = false;
    try {
      orchestrator = await this.pipelineStatusService.getSnapshot(runtimeMode);
    } catch (err) {
      fallbackUsed = runtimeMode !== 'orchestrator_mock';
      orchestrator = await this.pipelineStatusService.getSnapshot('orchestrator_mock');
      this.store.error = `Fallback ativo para orchestrator_mock: ${err.message}`;
      this.store.observedSourceMode = fallbackUsed ? 'fallback:orchestrator_mock' : 'orchestrator_mock';
    }
    return {
      system, orchestrator,
      metadata: {
        requested_mode: runtimeMode,
        observed_mode: this.store.observedSourceMode,
        imported_file_name: this.store.realReadMeta.importedFileName,
        real_read_status: this.store.realReadMeta.lastReadStatus,
        fallback_used: fallbackUsed
      }
    };
  }
}
