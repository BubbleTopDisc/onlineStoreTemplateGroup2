class Customer:
    def __init__(self, name, email, address, membership):
        self.name = name
        self.email = email
        self.address = address
        self.membership = membership

class Cart:
    def __init__(self, date, total, quantity, tax):
        self.date = date
        self.total = total
        self.quantity = quantity
        self.tax = tax