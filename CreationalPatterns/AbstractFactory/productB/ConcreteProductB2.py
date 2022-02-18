from productB.AbstractProductB import AbstractProductB
from productA.AbstractProductA import AbstractProductA

class ConcreteProductB2(AbstractProductB):

    def useful_function_b(self)-> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        The variant, Product B2, is only able to work correctly with the
        variant, Product A2. Nevertheless, it accepts any instance of
        AbstractProductA as an argument.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"