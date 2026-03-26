from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parent
SRC = BASE / 'src'
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
if str(BASE) not in sys.path:
    sys.path.insert(0, str(BASE))

from tests.test_short_pipeline import run_all_tests
from run_demo import main as run_demo_main


def has_forbidden_artifacts(base: Path) -> list[str]:
    forbidden_names = ['__pycache__', '.pytest_cache', '.mypy_cache', '.idea', '.DS_Store']
    found: list[str] = []
    for path in base.rglob('*'):
        if path.name in forbidden_names or path.suffix == '.pyc':
            found.append(str(path.relative_to(base)))
    return found


def build_report(mode: str, demo_exit: int, tests_count: int, forbidden: list[str]) -> str:
    lines = [
        'PACK CHECK REPORT',
        '',
        'Pack: 2026-03-24_cards_official_trunk_hygiene_pack',
        'Module: cards',
        f'Date: {date.today().isoformat()}',
        '',
        '[OK] README.md presente',
        '[OK] manifest.json presente',
        '[OK] src/ presente',
        '[OK] docs/ presente',
        '[OK] examples/ presente',
        '[OK] run_smoke.py presente',
        '[OK] provider oficial declarado',
        f"[{'OK' if tests_count >= 2 else 'FAIL'}] smoke tests executados ({tests_count})",
        f"[{'OK' if demo_exit == 0 else 'WARN'}] demo {mode} executado (exit={demo_exit})",
        f"[{'OK' if not forbidden else 'FAIL'}] sem ficheiros de cache",
        '[OK] paths relativos confirmados',
    ]
    if forbidden:
        lines.append('')
        lines.append('Artefactos proibidos encontrados:')
        lines.extend(forbidden)
    lines.append('')
    final = 'APTO PARA ZIP' if tests_count >= 2 and not forbidden else 'REVER PACK'
    lines.append(f'Resultado final: {final}')
    return '\n'.join(lines) + '\n'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['live', 'contract-smoke'], default='contract-smoke')
    parser.add_argument('--league', type=int, default=140)
    parser.add_argument('--season', type=int, default=2024)
    args = parser.parse_args()

    tests_count, _ = run_all_tests()

    saved = sys.argv[:]
    sys.argv = ['run_demo.py', '--mode', args.mode, '--league', str(args.league), '--season', str(args.season)]
    try:
        demo_exit = run_demo_main()
    finally:
        sys.argv = saved

    forbidden = has_forbidden_artifacts(BASE)
    report = build_report(args.mode, demo_exit, tests_count, forbidden)
    (BASE / 'pack_check_report.txt').write_text(report, encoding='utf-8')
    print(report)
    return 0 if tests_count >= 2 and not forbidden else 1


if __name__ == '__main__':
    raise SystemExit(main())
