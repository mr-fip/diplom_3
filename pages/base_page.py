from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import TimeoutException
import allure

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.url = None

    @allure.step("Открытие страницы")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Заполнение поля {locator} текстом '{text}'")
    def fill_input(self, locator, text):
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Ожидание исчезновения элемента {locator}")
    def wait_invisibility_of_element(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Клик по элементу {locator}")
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step("Получение текста элемента {locator}")
    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Получение текстов из элементов {locator}")
    def get_texts_from_elements(self, locator):
        self.wait_visibility_of_element(locator)
        elements = self.driver.find_elements(*locator)
        number_order = []
        for item in elements:
            number_order.append(item.text.strip())
        return number_order

    @allure.step("Получение текущего URL")
    def get_current_url(self, expected_url=None, timeout=30):
        if expected_url:
            WebDriverWait(self.driver, timeout).until(expected_conditions.url_to_be(expected_url))
        return self.driver.current_url

    @allure.step("Проверка исчезновения элемента {locator}")
    def is_disappeared(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout,1).until_not(expected_conditions.presence_of_element_located(locator))

    @allure.step("Проверка видимости элемента {locator}")
    def is_element_visible(self, locator):
        try:
            self.wait_visibility_of_element(locator)
            return True
        except TimeoutException:
            return False

    @allure.step("Проверка закрытия модального окна")
    def is_modal_closed(self, locator):
        try:
            self.is_disappeared(locator)
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание открытия модального окна")
    def wait_modal_opened(self, locator):
        self.wait_visibility_of_element(locator)

    @allure.step("Ожидание закрытия модального окна")
    def wait_modal_closed(self, locator):
        self.is_disappeared(locator)

    @allure.step("Скролл к элементу {locator} и клик")
    def scroll_to_and_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        element.click()