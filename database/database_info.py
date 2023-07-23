class database_info:
    def __init__(self, name, users, profits, user_history, sold):
        self.name = name
        self.users = users
        self.profits = profits
        self.user_history = user_history
        self.sold = sold
        

class sale_transactions:
    def __init__(self, sold, profits):
        self.sold = sold
        self.profits = profits

class customer_data:
    def __init__(self, name, users, user_history):
        self.name = name
        self.users = users
        self.user_history = user_history

class finacals :
    def __init__(self,sold,profits, expences, total_income ) :
        self.sold = sold
        self.profits = profits
        self.expences = expences
        self.total_income = total_income