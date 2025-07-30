from src.product import Product


class Category:
    """Класс предоставления продукта"""

    category_count = 0
    product_count = 0
    name: str
    description: str
    products: list

    def __init__(self, name: str, description: str, products: list) -> None:
        """Метод для инициализации экземпляра класса."""
        """Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(products)

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self.__products)} шт.'

    @property
    def products(self):
        """Создаем геттер для вызова атрибута продуктов"""
        prod_str = ""
        for prod in self.__products:
            prod_str += f"{str(prod)}\n"
        return prod_str

    @products.setter
    def products(self, prod):
        """Добавляем сеттер для добавление нового атрибута продукты"""
        self.__products.append(prod)
        Category.category_count += 1
        Category.product_count = len(self.__products)

    @property
    def products_in(self):
        """Возвращаем список"""
        return self.__products


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3, product4]
    )

    # print(str(category1))
    print(category1.products)