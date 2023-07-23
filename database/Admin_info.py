class Admin_info:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def all_stocks(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def on_sale(self, product, discount, price ):
        self.product = product
        self.discount = discount
        self.price = price

    def sales_made(self, sold, expenses, profit ):
        self.sold = sold
        self.expenses = expenses
        self.profit = profit