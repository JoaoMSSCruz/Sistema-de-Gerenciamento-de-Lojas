
def change_quantity_product(shop):
    category = str(input("\nType the category of the product: "))
    if not shop.category_exists(category):
        print("Category not existent.")
        return

    product_name = str(input("Type the name of the product: "))
    if product_name not in shop.get_category_product_names(category):
        print("Product not in the category.")
        return
    
    product = shop.get_product_by_name(product_name)

    while True:
        choice = str(input("Do you want to add or remove quantity? "))
        if choice in ["add", "remove"]:
            break

    quantity = int(input("How much? "))
    if choice == "add":
        product.increase_quantity(quantity)
    else:
        product.increase_quantity(quantity*(-1))

    print("The new quantity of the product is {}.".format(product.get_quantity()))

