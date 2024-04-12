import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestIngredient:
    # тест: метод get_type + параметр type
    @pytest.mark.parametrize("valid_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_ingredient_type_is_correct(self, valid_type):
        ingredient = Ingredient(valid_type, "some_ingredient", 100)
        assert ingredient.get_type() == valid_type

    # тест: метод get_name + параметр name
    def test_ingredient_name_is_correct(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "some_ingredient", 100)
        assert ingredient.get_name() == "some_ingredient"

    # тест: метод get_price + параметр price
    def test_ingredient_price_is_correct(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "some_ingredient", 100)
        assert ingredient.get_price() == 100

