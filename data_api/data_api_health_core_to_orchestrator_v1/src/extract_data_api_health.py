
from __future__ import annotations
import json
import os
from pathlib import Path
from datetime import datetime, timezone

DEFAULT_REL_EVENTS = Path('data_api/storage/state/league_140/season_2024/resume_events.state.json')
DEFAULT_REL_STATS = Path('data_api/storage/state/league_140/season_2024/fixture_statistics_context_activation_v1.state.json')


def _load_json(path: Path) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def _baseline_status(events_state: dict) -> str:
    done = events_state.get('done', []) or []
    failed = events_state.get('failed', []) or []
    if done and not failed:
        return 'green'
    if done:
        return 'degraded'
    return 'missing'


def _complementary_status(stats_state: dict) -> str:
    summary = stats_state.get('summary', {}) if isinstance(stats_state, dict) else {}
    result = summary.get('result')
    if result == 'green':
        return 'green'
    items = stats_state.get('items', []) if isinstance(stats_state, dict) else []
    if items:
        missing = sum(1 for item in items if item.get('statistics_status') != 'available')
        if missing == 0:
            return 'green'
        return 'degraded'
    return 'missing'


def _central_health(baseline_status: str, complementary_status: str) -> str:
    if baseline_status == 'green' and complementary_status == 'green':
        return 'healthy_enriched'
    if baseline_status == 'green' and complementary_status in {'missing', 'degraded'}:
        return 'healthy_baseline_only'
    if baseline_status == 'degraded':
        return 'degraded'
    return 'unhealthy'


def build_component(trunk_root: Path) -> tuple[dict, dict]:
    events_path = trunk_root / DEFAULT_REL_EVENTS
    stats_path = trunk_root / DEFAULT_REL_STATS

    events_state = _load_json(events_path)
    stats_state = _load_json(stats_path)

    baseline_status = _baseline_status(events_state)
    complementary_status = _complementary_status(stats_state)
    central_health = _central_health(baseline_status, complementary_status)
    source_mode = 'project'

    component = {
        'baseline_status': baseline_status,
        'complementary_status': complementary_status,
        'central_health': central_health,
        'source_mode': source_mode,
    }

    summary = {
        'phase': 'data_api_health_core_to_orchestrator_v1',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'trunk_root': str(trunk_root),
        'events_state_path': str(events_path),
        'statistics_state_path': str(stats_path),
        'events_done_count': len(events_state.get('done', []) or []),
        'statistics_items_count': len(stats_state.get('items', []) or []),
        'component': component,
        'result': 'green' if component['baseline_status'] != 'missing' else 'red',
    }
    return component, summary


def main() -> int:
    here = Path(__file__).resolve().parent.parent
    trunk_root = Path(os.environ.get('DATA_API_TRUNK_ROOT', here / '_trunk' / 'Data_API_Official_Trunk_v1'))
    out_examples = here / 'examples'
    out_logs = here / 'logs'
    out_examples.mkdir(parents=True, exist_ok=True)
    out_logs.mkdir(parents=True, exist_ok=True)

    component, summary = build_component(trunk_root)

    component_path = out_examples / 'data_api_health_component_generated.json'
    summary_path = out_logs / 'data_api_health_summary_generated.json'

    component_path.write_text(json.dumps(component, indent=2, ensure_ascii=False), encoding='utf-8')
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding='utf-8')

    print(json.dumps({
        'component_path': str(component_path),
        'summary_path': str(summary_path),
        'component': component,
        'result': summary['result'],
    }, indent=2, ensure_ascii=False))
    print('[OK] data_api_health_core_to_orchestrator_v1 completed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
