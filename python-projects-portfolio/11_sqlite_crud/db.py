import sqlite3
from contextlib import contextmanager

@contextmanager
def get_conn(db_path="app.db"):
    conn = sqlite3.connect(db_path)
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()
