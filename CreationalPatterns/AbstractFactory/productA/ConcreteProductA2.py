from productA.AbstractProductA import AbstractProductA

class ConcreteProductA2(AbstractProductA):
    """
    Concrete Products are created by corresponding Concrete Factories.
    """
    def useful_function_a(self)-> str:
        return "the result of the product A2"