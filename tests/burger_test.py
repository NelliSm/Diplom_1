import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_burger_init(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

    def test_add_ingredient(self, burger):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self, burger):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger):
        bun = Bun("black bun", 100)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        burger.add_ingredient(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.move_ingredient(2, 1)
        assert burger.ingredients == [bun, filling, sauce]

    def test_get_price(self, burger):
        bun = Bun("black bun", 100)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        assert burger.get_price() == 500

    def test_get_price_with_mocks(self, burger):
        bun_mock = Mock()
        bun_mock.get_price.return_value = 10
        sauce_mock = Mock()
        filling_mock = Mock()
        sauce_mock.get_price.return_value = 10
        filling_mock.get_price.return_value = 20
        burger.set_buns(bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)
        expected_price = 10 * 2 + 10 + 20
        assert (burger.get_price(), expected_price)

    @pytest.mark.parametrize("bun_price, sauce_price, filling_price, expected_price",
                             [(10, 20, 30, 70),
                              (100, 100, 100, 400)])
    def test_get_price_with_parametrize(self, burger, bun_price, sauce_price, filling_price, expected_price):
        bun_mock = Mock()
        bun_mock.get_price.return_value = bun_price
        sauce_mock = Mock()
        sauce_mock.get_price.return_value = sauce_price
        filling_mock = Mock()
        filling_mock.get_price.return_value = filling_price
        burger.set_buns(bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)
        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger):
        bun = Bun("black bun", 100)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        price_receipt = burger.get_receipt()
        assert "Price: 500" in price_receipt
