from classes.shop import Shop

def add_shop(shop_manager):
    shop_name = str(input("\nType the store name: "))

    if shop_manager.exists_shop(shop_name):
        print("This shop already exists.")
        return
    
    shop = Shop(shop_name)

    shop_manager.add_shop(shop_name, shop)

    print("Shop added successfully.")