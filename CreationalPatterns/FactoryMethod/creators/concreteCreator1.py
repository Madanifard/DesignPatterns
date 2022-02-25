from creators.creator import Creator
from products.product import Product
from products.concreteProduct1 import ConcreteProduct1

class ConcreteCreator1(Creator):
    """
    Concrete Creators override the factory method in order to change the resulting
    product's type.
    """
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()