from diresctors.director import Director
from builders.concretebuilder1 import ConcreateBuilder1

if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """
    director = Director()
    builder = ConcreateBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Strandard full feature product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.product_part_a()
    builder.product_part_b()
    builder.product_part_c()
    builder.product.list_parts()

    print("\n")