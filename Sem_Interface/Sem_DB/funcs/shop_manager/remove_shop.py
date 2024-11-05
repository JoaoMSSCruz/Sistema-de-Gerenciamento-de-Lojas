
def remove_shop(shop_manager):
    shop_name = str(input("\nType the store name: "))

    if not shop_manager.exists_shop(shop_name):
        print("This shop doesn't exists.")
        return

    shop_manager.remove_shop(shop_name)

    print("Shop removed successfully.")