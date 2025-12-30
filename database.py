import sqlite3

def get_db():
    return sqlite3.connect("shop.db")

def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mobiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT,
            model TEXT,
            price INTEGER
        )
    """)
    conn.commit()
    conn.close()
