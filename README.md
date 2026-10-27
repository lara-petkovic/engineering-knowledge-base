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

