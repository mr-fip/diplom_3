from selenium.webdriver.common.by import By

class LoginPageLocators:
    
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[contains(@class, 'Auth_link__') and text()='Восстановить пароль']")
    SUBMIT_BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, ".//button[text() = 'Войти']")

    