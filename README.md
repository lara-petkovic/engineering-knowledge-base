# Engineering Knowledge Base

A personal workspace for learning Python, exploring algorithms, and recording
practical programming knowledge. Exercises are organized by technical topic and
can be developed independently.

## Structure

```text
algorithms/       Python exercises grouped by algorithmic topic
.vscode/          Workspace settings and recommended extensions
pyproject.toml    Python requirements and Ruff configuration
.python-version   Python version used by the workspace
.gitignore        Exclusions for local environments and generated files
```

The local `.venv/` contains the Python environment and is excluded from Git.
Each exercise keeps its implementation and any example checks in the same file.
Topic folders can be added as needed.

## Usage

Activate the local environment from the repository root in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run an exercise by its path, for example:

```powershell
python algorithms/arrays_hashing/contains_duplicate.py
```

Activation is optional; the interpreter can also be called directly:

```powershell
.\.venv\Scripts\python.exe algorithms/arrays_hashing/contains_duplicate.py
```

Place checks under `if __name__ == "__main__":` so they run when the file is
executed directly. Use normal execution without `-O` to enable `assert` checks.

## Editor and formatting

VS Code settings use the local environment and Ruff for Python formatting on save.
Install the recommended Python, Pylance, and Ruff extensions. Select
`.venv\Scripts\python.exe` through **Python: Select Interpreter** if needed.

```powershell
python -m ruff check .
python -m ruff format --check .
```

Apply formatting with `python -m ruff format .`.

## Recreate the environment

Use the Python version recorded in `.python-version`:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install "ruff>=0.11,<1"
```
