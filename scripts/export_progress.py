from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tracker.analytics import summary
from tracker.database import ROOT, atomic_write_json, load_questions, read_json


def main() -> None:
    attempts = read_json(ROOT / "tracker/practice_log.json", [])
    output = ROOT / "exports" / f"progress-{datetime.now():%Y%m%d-%H%M%S}.json"
    atomic_write_json(
        output, {"summary": summary(load_questions(), attempts), "attempts": attempts}
    )
    print(output)


if __name__ == "__main__":
    main()
