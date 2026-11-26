import allure
import pytest

from data import MAP_LABELS, ROUTES


@allure.feature('Отрисовка маршрута')
class TestRouteMap:
    @allure.title('Два разных адреса отображаются двумя точками на карте')
    @pytest.mark.parametrize('start,finish', ROUTES, ids=['forward', 'backward'])
    def test_two_route_markers(self, routes_page, map_page, start, finish):
        routes_page.set_route(start, finish)
        first, second = map_page.route_markers()
        labels = set(map_page.marker_labels())

        assert (first['x'], first['y']) != (second['x'], second['y']), 'Точки должны находиться в разных местах'
        assert labels == MAP_LABELS, 'На карте должны быть подписи обоих адресов'
