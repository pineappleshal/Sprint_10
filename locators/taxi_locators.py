from selenium.webdriver.common.by import By


class TaxiLocators:
    TITLES = (By.CSS_SELECTOR, '.tcard .tcard-title')
    ACTIVE_TITLE = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    CARD = (By.XPATH, '//div[contains(concat(" ", @class, " "), " tcard ")][div[@class="tcard-title" and text()="{}"]]')
    INFO = (By.CSS_SELECTOR, '.tcard.active .tcard-i')
    TOOLTIP = (By.CSS_SELECTOR, '.tcard.active .__react_component_tooltip.show')
    DESCRIPTION = (By.CSS_SELECTOR, '.tcard.active .__react_component_tooltip.show .i-dPrefix')
    ACTIVE_PRICE = (By.CSS_SELECTOR, '.tcard.active .tcard-price')
    ACTIVE_IMAGE = (By.CSS_SELECTOR, '.tcard.active .tcard-icon img')
    PHONE = (By.XPATH, '//div[@class="np-text" and text()="Телефон"]')
    PAYMENT_LABEL = (By.CSS_SELECTOR, '.pp-text')
    PAYMENT_VALUE = (By.CSS_SELECTOR, '.pp-value-text')
    COMMENT = (By.ID, 'comment')
    COMMENT_LABEL = (By.XPATH, '//label[contains(text(),"Комментарий водителю")]')
    REQUIREMENTS = (By.XPATH, '//div[text()="Требования к заказу"]')
    LAPTOP_SWITCH = (By.XPATH, '//div[@class="r-sw-container"][div[text()="Столик для ноутбука"]]//span[contains(@class,"slider")]')
    LAPTOP_INPUT = (By.XPATH, '//div[@class="r-sw-container"][div[text()="Столик для ноутбука"]]//input')
    ORDER = (By.XPATH, '//button[.//span[normalize-space()="Ввести номер и заказать"]]')
