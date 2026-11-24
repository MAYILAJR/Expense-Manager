
from database import connect_db

connection = connect_db()
cursor = connection.cursor()

cursor.execute("""
    UPDATE transactions
    SET amount = %s
    WHERE transaction_id = %s
""", (300, 5))

connection.commit()

print("Transaction updated successfully!")

cursor.close()
connection.close()
