
def view_product(shop):

    product_name = str(input("Type the name of the product: "))

    product = shop.get_product_by_name(product_name)

    if product == []:
        print("Product not in the category.")
        return
    
    print("Name: {}, Description: {}, Price: {}€, Quantity: {}".format(product.get_name(), product.get_description(), product.get_price(), product.get_quantity()))
