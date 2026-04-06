import allure
from pages.base_page import BasePage
from locators.header import Header
from locators.order_feed import OrderFeed
from locators.burger_constructor import BurgerConstructor
from data import Timeouts

class HeaderNav(BasePage):
    @allure.step("Кликнуть по ссылке «Конструктор»")
    def click_constructor(self):
        self.js_click(Header.CONSTRUCTOR_LINK)
        self.wait_visible(BurgerConstructor.CONSTRUCTOR_TITLE, timeout=Timeouts.DEFAULT)

    @allure.step("Кликнуть по ссылке «Лента заказов»")
    def click_feed(self):
        self.js_click(Header.FEED_LINK)
        self.wait_for_url_contains("/feed", timeout=Timeouts.DEFAULT)
        self.wait_visible(OrderFeed.COUNTER_ALL, timeout=Timeouts.LONG)

    @allure.step("Кликнуть по ссылке «Личный кабинет»")
    def click_personal_account(self):
        self.js_click(Header.PERSONAL_ACCOUNT_LINK)

    @allure.step("Кликнуть по ссылке «Войти»")
    def click_login_link(self):
        self.js_click(Header.LOGIN_LINK)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Проверить, что открыта страница «Конструктор»")
    def is_on_constructor_page(self):
        return self.is_element_visible(BurgerConstructor.CONSTRUCTOR_TITLE)

    @allure.step("Проверить, что открыта страница «Лента заказов»")
    def is_on_feed_page(self):
        return self.is_element_visible(OrderFeed.COUNTER_ALL)
    