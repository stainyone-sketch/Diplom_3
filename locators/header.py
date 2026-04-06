from selenium.webdriver.common.by import By

class Header:
    CONSTRUCTOR_LINK = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and @href='/']")
    FEED_LINK = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and @href='/feed']")
    LOGIN_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    LOGIN_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGIN_LINK = (By.XPATH, "//button[contains(@class, 'button_button')][text()='Войти']")
    