from src.product import Product


class Category:
    """Класс предоставления продукта"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Метод для инициализации экземпляра класса."""
        """Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(products)

    def __str__(self) -> str:
        """Строковое отображение в следующем виде"""
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    @property
    def products(self) -> str:
        """Создаем геттер для вызова атрибута продуктов"""
        prod_str = ""
        for prod in self.__products:
            prod_str += f"{str(prod)}\n"
        return prod_str

    @products.setter
    def products(self, prod: "Product") -> None:
        """Добавляем сеттер для добавление нового атрибута продукты"""
        if isinstance(prod, Product):
            self.__products.append(prod)
            Category.category_count += 1
            Category.product_count = len(self.__products)
        else:
            raise TypeError

    @property
    def products_in(self) -> list:
        """Возвращаем список"""
        return self.__products

    def middle_price(self) -> float:
        """Метод, который вычисляет средний ценник всех товаров"""
        try:
            amount_goods = 0
            amount_quantity = 0
            for i in self.products_in:
                amount_goods += i.price * i.quantity
                amount_quantity += i.quantity
            return round(amount_goods / amount_quantity, 2)
        except ZeroDivisionError:
            return 0.0
