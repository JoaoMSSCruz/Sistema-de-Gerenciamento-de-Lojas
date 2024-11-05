
def inventory_report(shop):
    categories = shop.get_categories()

    if categories == {}:
        print("\nThere are no products yet.")

    for category in categories.keys():
        print("\n{}:".format(category))
        for product_name in categories[category]:
            product = shop.get_product_by_name(product_name)
            print("  Name: {}, Description: {}, Price: {}€, Quantity: {}".format(product.get_name(), product.get_description(), product.get_price(), product.get_quantity()))

