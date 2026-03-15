import sqlite3

def connect_db():
    conn = sqlite3.connect("contacts.db")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()