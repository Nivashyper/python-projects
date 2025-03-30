from db import get_conn

def setup():
    with get_conn() as c:
        c.execute("CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY, text TEXT)")

def add(text: str):
    with get_conn() as c:
        c.execute("INSERT INTO notes(text) VALUES (?)", (text,))

def list_all():
    with get_conn() as c:
        return [r[0:2] for r in c.execute("SELECT id, text FROM notes ORDER BY id")]

if __name__ == "__main__":
    setup(); add("hello sqlite"); print(list_all())
