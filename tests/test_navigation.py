import pytest
import allure
from data import Urls

@allure.epic("Навигация")
class TestNavigation:
    @pytest.mark.navigation
    @pytest.mark.smoke
    @allure.title("Переход по клику на «Конструктор»")
    def test_constructor_link(self, header_nav, base_url):
        header_nav.open(base_url)
        header_nav.click_feed()
        header_nav.click_constructor()
        assert header_nav.is_on_constructor_page(), "Страница конструктора не загрузилась"

    @allure.title("Переход по клику на «Лента заказов»")
    def test_feed_link(self, header_nav, base_url):
        header_nav.open(base_url)
        header_nav.click_feed()
        assert header_nav.is_on_feed_page(), "Страница ленты заказов не загрузилась"
        