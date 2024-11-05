from funcs.product.add_product import add_product
from funcs.product.remove_product import remove_product
from funcs.product.view_product import view_product
from funcs.product.change_quantity_product import change_quantity_product

def products_menu(shop):
    while True:
        texto_inicial = "\nChoose an option:\n1) Add Product\n2) Remove Product\n3) View Product\n4) Change Quantity Of Product\n5) Go Back\nChoice: "
        try:
            escolha = int(input(texto_inicial))
            if escolha == 1:
                add_product(shop)
            elif escolha == 2:
                remove_product(shop)
            elif escolha == 3:
                view_product(shop)
            elif escolha == 4:
                change_quantity_product(shop)
            elif escolha == 5:
                break

        except ValueError:
            print("\nPlease type a valid number.")
