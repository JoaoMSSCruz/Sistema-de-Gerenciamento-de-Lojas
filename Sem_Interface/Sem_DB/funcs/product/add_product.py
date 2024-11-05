from classes.product import Product

def add_product(shop):
    try:
        product_category = str(input("\nType the product category: "))
        if not shop.category_exists(product_category):
            print("Category not existent.")    
            return

        product_name = str(input("Type the product name: "))

        if product_name in shop.get_category(product_category).keys():
            print("Product already existent in this category.")
            return
        
        product_description = str(input("Type the product description: "))
        product_price = 0
        while product_price <= 0:
            product_price = float(input("Type the product price: "))
        
        product_quantity = -1
        while product_quantity < 0:
            product_quantity = int(input("Type the product quantity: "))

        product = Product(product_category, product_name, product_description, product_price)
        product.increase_quantity(product_quantity)

        shop.get_category(product_category)[product_name] = product

        print("Product added successfully.")
        
    except ValueError:
            print("\nPlease type a valid number.")



    