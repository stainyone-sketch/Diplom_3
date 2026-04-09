import allure
from data import Ingredients

def create_order(constructor_page, modal_page):
    constructor_page.add_ingredient_to_order(Ingredients.BUN_R2_D3)
    constructor_page.add_ingredient_to_order(Ingredients.SAUCE_SPICY_X)
    constructor_page.click_order_button()
    modal_page.wait_for_real_order_number()
    modal_page.close()