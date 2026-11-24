from selenium.webdriver.common.by import By


class RoutesLocators:
    FROM = (By.ID, 'from')
    TO = (By.ID, 'to')
    PICKER = (By.CSS_SELECTOR, '.type-picker.shown')
    MODES = (By.CSS_SELECTOR, '.type-picker .mode')
    ACTIVE_MODE = (By.CSS_SELECTOR, '.type-picker .mode.active')
    MODE = (By.XPATH, '//div[contains(concat(" ", @class, " "), " mode ") and text()="{}"]')
    TRANSPORTS = (By.CSS_SELECTOR, '.types-container .type')
    TRANSPORT = (By.XPATH, '//div[contains(concat(" ", @class, " "), " type ")][img[contains(@src, "/{}")] ]')
    ACTIVE_TRANSPORT_ICON = (By.CSS_SELECTOR, '.types-container .type.active img')
    PRICE = (By.CSS_SELECTOR, '.results-container .text')
    DURATION = (By.CSS_SELECTOR, '.results-container .duration')
    TAXI = (By.XPATH, '//button[normalize-space()="Вызвать такси"]')
    DRIVE = (By.XPATH, '//button[normalize-space()="Забронировать"]')


class MapLocators:
    MAP = (By.ID, 'map')
    START_MARKER = (By.CSS_SELECTOR, '#map [class*="route-pin__label-0"]')
    FINISH_MARKER = (By.CSS_SELECTOR, '#map [class*="route-pin__label-1"]')
    MARKER_LABELS = (By.CSS_SELECTOR, '#map [class$="route-pin__text"]')
