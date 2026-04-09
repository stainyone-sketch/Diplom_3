from selenium.webdriver.common.by import By

class Modal:
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CLOSE_BUTTON = (By.CLASS_NAME, "Modal_modal__close__TnseK")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    