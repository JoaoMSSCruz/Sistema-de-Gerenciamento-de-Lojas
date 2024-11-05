from funcs.category.add_category import add_category
from funcs.category.remove_category import remove_category
from funcs.category.show_all_categories import show_all_categories
from funcs.category.view_category import view_category

def category_menu(shop):
    while True:
        texto_inicial = "\nChoose an option:\n1) Add Category\n2) Remove Category\n3) Show All Categories\n4) View Category \n5) Go Back\nChoice: "
        try:
            escolha = int(input(texto_inicial))
            if escolha == 1:
                add_category(shop)
            elif escolha == 2:
                remove_category(shop)
            elif escolha == 3:
                show_all_categories(shop)
            elif escolha == 4:
                view_category(shop)
            elif escolha == 5:
                break

        except ValueError:
            print("\nPlease type a valid number.")
