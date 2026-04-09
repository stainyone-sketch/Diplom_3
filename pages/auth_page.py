import allure
from pages.base_page import BasePage
from locators.header import Header

class AuthPage(BasePage):
    LOGIN_EMAIL = Header.LOGIN_EMAIL
    LOGIN_PASSWORD = Header.LOGIN_PASSWORD
    LOGIN_BUTTON = Header.LOGIN_BUTTON

    @allure.step("Выполнить вход: {email}, {password}")
    def login(self, email, password):
        self.input_text(self.LOGIN_EMAIL, email)
        self.input_text(self.LOGIN_PASSWORD, password)
        self.js_click(self.LOGIN_BUTTON)
        