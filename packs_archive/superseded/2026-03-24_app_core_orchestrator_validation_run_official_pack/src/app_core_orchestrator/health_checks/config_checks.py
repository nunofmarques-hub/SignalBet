
from __future__ import annotations
from pathlib import Path
from typing import Dict, List

def run_config_checks(pack_root: str) -> List[Dict[str, object]]:
    root = Path(pack_root)
    api_env = root / 'api.env.txt'
    settings_file = root / 'src' / 'app_core_orchestrator' / 'manifests' / 'run_profiles.json'
    api_key_present = False
    if api_env.exists():
        text = api_env.read_text(encoding='utf-8').strip()
        api_key_present = text.startswith('API_KEY=') and len(text) > len('API_KEY=')
    return [
        {'check_id':'api_env_present','status':'PASS' if api_env.exists() else 'WARN','message':'api.env.txt presente.' if api_env.exists() else 'api.env.txt em falta no pack.','blocking':False},
        {'check_id':'api_key_present','status':'PASS' if api_key_present else 'WARN','message':'API key presente.' if api_key_present else 'API key não fornecida neste pack de staging.','blocking':False},
        {'check_id':'settings_file_present','status':'PASS' if settings_file.exists() else 'FAIL','message':'settings/run_profiles presentes.' if settings_file.exists() else 'run_profiles.json em falta.','blocking':True},
    ]
