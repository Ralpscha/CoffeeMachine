from menu import MENU, resources


# TODO: create report
def create_report():
    global total_revenue
    global water_available
    global milk_available
    global coffee_available

    print("dit is het rapport")
    print(f"We've got ${total_revenue:.2f} in the register")
    print(f"""
    Current resources are: 
    Water:  {water_available} ml
    Milk:   {milk_available}  ml
    Coffee: {coffee_available}g
""")

# TODO: give the price


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
        print(f"Sorry ${received_amount:.2f} is not enough money. Money refunded.")
        return False
    elif received_amount > price:
        print(f"Here is ${(received_amount - price):.2f} in change")
        total_revenue += price
        return True
    elif received_amount == price:
        print(f"Received ${received_amount:.2f} and that is the ${price:.2f}.")
        total_revenue += price
        return True


def make_order(product):
    global water_available
    global milk_available
    global coffee_available
    global total_revenue
    print(f"Our kitchen tries to make {product}, uno momento !")

    water_needed = MENU[product]['ingredients']['water']
    milk_needed = MENU[product]['ingredients']['milk']
    coffee_needed = MENU[product]['ingredients']['coffee']
    print(f"Ingredients needed: {water_needed}ml water, {milk_needed}ml milk, {coffee_needed}gr coffee. ")
    print(f"Ingredients available: {water_available}ml water, {milk_available}ml milk, {coffee_available}gr coffee. ")

    if water_needed > water_available or milk_needed > milk_available or coffee_needed > coffee_available:
        price = MENU[product]['cost']
        print(f"Ingredients supply too low. Can't make order, refund money: {price:.2f}")
        total_revenue -= price
    else:
        print(f"enough ingredients for {product}, enjoy!\n")
        water_available -= water_needed
        milk_available -= milk_needed
        coffee_available -= coffee_needed
        print(f"remaining ingredients = {water_available}ml water, {milk_available}ml milk, {coffee_available}gr coffee.\n")


total_revenue = 0
machine_on = True
water_available = resources['water']
milk_available = resources['milk']
coffee_available = resources['coffee']

# print(water, milk, coffee)

while machine_on:
    wens = input("What would you like? (espresso/latte/cappuccino): ")


    match wens:
        case 'off':
            machine_on = False
            print("Turning off the machine.")
        case 'report':
            create_report()
        case _:
            # price = give_menu_price(wens)
            price = MENU[wens]['cost']
            print(f"The menu price is ${price:.2f}")
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