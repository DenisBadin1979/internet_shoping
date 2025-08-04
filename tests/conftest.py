import pytest

from src.category import Category
from src.Category_Iterator import CategoryIterator
from src.grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


@pytest.fixture
def smartphone_one():
    return Smartphone(
        name="Phone 1",
        description="256GB, Серый цвет, 200MP камера",
        price=1.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый",
    )


@pytest.fixture
def smartphone_two():
    return Smartphone(
        name="Phone 2",
        description="Описания нет",
        price=5.0,
        quantity=10,
        efficiency=950.5,
        model="Раскладушка",
        memory=512,
        color="Желтый",
    )


@pytest.fixture
def grass_one():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass_two():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 100.0, 200, "США", "5 дней", "Темно-зеленый")
    #
