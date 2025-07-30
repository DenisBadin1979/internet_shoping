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

    @property
    def products(self):
        """Создаем геттер для вызова атрибута продкутов"""
        prod_str = ""
        for prod in self.__products:
            prod_str += f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
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
