import allure
import pytest

from data import TRANSPORTS


@allure.feature('Подготовка к заказу такси')
class TestTaxiPreparation:
    @allure.title('Переключение вида маршрута меняет активный таб и стоимость')
    @pytest.mark.parametrize('initial,target', [('Оптимальный', 'Быстрый'), ('Быстрый', 'Оптимальный')])
    def test_switch_mode_updates_tab_and_price(self, configured_route, initial, target):
        configured_route.select_mode(initial)
        before = configured_route.route_summary()
        configured_route.select_mode(target)
        after = configured_route.changed_summary(before)
        active_mode = configured_route.active_mode()

        assert active_mode == target
        assert before[0] != after[0], 'Стоимость маршрута должна пересчитываться'

    @allure.title('Переключение вида маршрута пересчитывает время в пути')
    @pytest.mark.parametrize('target', ['Оптимальный', 'Быстрый'])
    def test_switch_mode_updates_duration(self, configured_route, target):
        configured_route.select_mode('Свой')
        configured_route.select_transport('Пешком')
        before = configured_route.route_summary()
        configured_route.select_mode(target)
        after = configured_route.changed_summary(before)
        active_mode = configured_route.active_mode()

        assert active_mode == target
        assert before[1] != after[1], 'После пешего маршрута время должно пересчитаться'

    @allure.title('В режиме «Свой» доступны все шесть типов передвижения')
    def test_custom_mode_enables_transports(self, configured_route):
        configured_route.select_mode('Свой')
        active_mode = configured_route.active_mode()
        transports = configured_route.available_transports()

        assert active_mode == 'Свой'
        assert transports == [True] * len(TRANSPORTS)

    @allure.title('В режиме «Свой» выбирается тип передвижения {transport}')
    @pytest.mark.parametrize('transport,icon', TRANSPORTS.items(), ids=TRANSPORTS.keys())
    def test_custom_transport_can_be_selected(self, configured_route, transport, icon):
        configured_route.select_mode('Свой')
        configured_route.select_transport(transport)
        active_icon = configured_route.active_transport_icon()

        assert f'/{icon}-active.' in active_icon

    @allure.title('В быстром маршруте доступна кнопка «Вызвать такси»')
    def test_fast_route_has_taxi_button(self, configured_route):
        configured_route.select_mode('Быстрый')
        is_enabled = configured_route.taxi_button_is_enabled()

        assert is_enabled

    @allure.title('В своём маршруте с Драйв доступна кнопка «Забронировать»')
    def test_drive_has_booking_button(self, configured_route):
        configured_route.select_mode('Свой')
        configured_route.select_transport('Драйв')
        is_enabled = configured_route.drive_button_is_enabled()

        assert is_enabled
