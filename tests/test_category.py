def test_category_init(first_category):
    assert first_category.name == "Категория 1"
    assert first_category.description == "Описание категории 1"
    assert first_category.poducts_in == ["prod1", "prod2"]
    assert first_category.category_count == 1
    assert first_category.product_count == 2


def test_category_init2(second_category):
    assert second_category.name == "Категория 2"
    assert second_category.description == "Описание категории 2"
    assert second_category.poducts_in == ["prod3", "prod4"]
    assert second_category.category_count == 2
    assert second_category.product_count == 2


def test_category_products_property(three_category):
    assert three_category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"


def test_add_product_setter(three_category, product):
    assert len(three_category.poducts_in) == 1
    three_category.add_product = product
    assert len(three_category.poducts_in) == 2
