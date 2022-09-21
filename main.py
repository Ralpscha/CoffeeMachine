from menu import MENU, resources



# TODO: create report
def create_report():
    global total_revenue
    global water
    global milk
    global coffee

    print("dit is het rapport")
    print(f"We've got ${total_revenue} in the register")
    print(f"""
    Current resources are: 
    Water:  {water} ml
    Milk:   {milk}  ml
    Coffee: {coffee}g
""")

# TODO: give the price


def give_price(product):
    match product:
        case 'espresso':
            price = 1.5
        case 'latte':
            price = 2.0
        case 'cappuccino':
            price = 2.50
        case _:
            price = 0
    return price


def give_menu_price(product):
    return MENU[product]['cost']


def showdict():
    for item in MENU:
        print(MENU[item]['cost'])


# TODO receive money
def receive_money(price):
    global total_revenue
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    received_amount = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    if received_amount < price:
        print(f"Sorry ${received_amount} is not enough money. Money refunded.")
        return False
    elif received_amount > price:
        print(f"Here is ${round((received_amount - price), 2)} in change")
        total_revenue += price
        return True
    elif received_amount == price:
        print(f"Received ${received_amount} and that is the {price}.")
        total_revenue += price
        return True


def make_order(product):
    global water_available
    print(f"Our kitchen tries to make {product}, uno momento !")
    print(f"Ingredients needed: {MENU[product]['ingredients']} ")
    water_needed = MENU[product]['ingredients']['water']
    print(f"Water needed: {water_needed}, available = {water_available}")
    if water_needed > water_available:
        price = MENU[product]['costs']
        print(f"Water supply too low. Can't make order, refund money: {price}")
    else:
        print(f"enough water for {product}, enjoy!")
        water_available -= water_needed
        print(f"remaining water = {water_available}.")




total_revenue = 0
machine_on = True
water_available = resources['water']
milk_available = resources['milk']
coffee_available = resources['coffee']

# print(water, milk, coffee)

while machine_on:
    wens = input("What would you like? (espresso/latte/cappuccino): ")
    price = give_menu_price(wens)
    match wens:
        case 'off':
            machine_on = False
            print("Turning off the machine.")
        case 'report':
            create_report()
        case 'espresso':
            # price = give_price(wens)
            # print(f"The price is {price}")

            print(f"The menu price is {price:.2f}")
            if receive_money(price):
                print("money ok, let's brew some coffee")
                # cust_func_name = "make_" + wens
                # print(cust_func_name)
                # cust_func = locals()['make_' + wens]
                # cust_func(wens)
                make_order(wens)
            else:
                print("money not ok, next customer")


# showdict()