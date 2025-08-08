from src.grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product(name="Продукт_Тест", description="Описание продукта_тест", price=1.3, quantity=5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Продукт_Тест, Описание продукта_тест, 1.3, 5"

    Smartphone(
        name="Phone 2",
        description="Описания нет",
        price=5.0,
        quantity=10,
        efficiency=950.5,
        model="Раскладушка",
        memory=512,
        color="Желтый",
    )
    message = capsys.readouterr()
    assert (message.out.strip()) == "Smartphone(Phone 2, Описания нет, 5.0, 10"

    LawnGrass("Газонная трава 2", "Выносливая трава", 100.0, 200, "США", "5 дней", "Темно-зеленый")
    message = capsys.readouterr()
    assert (message.out.strip()) == "LawnGrass(Газонная трава 2, Выносливая трава, 100.0, 200"
