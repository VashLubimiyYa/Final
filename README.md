Abstract Base Class (ABC): The CoffeeMachine class is an abstract base class that defines the basic functionality of a coffee machine. It has an abstract method make_coffee() that must be implemented by subclasses.


import abc
class CoffeeMachine(abc.ABC):
    #Abstract base class for the coffee machine

    def __init__(self, bean_type):
        self.bean_type = bean_type

    def make_coffee(self):
        raise NotImplementedError





Concrete Classes: The EspressoMachine and AmericanoMachine classes are concrete subclasses of CoffeeMachine. They implement the make_coffee() method to make espresso and americano, respectively.

class EspressoMachine(CoffeeMachine):
    #Concrete class for making espresso

    def make_coffee(self):
        print(f"Making espresso with {self.bean_type} beans")

class AmericanoMachine(CoffeeMachine):
    #Concrete class for making americano

    def make_coffee(self):
        print(f"Making americano with {self.bean_type} beans")





Adapter: The CoffeeMachineAdapter class is an adapter that allows any coffee machine to be used with a generic interface. It takes a coffee_machine object as an argument and implements the make_coffee() method to call the make_coffee() method of the underlying coffee machine.

class CoffeeMachineAdapter(CoffeeMachine):
    #Adapter class to adapt any coffee machine to a generic interface

    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine

    def make_coffee(self):
        self.coffee_machine.make_coffee()





Singleton: The CoffeeMachineSingleton class is a singleton class that ensures only one instance of a coffee machine exists. It uses a private variable _instance to store the single instance and a custom __new__() method to control object creation.

class CoffeeMachineSingleton:
    #Singleton class to ensure only one coffee machine instance exists

    _instance = None

    def __new__(cls, bean_type):
        if cls._instance is None:
            cls._instance = super().__new__(cls, bean_type)
        return cls._instance





Strategy: The CoffeeMakingStrategy class is an abstract base class for coffee making strategies. It has an abstract method make_coffee() that must be implemented by subclasses.

#Strategy
class CoffeeMakingStrategy:
    #Abstract base class for coffee making strategies

    def make_coffee(self, coffee_machine):
        raise NotImplementedError





Concrete Strategies: The EspressoStrategy and AmericanoStrategy classes are concrete subclasses of CoffeeMakingStrategy. They implement the make_coffee() method to use the appropriate coffee machine to make espresso or americano.
    
class EspressoStrategy(CoffeeMakingStrategy):
    #Concrete strategy for making espresso

    def make_coffee(self, coffee_machine):
        coffee_machine.make_coffee()

class AmericanoStrategy(CoffeeMakingStrategy):
    #Concrete strategy for making americano

    def make_coffee(self, coffee_machine):
        coffee_machine.make_coffee()





Factory: The CoffeeMachineFactory class is a factory class that creates coffee machines based on bean type. It takes a bean_type argument and returns an instance of either EspressoMachine or AmericanoMachine.

class CoffeeMachineFactory:
    #Factory class to create coffee machines based on bean type

    def create_coffee_machine(self, bean_type):
        if bean_type == "espresso":
            return EspressoMachine(bean_type)
        elif bean_type == "americano":
            return AmericanoMachine(bean_type)
        else:
            raise ValueError(f"Invalid bean type: {bean_type}")





Decorator: The MilkDecorator and SugarDecorator classes are decorators that add milk or sugar to coffee. They take a coffee_machine object as an argument and override the get_name() method to return the name of the decorated coffee.

class MilkDecorator(CoffeeMachine):

    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine
    def get_name(self):
        return self.coffee_machine.get_name() + " with milk"
    
class SugarDecorator(CoffeeMachine):

    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine
    def get_name(self):
        return self.coffee_machine.get_name() + " with sugar"





Observer: The CoffeeMachineObserver class is an observer class that is notified when coffee is made. It implements the update() method to print a message indicating that the coffee is ready.

class CoffeeMachineObserver:
    #Observer class to be notified when coffee is made

    def update(self, coffee_machine):
        print(f"Coffee is ready: {coffee_machine.bean_type}")





The main function of the code prompts the user to select a coffee and then prompts the user to select components (milk, sugar, or both). It then creates a coffee machine based on the user's selections and decorates it with the chosen components. Finally, it calls the make_coffee() method of the decorated coffee machine to make the coffee.

def choose_coffee():

    print("Select your coffee:")
    print("1. Espresso")
    print("2. Americano")
    coffee_choice = int(input("Enter your choice: "))

    if coffee_choice == 1:
        choose_components()
    elif coffee_choice == 2:
        choose_components()
    else:
        print("Invalid coffee choice")
        return None


def choose_components():

    print("Select components:")
    print("1. milk")
    print("2. sugar")
    print("3. both")
    components_choice = int(input )

    if components_choice == 1:
        return MilkDecorator(CoffeeMachine)
    elif components_choice == 2:
        return SugarDecorator(CoffeeMachine)
    elif components_choice == 3:
        return SugarDecorator(MilkDecorator(CoffeeMachine))
    else:
        print("Invalid components choice")
        return None


def main():


    decorated_coffee_machine = choose_components()
    if decorated_coffee_machine is not None:
        decorated_coffee_machine.make_coffee()
    else:
        print("Invalid selection")
if __name__ == "__main__":

    main()
