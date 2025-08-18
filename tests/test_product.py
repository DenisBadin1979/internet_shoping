import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == "Продукт_Тест"
    assert product.description == "Описание продукта_тест"
    assert product.price == 1.3
    assert product.quantity == 5


def test_new_product():
    product = Product("ПродТест", "Описание ПродТест", 1.5, 7)
    product.name = "ПродТест"
    product.description = "Описание ПродТест"
    product.price = 1.5
    product.quantity = 7


def test_price_new(capsys, product):
    product.price = -100
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_products_str(product):
    assert str(product) == "Продукт_Тест, 1.3 руб. Остаток: 5 шт."


def test_products_add(product, product1):
    assert (product + product1) == 17.0


def test_iterator_category(prod_iterator):
    assert prod_iterator.index == 0
    assert next(prod_iterator).name == "Samsung Galaxy S23 Ultra"
    with pytest.raises(StopIteration):
        next(prod_iterator)
