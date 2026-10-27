# Engineering Knowledge Base

A personal collection of Python exercises and practical engineering notes.

- `algorithms/` — exercises grouped by topic, with example checks in each file.
- Learning notes:
  - [Algorithm logic and problem-solving](docs/problem-solving/)
  - [Python functions and methods](docs/python-functions/)
  - [Python data structures](docs/data-structures/)

## Run an exercise

From the repository root, using the local Python environment:

```powershell
.\.venv\Scripts\python.exe algorithms/arrays_hashing/contains_duplicate.py
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
