import sqlite3
import os

DB_NAME = "pipeline_activity.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS module_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            module_name TEXT,
            open_time TEXT,
            close_time TEXT,
            status TEXT
            machine_name TEXT,
            username TEXT
        )
    """)

    conn.commit()
    conn.close()