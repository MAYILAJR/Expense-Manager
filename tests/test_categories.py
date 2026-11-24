
from database import connect_db

connection = connect_db()

cursor = connection.cursor()

cursor.execute("SELECT * FROM categories")

categories = cursor.fetchall()

for category in categories:
    print(category)

cursor.close()
connection.close()
