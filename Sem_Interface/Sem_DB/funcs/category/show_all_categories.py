
def show_all_categories(shop):
    if shop.get_categories() == {}:
        print("\nThere are no categories yet.")
        return 

    print("\nThis is the list of categories: ")
    index = 1
    for category in shop.get_categories():
        print("{}) {}".format(index, category))
        index += 1