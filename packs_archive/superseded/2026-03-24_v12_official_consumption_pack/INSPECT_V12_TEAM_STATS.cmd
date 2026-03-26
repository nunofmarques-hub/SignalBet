@echo off
setlocal

set PROJECT_ROOT=U:\Users\genuser\Desktop\SignalBet
set TRUNK_ROOT=%PROJECT_ROOT%\data_api\Data_API_Official_Trunk_v1
set PYTHONPATH=%TRUNK_ROOT%

python -c "from data_api.services.statistics_service import get_team_statistics; import json; data=get_team_statistics(33,140,2024); print(type(data)); print(json.dumps(data, indent=2, ensure_ascii=False)[:8000])"

pause