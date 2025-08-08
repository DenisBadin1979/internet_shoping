from src.product import Product


class Smartphone(Product):
    """Класс «Смартфон» (Smartphone ) наследник класса Product. Инициализируем расширен атрибутами: производительность,
    модель, объем встроенной памяти, цвет."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: int, color: str
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Product") -> float:
        """Вычисление суммы стоимости всех товаров в классе"""

        if type(other) is Smartphone:
            p1 = self.price * self.quantity
            p2 = other.price * other.quantity
            return p1 + p2
        raise TypeError
