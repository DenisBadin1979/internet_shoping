def test_product_init(product):
    assert product.name == "Продукт_Тест"
    assert product.description == "Описание продукта_тест"
    assert product.price == 1.3
    assert product.quantity == 5
