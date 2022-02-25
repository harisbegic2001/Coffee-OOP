from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
moneymachine = MoneyMachine()
coffemaker = CoffeeMaker()
while True:
    unos = input(f"What would you like? {menu.get_items()}: ").lower()
    
    if unos == "report":
        moneymachine.report()
        coffemaker.report()       
            
    if unos == "off":
        print("Machine is turning off")
        break
    
    if unos == "espresso":
        izbor = menu.find_drink(unos)
        if not coffemaker.is_resource_sufficient(izbor):
            print("Not enough resources :(")
        else:
            
            if not moneymachine.make_payment(izbor.cost):
                print("Insufficient amount, you will get refund")

            else:
                coffemaker.make_coffee(izbor)
                
            
            
        

    elif unos == "latte":
        izbor = menu.find_drink(unos)
        if not coffemaker.is_resource_sufficient(izbor):
            print("Not enough resources :(")
        else:
            
            if not moneymachine.make_payment(izbor.cost):
                print("Insufficient amount, you will get refund")

            else:
                coffemaker.make_coffee(izbor)
        

    elif unos == "cappuccino":
        izbor = menu.find_drink(unos)
        if not coffemaker.is_resource_sufficient(izbor):
            print("Not enough resources :(")
        else:
            
            if not moneymachine.make_payment(izbor.cost):
                print("Insufficient amount, you will get refund")

            else:
                coffemaker.make_coffee(izbor)
    