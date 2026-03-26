import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / 'motor' / 'candidate_generation'))
from generate_candidates import generate_all_cases
cases = generate_all_cases(ROOT / 'motor' / 'data_handoff' / 'trunk_fixtures_sample.json', ROOT / 'motor' / 'data_handoff' / 'trunk_fixture_statistics_sample.json', ROOT / 'motor' / 'data_handoff' / 'trunk_case_contexts.json')
summary={'generated_cases':[],'count':0}
for adapted, engine_output, candidate in cases:
    cid=adapted['case_id']
    summary['generated_cases'].append({'case_id': cid,'score': candidate['score_raw'],'candidate_status': candidate['module_specific_payload']['candidate_status'],'band': candidate['module_specific_payload']['band'],'selection': candidate['selection'],'confidence_raw': candidate['confidence_raw'],'risk_raw': candidate['risk_raw']})
    (ROOT / 'output_contratual' / f'{cid}_engine_output.json').write_text(json.dumps(engine_output, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT / 'output_contratual' / f'{cid}_market_pick.json').write_text(json.dumps(candidate, ensure_ascii=False, indent=2), encoding='utf-8')
summary['count']=len(summary['generated_cases'])
(ROOT / 'output_contratual' / 'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(summary, ensure_ascii=False, indent=2))
