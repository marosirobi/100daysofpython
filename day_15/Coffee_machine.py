from machine_details import*

def report(resources: object) -> None:
    for source in resources:
        print(f"{source}: {resources[source]}")

def check_resources(order):
    not_enough = []
    for source in resources:
        for ingred in MENU[order]["ingredients"]:
            if source == ingred and (resources[source] - MENU[order]["ingredients"][ingred]) < 0:
                not_enough.append(ingred)
    return not_enough

def print_not_enough(order):
    not_enough = check_resources(order)
    for ingred in not_enough:
        print(f"Sorry, there is not enough {ingred}.")

def money_converter():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    dollar = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return dollar

def enough_money(order,money):
    if MENU[order]["cost"] > money:
        return -1
    elif MENU[order]["cost"] == money:
        return 0
    elif MENU[order]["cost"] < money:
        return round(money - MENU[order]["cost"],3)

def making_coffee(order):
    if len(check_resources(order)) > 0:
        print_not_enough(order)
        on = False
    else:
        print("Please insert coins.")
        money = money_converter()
        change = enough_money(order, money)
        if change == -1:
            print("Sorry, that's not enough money. Money refunded")
            on = False
        elif change > 0:
            print(f"Here's the change: {change}")
            money -= change
            resources["money"] += round(money, 1)
            print(f"{order} in the making...done")

            for source in resources:
                for ingred in MENU[order]["ingredients"]:
                    if source == ingred:
                        resources[source] -= MENU[order]["ingredients"][ingred]
        else:
            print(f"{order} in the making...done")

            for source in resources:
                for ingred in MENU[order]["ingredients"]:
                    if source == ingred:
                        resources[source] -= MENU[order]["ingredients"][ingred]


def main():
    on = True
    while on:
        order = input("What would you like? (espresso/latte/cappuccino) ").lower()
        if order == "report":
            report(resources)
        elif order == "off":
            on = False
        else:
            making_coffee(order)


main()
