import pytest

from src.category import Category
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
