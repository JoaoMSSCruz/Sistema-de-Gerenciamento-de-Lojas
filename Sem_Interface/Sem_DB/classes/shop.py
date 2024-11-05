class Shop:
    def __init__(self, name):
        self.name = name
        self.categories = {}

    def add_category(self, category):
        self.categories[category] = {}

    def remove_category(self, category):
        self.get_categories().pop(category)

    def get_categories(self):
        return self.categories
    
    def get_category_product_names(self, category):
        return self.get_category(category).keys()
    
    def get_category_products(self, category):
        return self.get_category(category).values()
    
    def get_category(self, category):
        return self.get_categories()[category]
    
    def category_exists(self, category):
        if category in self.get_categories().keys():
            return True
        else:
            return False
        
    def add_product_to_category(self, category, product):
        self.categories[category][product.get_name()] = product

    def get_product_by_name(self, product_name):
        for category in self.get_categories().values():
            if product_name in category.keys():
                return category[product_name]
        return []