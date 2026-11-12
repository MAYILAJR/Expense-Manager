class ExpenseManager:
    def __init__(self):
        self.transactions = []
        self.categories = []
        self.next_id = 1

    def add_transaction(self, transaction):
        transaction.transaction_id = self.next_id
        self.transactions.append(transaction)
        self.next_id += 1

    def add_category(self, category):
        self.categories.append(category)

    def show_transactions(self):
        for transaction in self.transactions:
            transaction.display_info()

    def calculate_total_expenses(self):
        total = 0

        for transaction in self.transactions:
            if transaction.transaction_type == "expense":
                total = total + transaction.amount

        return total

    def calculate_total_income(self):
        total = 0

        for transaction in self.transactions:
            if transaction.transaction_type == "income":
                total = total + transaction.amount

        return total

    def calculate_balance(self):
        total_income = self.calculate_total_income()
        total_expenses = self.calculate_total_expenses()

        balance = total_income - total_expenses

        return balance
