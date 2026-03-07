from database import get_connection
from datetime import datetime
import platform
import getpass


machine = platform.node()
user = getpass.getuser()

def log_module_open(module_name):
    conn = get_connection()
    cursor = conn.cursor()

    open_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO module_activity (module_name, open_time, status)
        VALUES (?, ?, ?)
    """, (module_name, open_time, "OPEN"))

    conn.commit()
    module_id = cursor.lastrowid
    conn.close()

    return module_id


def log_module_close(module_id):
    conn = get_connection()
    cursor = conn.cursor()

    close_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        UPDATE module_activity
        SET close_time = ?, status = ?
        WHERE id = ?
    """, (close_time, "COMPLETED", module_id))

    conn.commit()
    conn.close()


def get_all_logs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM module_activity ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    return rows


def get_incomplete_modules():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT module_name, open_time
        FROM module_activity
        WHERE status = 'OPEN'
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

def get_last_module_status(module_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT open_time, close_time, status
        FROM module_activity
        WHERE module_name = ?
        ORDER BY id DESC
        LIMIT 1
    """, (module_name,))

    result = cursor.fetchone()
    conn.close()

    return result