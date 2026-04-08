import allure
import pytest
from data import Ingredients
from helpers import create_order

@allure.epic("Лента заказов")
class TestOrderFeed:
    @pytest.mark.order_feed
    @pytest.mark.smoke
    @allure.title("Счётчик «Выполнено за всё время» увеличивается после создания заказа")
    def test_total_counter_increases(self, logged_in_user, constructor_page, order_feed_page, header_nav, modal_page):
        header_nav.click_feed()
        before = order_feed_page.get_total_orders_count()
        allure.attach(str(before), name="Счётчик «Выполнено за всё время» ДО", attachment_type=allure.attachment_type.TEXT)

        header_nav.click_constructor()
        create_order(constructor_page, modal_page)

        header_nav.click_feed()
        order_feed_page.wait_for_increase_total(before)
        after = order_feed_page.get_total_orders_count()
        allure.attach(str(after), name="Счётчик «Выполнено за всё время» ПОСЛЕ", attachment_type=allure.attachment_type.TEXT)
        assert after > before

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается после создания заказа")
    def test_today_counter_increases(self, logged_in_user, constructor_page, order_feed_page, header_nav, modal_page):
        header_nav.click_feed()
        before = order_feed_page.get_today_orders_count()
        allure.attach(str(before), name="Счётчик «Выполнено за сегодня» ДО", attachment_type=allure.attachment_type.TEXT)

        header_nav.click_constructor()
        create_order(constructor_page, modal_page)

        header_nav.click_feed()
        order_feed_page.wait_for_increase_today(before)
        after = order_feed_page.get_today_orders_count()
        allure.attach(str(after), name="Счётчик «Выполнено за сегодня» ПОСЛЕ", attachment_type=allure.attachment_type.TEXT)
        assert after > before

    @allure.title("Номер заказа появляется в разделе «В работе» после оформления")
    def test_order_number_in_progress(self, logged_in_user, constructor_page, order_feed_page, header_nav, modal_page):
        header_nav.click_constructor()
        constructor_page.add_ingredient_to_order(Ingredients.BUN_R2_D3)
        constructor_page.add_ingredient_to_order(Ingredients.SAUCE_SPICY_X)
        constructor_page.click_order_button()
        order_number = modal_page.wait_for_real_order_number()
        modal_page.close()

        header_nav.click_feed()
        order_feed_page.wait_for_order_in_progress(order_number)
        in_progress = order_feed_page.get_in_progress_orders()
        assert order_number in in_progress