from selenium.webdriver.common.by import By

class BurgerConstructor:
    CONSTRUCTOR_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    TOTAL_PRICE = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__totalContainer')]/p")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
