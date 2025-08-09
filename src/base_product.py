from abc import ABC, abstractmethod


class BatProduct(ABC):
    """Абстрактный класс для класса Продукты, смартфоны, трава газонная"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
