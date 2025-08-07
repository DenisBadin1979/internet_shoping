from abc import ABC, abstractmethod

class BatProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product (cls, *args, **kwargs):
        pass

