
from database import connect_db

connection = connect_db()
cursor = connection.cursor()

cursor.execute("""
    INSERT INTO transactions
    (amount, transaction_type, category_id, description, transaction_date)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING transaction_id
""", (250, "expense", 1, "Python test", "2026-11-16"))

transaction_id = cursor.fetchone()

connection.commit()

print("Transaction added successfully!")
print("Transaction ID:", transaction_id[0])

cursor.close()
connection.close()
