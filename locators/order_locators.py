from selenium.webdriver.common.by import By


class OrderLocators:
    MODAL = (By.CSS_SELECTOR, '.order.shown .order-body')
    TITLE = (By.CSS_SELECTOR, '.order.shown .order-header-title')
    TIMER = (By.CSS_SELECTOR, '.order.shown .order-header-time')
    CANCEL = (By.XPATH, '//div[contains(@class,"order-btn-group")][div[text()="Отменить"]]/button')
    DETAILS = (By.XPATH, '//div[contains(@class,"order-btn-group")][div[text()="Детали"]]/button')
    DETAILS_PANEL = (By.CSS_SELECTOR, '.order.shown .order-details.shown')
    DETAIL_VALUE = (By.XPATH, '//div[@class="order-details-content"][div[@class="o-d-sh" and text()="{}"]]/div[@class="o-d-h"]')
    COST = (By.XPATH, '//div[@class="order-details-content"][div[text()="Еще про поездку"]]/div[@class="o-d-sh"]')
    NUMBER = (By.CSS_SELECTOR, '.order.shown .order-number .number')
    CAR = (By.CSS_SELECTOR, '.order.shown .order-number img')
    RATING = (By.CSS_SELECTOR, '.order.shown .order-btn-rating')
    DRIVER_NAME = (By.XPATH, '//div[@class="order-btn-group"][div[@class="order-button"]]/div[2]')
    DRIVER_PHOTO = (By.CSS_SELECTOR, '.order.shown .order-btn-group div.order-button img')
