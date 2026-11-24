import re

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import ORDER_TIMEOUT
from locators.order_locators import OrderLocators
from pages.base_page import BasePage


class OrderModal(BasePage):
    @allure.step('Прочитать состояние окна поиска машины')
    def search_state(self):
        self.visible(OrderLocators.MODAL)
        self.wait.until(lambda _: self.timer_seconds() > 0)
        return {
            'title': self.visible(OrderLocators.TITLE).text,
            'timer': self.visible(OrderLocators.TIMER).text,
            'cancel': self.is_clickable(OrderLocators.CANCEL),
            'details': self.is_clickable(OrderLocators.DETAILS),
        }

    @allure.step('Дождаться окончания поиска машины без изменения таймера')
    def wait_for_car(self):
        WebDriverWait(self.driver, ORDER_TIMEOUT).until(
            EC.text_to_be_present_in_element(OrderLocators.TITLE, 'мин. и приедет')
        )

    @allure.step('Проверить уменьшение таймера поиска')
    def timer_decreases(self, previous):
        minutes, seconds = map(int, previous.split(':'))
        return bool(self.wait.until(lambda _: self.timer_seconds() < minutes * 60 + seconds))

    def timer_seconds(self):
        minutes, seconds = map(int, self.visible(OrderLocators.TIMER).text.split(':'))
        return minutes * 60 + seconds

    @allure.step('Прочитать элементы совершённого заказа')
    def completed_state(self):
        return {
            'title': self.visible(OrderLocators.TITLE).text,
            'number': self.visible(OrderLocators.NUMBER).text,
            'car_image': self.visible(OrderLocators.CAR).get_attribute('src'),
            'car_image_loaded': self.image_is_loaded(OrderLocators.CAR),
            'driver': self.visible(OrderLocators.DRIVER_NAME).text,
            'photo_loaded': self.image_is_loaded(OrderLocators.DRIVER_PHOTO),
            'rating': self.visible(OrderLocators.RATING).text,
            'cancel': self.is_clickable(OrderLocators.CANCEL),
            'details': self.is_clickable(OrderLocators.DETAILS),
        }

    @allure.step('Открыть детали заказа')
    def open_details(self):
        self.click(OrderLocators.DETAILS)
        self.visible(OrderLocators.DETAILS_PANEL)

    @allure.step('Прочитать адреса, способ оплаты и стоимость из деталей')
    def details(self):
        cost = self.visible(OrderLocators.COST).text
        return {
            'from': self.visible(self.format_locator(OrderLocators.DETAIL_VALUE, 'Адрес подачи')).text,
            'to': self.visible(self.format_locator(OrderLocators.DETAIL_VALUE, 'Адрес назначения')).text,
            'payment': self.visible(self.format_locator(OrderLocators.DETAIL_VALUE, 'Способ оплаты')).text,
            'price': int(re.search(r'\d+', cost).group()),
        }

    @allure.step('Отменить заказ')
    def cancel(self):
        self.click(OrderLocators.CANCEL)

    @allure.step('Проверить закрытие окна заказа')
    def is_closed(self):
        return bool(self.wait.until(EC.invisibility_of_element_located(OrderLocators.MODAL)))
