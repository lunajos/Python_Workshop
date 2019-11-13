# Create a Restaurant class
# Define __init__ with params
# Assign Values

# Create a create order method
# Create a pick up method
# Create a dine in method
# Show available tables
# Show menu


class Restaurant:

    def __init__(self, tables, restaurant_name, menu_items):
        self.tables = tables
        self.restaurantName = restaurant_name
        self.menu_items = menu_items

    def print_menu(self):
        print("****************************************")
        print("\t\t" + self.restaurantName + "\n\n")
        for x in self.menu_items:
            print("\t\t" + x + ":\t" + str(self.menu_items[x]))
        print("****************************************")

    def show_tables(self):
        return self.tables

    def dine_in(self, guests):
        self.tables -= guests
