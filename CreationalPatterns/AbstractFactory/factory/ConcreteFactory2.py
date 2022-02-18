from factory.AbstractFactory import AbstractFactory
from productA.AbstractProductA import AbstractProductA
from productA.ConcreteProductA2 import ConcreteProductA2
from productB.AbstractProductB import AbstractProductB
from productB.ConcreteProductB2 import ConcreteProductB2

class ConcreteFactory2(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """
    def create_product_a(self)-> AbstractProductA:
        return ConcreteProductA2()
    
    def create_product_b(self)-> AbstractProductB:
        return ConcreteProductB2()