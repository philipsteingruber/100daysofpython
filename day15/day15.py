from menu import MENU

resources = {
    "water": {
        'friendly_name': 'Water',
        'unit': 'ml',
        'amount': 300
    },
    "milk": {
        'friendly_name': 'Milk',
        'unit': 'ml',
        'amount': 200
    },
    "coffee": {
        'friendly_name': 'Coffee beans',
        'unit': 'g',
        'amount': 100
    },
    "money": {
        'friendly_name': 'Money',
        'unit': 'dollars',
        'amount': 0
    },
}


def print_report():
    for resource in resources.values():
        friendly_name = resource['friendly_name']
        unit = resource['unit']
        amount = resource['amount']

        print(f'{friendly_name}: {amount} {unit}')


def sufficient_resources(drink: str) -> bool:
    if resources['water']['amount'] < MENU[drink]['ingredients']['water']:
        print('Insufficient water.')
        return False
    elif resources['coffee']['amount'] < MENU[drink]['ingredients']['coffee']:
        print('Insufficient coffee.')
        return False
    elif drink != 'espresso' and resources['milk']['amount'] < MENU[drink]['ingredients']['milk']:
        print('Insufficient milk.')
        return False
    else:
        return True


def process_coins() -> float:
    money_inserted: float = 0
    money_inserted += int(input('Number of quarters: ')) * 0.25
    money_inserted += int(input('Number of dimes: ')) * 0.10
    money_inserted += int(input('Number of nickels: ')) * 0.05
    money_inserted += int(input('Number of pennies: ')) * 0.01

    return money_inserted


def transaction_successful(money_inserted: float, drink_price: float) -> bool:
    return money_inserted >= drink_price


def process_transaction(money_inserted: float, drink_price: float) -> None:
    print(f'Change: {round(money_inserted-drink_price, 2)}')
    resources['money']['amount'] += drink_price


def make_drink(drink: str):
    resources['water']['amount'] -= MENU[drink]['ingredients']['water']
    resources['coffee']['amount'] -= MENU[drink]['ingredients']['coffee']

    if drink != 'espresso':
        resources['milk']['amount'] -= MENU[drink]['ingredients']['milk']

    print(f"Here's your {drink}!")


def main():
    while True:
        request = input('What would you like? ').casefold()

        if request == 'off':
            print('Turning off.')
            break
        elif request == 'report':
            print_report()
        elif request in MENU.keys():
            if sufficient_resources(request):
                money_inserted = process_coins()
                if transaction_successful(money_inserted, MENU[request]['cost']):
                    process_transaction(money_inserted, MENU[request]['cost'])
                    make_drink(request)


if __name__ == '__main__':
    main()
