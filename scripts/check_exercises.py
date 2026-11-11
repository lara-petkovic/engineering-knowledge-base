import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    exercises = sorted(
        path.relative_to(root)
        for path in (root / "algorithms").glob("*/*.py")
        if path.name not in {"helpers.py", "__init__.py"}
    )
    if not exercises:
        print("No exercises found", file=sys.stderr)
        return 1

    failed = []
    for exercise in exercises:
        print(f"Running {exercise}", flush=True)
        module = ".".join(exercise.with_suffix("").parts)
        result = subprocess.run([sys.executable, "-m", module], cwd=root, check=False)
        if result.returncode:
            failed.append(str(exercise))

    if failed:
        print("Failed exercises: " + ", ".join(failed), file=sys.stderr)
        return 1

    print(f"All {len(exercises)} exercises passed!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
