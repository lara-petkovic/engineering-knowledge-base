# Engineering Knowledge Base

A personal collection of Python exercises and practical engineering notes.

- `algorithms/` — exercises grouped by topic, with example checks in each file.
- Learning notes:
  - [Algorithm logic and problem-solving](docs/problem-solving/)
  - [Python functions and methods](docs/python-functions/)
  - [Python data structures](docs/data-structures/)

## Run an exercise

From the repository root, using the local Python environment:

In VS Code, F5 uses the **Python: Current exercise** configuration. It sets
`PYTHONPATH` to the repository root so direct file execution can import shared
helpers. The Python terminal uses `.vscode/python.env`; open a new terminal after
changing these settings.

```powershell
.\.venv\Scripts\python.exe -m algorithms.arrays_hashing.contains_duplicate
```

## Shared test helpers

All exercises use `run_tests` from `algorithms/test_helpers.py`. Each case is
`((arguments,), expected)`. Keep the solution and cases in the exercise file:

```python
from algorithms.test_helpers import run_tests

# Define Solution above this block.
if __name__ == "__main__":
    cases = [
        (([1, 2, 3],), False),
        (([1, 2, 1],), True),
    ]
    raise SystemExit(run_tests(Solution().containsDuplicate, cases))
```

Pass a list of methods to test several solutions. Optional arguments support
unordered results (`normalize=sorted` or `normalize=normalize_groups`), custom
checks (`check=check_two_sum`), and input preservation (`unchanged=True`). Custom
checks receive `(arguments, result, expected)` and raise `AssertionError` on failure.
The runner checks result types, copies inputs for each call, prints pass/fail
results, and returns a nonzero exit code if any case fails.

Linked-list exercises also use `algorithms/linked_list/helpers.py` for `ListNode`
and conversions. They pass `prepare=prepare_linked_lists` and
`convert=linked_list_to_list` to the same runner, including cycle detection.

Outside VS Code, run individual exercises with `-m` from the repository root so
shared imports resolve. To run all exercises:

```powershell
.\.venv\Scripts\python.exe scripts/check_exercises.py
```

## GitHub checks

GitHub Actions runs all exercises and checks lint and formatting with Ruff on
every push and pull request. View results in the **Actions** tab. To run checks
manually, select **Python checks → Run workflow** (available once the workflow
is on the default branch).

## Checks before committing

Install the development dependencies and enable the local Git hook once:

```powershell
.\.venv\Scripts\python.exe -m pip install "pre-commit>=4,<5" "ruff>=0.11,<1"
.\.venv\Scripts\python.exe -m pre_commit install
```

Before each commit, the hook runs all exercise checks, Ruff lint, and Ruff
format checks. A commit is rejected if any check fails. GitHub Actions runs
the same checks as an additional safeguard. The hook can be bypassed with
`--no-verify`, so keep the GitHub checks required for merging if you want
server-side enforcement too.
