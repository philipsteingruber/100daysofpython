from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    running = True
    while running:
        order = input('What would you like? (espresso/latte/cappuccino/) ').casefold()

        if order == 'off':
            running = False
        elif order == 'report':
            coffee_maker.report()
            money_machine.report()
        elif order in menu.get_items().split('/'):
            drink = menu.find_drink(order)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print('Invalid order.')


if __name__ == '__main__':
    main()