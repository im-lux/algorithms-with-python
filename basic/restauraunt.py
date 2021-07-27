print ("Welcome to Get GOOD FOOD Restaurant!")

menu = {}

while True:
    dish_name = input("Please enter the name of the dish: ")
    dish_price = input("Please enter the price for a %s: " % dish_name)
    menu[dish_name] = dish_price

    new = input("Would you like to enter a new dish? (y/n)")

    if new == "no" or new == "n":
        break

print ("Menu: %s" % menu)

with open("menu.txt", "w+") as menu_file:
    for dish in menu:
        menu_file.write("%s, %s EUR\n" % (dish, menu[dish]))

print
print ("Thank You. GOODBYE!")