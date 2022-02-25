from itertools import product
from creators.creator import Creator
from products.product import Product
from products.concreteProduct2 import ConcreteProduct2

class ConcreteCreator2(Creator):
    """
    Concrete Creators override the factory method in order to change the resulting
    product's type.
    """
    def factory_method(self) -> product:
        return ConcreteProduct2()