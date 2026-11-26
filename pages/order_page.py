import re

import allure

from config import ORDER_TIMEOUT
from locators.order_locators import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Прочитать состояние окна поиска машины')
    def search_state(self):
        self.visible(OrderLocators.MODAL)
        self.wait_until(lambda: self.timer_seconds() > 0)
        return {
            'title': self.text(OrderLocators.TITLE),
            'timer': self.text(OrderLocators.TIMER),
            'cancel': self.is_clickable(OrderLocators.CANCEL),
            'details': self.is_clickable(OrderLocators.DETAILS),
        }

    @allure.step('Дождаться окончания поиска машины без изменения таймера')
    def wait_for_car(self):
        self.wait_for_text(OrderLocators.TITLE, 'мин. и приедет', timeout=ORDER_TIMEOUT)

    @allure.step('Дождаться изменения таймера поиска')
    def changed_timer(self, previous):
        self.wait_until(lambda: self.text(OrderLocators.TIMER) != previous)
        return self.text(OrderLocators.TIMER)

    def timer_seconds(self):
        minutes, seconds = map(int, self.text(OrderLocators.TIMER).split(':'))
        return minutes * 60 + seconds

    @allure.step('Прочитать элементы совершённого заказа')
    def completed_state(self):
        return {
            'title': self.text(OrderLocators.TITLE),
            'number': self.text(OrderLocators.NUMBER),
            'car_image': self.attribute(OrderLocators.CAR, 'src'),
            'car_image_loaded': self.image_is_loaded(OrderLocators.CAR),
            'driver': self.text(OrderLocators.DRIVER_NAME),
            'photo_loaded': self.image_is_loaded(OrderLocators.DRIVER_PHOTO),
            'rating': self.text(OrderLocators.RATING),
            'cancel': self.is_clickable(OrderLocators.CANCEL),
            'details': self.is_clickable(OrderLocators.DETAILS),
        }

    @allure.step('Открыть детали заказа')
    def open_details(self):
        self.click(OrderLocators.DETAILS)
        self.visible(OrderLocators.DETAILS_PANEL)

    @allure.step('Прочитать адреса, способ оплаты и стоимость из деталей')
    def details(self):
        cost = self.text(OrderLocators.COST)
        return {
            'from': self.text(self.format_locator(OrderLocators.DETAIL_VALUE, 'Адрес подачи')),
            'to': self.text(self.format_locator(OrderLocators.DETAIL_VALUE, 'Адрес назначения')),
            'payment': self.text(self.format_locator(OrderLocators.DETAIL_VALUE, 'Способ оплаты')),
            'price': int(re.search(r'\d+', cost).group()),
        }

    @allure.step('Отменить заказ')
    def cancel(self):
        self.click(OrderLocators.CANCEL)

    @allure.step('Проверить закрытие окна заказа')
    def is_closed(self):
        return self.is_hidden(OrderLocators.MODAL)
