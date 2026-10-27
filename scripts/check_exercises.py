import subprocess
import sys
from pathlib import Path


def main() -> int:
    exercises = sorted(Path("algorithms").rglob("*.py"))
    if not exercises:
        print("No exercises found", file=sys.stderr)
        return 1

    failed = []
    for exercise in exercises:
        print(f"Running {exercise}", flush=True)
        result = subprocess.run([sys.executable, str(exercise)], check=False)
        if result.returncode:
            failed.append(str(exercise))

    if failed:
        print("Failed exercises: " + ", ".join(failed), file=sys.stderr)
        return 1

    print(f"All {len(exercises)} exercises passed!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
