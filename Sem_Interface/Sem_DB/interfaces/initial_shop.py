from interfaces.products_menu import products_menu
from interfaces.category_menu import category_menu
from funcs.inventory_report import inventory_report

def initial_shop(shop):
    while True:
        texto_inicial = "\nChoose an option:\n1) Product Menu\n2) Category Menu\n3) Inventory Report\n4) Go Back\nChoice: "
        try:
            escolha = int(input(texto_inicial))
            if escolha == 1:
                products_menu(shop)
            elif escolha == 2:
                category_menu(shop)
            elif escolha == 3:
                inventory_report(shop)
            elif escolha == 4:
                break

        except ValueError:
            print("\nPlease type a valid number.")
