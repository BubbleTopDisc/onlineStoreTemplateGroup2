class Admin:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def restock(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def put_on_sale(self, product, discount):
        self.product = product
        self.discount = discount
