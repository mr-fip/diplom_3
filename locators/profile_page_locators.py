from selenium.webdriver.common.by import By

class ProfilePageLocators:
    
    ACCOUNT_TEXT_IN_PROFILE = (By.XPATH, ".//p[contains(@class, 'Account_text')]")
    HISTORY_ORDER_BUTTON_IN_PROFILE = (By.CSS_SELECTOR, 'a[href="/account/order-history"]')
    BUTTON_LOGOUT_PROFILE = (By.XPATH, ".//button[text() = 'Выход']")
    ALL_ORDERS_IN_HISTORY_USER = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]//p[contains(@class, 'digits') and not(contains(@class, 'mr-2'))]")
    PROFILE_MENU =  (By.XPATH, "//ul[contains(@class, 'Account_list')]")