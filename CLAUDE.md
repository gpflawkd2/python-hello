# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Personal Python study repository (Korean-language comments/notes). Python 3.14.7. No package, no build system, no test suite — scripts are run directly and read top-to-bottom as learning material.

## Commands

Activate the virtual environment before installing packages or running any script (macOS with Homebrew Python blocks global `pip install` with an `externally-managed-environment` error):

```bash
source .venv/bin/activate
```

Install dependencies from the pinned list:

```bash
pip install -r requirements.txt
```

Run any script directly, e.g.:

```bash
python syntax/print.py
```

After adding a new dependency, re-freeze the lock file:

```bash
pip freeze > requirements.txt
```

### Running in a terminal

The virtual environment is never activated automatically — each new terminal session needs:

```bash
source .venv/bin/activate
python syntax/print.py
```

Without this, the system Homebrew Python runs instead and any script using `requests`, `pandas`, `fastapi`, etc. fails with `ModuleNotFoundError`.

### Running in VSCode

`.vscode/settings.json` (workspace-scoped, does not affect other projects such as the C# one on this machine) pins the interpreter to `.venv`. Opening this folder auto-activates `.venv` in the integrated terminal and uses it for "Run Python File" — no manual steps needed. If VSCode still shows the system interpreter, run "Developer: Reload Window".