import sqlite3
from pathlib import Path

DB_PATH = Path("data/service.db")


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT)
        
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            duration INTEGER NOT NULL)
                
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            service_id INTEGER NOT NULL,
            status TEXT NOT NULL,
            total_price REAL NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (client_id) REFERENCES clients(id),
            FOREIGN KEY (service_id) REFERENCES services(id))
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL)
        """)

        conn.commit()