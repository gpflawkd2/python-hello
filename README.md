# python-hello
Python study

## Prerequisites
+ Python Version 3.14.7 
+ Visual Studio Code

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Opening the project folder in VSCode auto-selects `.venv` as the interpreter (configured in `.vscode/settings.json`), so the integrated terminal and "Run Python File" use it without extra steps.

## Project structure

- `syntax/` — one script per Python language feature (print, variables, data types, numbers, strings, lists). Each file runs standalone, e.g. `python syntax/print.py`.
- `example/` — practical scripts built on the third-party stack in `requirements.txt` (`requests`, `pandas`, `fastapi`, `uvicorn`, etc.), such as calling external APIs and loading results into a DataFrame.

See [CLAUDE.md](CLAUDE.md) for more detail on environment setup and running scripts.
