from coffee_machine_logo import  logo
from coffee_machine_menu import menu, resources

amount = 0

def coffee_machine():

    def check_resources(order_ingredients):
        """ For checking resources if it's sufficient for the order or not"""
        for ingredient in order_ingredients:
            if order_ingredients[ingredient] > resources[ingredient]:
                print(f"Sorry, {ingredient} is too low to for your current order.")
                return False
        return True

    def process_coin():
        """ For checking the amount buyer inserted or has for the coffee"""
        print("Please insert coin.")
        total = 0
        coins_ten = int(input("How many $10 coins do you have?:  "))
        coins_five = int(input("How many $5 coins do you have?:  "))
        coins_one = int(input("How many $1 coins do you have?:  "))
        total = (coins_ten * 10)  + (coins_five * 5) + (coins_one * 1) + total
        return total

    def make_coffee(coffee_name, coffee_ingredient):
        """ For making a coffee  if  the payment is successful"""
        for items in coffee_ingredient:
            resources[items] -= coffee_ingredient[items]
        print(f"Here is your coffee {coffee_name}. Do enjoy and give feedback.")


    def is_payment_successful(money_received, coffee_cost):
        """ Check if payment is successful"""
        if money_received >= coffee_cost:
            global amount
            amount += coffee_cost
            change =  money_received - coffee_cost
            print("Payment is successful.")
            print(f"Your payment is more than the {buyers_choice} cost, here is your ${round(change,2)} balance")
            return True
        elif money_received < coffee_cost:
            print(f"Sorry, you inserted ${money_received} and it isn't enough money for your order.Money is refunded")
            return False
        return None


    def go_ahead():
        """ Used to know if the user wants to continue with the purchase or not """
        ahead = input("Would you like to go ahead? Y/N\n").lower()
        if ahead == "y":
            if check_resources(coffee_type["ingredients"]):
                payment = process_coin()
                if is_payment_successful(payment, coffee_type["cost"]):
                    make_coffee(buyers_choice, coffee_type["ingredients"])
        else:
            print("Thank you for shopping!")
        return


    choice = True
    print(logo)
    while choice:
        buyers_choice = input("What will you like to have? Latte, Espresso, Chocolate or Cappuccino?\n").lower()
        if buyers_choice == "latte":
            coffee_type = menu[buyers_choice]
            print(f"Latte cost {coffee_type["cost"]}")
            go_ahead()
        elif buyers_choice == "chocolate":
            coffee_type = menu[buyers_choice]
            print(f"Chocolate cost {coffee_type["cost"]}")
            go_ahead()
        elif buyers_choice == "espresso":
            coffee_type = menu[buyers_choice]
            print(f"Espresso cost {coffee_type["cost"]}")
            go_ahead()
        elif buyers_choice == "cappuccino":
            coffee_type = menu[buyers_choice]
            print(f"Cappuccino cost {coffee_type["cost"]}")
            go_ahead()
        elif buyers_choice == "off":
            choice = False
        elif buyers_choice == "report":
            print(f"Water is {resources['water']}ml")
            print(f"Milk is {resources['milk']}ml")
            print(f"Coffee is {resources['coffee']}ml")
            print(f"Cocoa is {resources['cocoa']}ml")
            print(f" Total amount  is $ {amount}")
        elif buyers_choice == "exit":
            quit()


coffee_machine()