from abc import ABC, abstractmethod

class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def product_part_a(self) -> None:
        pass
    
    @abstractmethod
    def product_part_b(self) -> None:
        pass

    @abstractmethod
    def product_part_c(self) -> None:
        pass