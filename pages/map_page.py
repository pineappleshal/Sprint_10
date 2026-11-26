import allure

from config import MAP_TIMEOUT
from locators.routes_locators import MapLocators
from pages.base_page import BasePage


class MapPage(BasePage):
    @allure.step('Дождаться отображения двух точек маршрута на карте')
    def route_markers(self):
        start = self.rectangle(MapLocators.START_MARKER, timeout=MAP_TIMEOUT)
        finish = self.rectangle(MapLocators.FINISH_MARKER, timeout=MAP_TIMEOUT)
        return start, finish

    @allure.step('Прочитать подписи точек маршрута')
    def marker_labels(self):
        return self.texts(MapLocators.MARKER_LABELS, count=2, timeout=MAP_TIMEOUT)
