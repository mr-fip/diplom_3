import allure
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.feature("Авторизация")
class TestLoginPage:

    @allure.story("Выход из системы")
    @allure.title("Выход пользователя из аккаунта")
    def test_logout_user(self, driver, login_user_via_localStorage):
        with allure.step("Перейти в профиль пользователя"):
            main_page = MainPage(driver)
            main_page.click_on_button_profile_page()
        
        with allure.step("Нажать кнопку выхода"):
            profile_page = ProfilePage(driver)
            profile_page.click_on_logout_button()
        
        with allure.step("Проверить отображение кнопки входа"):
            login_page = LoginPage(driver)
            assert login_page.is_login_button_visible(), "Кнопка входа не отображается"