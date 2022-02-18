from factory.AbstractFactory import AbstractFactory
from productA.AbstractProductA import AbstractProductA 
from productA.ConcreteProductA1 import ConcreteProductA1
from productB.AbstractProductB import AbstractProductB 
from productB.ConcreteProductB2 import ConcreteProductB2

class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()