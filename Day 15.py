from Tools.scripts.summarize_stats import TOTAL

menu = {

    "espresso": {
        "ingredients": {
            "water": 50,
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100

}
def is_resources_sufficient(order_ingredients):
    """Returns True when order can pe placed"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False                                        #is_enough = False
    return True    # is_enough = True
def process_coins():
    """ Return the total calculated from the coins inserted."""
    print("Insert coins.")
    total =  int(input (f"How many quarters? :")) *0.25
    total += int(input(f"How many dimes? :")) *0.1
    total += int(input(f"How many nickles? :") ) *0.05
    total += int(input(f"How many pennies? :") ) *0.01
    return total

def is_transaction(money_received , drink_cost):
    """ Return True when payment is accepted otherwise False. """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost ,2)
        print(f"Here is  ${change} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Money not sufficient! Money refunded.")
        return False

def make_coffee(drink_name,ordered_ingredients):
    """ Deduct the required ingredients from the resources."""
    for item in ordered_ingredients:
        resources[item] -= ordered_ingredients[item]
        print(f"Here is your {drink_name}. Enjoy!")



is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{ resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffe:{resources['coffee']}g")
        print(f"money:{profit}")
    else:
        drink = menu[choice]
        print(drink)
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])





















