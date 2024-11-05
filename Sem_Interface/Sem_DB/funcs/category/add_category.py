
def add_category(shop):
    category = str(input("\nType the name of the new category: "))

    if shop.category_exists(category):
        print("Category already existent.")
        return

    shop.add_category(category)
    print("Category added successfully!")




    