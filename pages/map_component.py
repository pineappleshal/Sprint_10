import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import MAP_TIMEOUT
from locators.routes_locators import MapLocators
from pages.base_page import BasePage


class MapComponent(BasePage):
    @allure.step('Дождаться отображения двух точек маршрута на карте')
    def route_markers(self):
        wait = WebDriverWait(self.driver, MAP_TIMEOUT)
        start = wait.until(EC.visibility_of_element_located(MapLocators.START_MARKER))
        finish = wait.until(EC.visibility_of_element_located(MapLocators.FINISH_MARKER))
        return start.rect, finish.rect

    @allure.step('Прочитать подписи точек маршрута')
    def marker_labels(self):
        WebDriverWait(self.driver, MAP_TIMEOUT).until(
            lambda _: len(self.texts(MapLocators.MARKER_LABELS)) == 2
        )
        return self.texts(MapLocators.MARKER_LABELS)
