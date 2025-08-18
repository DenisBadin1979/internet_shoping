import pytest


def test_init_grass1(grass_one):
    assert grass_one.name == "Газонная трава"
    assert grass_one.description == "Элитная трава для газона"
    assert grass_one.price == 500.00
    assert grass_one.quantity == 20
    assert grass_one.country == "Россия"
    assert grass_one.germination_period == "7 дней"
    assert grass_one.color == "Зеленый"


def test_init_grass2(grass_two):
    assert grass_two.name == "Газонная трава 2"
    assert grass_two.description == "Выносливая трава"
    assert grass_two.price == 100.00
    assert grass_two.quantity == 200
    assert grass_two.country == "США"
    assert grass_two.germination_period == "5 дней"
    assert grass_two.color == "Темно-зеленый"


def test_grass_add(grass_one, grass_two):
    assert (grass_one + grass_two) == 30000.0


def test_grass_add_error(grass_one, grass_two):
    with pytest.raises(TypeError):
        grass_one + 1
