from abc import ABC, abstractmethod
from typing import Self


class BatProduct(ABC):
    """Абстрактный класс для класса Продукты, смартфоны, трава газонная"""

    @classmethod
    @abstractmethod
    def new_product(cls, prod_dict: dict) -> Self:
        pass
