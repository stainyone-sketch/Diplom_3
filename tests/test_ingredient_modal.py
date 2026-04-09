import pytest
import allure
from data import Ingredients, ModalTexts, Timeouts, Urls

@allure.epic("Ингредиенты")
class TestIngredientModal:
    @pytest.mark.modal
    @pytest.mark.smoke
    @allure.title("Клик на ингредиент открывает окно с деталями")
    def test_ingredient_modal_opens(self, constructor_page, modal_page):
        constructor_page.open(Urls.BASE)
        constructor_page.click_ingredient(Ingredients.BUN_R2_D3)
        assert modal_page.is_ingredient_details_visible()
        assert modal_page.get_ingredient_details_title() == ModalTexts.TITLE # По какой-то причине гит не увидел коммит. Этот тест был исправлен.

    @pytest.mark.modal
    @allure.title("Закрытие модального окна крестиком")
    def test_ingredient_modal_closes(self, constructor_page, modal_page):
        constructor_page.open(Urls.BASE)
        constructor_page.click_ingredient(Ingredients.BUN_R2_D3)
        modal_page.close()
        assert not modal_page.is_ingredient_details_visible(timeout=Timeouts.SHORT) # Я сначала не понял, а потом как понял. Надеюсь.
