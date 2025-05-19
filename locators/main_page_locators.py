from selenium.webdriver.common.by import By

class MainPageLocators:
    
    BUTTON_PROFILE_ACCOUNT = (By.XPATH, ".//a[@href='/account']")
    CONSTRUCTOR_BUTTON = (By.XPATH, './/a[@href="/"]/p')
    FEED_BUTTON = (By.XPATH, './/a[@href="/feed"]/p')
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")
    INGREDIENT_IN_CONSTRUCTOR = (By.XPATH, "//img[@alt='Краторная булка N-200i']")
    BUN_COUNTER = (By.XPATH, "//p[contains(text(), 'Краторная булка N-200i')]/preceding-sibling::div[contains(@class, 'counter_')]/p")
    BUN_STATS_IN_MODAL = (By.XPATH, "//ul[contains(@class, 'Modal_modal__statsList')]")
    CLOSE_BUN_TITLE_IN_MODAL = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    CLOSE_ORDER_MODAL = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]") 
    BURGER_CONSTRUCTOR_ZONE = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]") 
    BUTTON_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_ACCEPTANCE_NOTIFICATION = (By.XPATH, "//p[contains(@class, 'undefined text') and text()='Ваш заказ начали готовить' ] ")
    NUMBER_ORDER_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large mb-8')]") 
    SUCCESS_ORDER_INDICATOR = (By.CSS_SELECTOR, '[alt="tick animation"]')
    LOADING_ORDER_INDICATOR = (By.CSS_SELECTOR, '[alt="loading animation"]')
    MODAL_OPENED = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    MODAL_OVERLAY_WHEN_ORDER_PROCESS = (By.XPATH, '//img[@alt="loading animation"]/following-sibling::div[contains(@class, "Modal_modal_overlay_")]')




