import allure
import pytest
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage
from pages.main_page import MainPage

@allure.feature("Лента заказов")
class TestOrderFeedPage:
    
    @allure.story("Навигация по страницам")
    @allure.title("Переход в ленту заказов")
    def test_navigate_to_feed_order(self, driver):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        with allure.step("Нажать кнопку ленты заказов"):
            main_page.click_on_feed_order_button()
        with allure.step("Проверить заголовок страницы"):
            order_feed_page = OrderFeedPage(driver)
            assert order_feed_page.check_text_on_feed_title(), 'Не появился заголовок страницы'

    @allure.story("Работа с модальными окнами")
    @allure.title("Открытие модального окна с деталями заказа")
    def test_order_details_modal_open(self, driver):
        with allure.step("Открыть страницу ленты заказов"):
            order_feed_page = OrderFeedPage(driver)
            order_feed_page.open()
        with allure.step("Нажать на карточку заказа"):
            order_feed_page.click_on_order_card()
        with allure.step("Проверить открытие модального окна"):
            assert order_feed_page.check_text_order_in_modal(), 'Окно заказа не открылось'

    @allure.story("Проверка счетчиков")
    @allure.title("Увеличение счетчика всех заказов")
    @pytest.mark.skip(reason="Сайт не адаптирован под движок Firefox")
    def test_total_orders_counter_increases(self, driver, login_user_via_localStorage):
        with allure.step("Перейти в ленту заказов"):
            main_page = MainPage(driver)
            main_page.click_on_feed_order_button()
            order_feed_page = OrderFeedPage(driver)
            initial_count = order_feed_page.get_total_orders_count()
        with allure.step("Создать новый заказ"):
            main_page.create_order_on_main_and_return_to_feed()
        with allure.step("Проверить увеличение счетчика"):
            final_count = order_feed_page.get_total_orders_count()
            assert final_count > initial_count, "Счётчик не увеличился"

    @allure.story("Проверка счетчиков")
    @allure.title("Увеличение счетчика заказов за сегодня")
    @pytest.mark.skip(reason="Сайт не адаптирован под движок Firefox")
    def test_today_orders_counter_increases(self, driver, login_user_via_localStorage):
        with allure.step("Перейти в ленту заказов"):
            main_page = MainPage(driver)
            main_page.click_on_feed_order_button()
            order_feed_page = OrderFeedPage(driver)
            initial_count = order_feed_page.get_today_orders_count()
        with allure.step("Создать новый заказ"):
            main_page.create_order_on_main_and_return_to_feed()
        with allure.step("Проверить увеличение счетчика"):
            final_count = order_feed_page.get_today_orders_count()
            assert final_count > initial_count, "Счётчик не увеличился."

    @allure.story("Отображение заказов")
    @allure.title("Появление заказа в списке 'В работе'")
    @pytest.mark.skip(reason="Сайт не адаптирован под движок Firefox")
    def test_order_appears_in_progress_list(self, driver, login_user_via_localStorage):
        with allure.step("Создать новый заказ"):
            main_page = MainPage(driver)
            main_page.drag_ingredient_to_constructor()
            main_page.click_on_button_order()
            order_number = main_page.get_number_order_from_modal_window()
            main_page.close_order_modal()
        with allure.step("Перейти в ленту заказов"):
            main_page.click_on_feed_order_button()
        with allure.step("Проверить наличие заказа в списке"):
            order_feed_page = OrderFeedPage(driver)
            order_numbers_in_progress = order_feed_page.get_all_order_numbers_in_progress()
            assert order_number in order_numbers_in_progress, f"Заказ {order_number} не найден в списке"

    @allure.story("Отображение заказов")
    @allure.title("Появление заказа пользователя в общей ленте")
    @pytest.mark.skip(reason="Сайт не адаптирован под движок Firefox")
    def test_user_order_appears_in_feed(self, driver, login_user_via_localStorage):
        with allure.step("Создать заказ"):
            main_page = MainPage(driver)
            main_page.create_order_and_close_modal()
        with allure.step("Получить номер заказа из истории"):
            main_page.click_on_button_profile_page()
            profile_page = ProfilePage(driver)
            profile_page.click_on_history_order_button()
            history_order_number = profile_page.get_last_order_number_in_history_user()
        with allure.step("Проверить наличие заказа в ленте"):
            main_page.click_on_feed_order_button()
            order_feed_page = OrderFeedPage(driver)
            order_numbers_feed = order_feed_page.get_all_order_numbers_feed()
            assert history_order_number in order_numbers_feed, f"Заказ {history_order_number} не найден в ленте"