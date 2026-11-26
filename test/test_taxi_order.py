import re

import allure

from data import ADDRESSES


@allure.feature('Этапы заказа такси')
class TestTaxiOrder:
    @allure.title('Заказ рабочего тарифа со столиком открывает окно поиска машины')
    def test_order_opens_search_window(self, placed_order):
        state = placed_order.search_state()

        assert state['title'] == 'Поиск машины'
        assert re.fullmatch(r'\d{2}:\d{2}', state['timer']), 'Должен отображаться таймер обратного отсчёта'
        assert state['cancel'] and state['details'], 'Должны быть доступны обе кнопки'

    @allure.title('Таймер поиска машины отсчитывает время назад')
    def test_search_timer_counts_down(self, placed_order):
        before = placed_order.search_state()['timer']
        after = placed_order.changed_timer(before)

        assert re.fullmatch(r'\d{2}:\d{2}', after)
        assert after < before, 'Время поиска должно уменьшаться'

    @allure.title('После поиска отображается окно заказа с данными машины и водителя')
    def test_search_finishes_with_car_and_driver(self, completed_order, order_expectations):
        state = completed_order.completed_state()

        assert re.fullmatch(r'\d+ мин\. и приедет', state['title'])
        assert re.fullmatch(r'[а-яa-z]\s?\d{3}\s?[а-яa-z]{2}', state['number'], re.IGNORECASE)
        assert state['car_image'] == order_expectations['image'] and state['car_image_loaded']
        assert state['driver'] and state['photo_loaded']
        assert re.fullmatch(r'[0-5][,.]\d', state['rating'])
        assert state['cancel'] and state['details']

    @allure.title('В деталях заказа сохранены выбранные адреса и способ оплаты')
    def test_details_show_route_and_payment(self, completed_order, order_expectations):
        completed_order.open_details()
        details = completed_order.details()
        expected = {
            'from': ADDRESSES[0], 'to': ADDRESSES[1],
            'payment': order_expectations['payment'],
        }
        actual = {key: details[key] for key in expected}

        assert actual == expected

    @allure.title('Стоимость в деталях заказа совпадает со стоимостью выбранного тарифа')
    def test_details_price_matches_tariff(self, completed_order, order_expectations):
        completed_order.open_details()
        price = completed_order.details()['price']

        assert price == order_expectations['price']

    @allure.title('Отмена во время поиска закрывает окно заказа')
    def test_cancel_closes_search_window(self, placed_order):
        placed_order.search_state()
        placed_order.cancel()
        is_closed = placed_order.is_closed()

        assert is_closed

    @allure.title('Отмена после поиска машины закрывает окно заказа')
    def test_cancel_closes_completed_order(self, completed_order):
        completed_order.cancel()
        is_closed = completed_order.is_closed()

        assert is_closed
