from src.base_product import BatProduct
from src.print_mixin import PrintMixin


class Product(BatProduct, PrintMixin):
    """Класс предоставления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса."""
        """Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError(
                "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
            )
        super().__init__()

    def __str__(self) -> str:
        """Строковое отображение в следующем виде"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Вычисление суммы стоимости всех товаров"""
        if type(other) is Product:
            p1 = self.__price * self.quantity
            p2 = other.__price * other.quantity
            return p1 + p2
        raise TypeError

    @classmethod
    def new_product(cls, prod_dict: dict) -> "Product":
        """Вызываем класс-метод для добавления нового продукта"""
        name = prod_dict.get("name", "")
        description = prod_dict.get("description", "")
        price = prod_dict.get("price", 0.00)
        quantity = prod_dict.get("quantity", 0)
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для вызова приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для установления цены, но нен ниже 0"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price
