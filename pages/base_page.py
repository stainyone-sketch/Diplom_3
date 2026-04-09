import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data import Timeouts

class BasePage:
    def __init__(self, driver, timeout=Timeouts.DEFAULT):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть URL: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент по локатору: {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Найти все элементы по локатору: {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Ожидать видимость элемента: {locator}")
    def wait_visible(self, locator, timeout=None):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидать кликабельность элемента: {locator}")
    def wait_clickable(self, locator, timeout=None):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидать невидимость элемента: {locator}")
    def wait_invisible(self, locator, timeout=None):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Кликнуть по элементу {locator} (опционально JS)")
    def click(self, locator, use_js=False, timeout=None):
        element = self.wait_clickable(locator, timeout)
        if use_js:
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Эмуляция drag-and-drop через JavaScript")
    def drag_and_drop_js(self, source_element, target_element):
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var dragStartEvent = new DragEvent('dragstart', { bubbles: true });
            var dropEvent = new DragEvent('drop', { bubbles: true });
            var dragEndEvent = new DragEvent('dragend', { bubbles: true });
            source.dispatchEvent(dragStartEvent);
            target.dispatchEvent(dropEvent);
            source.dispatchEvent(dragEndEvent);
        """, source_element, target_element)

    @allure.step("Ввести текст '{text}' в элемент {locator}")
    def input_text(self, locator, text, timeout=None):
        element = self.wait_visible(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator, timeout=None):
        return self.wait_visible(locator, timeout).text

    @allure.step("Проверить видимость элемента {locator}")
    def is_element_visible(self, locator, timeout=Timeouts.DEFAULT):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Дождаться изменения текста элемента {locator} (не равен {old_text})")
    def wait_for_text_to_change(self, locator, old_text, timeout=Timeouts.DEFAULT):
        def condition(driver):
            try:
                current = self.get_text(locator, timeout=Timeouts.SHORT)
                return current != old_text
            except (TimeoutException, StaleElementReferenceException):
                return False
        WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Дождаться, когда число в элементе {locator} станет не равно {not_value}")
    def wait_for_number_not_equal(self, locator, not_value, timeout=Timeouts.DEFAULT):
        def condition(driver):
            try:
                current = self.get_text(locator, timeout=Timeouts.SHORT)
                return current != not_value
            except:
                return False
        WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Дождаться увеличения числового значения элемента {locator} относительно {initial_value}")
    def wait_for_number_to_increase(self, locator, initial_value, timeout=Timeouts.SHORT):
        def condition(driver):
            try:
                current = int(self.get_text(locator, timeout=Timeouts.SHORT))
                return current > initial_value
            except:
                return False
        WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Дождаться появления текста в списке элементов")
    def wait_for_text_in_list(self, locator, expected_text, timeout=Timeouts.DEFAULT):
        def condition(driver):
            elements = self.find_elements(locator)
            texts = [el.text for el in elements]
            return expected_text in texts
        WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Кликнуть по элементу через JS (без ожидания кликабельности): {locator}")
    def js_click(self, locator, timeout=None):
        element = self.wait_visible(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидать, что URL содержит {partial_url}")
    def wait_for_url_contains(self, partial_url, timeout=Timeouts.DEFAULT):
        WebDriverWait(self.driver, timeout).until(lambda d: partial_url in d.current_url)

    @allure.step("Закрыть все модальные окна (клик по оверлею или ESC)")
    def close_all_modals(self):
        try:
            overlay = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
            if self.is_element_visible(overlay, timeout=Timeouts.SHORT):
                self.js_click(overlay)
                self.wait_invisible(overlay, timeout=Timeouts.SHORT)
        except:
            pass
        try:
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        except:
            pass
        