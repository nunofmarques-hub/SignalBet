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
    provider_registry = (providers/'providers.json').exists() or (providers/'registry.json').exists()
    contract_present = any(contracts.glob('*.json')) if contracts.exists() else False
    service_present = any(services.glob('*.json')) if services.exists() else False
    storage_present = any(storage.rglob('*.json')) if storage.exists() else False
    return [
        {'check_id':'data_api_root_present','status':'PASS' if da.exists() else 'FAIL','message':'data_api/ encontrada.' if da.exists() else 'data_api/ em falta.','blocking':True},
        {'check_id':'official_trunk_root_present','status':'PASS' if trunk.exists() else 'FAIL','message':'Data_API_Official_Trunk_v1 encontrado.' if trunk.exists() else 'Data_API_Official_Trunk_v1 em falta.','blocking':True},
        {'check_id':'providers_registry_present','status':'PASS' if provider_registry else 'FAIL','message':'Registry de providers encontrado.' if provider_registry else 'Registry de providers em falta.','blocking':True},
        {'check_id':'official_files_present','status':'PASS' if contract_present else 'FAIL','message':'Contracts oficiais presentes.' if contract_present else 'Contracts oficiais em falta.','blocking':True},
        {'check_id':'services_present','status':'PASS' if service_present else 'WARN','message':'Services presentes.' if service_present else 'Services em falta.','blocking':False},
        {'check_id':'latest_snapshot_available','status':'PASS' if storage_present else 'WARN','message':'Snapshot/cache utilizável encontrado.' if storage_present else 'Sem snapshot/cache utilizável.','blocking':False},
    ]
