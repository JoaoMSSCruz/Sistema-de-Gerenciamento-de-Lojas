
class Shop_Manager:
    def __init__(self):
        self.shops = {}

    def add_shop(self, shop_name, shop):
        self.get_shops()[shop_name] = shop
    
    def remove_shop(self, shop_name):
        self.get_shops().pop(shop_name)

    def get_shops(self):
        return self.shops
    
    def exists_shop(self, shop_name):
        return shop_name in self.get_shops().keys()