import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.header_nav import HeaderNav
from pages.auth_page import AuthPage
from pages.constructor_page import ConstructorPage
from pages.modal_page import ModalPage
from pages.order_feed_page import OrderFeedPage
from pages.base_page import BasePage
from data import Urls, FixedUser

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    yield driver
    try:
        BasePage(driver).close_all_modals()
    except:
        pass
    driver.quit()

@pytest.fixture
def header_nav(driver):
    return HeaderNav(driver)

@pytest.fixture
def auth_page(driver):
    return AuthPage(driver)

@pytest.fixture
def constructor_page(driver):
    return ConstructorPage(driver)

@pytest.fixture
def modal_page(driver):
    return ModalPage(driver)

@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)

@pytest.fixture
def logged_in_user(auth_page, header_nav, constructor_page):
    auth_page.open(Urls.BASE)
    header_nav.click_personal_account()
    header_nav.click_login_link()
    auth_page.login(FixedUser.EMAIL, FixedUser.PASSWORD)
    constructor_page.wait_visible(constructor_page.ORDER_BUTTON)
    return {"email": FixedUser.EMAIL, "password": FixedUser.PASSWORD}
