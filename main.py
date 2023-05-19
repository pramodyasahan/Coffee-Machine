class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0,
        }
        self.menu = {
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

    def report(self):
        print(f"    Water: {self.resources['water']}ml")
        print(f"    Milk: {self.resources['milk']}ml")
        print(f"    Coffee: {self.resources['coffee']}g")
        print(f"    Money: ${self.resources['money']}")

    def check_resources(self, coffee):
        for item, amount in self.menu[coffee]["ingredients"].items():
            if self.resources[item] < amount:
                print(f"Sorry there is not enough {item}")
                return False
        return True

    def manage_resources(self, coffee):
        for item, amount in self.menu[coffee]["ingredients"].items():
            self.resources[item] -= amount

    def process_coins(self):
        print("Please insert coins.")
        total = int(input("    How many quarters? ")) * 0.25
        total += int(input("    How many dimes? ")) * 0.10
        total += int(input("    How many nickles? ")) * 0.05
        total += int(input("    How many pennies? ")) * 0.01
        return total

    def serve_coffee(self, coffee):
        total = self.process_coins()
        if total >= self.menu[coffee]['cost']:
            change = total - self.menu[coffee]['cost']
            print(f"Here is ${round(change, 2)} in change.")
            self.resources['money'] += self.menu[coffee]['cost']
            print(f"Here is your {coffee} ☕️. Enjoy!")
            self.manage_resources(coffee)
        else:
            print("Sorry that's not enough money.Money refunded.")

    def run(self):
        while True:
            request = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
            if request == "report":
                self.report()
            elif request in self.menu.keys():
                if self.check_resources(request):
                    self.serve_coffee(request)
            elif request == "off":
                break
            else:
                print("Invalid input. Please enter espresso, latte or cappuccino.")


# CreatingCoffee Machine Instance
coffeeMachine = CoffeeMachine()
coffeeMachine.run()
