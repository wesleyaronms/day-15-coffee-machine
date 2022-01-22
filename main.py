from data import MENU
from data import resources


def resources_check(which_coffee):
    if resources['water'] >= MENU[which_coffee]['ingredients']['water']:
        if resources['coffee'] >= MENU[which_coffee]['ingredients']['coffee']:
            if user_input == "espresso":
                return True
            else:
                if resources['milk'] >= MENU[which_coffee]['ingredients']['milk']:
                    return True
                else:
                    print(f"Sorry there is not enough milk")
                    return False
        else:
            print(f"Sorry there is not enough coffee")
            return False
    else:
        print(f"Sorry there is not enough water")
        return False


def change(coins):
    if coins < MENU[user_input]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(user_money - MENU[user_input]["cost"], 2)
        print(f"Here is ${change} in change.")
        return True


def make(coffee):
    for ingredient in MENU[coffee]['ingredients']:
        resources[ingredient] -= MENU[coffee]['ingredients'][ingredient]


on = True
money = 0

while on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        on = False
    elif user_input == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${money}")
    else:
        if resources_check(user_input):
            print("Please insert coins.")
            user_money = int(input("How many quarters?: ")) * 0.25
            user_money += int(input("How many dimes?: ")) * 0.10
            user_money += int(input("How many nickles?: ")) * 0.05
            user_money += int(input("How many pennies?: ")) * 0.01
            if change(user_money):
                money += MENU[user_input]["cost"]
                make(user_input)
                print(f"Here is your {user_input} ☕ Enjoy!")
            else:
                on = False
        else:
            on = False
