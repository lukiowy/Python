MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report(choice):
    if choice == "report":
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${profit}")
    
def adding_money():
    money = 0
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    money += (quarters * 0.25)
    dimes = int(input("How many dimes? "))
    money += (dimes * 0.1)
    nickles = int(input("How many nickles? "))
    money += (nickles * 0.05)
    pennies = int(input("How many pennies? "))
    money += (pennies * 0.01)
    return money

def coffee(choice):
    price = MENU[choice]["cost"]
    print(f"This will cost ${price}.")
    money = adding_money()
    if price > money:
        print("Sorry that's not enough. Money refunded.")
    elif money > price:
        change = round(money - price,2)
        print(f"Here is your change: ${change}")
        print(f"Here is your {choice}. Enjoy!")
        global profit
        profit += price
    elif money == price:
        print(f"Here is your {choice}. Enjoy!")

def check_resources(choice):
    ingredients = MENU[choice]["ingredients"]
    menu_water = ingredients["water"]
    menu_coffe = ingredients["coffee"]
    menu_milk = 0
    if choice == "latte" or choice == "cappuccino":
        menu_milk = ingredients["milk"]

    resources_water = resources["water"]
    resources_coffe = resources["coffee"]
    resources_milk = resources["milk"]

    if resources_water >= menu_water and resources_milk >= menu_milk and resources_coffe >= menu_coffe:
        coffee(choice)
        water = resources_water - menu_water 
        resources["water"] = water
    else:
        print("There is not enough resources.")

profit = 0
running = True
while running:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print("Goodbye :)")
        running = False
    elif choice == "report":
        print_report(choice)
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        check_resources(choice)