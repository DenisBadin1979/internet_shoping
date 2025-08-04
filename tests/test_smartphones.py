import pytest


def test_smartphone_init1(smartphone_one):
    assert smartphone_one.name == "Phone 1"
    assert smartphone_one.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_one.price == 1.0
    assert smartphone_one.quantity == 5
    assert smartphone_one.efficiency == 95.5
    assert smartphone_one.model == "S23 Ultra"
    assert smartphone_one.memory == 256
    assert smartphone_one.color == "Серый"


def test_smartphone_init2(smartphone_two):
    assert smartphone_two.name == "Phone 2"
    assert smartphone_two.description == "Описания нет"
    assert smartphone_two.price == 5.0
    assert smartphone_two.quantity == 10
    assert smartphone_two.efficiency == 950.5
    assert smartphone_two.model == "Раскладушка"
    assert smartphone_two.memory == 512
    assert smartphone_two.color == "Желтый"


def test_smartphones_add(smartphone_one, smartphone_two):
    assert (smartphone_one + smartphone_two) == 55.0


def test_smartphones_add_error(smartphone_one, smartphone_two):
    with pytest.raises(TypeError):
        smartphone_one + 1
