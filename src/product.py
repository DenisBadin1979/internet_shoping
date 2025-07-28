from typing import Any


class Product:
    """Класс предоставления продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса."""
        """Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, prod_dict: dict) -> None | Any:
        """Вызываем класс-метод для добавления нового продукта"""
        name = prod_dict.get("name")
        description = prod_dict.get("description")
        price = prod_dict.get("price")
        quantity = prod_dict.get("quantity")
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для вызова приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для установления цены, но нен ниже 0"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price
