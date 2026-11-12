class Category:
    def __init__(self,name,transaction_type):
        self.name = name
        self.transaction_type = transaction_type

    def display_info(self):
        print("Name:",self.name)
        print("Transaction Type:",self.transaction_type)