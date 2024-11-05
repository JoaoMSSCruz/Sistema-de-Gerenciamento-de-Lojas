
def remove_category(shop):
    category = str(input("Type the name of the category you want to remove: "))

    if not shop.category_exists(category):
        print("Category not founded.")
        return

    escolha = ""
    while escolha != "y" and escolha != "n":
        escolha = input("Are you sure about your choice? y/n ")
        if escolha == "n":
            return
    
    shop.remove_category(category)
    print("Category removed successfully!")
    