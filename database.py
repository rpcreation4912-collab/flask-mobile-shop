import sqlite3

def get_db():
    conn = sqlite3.connect("mydatabase.db")
    return conn

def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)"
    )
    conn.commit()
    conn.close()
