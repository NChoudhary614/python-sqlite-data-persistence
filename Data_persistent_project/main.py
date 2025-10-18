from database.database import (
    initialize_database, add_user, add_transaction,
    fetch_transactions, backup_database, restore_database
)

def main():
    initialize_database()
    add_user('Alice', 'alice@example.com')
    add_user('Bob', 'bob@example.com')
    add_transaction(1, 250.50, '2025-10-18')
    add_transaction(2, 99.99, '2025-10-18')
    print(fetch_transactions())
    backup_database()
    # To restore, uncomment and provide the correct backup file path:
    # restore_database('backups/company_data_backup_20251018_123000.db')

if __name__ == '__main__':
    main()
