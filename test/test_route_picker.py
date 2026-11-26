import allure
import pytest

from data import ADDRESSES, ROUTES, ROUTE_MODES, SAME_ADDRESS_RESULT


@allure.feature('Отрисовка блока с выбором маршрута')
class TestRoutePicker:
    @allure.title('После ввода разных адресов отображается блок выбора маршрута')
    @pytest.mark.parametrize('start,finish', ROUTES, ids=['forward', 'backward'])
    def test_route_picker_for_different_addresses(self, routes_page, start, finish):
        routes_page.set_route(start, finish)
        is_visible = routes_page.route_picker_is_visible()
        modes = tuple(routes_page.mode_names())

        assert is_visible
        assert modes == ROUTE_MODES

    @allure.title('При одинаковых адресах маршрут бесплатный и занимает ноль минут')
    @pytest.mark.parametrize('address', ADDRESSES, ids=['khamovniki', 'zubovsky'])
    def test_same_address_route_is_free(self, routes_page, address):
        routes_page.set_route(address, address)
        is_visible = routes_page.route_picker_is_visible()
        summary = routes_page.route_summary()

        assert is_visible
        assert summary == SAME_ADDRESS_RESULT
