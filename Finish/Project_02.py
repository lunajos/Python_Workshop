from Modules.Project_3 import Restaurant

menu_items = {
  "Soup": 2.22,
  "Large Pizza": 10.95,
  "Salad": 4.21
}

res = Restaurant(10, "Pizza Malls", menu_items)
res.print_menu()
res.dine_in(4)
print(res.show_tables())

menu_items_2 = {
  "Soup": 2.22,
  "Pasts": 9.99,
  "Salad": 5.21,
  "Baked Ziti": 99.99
}

new_res = Restaurant(1111, "test", menu_items_2)
new_res.print_menu()
new_res.dine_in(4)
print(new_res.show_tables())
