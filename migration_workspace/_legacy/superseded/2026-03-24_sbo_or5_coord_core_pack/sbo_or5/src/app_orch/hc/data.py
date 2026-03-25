from __future__ import annotations
from pathlib import Path

def run(project_root: str):
    root = Path(project_root)
    da = root / 'data_api'
    trunk = da / 'Data_API_Official_Trunk_v1'
    providers = trunk / 'providers'
    contracts = trunk / 'contracts'
    services = trunk / 'services'
    storage = trunk / 'storage'
    return [
        {'check_id':'data_api_root_present','status':'PASS' if da.exists() else 'FAIL','message':'data_api/ encontrada.' if da.exists() else 'data_api/ em falta.','blocking':True},
        {'check_id':'official_trunk_root_present','status':'PASS' if trunk.exists() else 'FAIL','message':'Data_API_Official_Trunk_v1 encontrado.' if trunk.exists() else 'Data_API_Official_Trunk_v1 em falta.','blocking':True},
        {'check_id':'official_trunk_readme_present','status':'PASS' if (trunk/'README.md').exists() else 'WARN','message':'README do trunk encontrado.' if (trunk/'README.md').exists() else 'README do trunk em falta.','blocking':False},
        {'check_id':'providers_registry_present','status':'PASS' if (providers/'providers.json').exists() else 'FAIL','message':'Registry de providers encontrado.' if (providers/'providers.json').exists() else 'Registry de providers em falta.','blocking':True},
        {'check_id':'official_files_present','status':'PASS' if providers.exists() and contracts.exists() else 'FAIL','message':'Providers e contracts presentes.' if providers.exists() and contracts.exists() else 'Providers ou contracts em falta.','blocking':True},
        {'check_id':'services_present','status':'PASS' if services.exists() else 'WARN','message':'Services presentes.' if services.exists() else 'Services em falta.','blocking':False},
        {'check_id':'latest_snapshot_available','status':'PASS' if any(storage.glob('*.json')) else 'WARN','message':'Snapshot/cache utilizável encontrado.' if any(storage.glob('*.json')) else 'Sem snapshot/cache utilizável.','blocking':False},
    ]
