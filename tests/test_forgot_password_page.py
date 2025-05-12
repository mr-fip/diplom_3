import allure
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from data import Data
from url import Url

@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.story("Навигация")
    @allure.title("Переход на страницу восстановления пароля")
    def test_navigate_to_password_recovery_page(self, driver):
        with allure.step("Открыть страницу входа"):
            login_page = LoginPage(driver)
            login_page.open()
        
        with allure.step("Нажать 'Забыли пароль?'"):
            login_page.click_on_forgot_password()
        
        with allure.step("Проверить URL страницы восстановления"):
            forgot_password_page = ForgotPasswordPage(driver)
            current_url = forgot_password_page.get_current_url()
            assert current_url == Url.forgot_password_url, f"Ожидалось '{Url.forgot_password_url}', получили '{current_url}'"

    @allure.story("Восстановление пароля")
    @allure.title("Отправка email для восстановления пароля")
    def test_submit_email_for_password_recovery(self, driver):
        with allure.step("Открыть страницу восстановления пароля"):
            forgot_password_page = ForgotPasswordPage(driver)
            forgot_password_page.open()
        
        with allure.step("Заполнить форму восстановления"):
            forgot_password_page.fill_form_recovery_email(Data.EMAIL_FOR_RECOVERY)
            forgot_password_page.click_on_button_recovery()
        
        with allure.step("Проверить переход на страницу сброса пароля"):
            current_url = forgot_password_page.get_current_url(Url.reset_password_url)
            assert current_url == Url.reset_password_url, f"Ожидалось '{Url.reset_password_url}', получили '{current_url}'"

    @allure.story("Взаимодействие с формой")
    @allure.title("Переключение видимости пароля и подсветка поля")
    def test_toggle_password_visibility_and_highlight_input(self, driver):
        with allure.step("Открыть и заполнить форму восстановления"):
            forgot_password_page = ForgotPasswordPage(driver)
            forgot_password_page.open()
            forgot_password_page.click_on_button_recovery()
            forgot_password_page.fill_form_recovery_password(Data.PASSWORD_FOR_RECOVERY)
        
        with allure.step("Нажать иконку показа пароля"):
            forgot_password_page.click_icon_show_password()
        
        with allure.step("Проверить активность поля ввода"):
            assert forgot_password_page.is_password_input_active(), "Поле не подсвечено"