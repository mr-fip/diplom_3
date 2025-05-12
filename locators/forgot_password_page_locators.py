from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    
    TITLE_FORM_FORGOT_PASSWORD = (By.XPATH ,".//h2[text()='Восстановление пароля']")
    INPUT_EMAIL_FORGOT = (By.XPATH, ".//input[@type='text']")
    SUBMIT_BUTTON_ACCOUNT_RECOVERY = (By.XPATH, "//button[contains(@class, 'button_button__') and contains(@class, 'button_button_type_primary__')]")  
    SUBMIT_BUTTON_FORGOT_FORM = (By.XPATH, ".//p[text() = 'Вспомнили пароль?']/a")  
    HIDE_AND_SHOW_INPUT_PASSWORD = (By.CSS_SELECTOR, 'svg[fill="#F2F2F3"][viewBox="0 0 24 24"][width="24"][height="24"]') 
    INPUT_PASSWORD_FORGOT = (By.XPATH, ".//input[@type='password']")  
    INPUT_PASSWORD_IS_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
