from database import connect_db

try:
    connection = connect_db()

    print("Connection to PostgreSQL successful!")

    connection.close()

except Exception as error:
    print("Connection failed:", error)