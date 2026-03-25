from __future__ import annotations

from data_api.config import DEFAULT_LEAGUE, DEFAULT_SEASON, REQUESTS_PER_DAY, REQUESTS_PER_MINUTE
from data_api.paths import ensure_base_dirs, RAW_DIR, NORMALIZED_DIR, DERIVED_DIR, STATE_DIR, LOGS_DIR

def main() -> None:
    ensure_base_dirs()
    print("[OK] Base directories ensured")
    print(f"DEFAULT_LEAGUE={DEFAULT_LEAGUE}")
    print(f"DEFAULT_SEASON={DEFAULT_SEASON}")
    print(f"REQUESTS_PER_MINUTE={REQUESTS_PER_MINUTE}")
    print(f"REQUESTS_PER_DAY={REQUESTS_PER_DAY}")
    print(f"RAW_DIR={RAW_DIR}")
    print(f"NORMALIZED_DIR={NORMALIZED_DIR}")
    print(f"DERIVED_DIR={DERIVED_DIR}")
    print(f"STATE_DIR={STATE_DIR}")
    print(f"LOGS_DIR={LOGS_DIR}")

if __name__ == "__main__":
    main()
