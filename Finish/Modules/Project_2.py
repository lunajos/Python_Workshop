# Create a Restaurant class
class Restaurant:

    # Define __init__ with params
    def __init__(self, tables, restaurant_name, menu_items):
        self.tables = tables
        self.restaurantName = restaurant_name
        self.menu_items = menu_items

    # Create a print menu method
    def print_menu(self):
        print("****************************************")
        print("\t\t" + self.restaurantName + "\n\n")
        for x in self.menu_items:
            print("\t\t" + x + ":\t" + str(self.menu_items[x]))
        print("****************************************")

    # Return available tables
    def show_tables(self):
        return self.tables

    # Create Dine in method
    def dine_in(self, guests):
        self.tables -= guests
