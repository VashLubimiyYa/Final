import abc


class CoffeeMachine(abc.ABC):
    #Abstract base class for the coffee machine

    def __init__(self, bean_type):
        self.bean_type = bean_type

    def make_coffee(self):
        raise NotImplementedError

class EspressoMachine(CoffeeMachine):
    #Concrete class for making espresso

    def make_coffee(self):
        print(f"Making espresso with {self.bean_type} beans")

class AmericanoMachine(CoffeeMachine):
    #Concrete class for making americano

    def make_coffee(self):
        print(f"Making americano with {self.bean_type} beans")




#Adapter
class CoffeeMachineAdapter(CoffeeMachine):
    #Adapter class to adapt any coffee machine to a generic interface

    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine

    def make_coffee(self):
        self.coffee_machine.make_coffee()




#Singleton
class CoffeeMachineSingleton:
    #Singleton class to ensure only one coffee machine instance exists

    _instance = None

    def __new__(cls, bean_type):
        if cls._instance is None:
            cls._instance = super().__new__(cls, bean_type)
        return cls._instance




#Strategy
class CoffeeMakingStrategy:
    #Abstract base class for coffee making strategies

    def make_coffee(self, coffee_machine):
        raise NotImplementedError
    
class EspressoStrategy(CoffeeMakingStrategy):
    #Concrete strategy for making espresso

    def make_coffee(self, coffee_machine):
        coffee_machine.make_coffee()

class AmericanoStrategy(CoffeeMakingStrategy):
    #Concrete strategy for making americano

    def make_coffee(self, coffee_machine):
        coffee_machine.make_coffee()




#Factory
class CoffeeMachineFactory:
    #Factory class to create coffee machines based on bean type

    def create_coffee_machine(self, bean_type):
        if bean_type == "espresso":
            return EspressoMachine(bean_type)
        elif bean_type == "americano":
            return AmericanoMachine(bean_type)
        else:
            raise ValueError(f"Invalid bean type: {bean_type}")




#Decorator
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





#Observer
class CoffeeMachineObserver:
    #Observer class to be notified when coffee is made

    def update(self, coffee_machine):
        print(f"Coffee is ready: {coffee_machine.bean_type}")





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

