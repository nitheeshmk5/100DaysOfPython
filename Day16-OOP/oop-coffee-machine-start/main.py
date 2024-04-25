from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachine = MoneyMachine()
coffeMaker = CoffeeMaker()
menu = Menu()

again = True

while again:
    options = menu.get_items()
    choice = input(f"What you like ? ({options}) : ")
    if choice == "off":
        again = False
    elif choice == "report":
        coffeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeMaker.make_coffee(drink)

