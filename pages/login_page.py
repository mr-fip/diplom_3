from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from url import Url
import allure

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Url.login_page_url
        self.locators = LoginPageLocators()

    @allure.step("Нажатие на ссылку 'Забыли пароль'")
    def click_on_forgot_password(self):
        self.click_on_element(self.locators.FORGOT_PASSWORD_BUTTON)

    @allure.step("Проверка видимости кнопки входа в аккаунт")
    def is_login_button_visible(self):
        return self.is_element_visible(self.locators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT)