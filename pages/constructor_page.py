import allure
from pages.base_page import BasePage
from locators.burger_ingredients import BurgerIngredients
from locators.burger_constructor import BurgerConstructor
from data import Timeouts

class ConstructorPage(BasePage):
    ORDER_BUTTON = BurgerConstructor.ORDER_BUTTON
    TOTAL_PRICE = BurgerConstructor.TOTAL_PRICE
    CONSTRUCTOR_AREA = BurgerConstructor.CONSTRUCTOR_AREA

    @allure.step("Кликнуть по ингредиенту: {name}")
    def click_ingredient(self, name):
        locator = BurgerIngredients.ingredient_card(name)
        self.js_click(locator)

    @allure.step("Добавить ингредиент в заказ (drag-and-drop): {name}")
    def add_ingredient_to_order(self, name):
        ingredient = self.wait_visible(BurgerIngredients.ingredient_card(name))
        target = self.wait_visible(self.CONSTRUCTOR_AREA)
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var dragStartEvent = new DragEvent('dragstart', { bubbles: true });
            var dropEvent = new DragEvent('drop', { bubbles: true });
            var dragEndEvent = new DragEvent('dragend', { bubbles: true });
            source.dispatchEvent(dragStartEvent);
            target.dispatchEvent(dropEvent);
            source.dispatchEvent(dragEndEvent);
        """, ingredient, target)

    @allure.step("Получить счётчик ингредиента: {name}")
    def get_ingredient_counter(self, name):
        locator = BurgerIngredients.ingredient_counter(name)
        element = self.wait_visible(locator)
        return int(element.text)

    @allure.step("Кликнуть по кнопке «Оформить заказ»")
    def click_order_button(self):
        btn = self.wait_visible(self.ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        self.click(self.ORDER_BUTTON, use_js=True)
        from locators.modal import Modal
        self.wait_visible(Modal.ORDER_NUMBER, timeout=Timeouts.DEFAULT)
