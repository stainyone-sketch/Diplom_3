from selenium.webdriver.common.by import By

class BurgerIngredients:
    TAB_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div")
    TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div")
    TAB_FILLINGS = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    @staticmethod
    def ingredient_card(name):
        return (By.XPATH, f"//a[contains(@class, 'BurgerIngredient') and .//p[text()='{name}']]")
    
    @staticmethod
    def ingredient_counter(name):
        return (By.XPATH, f"//a[contains(@class, 'BurgerIngredient') and .//p[text()='{name}']]//p[contains(@class, 'counter_counter__num')]")
    