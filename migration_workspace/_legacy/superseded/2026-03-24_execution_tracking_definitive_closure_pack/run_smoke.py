from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
cmd = [sys.executable, str(root / 'src' / 'execution_tracking' / 'orchestrator.py')]
raise SystemExit(subprocess.call(cmd))
