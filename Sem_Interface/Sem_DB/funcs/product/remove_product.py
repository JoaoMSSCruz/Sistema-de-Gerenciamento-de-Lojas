
def remove_product(shop):
    try:
        product_name = str(input("Type the product name: "))

        product = shop.get_product_by_name(product_name)

        if product == []:
             print("Product not existent.")
             return
        
        shop.get_category(product.get_category()).pop(product_name)

        print("Product removed successfully.")

    except ValueError:
            print("\nPlease type a valid number.")



    