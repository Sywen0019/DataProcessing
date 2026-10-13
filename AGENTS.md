# Repository Guidelines

## Project Structure & Module Organization

This repository contains Python data-processing coursework. `EXP01/EXP01.pdf` and `HW01/HW01.pdf` define the respective tasks. Keep each task's notebooks, helper modules, and generated data in its own directory. For example, place `student_utils.py` beside the EXP01 notebook and its data under `EXP01/exp01_data/`. Preserve the original PDFs.

`README.md` provides the directory overview and setup instructions; `environment.yml` records the shared development environment. The repository includes both coursework notebooks, `EXP01/student_utils.py`, and the reproducible sample outputs in `EXP01/exp01_data/` (`students.txt`, `report.txt`, and `students.pkl`). Keep the README inventory consistent with tracked files. There is currently no application package, dedicated test directory, or build pipeline.

## Environment & Development Commands

Use the Python 3.12 Conda environment `ALICE`, located on this workstation at `Z:\Anaconda\anaconda\envs\ALICE`. Keep environments outside the repository and use ALICE for coursework. Inspect and reuse an existing environment; do not delete or recreate it automatically.

Run from the repository root in PowerShell:

```powershell
conda activate ALICE
python -c "import os, sys; print(sys.executable); print(os.environ.get('CONDA_DEFAULT_ENV'))"
python -m pip check
Set-Location EXP01  # Use HW01 for the homework task.
python -m jupyter lab
```

Select `Python (ALICE)` in Jupyter or VS Code. Ensure the notebook working directory is its task directory so relative data paths and sibling imports resolve correctly. On another machine, create the environment from the repository root with `conda env create -f environment.yml`, then run `conda activate ALICE` and register its kernel:

```powershell
python -m ipykernel install --user --name alice --display-name "Python (ALICE)"
```

Use `python -m pip check` to check dependency consistency. No build command is required.

## Coding Style & Naming Conventions

Use four-space indentation, `snake_case` for functions and variables, and `PascalCase` for classes. Prefer standard-library solutions, UTF-8 text files, and paths relative to the task directory. Explain reasoning in Markdown cells. Follow submission names such as `<student_id>_<name>_exp01.ipynb` and `<student_id>_<name>_hw01.ipynb`. No formatter or linter is configured.

## Testing Guidelines

No automated test framework or coverage threshold is configured. Restart the kernel and run all notebook cells before submission. Check expected results, boundary cases, exception handling, and file paths. Verify that `sys.executable` points to ALICE and `CONDA_DEFAULT_ENV` equals `ALICE`; investigate mismatches before continuing. Report actual execution results.

For documentation-only changes, verify paths, commands, UTF-8 encoding, and `git diff --check`; notebook execution is unnecessary unless the documentation change depends on new execution results. Do not claim tests or notebook runs that were not performed.

## Commit & Pull Request Guidelines

Use concise, imperative subjects, for example `Add EXP01 file parsing exercises`. Keep changes focused on the requested task. Inspect the working tree before editing and stage explicitly named files so unrelated local work is preserved. For documentation updates, commit only the requested documentation unless a broader scope is authorized. PRs should describe changes, identify the relevant assignment or issue, and report validation performed. Include screenshots only when needed to review visual output.

When a push is requested, verify the current branch and remote, review the staged diff, and push the resulting commit. Do not force-push or overwrite remote changes; fetch and reconcile divergence if necessary. Report the commit and push result.

## Parallel Work

Agents share ALICE but work independently in `EXP01/` and `HW01/`. Coordinate shared dependency changes, record necessary additions in `environment.yml`, and avoid unnecessary frameworks. Keep environment directories, caches, checkpoints, and secrets out of commits.
