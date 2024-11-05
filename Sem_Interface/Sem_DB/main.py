# Import the 'inicial' function from the 'interfaces.inicial' module.
from interfaces.initial import initial

# Import the 'Loja' class from the 'classes.loja' module.
from classes.shop_manager import Shop_Manager

# Create an instance of the 'Loja' class with the name "Lojinha".
shop_manager = Shop_Manager()

# Define the main function to serve as the entry point of the program.
# This function calls the 'inicial' function, passing the 'loja' instance as an argument.
def main():
    global shop_manager
    initial(shop_manager)

if __name__ == "__main__":
    main()
