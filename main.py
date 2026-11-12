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
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount: "))

        while True:
            try:
                amount = float(input("Enter amount: "))

                if amount > 0:
                    break
                else:
                    print("Amount must be greater than zero.")

            except ValueError:
                print("Please enter a valid number.")

        category = input("Enter category: ")
        description = input("Enter description: ")
        date = input("Enter date (YYYY-MM-DD): ")

        transaction = Transaction(
            1,
            amount,
            "expense",
            category,
            description,
            date
        )

        manager.add_transaction(transaction)
        print("Expense added successfully!")

    elif choice == "2":
        print("Add income")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        date = input("Enter date (YYYY-MM-DD): ")

        transaction = Transaction(
        2,
        amount,
        "income",
        category,
        description,
        date
        )
        manager.add_transaction(transaction)
        print("Income added successfully!")


    elif choice == "3":
        manager.show_transactions()

    elif choice == "4":
        print("Total expenses:", manager.calculate_total_expenses())

    elif choice == "5":
        print("Total income:", manager.calculate_total_income())

    elif choice == "6":
        print("Balance:", manager.calculate_balance())

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")