import allure
import pytest
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from url import Url

@allure.feature("Профиль пользователя")
class TestProfilePage:

    @allure.story("Навигация по профилю")
    @allure.title("Переход в профиль пользователя")
    def test_navigate_to_profile(self, driver, login_user_via_localStorage):
        with allure.step("Нажать кнопку перехода в профиль"):
            main_page = MainPage(driver)
            main_page.click_on_button_profile_page()
        with allure.step("Проверить текст информации профиля"):
            profile_page = ProfilePage(driver)
            assert profile_page.is_profile_info_text_correct(), 'Ожидаемый текст не найден'

    @allure.story("История заказов")
    @allure.title("Переход в историю заказов из профиля")
    def test_navigate_to_history_order_profile(self, driver, login_user_via_localStorage):
        with allure.step("Перейти в профиль пользователя"):
            main_page = MainPage(driver)
            main_page.click_on_button_profile_page()
        with allure.step("Нажать кнопку истории заказов"):
            profile_page = ProfilePage(driver)
            profile_page.click_on_history_order_button()
        with allure.step("Проверить URL страницы истории заказов"):
            current_url = profile_page.get_current_url(Url.order_history_profile_url)
            assert current_url == Url.order_history_profile_url, f"Ожидалось '{Url.order_history_profile_url}', получили '{current_url}'"