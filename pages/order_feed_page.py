import allure
from pages.base_page import BasePage
from locators.order_feed import OrderFeed
from selenium.webdriver.support import expected_conditions as EC
from data import Timeouts

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeed

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_total_orders_count(self):
        element = self.wait.until(EC.visibility_of_element_located(self.locators.COUNTER_ALL))
        return int(element.text)

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_today_orders_count(self):
        element = self.wait.until(EC.visibility_of_element_located(self.locators.COUNTER_TODAY))
        return int(element.text)

    @allure.step("Получить список номеров заказов в работе")
    def get_in_progress_orders(self):
        elements = self.driver.find_elements(*self.locators.ORDERS_IN_PROGRESS)
        return [el.text for el in elements]

    @allure.step("Дождаться появления номера заказа в разделе «В работе»")
    def wait_for_order_in_progress(self, order_number, timeout=Timeouts.LONG):
        self.wait_for_text_in_list(self.locators.ORDERS_IN_PROGRESS, order_number, timeout)

    @allure.step("Дождаться увеличения общего счётчика")
    def wait_for_increase_total(self, initial_value, timeout=Timeouts.LONG):
        self.wait_for_number_to_increase(self.locators.COUNTER_ALL, initial_value, timeout)

    @allure.step("Дождаться увеличения сегодняшнего счётчика")
    def wait_for_increase_today(self, initial_value, timeout=Timeouts.LONG):
        self.wait_for_number_to_increase(self.locators.COUNTER_TODAY, initial_value, timeout)
        