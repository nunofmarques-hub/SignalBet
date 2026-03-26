export function getPipelineStatus(runtime){ return { state: runtime.pipeline_state, stage: runtime.current_stage, final_result: runtime.final_result }; }
