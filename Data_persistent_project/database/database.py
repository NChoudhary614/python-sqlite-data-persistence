import sqlite3
import os
import shutil
import datetime
from .models import USER_TABLE_SQL, TRANSACTION_TABLE_SQL

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'company_data.db')
BACKUP_DIR = os.path.join(os.path.dirname(__file__), '..', 'backups')

def get_connection():
    return sqlite3.connect(DB_PATH)

def initialize_database():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(USER_TABLE_SQL)
        cursor.execute(TRANSACTION_TABLE_SQL)
        conn.commit()

def add_user(name, email):
    with get_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
            conn.commit()
        except sqlite3.IntegrityError:
            print(f"User with email {email} already exists.")

def add_transaction(user_id, amount, date):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO transactions (user_id, amount, date) VALUES (?, ?, ?)', (user_id, amount, date))
        conn.commit()

def fetch_transactions():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM transactions')
        return cursor.fetchall()

def backup_database():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(BACKUP_DIR, f'company_data_backup_{timestamp}.db')
    shutil.copy(DB_PATH, backup_file)
    print(f'Backup created: {backup_file}')

def restore_database(backup_file):
    shutil.copy(backup_file, DB_PATH)
    print('Database restored from backup!')
