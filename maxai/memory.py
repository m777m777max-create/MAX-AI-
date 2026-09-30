import sqlite3
from pathlib import Path
from datetime import datetime

class Memory:
    def __init__(self, path=None):
        path = Path(path or (Path(__file__).resolve().parent.parent / "data" / "max_ai.db"))
        path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(str(path), check_same_thread=False)
        self.db.execute(
            "CREATE TABLE IF NOT EXISTS memory (id INTEGER PRIMARY KEY, key TEXT UNIQUE, value TEXT, updated_at TEXT)"
        )
        self.db.commit()

    def save(self, key, value):
        self.db.execute(
            "INSERT INTO memory(key,value,updated_at) VALUES(?,?,?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
            (key, value, datetime.now().isoformat(timespec="seconds"))
        )
        self.db.commit()

    def all(self):
        return self.db.execute("SELECT key,value FROM memory ORDER BY id DESC").fetchall()
