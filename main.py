MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}


def check_resources(coffee):
    sufficient = bool
    for key_value in resources.keys():
        for x in range(3):
            if resources[key_value] < MENU[coffee]["ingredients"][key_value]:
                sufficient = False
                return key_value, sufficient
        break
    sufficient = True
    return None, sufficient


def manage_resources(coffee):
    count = 0
    for value in resources.keys():
        resources[value] = resources[value] - MENU[coffee]["ingredients"][value]
        count += 1
        if count == 3:
            break


def report():
    print(f"    Water: {resources['water']}ml")
    print(f"    Milk: {resources['milk']}ml")
    print(f"    Coffee: {resources['coffee']}g")
    print(f"    Money: ${resources['money']}")


def serve_coffee(coffee):
    resources['money'] += MENU[coffee]['cost']
    change = total - MENU[coffee]['cost']
    print(f"Here is ${round(change, 2)} in change.")
    print(f"Here is your {coffee} ☕️. Enjoy!")
    manage_resources(coffee)


start = True
while start:
    total = 0
    request = input("What would you like? (espresso/latte/cappuccino): ")

    while request.lower() == "report":
        report()
        request = input("What would you like? (espresso/latte/cappuccino): ")

    else:
        result_key, result_bool = check_resources(request.lower())

        if request.lower() == "off":
            break

        if not result_bool:
            print(f"Sorry there is not enough {result_key}")
        else:
            print("Please insert coins.")
            total += int(input("    How many quarters: ")) * 0.25
            total += int(input("    How many dimes: ")) * 0.10
            total += int(input("    How many nickles: ")) * 0.05
            total += int(input("    How many pennies: ")) * 0.01

            if request.lower() == "espresso":
                if total >= MENU[request.lower()]['cost']:
                    serve_coffee("espresso")
                else:
                    print("Sorry that's not enough money. Money refunded.")

            elif request.lower() == "latte":
                if total >= MENU[request.lower()]['cost']:
                    serve_coffee("latte")
                else:
                    print("Sorry that's not enough money. Money refunded.")

            elif request.lower() == "cappuccino":
                if total >= MENU[request.lower()]['cost']:
                    serve_coffee("cappuccino")
                else:
                    print("Sorry that's not enough money. Money refunded.")
