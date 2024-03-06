from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:

    def test_ingredient_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'sour cream', 200)
        ingredient.get_name()
        assert ingredient.name == 'sour cream'

    def test_ingredient_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'sour cream', 200)
        ingredient.get_price()
        assert ingredient.price == 200

    def test_ingredient_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'sour cream', 200)
        ingredient.get_type()
        assert ingredient.type == 'SAUCE'
