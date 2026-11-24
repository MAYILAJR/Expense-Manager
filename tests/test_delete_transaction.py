
from database import connect_db

connection = connect_db()
cursor = connection.cursor()

cursor.execute("""
    DELETE FROM transactions
    WHERE transaction_id = %s
    RETURNING transaction_id
""", (5,))

deleted_transaction = cursor.fetchone()

connection.commit()

if deleted_transaction:
    print("Transaction deleted successfully!")
else:
    print("Transaction not found!")

cursor.close()
connection.close()
