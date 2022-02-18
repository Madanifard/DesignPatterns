from productB.AbstractProductB import AbstractProductB
from productA.AbstractProductA import AbstractProductA

class ConcreateProductB1(AbstractProductB):

    def useful_function_b(self)-> str:
        return "The result of the product B1."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"
