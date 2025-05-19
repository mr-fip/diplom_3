import allure
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.feature("Главная страница")
class TestMainPage:

    @allure.story("Навигация")
    @allure.title("Переход в конструктор бургеров")
    def test_navigate_to_constructor(self, driver):
        with allure.step("Открыть страницу логина"):
            login_page = LoginPage(driver)
            login_page.open()
        with allure.step("Нажать кнопку конструктора"):
            main_page = MainPage(driver)
            main_page.click_on_constructor_button()
        with allure.step("Проверить заголовок конструктора"):
            assert main_page.check_text_on_constructor_title(), 'Не появился заголовок страницы'

    @allure.story("Модальные окна")
    @allure.title("Открытие модального окна с составом булки")
    def test_open_modal_window_bun(self, driver):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        with allure.step("Нажать на ингредиент в конструкторе"):
            main_page.click_on_ingredient_in_constructor()
        with allure.step("Проверить отображение модального окна"):
            assert main_page.is_image_bun_in_module_window_visible(), 'Не появился состав в модальном окне'

    @allure.story("Модальные окна")
    @allure.title("Закрытие модального окна с составом булки")
    def test_open_close_window_bun(self, driver):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        with allure.step("Открыть и закрыть модальное окно"):
            main_page.click_on_ingredient_in_constructor()
            main_page.click_on_close_modal()
        with allure.step("Проверить закрытие модального окна"):
            assert main_page.is_modal_bun_closed(), "Модальное окно не закрылось"

    @allure.story("Конструктор бургеров")
    @allure.title("Добавление ингредиента в заказ (drag and drop)")
    @pytest.mark.skip(reason="drag_and_drop не работает в Firefox")
    def test_add_ingredient_in_order_drag_and_drop(self, driver):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        with allure.step("Добавить ингредиент в конструктор"):
            main_page.drag_ingredient_to_constructor()
        with allure.step("Проверить счетчик булок"):
            assert main_page.check_value_counter_buns(), "Состав не изменился"

    @allure.story("Оформление заказа")
    @allure.title("Создание заказа авторизованным пользователем")
    @pytest.mark.skip(reason="Сайт не адаптирован под движок Firefox")
    def test_placing_order_logged_user(self, driver, login_user_via_localStorage):
        with allure.step("Добавить ингредиент в конструктор"):
            main_page = MainPage(driver)
            main_page.drag_ingredient_to_constructor()
        with allure.step("Нажать кнопку оформления заказа"):
            main_page.click_on_button_order()
        with allure.step("Проверить уведомление о подтверждении заказа"):
            assert main_page.check_text_order_acceptance_notification(), 'Подтверждением заказа не появилось'