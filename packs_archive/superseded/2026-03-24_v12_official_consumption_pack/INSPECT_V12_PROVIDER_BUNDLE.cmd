@echo off
setlocal

set PROJECT_ROOT=U:\Users\genuser\Desktop\SignalBet
set TRUNK_ROOT=%PROJECT_ROOT%\data_api\Data_API_Official_Trunk_v1
set PACK_DIR=%PROJECT_ROOT%\migration_workspace\v12\2026-03-24_v12_final_fixed_pack

set PYTHONPATH=%TRUNK_ROOT%;%PACK_DIR%

cd /d "%PACK_DIR%"
python -c "from motor.provider_bridge import load_official_bundle; b=load_official_bundle(140,2024); print(type(b)); print(dir(b)); print(getattr(b,'__dict__', 'NO_DICT'))"

pause