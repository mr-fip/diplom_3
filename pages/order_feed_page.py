from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage
from data import Data
from url import Url
import allure

class OrderFeedPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Url.ORDER_FEED_PAGE_URL
        self.locators = OrderFeedPageLocators()

    @allure.step("Проверка текста заголовка ленты заказов")
    def check_text_on_feed_title(self):
        self.wait_visibility_of_element(self.locators.FEED_TITLE)
        tex_title_form_feed = self.get_text_element(self.locators.FEED_TITLE)
        return tex_title_form_feed == Data.TEXT_TITLE_ON_FEED_FORM

    @allure.step("Нажатие на карточку заказа")
    def click_on_order_card(self):
        self.click_on_element(self.locators.FIRS_ORDER_CARD_IN_FEED)

    @allure.step("Проверка текста заказа в модальном окне")
    def check_text_order_in_modal(self):
        self.wait_modal_opened(self.locators.ORDER_MODAL)
        order_text = self.get_text_element(self.locators.ORDER_TEXT_IN_ORDER_MODAL)
        return order_text == Data.TEXT_MODULE_FEED

    @allure.step("Получение общего количества заказов")
    def get_total_orders_count(self):
        self.wait_visibility_of_element(self.locators.TOTAL_ORDERS_COUNTER)
        return int(self.get_text_element(self.locators.TOTAL_ORDERS_COUNTER))

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders_count(self):
        self.wait_visibility_of_element(self.locators.TODAY_ORDERS_COUNTER)
        return int(self.get_text_element(self.locators.TODAY_ORDERS_COUNTER))

    @allure.step("Получение номеров всех заказов в ленте")
    def get_all_order_numbers_feed(self):
        self.wait_visibility_of_element(self.locators.ALL_ORDERS_IN_FEED)
        raw_numbers = self.get_texts_from_elements(self.locators.ALL_ORDERS_IN_FEED)
        cleaned_numbers = []
        for text in raw_numbers:
            if text.startswith("#"):
                text = text[1:]
            cleaned_numbers.append(text.lstrip('0'))
        return cleaned_numbers

    @allure.step("Получение номеров заказов в процессе приготовления")
    def get_all_order_numbers_in_progress(self):
        self.wait_visibility_of_element(self.locators.ALL_ORDERS_IN_PROGRESS)
        raw_numbers = self.get_texts_from_elements(self.locators.ALL_ORDERS_IN_PROGRESS)
        cleaned_numbers = []
        for text in raw_numbers:
            cleaned_numbers.append(text.lstrip('0'))
        return cleaned_numbers