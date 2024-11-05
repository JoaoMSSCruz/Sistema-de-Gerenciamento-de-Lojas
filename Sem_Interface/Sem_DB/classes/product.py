class Product:
    def __init__(self, category, name, description, price):
        # Initialize product with category, name, description, price, and set quantity to 0
        self.name = name
        self.description = description
        self.price = price
        self.quantity = 0
        self.category = category

    def get_category(self):
        return self.category

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity
    
    def increase_quantity(self, quantity):
        # Increase product quantity by specified amount
        self.quantity += quantity
        if self.quantity < 0:
            self.quantity = 0