
def view_category(shop):
    category = str(input("\nType the name of the category: "))
    if not shop.category_exists(category):
        print("Category not existent.")
        return

    if shop.get_category(category) == {}:
        print("The category is empty.")
        return

    print("These are the products in the category: \n")
    for product in shop.get_category_products(category):
        print("Name: {}, Description: {}, Price: {}€, Quantity: {}".format(product.get_name(), product.get_description(), product.get_price(), product.get_quantity()))
