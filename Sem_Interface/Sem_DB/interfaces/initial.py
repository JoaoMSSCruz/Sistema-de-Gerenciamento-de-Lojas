from funcs.shop_manager.add_shop import add_shop
from funcs.shop_manager.remove_shop import remove_shop
from funcs.shop_manager.select_store import select_store

def initial(shop_manager):
    while True:
        texto_inicial = "\nChoose an option:\n1) Add Shop\n2) Remove Shop\n3) Select Store\n4) Leave\nChoice: "
        try:
            escolha = int(input(texto_inicial))
            if escolha == 1:
                add_shop(shop_manager)
            elif escolha == 2:
                remove_shop(shop_manager)
            elif escolha == 3:
                select_store(shop_manager)
            elif escolha == 4:
                break

        except ValueError:
            print("\nPlease type a valid number.")