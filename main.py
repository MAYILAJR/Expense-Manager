
from transaction import Transaction
from expense_manager import ExpenseManager


manager = ExpenseManager()


while True:

    print("\n--- Expense Manager ---")
    print("1. Add an expense")
    print("2. Add an income")
    print("3. Show all transactions")
    print("4. Show total expenses")
    print("5. Show total income")
    print("6. Show balance")
    print("7. Update a transaction")
    print("8. Delete a transaction")
    print("9. Add a category")
    print("10. Show all categories")
    print("11. Delete a category")
    print("0. Exit")

    choice = input("Choose an option: ")

    # ADD AN EXPENSE
    if choice == "1":

        print("\n--- Add an Expense ---")

        category = manager.get_valid_category("expense")

        if category is not None:

            amount = manager.get_valid_amount()
            description = manager.get_valid_description()
            date = manager.get_valid_date()

            transaction = Transaction(
                0,
                amount,
                "expense",
                category,
                description,
                date
            )

            manager.add_transaction(transaction)

    # ADD AN INCOME
    elif choice == "2":

        print("\n--- Add an Income ---")

        category = manager.get_valid_category("income")

        if category is not None:

            amount = manager.get_valid_amount()
            description = manager.get_valid_description()
            date = manager.get_valid_date()

            transaction = Transaction(
                0,
                amount,
                "income",
                category,
                description,
                date
            )

            manager.add_transaction(transaction)

    # SHOW ALL TRANSACTIONS
    elif choice == "3":

        manager.show_transactions()

    # SHOW TOTAL EXPENSES
    elif choice == "4":

        print(
            "Total expenses:",
            manager.calculate_total_expenses()
        )

    # SHOW TOTAL INCOME
    elif choice == "5":

        print(
            "Total income:",
            manager.calculate_total_income()
        )

    # SHOW BALANCE
    elif choice == "6":

        print(
            "Balance:",
            manager.calculate_balance()
        )

    # UPDATE TRANSACTION
    elif choice == "7":

        manager.update_transaction()

    # DELETE TRANSACTION
    elif choice == "8":

        manager.delete_transaction()

    # ADD CATEGORY
    elif choice == "9":

        manager.add_category()

    # SHOW ALL CATEGORIES
    elif choice == "10":

        manager.show_categories()

    # DELETE CATEGORY
    elif choice == "11":

        manager.delete_category()

    # EXIT
    elif choice == "0":

        print("Goodbye!")
        break

    # INVALID OPTION
    else:

        print("Invalid option. Try again.")
