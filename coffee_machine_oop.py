from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_working = True

while is_working:
    order = menu.get_items()
    user_operation = input(f"What would you like? {order}")
    if user_operation == "off":
        is_working = False
    elif user_operation == "report":
        coffee_maker.report()
        money_machine.report()
        is_working = False
    elif user_operation == 'latte' or user_operation == 'espresso' or user_operation == "cappuccino" :
        drink = menu.find_drink(user_operation)
        if coffee_maker.is_resource_sufficient(drink) is True:
            if money_machine.make_payment(drink.cost) is True:
                coffee_maker.make_coffee(drink)
            else:
                is_working = False
        else:
            is_working = False
    else:
        print("Please choose a correct operation")
        is_working = False