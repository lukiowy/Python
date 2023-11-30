from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
m = Menu()
cm = CoffeeMaker()
my = MoneyMachine()
running = True
while running:
    whole_menu = m.get_items()
    choice = input(f"What would you like ({whole_menu}): ")
    if choice == "off":
        print("Goodbye :)")
        running = False
    elif choice == "report":
        report = cm.report()
        rep = my.report()
    elif choice in whole_menu:
        drink = m.find_drink(choice)
        if cm.is_resource_sufficient(drink) == True:
            cost = drink.cost
            print(f"This will cost ${cost}.")
            if my.make_payment(cost) == True:
                cm.make_coffee(drink)
