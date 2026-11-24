import allure

from config import BASE_URL
from data import TRANSPORTS
from locators.routes_locators import RoutesLocators
from pages.base_page import BasePage


class RoutesPage(BasePage):
    @allure.step('Открыть Яндекс.Маршруты')
    def open(self):
        self.driver.get(BASE_URL)
        self.visible(RoutesLocators.FROM)
        return self

    @allure.step('Задать маршрут: {start} → {finish}')
    def set_route(self, start, finish):
        self.fill(RoutesLocators.FROM, start)
        self.fill(RoutesLocators.TO, finish)
        self.visible(RoutesLocators.PICKER)
        self.visible(RoutesLocators.PRICE)
        self.visible(RoutesLocators.DURATION)

    @allure.step('Выбрать вид маршрута «{mode}»')
    def select_mode(self, mode):
        self.click(self.format_locator(RoutesLocators.MODE, mode))
        self.wait.until(lambda _: self.active_mode() == mode)

    def active_mode(self):
        return self.visible(RoutesLocators.ACTIVE_MODE).text

    @allure.step('Получить стоимость и время маршрута')
    def route_summary(self):
        return self.visible(RoutesLocators.PRICE).text, self.visible(RoutesLocators.DURATION).text

    @allure.step('Дождаться обновления информации о маршруте')
    def changed_summary(self, previous):
        self.wait.until(lambda _: self.route_summary() != previous)
        return self.route_summary()

    @allure.step('Проверить блок выбора маршрута')
    def route_picker_is_visible(self):
        return self.visible(RoutesLocators.PICKER).is_displayed()

    def mode_names(self):
        return self.texts(RoutesLocators.MODES)

    @allure.step('Проверить доступность шести типов передвижения')
    def available_transports(self):
        return [element.is_enabled() and 'disabled' not in element.get_attribute('class')
                for element in self.visible_elements(RoutesLocators.TRANSPORTS)]

    @allure.step('Выбрать тип передвижения «{transport}»')
    def select_transport(self, transport):
        icon = TRANSPORTS[transport]
        self.click(self.format_locator(RoutesLocators.TRANSPORT, icon))
        self.wait.until(lambda _: f'/{icon}-active.' in self.active_transport_icon())

    def active_transport_icon(self):
        return self.visible(RoutesLocators.ACTIVE_TRANSPORT_ICON).get_attribute('src')

    def taxi_button_is_enabled(self):
        return self.is_clickable(RoutesLocators.TAXI)

    def drive_button_is_enabled(self):
        return self.is_clickable(RoutesLocators.DRIVE)

    @allure.step('Нажать «Вызвать такси»')
    def call_taxi(self):
        self.click(RoutesLocators.TAXI)
