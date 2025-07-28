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
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
