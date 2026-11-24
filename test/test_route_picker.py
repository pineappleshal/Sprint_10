import allure
import pytest

from data import ADDRESSES, ROUTES, ROUTE_MODES, SAME_ADDRESS_RESULT


@allure.feature('Отрисовка блока с выбором маршрута')
class TestRoutePicker:
    @allure.title('После ввода разных адресов отображается блок выбора маршрута')
    @pytest.mark.parametrize('start,finish', ROUTES, ids=['forward', 'backward'])
    def test_route_picker_for_different_addresses(self, routes_page, start, finish):
        routes_page.set_route(start, finish)

        assert routes_page.route_picker_is_visible()
        assert tuple(routes_page.mode_names()) == ROUTE_MODES

    @allure.title('При одинаковых адресах маршрут бесплатный и занимает ноль минут')
    @pytest.mark.parametrize('address', ADDRESSES, ids=['khamovniki', 'zubovsky'])
    def test_same_address_route_is_free(self, routes_page, address):
        routes_page.set_route(address, address)

        assert routes_page.route_picker_is_visible()
        assert routes_page.route_summary() == SAME_ADDRESS_RESULT
