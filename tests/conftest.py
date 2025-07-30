import pytest

from src.category import Category
from src.Category_Iterator import CategoryIterator
from src.product import Product


@pytest.fixture
def first_category():
    return Category(name="Категория 1", description="Описание категории 1", products=["prod1", "prod2"])


@pytest.fixture
def second_category():
    return Category(name="Категория 2", description="Описание категории 2", products=["prod3", "prod4"])


@pytest.fixture
def product():
    return Product(name="Продукт_Тест", description="Описание продукта_тест", price=1.3, quantity=5)


@pytest.fixture
def product1():
    return Product(name="Продукт_Тест", description="Описание продукта_тест", price=1.5, quantity=7)


@pytest.fixture
def three_category():
    return Category(
        name="Категория 1",
        description="Описание категории 1",
        products=[Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)],
    )


@pytest.fixture
def four_category():
    return Category(
        name="Категория 1",
        description="Описание категории 1",
        products=[Product("Samsung ", "25, цвет, 200MP камера", 100000.0, 7)],
    )


@pytest.fixture
def prod_iterator(three_category):
    return CategoryIterator(three_category)
