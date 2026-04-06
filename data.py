# data.py

class Urls:
    BASE = "https://stellarburgers.education-services.ru"
    FEED = BASE + "/feed"

class Timeouts:
    SHORT = 3
    DEFAULT = 10
    LONG = 20

class Ingredients:
    BUN_R2_D3 = "Флюоресцентная булка R2-D3"
    BUN_KRASTOR = "Краторная булка N-200i"
    SAUCE_SPICY_X = "Соус Spicy-X"
    SAUCE_SPACE = "Соус фирменный Space Sauce"
    FILLING_PROTOSTOMIA = "Мясо бессмертных моллюсков Protostomia"
    
    ALL = [BUN_R2_D3, BUN_KRASTOR, SAUCE_SPICY_X, SAUCE_SPACE, FILLING_PROTOSTOMIA]
    FOR_COUNTER_TEST = [BUN_R2_D3, SAUCE_SPICY_X, FILLING_PROTOSTOMIA]

class ModalTexts:
    TITLE = "Детали ингредиента"

class FixedUser:
    EMAIL = "niy123@yandex.ru"
    PASSWORD = "s9T-ZLN-ymZ-YZ3"