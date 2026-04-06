import allure
import pytest
from data import Ingredients
from locators.burger_ingredients import BurgerIngredients

@allure.epic("Конструктор")
class TestAddIngredient:
    @pytest.mark.constructor
    @pytest.mark.smoke
    @pytest.mark.parametrize("ingredient", Ingredients.FOR_COUNTER_TEST)
    @allure.title("При добавлении ингредиента {ingredient} счётчик увеличивается")
    def test_counter_increases(self, constructor_page, base_url, ingredient):
        constructor_page.open(base_url)
        initial = constructor_page.get_ingredient_counter(ingredient)
        constructor_page.add_ingredient_to_order(ingredient)
        constructor_page.wait_for_text_to_change(
            BurgerIngredients.ingredient_counter(ingredient), 
            str(initial)
        )
        new_value = constructor_page.get_ingredient_counter(ingredient)
        assert new_value > initial
        