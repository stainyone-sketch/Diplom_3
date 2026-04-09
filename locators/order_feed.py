from selenium.webdriver.common.by import By

class OrderFeed:
    COUNTER_ALL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.XPATH,
"//ul[contains(@class, 'OrderFeed_orderListReady')]"
    "/li[contains(@class, 'text') and contains(@class, 'text_type_digits-default')]")
