import re

import allure

from data import ADDRESSES


@allure.feature('Полный сценарий заказа такси')
class TestTaxiOrder:
    @allure.title('Заказ рабочего тарифа со столиком открывает окно поиска машины')
    def test_search_window(self, work_tariff, order_modal):
        assert work_tariff.laptop_table_is_selected()
        work_tariff.order()
        state = order_modal.search_state()

        assert state['title'] == 'Поиск машины'
        assert re.fullmatch(r'\d{2}:\d{2}', state['timer']), 'Должен отображаться таймер обратного отсчёта'
        assert order_modal.timer_decreases(state['timer'])
        assert state['cancel'] and state['details'], 'Должны быть доступны обе кнопки'
        order_modal.cancel()
        assert order_modal.is_closed()

    @allure.title('Полный заказ: ожидание машины, сведения о водителе, детали и отмена')
    def test_complete_taxi_order_flow(self, work_tariff, order_modal):
        expected_price = work_tariff.price()
        expected_image = work_tariff.tariff_image()
        expected_payment = work_tariff.payment()
        assert work_tariff.laptop_table_is_selected()
        work_tariff.order()
        order_modal.wait_for_car()
        state = order_modal.completed_state()

        assert re.fullmatch(r'\d+ мин\. и приедет', state['title'])
        assert re.fullmatch(r'[а-яa-z]\s?\d{3}\s?[а-яa-z]{2}', state['number'], re.IGNORECASE)
        assert state['car_image'] == expected_image and state['car_image_loaded']
        assert state['driver'] and state['photo_loaded']
        assert re.fullmatch(r'[0-5][,.]\d', state['rating'])
        assert state['cancel'] and state['details']

        order_modal.open_details()
        assert order_modal.details() == {
            'from': ADDRESSES[0], 'to': ADDRESSES[1],
            'payment': expected_payment, 'price': expected_price,
        }
        order_modal.cancel()
        assert order_modal.is_closed()
