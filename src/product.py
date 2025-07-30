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

    def __str__(self):
        """Строковое отображение в следующем виде"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        p1 = self.__price * self.quantity
        p2 = other.__price * other.quantity
        return p1 + p2
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

if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # print(str(product1))
    # print(str(product2))
    # print(str(product3))

    # print(product1 + product2)
    # print(product1 + product3)
    # print(product2 + product3)