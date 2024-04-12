import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from praktikum.burger import Burger


@pytest.fixture(scope="function")
def burger_get_receipt_mock_data():
    mock_test_data = {"bun": "mock bun",
                      "filling_type": "filling",
                      "ingredient": "mock ingredient",
                      "price": 500}
    return mock_test_data


@pytest.fixture(scope="function")
def mock_bun():
    mock_bun = Mock(name="mock bun", price=100)
    return mock_bun


@pytest.fixture(scope="function")
def mock_ingredient():
    mock_ingredient = Mock(type=INGREDIENT_TYPE_FILLING, name="mock ingredient", price=150)
    return mock_ingredient


@pytest.fixture(scope="function")
def mock_sauce():
    mock_sauce = Mock(type=INGREDIENT_TYPE_SAUCE, name="mock sauce", price=50)
    return mock_sauce


@pytest.fixture(scope="function")
def burger_sample():
    burger = Burger()
    burger.set_buns(Bun("high-protein", 250))
    burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "kotletka", 100))
    return burger
