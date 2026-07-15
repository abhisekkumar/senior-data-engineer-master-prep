from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from dashboard.services import log_practice_attempt


def score(value: str) -> int:
    parsed = int(value)
    if not 0 <= parsed <= 5:
        raise argparse.ArgumentTypeError("scores must be between 0 and 5")
    return parsed


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Append a practice attempt and update spaced-repetition metadata."
    )
    parser.add_argument("--question", required=True)
    parser.add_argument(
        "--result", required=True, choices=["completed", "completed_with_hint", "incorrect"]
    )
    parser.add_argument("--confidence-before", type=int, required=True, choices=range(1, 6))
    parser.add_argument("--confidence-after", type=int, required=True, choices=range(1, 6))
    parser.add_argument("--minutes", type=int, required=True)
    parser.add_argument("--hints", type=int, default=0)
    parser.add_argument("--mistake", action="append", default=[])
    parser.add_argument("--notes", default="")
    parser.add_argument("--clarifying-score", type=score, default=3)
    parser.add_argument("--brute-force-score", type=score, default=3)
    parser.add_argument("--optimal-score", type=score, default=3)
    parser.add_argument("--coding-score", type=score, default=3)
    parser.add_argument("--complexity-score", type=score, default=3)
    parser.add_argument("--communication-score", type=score, default=3)
    args = parser.parse_args()
    if args.minutes < 0 or args.hints < 0:
        parser.error("minutes and hints cannot be negative")
    attempt = log_practice_attempt(
        question_id=args.question,
        result=args.result,
        confidence_before=args.confidence_before,
        confidence_after=args.confidence_after,
        minutes_spent=args.minutes,
        hints_used=args.hints,
        mistakes=args.mistake,
        notes=args.notes,
        clarifying_questions_score=args.clarifying_score,
        brute_force_score=args.brute_force_score,
        optimal_approach_score=args.optimal_score,
        coding_score=args.coding_score,
        complexity_score=args.complexity_score,
        communication_score=args.communication_score,
    )
    print(
        f"Logged {attempt['attempt_id']}; confidence {attempt['confidence_after']}/5; "
        f"{attempt['next_action']}"
    )


if __name__ == "__main__":
    main()
