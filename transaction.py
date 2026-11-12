class Transaction:
    def __init__(self, transaction_id, amount, transaction_type, category, description, date):
        self.transaction_id = transaction_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.category = category
        self.description = description
        self.date = date

    def display_info(self):
        print("ID:",self.transaction_id)
        print("Amount:",self.amount)
        print("Type:",self.transaction_type)
        print("Category:",self.category)
        print("Description:",self.description)
        print("Date:",self.date)