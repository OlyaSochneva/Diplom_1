import pytest
from praktikum.burger import Burger
from unittest.mock import patch

from assistant_methods import check_receipt


class TestBurger:
    # тесты метода init:
    def test_burger_init_bun(self):
        burger = Burger()
        assert burger.bun is None

    def test_burger_init_ingredients(self):
        burger = Burger()
        assert burger.ingredients == []

    # тест: метод set_buns c мок-булочкой
    def test_burger_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # тест: метод add_ingredient c мок-ингредиентом
    @patch('praktikum.ingredient.Ingredient')
    def test_burger_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    # тест: метод remove_ingredient c мок-ингредиентом
    def test_burger_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    # тест: метод move_ingredient c мок-ингредиентами
    def test_burger_move_ingredient(self, mock_ingredient, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_sauce)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient

    # тест: метод get_price c моками Bun.get_price и Ingredient.get_price
    @patch("praktikum.ingredient.Ingredient.get_price")
    @patch("praktikum.bun.Bun.get_price")
    def test_burger_get_price(self, mock_bun_get_price, mock_ingredient_get_price, burger_sample):
        mock_bun_get_price.return_value = 100
        mock_ingredient_get_price.return_value = 150
        burger = burger_sample
        price = burger.get_price()
        assert price == 350

    # тест: метод get_receipt с моками Bun.get_name, Ingredient.get_type, Ingredient.get_name и Burger.get_price
    @patch("praktikum.burger.Burger.get_price")
    @patch("praktikum.ingredient.Ingredient.get_name")
    @patch("praktikum.ingredient.Ingredient.get_type")
    @patch("praktikum.bun.Bun.get_name")
    def test_burger_get_receipt(self, mock_bun_get_name, mock_ingredient_get_type, mock_ingredient_get_name,
                                mock_price, burger_get_receipt_mock_data, burger_sample):
        mock_bun_get_name.return_value = burger_get_receipt_mock_data["bun"]
        mock_ingredient_get_type.return_value = burger_get_receipt_mock_data["filling_type"]
        mock_ingredient_get_name.return_value = burger_get_receipt_mock_data["ingredient"]
        mock_price.return_value = burger_get_receipt_mock_data["price"]
        burger = burger_sample
        receipt = burger.get_receipt()
        check = check_receipt(receipt, burger_get_receipt_mock_data)
        assert check == "OK"
