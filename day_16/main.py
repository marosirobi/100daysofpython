from day_16.menu import MenuItem
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    coffee = CoffeeMaker()
    money = MoneyMachine()
    menu = Menu()

    on = True
    while on:
        order = input(f"What would you like? {menu.get_items()} ").lower()
        if order == "report":
            coffee.report()
            money.report()
        elif order == "off":
            on = False
        else:
            drink = menu.find_drink(order)
            if coffee.is_resource_sufficient(drink) == True:
                if money.make_payment(drink.cost):
                    coffee.make_coffee(drink)



main()