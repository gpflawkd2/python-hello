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
- `model/` — Pydantic schemas (`Customer`, `Market`) shared by the layers below.
- `data/` — persistence layer. `data/init.py` opens the SQLite connection used by the app; `data/customer.py` and `data/market.py` read/write using those models.
- `service/` — thin business-logic layer between `data/` and `web/`.
- `web/` — FastAPI `APIRouter`s, one per resource (`/customer`, `/market`), mounted onto the app in `main.py`.
- `main.py` — app entrypoint; includes the routers and runs the server.

Run the app with:

```bash
source .venv/bin/activate
python main.py
```

Then try, e.g. with `httpie` (`http GET localhost:8000/customer/`) or `curl`:

```bash
curl -s http://localhost:8000/customer/
curl -s http://localhost:8000/market/
```

See [CLAUDE.md](CLAUDE.md) for more detail on environment setup and running scripts.

## Database

### SQLite (current setup — `data/init.py`)

The app connects to a single shared SQLite database rather than SQLAlchemy. `data/init.py` runs at import time and sets up a module-level connection and cursor that the rest of `data/` reuses:

```python
# data/init.py
from pathlib import Path
from sqlite3 import connect, Connection, Cursor

conn: Connection | None = None
curs: Cursor | None = None

def create_db():
    global conn, curs
    top_dir = Path(__file__).resolve().parents[1]
    db_dir = top_dir / "db"
    db_dir.mkdir(exist_ok=True)
    db_path = str(db_dir / "customer.db")
    conn = connect(db_path, check_same_thread=False)
    curs = conn.cursor()

create_db()
```

- The database file lives at `db/customer.db`, resolved relative to the project root so it works regardless of the current working directory; the `db/` folder is created automatically if missing.
- `check_same_thread=False` is required because FastAPI/uvicorn can serve requests on different threads than the one that opened the connection.
- `conn`/`curs` are created once on import and reused by every module under `data/` (e.g. `data/customer.py` calls `curs.execute(...)` to create the `customers` table on import).
- `db/customer.db` is a local, generated file and is covered by the `*.db` rule in `.gitignore` — it should never be committed.
- `data/market.py` does **not** use this database yet — it still returns an in-memory fake list, so only the customer data path is backed by SQLite so far.

### SQLAlchemy (alternative pattern, e.g. for PostgreSQL)

`sqlalchemy` + `psycopg2-binary` are installed so the same code can target SQLite locally and PostgreSQL in other environments — just switch the `DATABASE_URL` env var; SQLite needs no extra driver since `sqlite3` is built into Python.

```python
# db.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///app.db")
# Postgres example: postgresql+psycopg2://user:pw@host/db

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

```python
# models.py
from sqlalchemy import Column, Integer, String
from db import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
```

Usage with FastAPI (`Depends(get_db)` injects a session per request):

```python
# main.py
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import uvicorn

from db import engine, Base, get_db
from models import Item

Base.metadata.create_all(bind=engine)  # creates tables if they don't exist

app = FastAPI()


class ItemCreate(BaseModel):
    name: str


@app.get("/items")
def list_items(db: Session = Depends(get_db)):
    return db.query(Item).all()


@app.post("/items")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
```

#### Trying it locally

With no `DATABASE_URL` set, `db.py` defaults to `sqlite:///app.db` — a file created next to wherever the app runs, no server or extra setup needed. Save the three snippets above as `db.py`, `models.py`, `main.py` in the same folder, then:

```bash
source .venv/bin/activate
python main.py
```

Verify with:

```bash
curl -s http://localhost:8000/items
curl -s -X POST http://localhost:8000/items -H "Content-Type: application/json" -d '{"name":"test item"}'
curl -s http://localhost:8000/items
```

or open `http://localhost:8000/docs` for the interactive Swagger UI. The generated `app.db` file is local-only and should not be committed (see `.gitignore`).

To use PostgreSQL instead, set `DATABASE_URL` before running, e.g. `export DATABASE_URL=postgresql+psycopg2://user:pw@host/db`.
