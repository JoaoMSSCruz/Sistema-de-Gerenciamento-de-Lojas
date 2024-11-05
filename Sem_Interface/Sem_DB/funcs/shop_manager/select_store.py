from interfaces.initial_shop import initial_shop

def select_store(shop_manager):
    if shop_manager.get_shops() == {}:
        print("\nThere are no shops available.")
        return

    print("\nShops available:")
    
    for shop_name in shop_manager.get_shops():
        print(" -{}".format(shop_name))
    
    shop_name = ""
    while not shop_manager.exists_shop(shop_name):
        shop_name = str(input("Type the shop you want to select: "))

    initial_shop(shop_manager.get_shops()[shop_name])