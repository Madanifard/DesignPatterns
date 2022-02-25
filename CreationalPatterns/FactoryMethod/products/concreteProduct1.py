from products.product import Product

class ConcreteProduct1(Product):
    """
    Concrete Products provide various implementations of the Product interface.
    """
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"