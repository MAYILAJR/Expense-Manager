
from database import connect_db
from transaction import Transaction
import math
import psycopg
from datetime import datetime


class ExpenseManager:

    def __init__(self):
        self.transactions = []
        self.categories = []

    # ADD TRANSACTION
    def add_transaction(self, transaction):
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT category_id
            FROM categories
            WHERE category_name = %s
            AND transaction_type = %s
        """, (
            transaction.category,
            transaction.transaction_type
        ))

        category = cursor.fetchone()

        if category is None:
            print("Category not found in database!")
            cursor.close()
            connection.close()
            return

        category_id = category[0]

        cursor.execute("""
            INSERT INTO transactions
            (amount, transaction_type, category_id, description, transaction_date)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING transaction_id
        """, (
            transaction.amount,
            transaction.transaction_type,
            category_id,
            transaction.description,
            transaction.date
        ))

        result = cursor.fetchone()
        transaction.transaction_id = result[0]

        connection.commit()

        self.transactions.append(transaction)

        cursor.close()
        connection.close()

        print("Transaction saved successfully!")

    # UPDATE TRANSACTION
    def update_transaction(self):

        print("\n--- Transactions Available ---")
        self.show_transactions()

        while True:
            try:
                transaction_id = int(
                    input("Enter the transaction ID you want to update: ")
                )

                if transaction_id <= 0:
                    print("ID must be greater than zero.")
                else:
                    break

            except ValueError:
                print("Please enter a valid ID.")

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT transaction_type
            FROM transactions
            WHERE transaction_id = %s
        """, (transaction_id,))

        result = cursor.fetchone()

        if result is None:
            print("Transaction not found!")
            cursor.close()
            connection.close()
            return

        transaction_type = result[0]

        print("\nTransaction found!")

        print("\nWhat do you want to update?")
        print("1. Amount")
        print("2. Category")
        print("3. Description")
        print("4. Date")
        print("0. Cancel")

        choice = input("Choose an option: ")

        if choice == "1":

            new_value = self.get_valid_amount(transaction_type)

            cursor.execute("""
                UPDATE transactions
                SET amount = %s
                WHERE transaction_id = %s
            """, (new_value, transaction_id))

        elif choice == "2":

            new_category = self.get_valid_category()

            cursor.execute("""
                SELECT category_id
                FROM categories
                WHERE category_name = %s
                AND transaction_type = %s
            """, (new_category, transaction_type))

            category = cursor.fetchone()

            if category is None:
                print("Category not found!")
                cursor.close()
                connection.close()
                return

            cursor.execute("""
                UPDATE transactions
                SET category_id = %s
                WHERE transaction_id = %s
            """, (category[0], transaction_id))

        elif choice == "3":

            new_description = self.get_valid_description()

            cursor.execute("""
                UPDATE transactions
                SET description = %s
                WHERE transaction_id = %s
            """, (new_description, transaction_id))

        elif choice == "4":

            new_date = self.get_valid_date()

            cursor.execute("""
                UPDATE transactions
                SET transaction_date = %s
                WHERE transaction_id = %s
            """, (new_date, transaction_id))

        elif choice == "0":

            print("Update cancelled.")
            cursor.close()
            connection.close()
            return

        else:

            print("Invalid option.")
            cursor.close()
            connection.close()
            return

        connection.commit()

        cursor.close()
        connection.close()

        print("Transaction updated successfully!")

    
    # DELETE TRANSACTION
    def delete_transaction(self):

        print("\n--- Transactions Available ---")
        self.show_transactions()

        while True:
            try:
                transaction_id = int(
                    input("Enter the transaction ID you want to delete: ")
                )

                if transaction_id <= 0:
                    print("ID must be greater than zero.")
                else:
                    break

            except ValueError:
                print("Please enter a valid ID.")

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT transaction_id
            FROM transactions
            WHERE transaction_id = %s
        """, (transaction_id,))

        result = cursor.fetchone()

        if result is None:
            print("Transaction not found!")
            cursor.close()
            connection.close()
            return

        confirmation = input(
            "Are you sure you want to delete this transaction? (yes/no): "
        ).strip().lower()

        if confirmation == "yes":

            cursor.execute("""
                DELETE FROM transactions
                WHERE transaction_id = %s
            """, (transaction_id,))

            connection.commit()

            print("Transaction deleted successfully!")

        else:
            print("Deletion cancelled.")

        cursor.close()
        connection.close()

    
    # ADD CATEGORY
    def add_category(self):

        category_name = input("Enter category name: ").strip()

        if not category_name:
            print("Category name cannot be empty.")
            return

        print("\nSelect category type:")
        print("1. Expense")
        print("2. Income")

        choice = input("Choose an option: ")

        if choice == "1":
            transaction_type = "expense"

        elif choice == "2":
            transaction_type = "income"

        else:
            print("Invalid option.")
            return

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT category_id
            FROM categories
            WHERE category_name = %s
            AND transaction_type = %s
        """, (category_name, transaction_type))

        existing_category = cursor.fetchone()

        if existing_category is not None:
            print("This category already exists!")
            cursor.close()
            connection.close()
            return

        cursor.execute("""
            INSERT INTO categories (category_name, transaction_type)
            VALUES (%s, %s)
        """, (category_name, transaction_type))

        connection.commit()

        cursor.close()
        connection.close()

        print("Category added successfully!")



    
    # SHOW ALL CATEGORIES
    def show_categories(self):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT category_id, category_name, transaction_type
            FROM categories
            ORDER BY category_id
        """)

        categories = cursor.fetchall()

        if not categories:
            print("No categories found.")
        else:
            print("\n--- Available Categories ---")

            for category in categories:
                print("ID:", category[0])
                print("Category:", category[1])
                print("Type:", category[2])
                print("------------------------")

        cursor.close()
        connection.close()


    
    # DELETE CATEGORY
    def delete_category(self):

        print("\n--- Available Categories ---")
        self.show_categories()

        while True:
            try:
                category_id = int(
                    input("Enter the category ID you want to delete: ")
                )

                if category_id <= 0:
                    print("ID must be greater than zero.")
                else:
                    break

            except ValueError:
                print("Please enter a valid ID.")

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT category_id
            FROM categories
            WHERE category_id = %s
        """, (category_id,))

        category = cursor.fetchone()

        if category is None:
            print("Category not found!")
            cursor.close()
            connection.close()
            return

        cursor.execute("""
            SELECT transaction_id
            FROM transactions
            WHERE category_id = %s
        """, (category_id,))

        transactions = cursor.fetchall()

        if transactions:
            print("This category is currently used by transactions.")
            print("You must reassign or delete those transactions first.")

            cursor.close()
            connection.close()
            return

        confirmation = input(
            "Are you sure you want to delete this category? (yes/no): "
        ).strip().lower()

        if confirmation == "yes":

            cursor.execute("""
                DELETE FROM categories
                WHERE category_id = %s
            """, (category_id,))

            connection.commit()

            print("Category deleted successfully!")

        else:
            print("Deletion cancelled.")

        cursor.close()
        connection.close()

    

    # SHOW TRANSACTIONS
    def show_transactions(self):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                t.transaction_id,
                t.amount,
                t.transaction_type,
                c.category_name,
                t.description,
                t.transaction_date
            FROM transactions t
            JOIN categories c
            ON t.category_id = c.category_id
            ORDER BY t.transaction_id
        """)

        transactions = cursor.fetchall()

        if not transactions:
            print("No transactions found.")
        else:
            for transaction in transactions:
                transaction_obj = Transaction(*transaction)
                transaction_obj.display_info()
                print("------------------------")

        cursor.close()
        connection.close()

    # CALCULATE TOTAL EXPENSES
    def calculate_total_expenses(self):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COALESCE(SUM(amount), 0)
            FROM transactions
            WHERE transaction_type = %s
        """, ("expense",))

        total = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return total

    # CALCULATE TOTAL INCOME
    def calculate_total_income(self):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COALESCE(SUM(amount), 0)
            FROM transactions
            WHERE transaction_type = %s
        """, ("income",))

        total = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return total

    # CALCULATE BALANCE
    def calculate_balance(self):

        total_income = self.calculate_total_income()
        total_expenses = self.calculate_total_expenses()

        balance = total_income - total_expenses

        return balance


    
    # VALIDATE AMOUNT
    def get_valid_amount(self):

        while True:
            try:
                amount = float(input("Enter the amount: "))

                if not math.isfinite(amount):
                    print("Amount must be a valid number.")
                    continue

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue

                return amount

            except ValueError:
                print("Invalid input. Please enter a numeric value.")


    
    # VALIDATE DATE
    def get_valid_date(self):

        while True:

            date_str = input(
                "Enter the date (YYYY-MM-DD): "
            ).strip()

            try:
                date = datetime.strptime(
                    date_str,
                    "%Y-%m-%d"
                ).date()

                return date

            except ValueError:
                print("Invalid date. Please use YYYY-MM-DD.")



    
    
    # VALIDATE CATEGORY
    def get_valid_category(self, transaction_type):

        while True:

            category_name = input("Enter category: ").strip()

            if not category_name:
                print("Category name cannot be empty.")
                continue

            connection = connect_db()

            if connection is None:
                return None

            cursor = connection.cursor()

            cursor.execute("""
                SELECT category_id
                FROM categories
                WHERE category_name = %s
                AND transaction_type = %s
            """, (category_name, transaction_type))

            existing_category = cursor.fetchone()

            cursor.close()
            connection.close()

            if existing_category is not None:
                return category_name

            print("This category does not exist.")

            confirmation = input(
                "Do you want to create it? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":

                connection = connect_db()

                if connection is None:
                    return None

                cursor = connection.cursor()

                try:
                    cursor.execute("""
                        INSERT INTO categories
                        (category_name, transaction_type)
                        VALUES (%s, %s)
                    """, (category_name, transaction_type))

                    connection.commit()

                    print("Category created successfully!")

                    return category_name

                except psycopg.Error as error:
                    connection.rollback()
                    print("Could not create category:", error)
                    return None

                finally:
                    cursor.close()
                    connection.close()

            elif confirmation == "no":
                print("Please enter another category.")

            else:
                print("Please enter yes or no.")

    
    
    # VALIDATE DESCRIPTION
    def get_valid_description(self):

        description = input(
            "Enter description (optional): "
        ).strip()

        return description

