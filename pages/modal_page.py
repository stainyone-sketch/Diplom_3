import allure
from pages.base_page import BasePage
from locators.modal import Modal
from data import Timeouts

class ModalPage(BasePage):
    @allure.step("Закрыть модальное окно (крестик)")
    def close(self):
        close_btn = self.wait_clickable(Modal.CLOSE_BUTTON)
        try:
            close_btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", close_btn)
        self.wait_invisible(Modal.MODAL_OVERLAY)

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number(self):
        return self.get_text(Modal.ORDER_NUMBER)

    @allure.step("Дождаться реального номера заказа")
    def wait_for_real_order_number(self, timeout=Timeouts.DEFAULT):
        self.wait_for_number_not_equal(Modal.ORDER_NUMBER, "9999", timeout=timeout)
        return self.get_order_number()

    @allure.step("Проверить видимость модального окна с деталями ингредиента")
    def is_ingredient_details_visible(self, timeout=Timeouts.SHORT):
        return self.is_element_visible(Modal.INGREDIENT_DETAILS, timeout)
    
    @allure.step("Получить текст заголовка деталей ингредиента")
    def get_ingredient_details_title(self):
        return self.get_text(Modal.INGREDIENT_DETAILS)
    