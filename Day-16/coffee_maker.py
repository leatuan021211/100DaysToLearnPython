class CoffeeMaker:
    """Models the machine that makes the coffee"""
    
    def __init__(self):
        self.resources = {
            "water": 1000,
            "milk": 1000,
            "coffee": 200,
        }
        
    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")    
        
    def is_resource_sufficent(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in drink:
            if drink[item] >= self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True
    
    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
            
        print(f"Here is your {order.name}")