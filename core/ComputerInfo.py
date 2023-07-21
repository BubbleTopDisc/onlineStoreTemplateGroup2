class ComputerInfo:
    def __init__(self, name, description, price, category, manufacturer):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.manufacturer = manufacturer

class Category:
    def __init__(self, name):
        self.name = name

class Manufacturer:
    def __init__(self, name):
        self.name = name