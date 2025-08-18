from src.product import Product


class LawnGrass(Product):
    """Класс «Трава газонная» наследник класса Product расширен атрибутами:
    страна-производитель, срок прорастания, цвет"""

    def __init__(
        self, name: str, description: str, price: float, quantity: int, country: str, germination_period: int, color: str
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: "Product") -> float:
        """Вычисление суммы стоимости всех товаров в классе"""

        if type(other) is LawnGrass:
            p1 = self.price * self.quantity
            p2 = other.price * other.quantity
            return p1 + p2
        raise TypeError
