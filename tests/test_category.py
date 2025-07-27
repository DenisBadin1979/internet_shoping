def test_category_init(first_category):
    assert first_category.name == "Категория 1"
    assert first_category.description == "Описание категории 1"
    assert first_category.products == ["prod1", "prod2"]
    assert first_category.category_count == 1
    assert first_category.product_count == 2


def test_category_init2(second_category):
    assert second_category.name == "Категория 2"
    assert second_category.description == "Описание категории 2"
    assert second_category.products == ["prod3", "prod4"]
    assert second_category.category_count == 2
    assert second_category.product_count == 2
