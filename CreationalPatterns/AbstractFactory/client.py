from factory.AbstractFactory import AbstractFactory
from factory.ConcreteFactory1 import ConcreteFactory1
from factory.ConcreteFactory2 import ConcreteFactory2

def client_code(factory: AbstractFactory)-> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    

    product_b = factory.create_product_b()
    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == '__main__':
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")
    
    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())