from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    
    FEED_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")
    FIRS_ORDER_CARD_IN_FEED = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]")
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    ORDER_TEXT_IN_ORDER_MODAL = (By.XPATH, "//p[text()= 'Cостав']")
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ALL_ORDERS_IN_FEED = (By.XPATH, "//p[starts-with(text(),'#')]") 
    ALL_ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'digits')]")