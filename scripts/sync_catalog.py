from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tracker.catalog import sync_catalog


def main() -> None:
    result = sync_catalog()
    for question in result["added"]:
        print(f"Added {question['id']}: {question['file_path']}")
    for conflict in result["conflicts"]:
        print(f"Conflict: {conflict}", file=sys.stderr)
    print(f"Catalog contains {result['total']} tracked exercises.")
    if result["conflicts"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
