import allure
import pytest
from selenium.common.exceptions import WebDriverException

from data import ADDRESSES
from helpers.browser_factory import create_browser
from pages.base_page import BasePage
from pages.map_page import MapPage
from pages.order_page import OrderPage
from pages.routes_page import RoutesPage
from pages.taxi_page import TaxiPage


def pytest_addoption(parser):
    parser.addoption('--headed', action='store_true', help='Показывать окно Chrome')


@pytest.fixture
def driver(request):
    browser = create_browser(headed=request.config.getoption('--headed'))
    yield browser
    browser.quit()


@pytest.fixture
def routes_page(driver):
    return RoutesPage(driver).open()


@pytest.fixture
def configured_route(routes_page):
    routes_page.set_route(*ADDRESSES)
    return routes_page


@pytest.fixture
def map_page(driver):
    return MapPage(driver)


@pytest.fixture
def taxi_page(driver, configured_route):
    configured_route.select_mode('Быстрый')
    configured_route.call_taxi()
    return TaxiPage(driver)


@pytest.fixture
def work_tariff(taxi_page):
    taxi_page.select_tariff('Рабочий')
    taxi_page.enable_laptop_table()
    return taxi_page


@pytest.fixture
def order_page(driver):
    return OrderPage(driver)


@pytest.fixture
def order_expectations(work_tariff):
    return {
        'price': work_tariff.price(),
        'image': work_tariff.tariff_image(),
        'payment': work_tariff.payment(),
    }


@pytest.fixture
def placed_order(work_tariff, order_page, order_expectations):
    work_tariff.order()
    return order_page


@pytest.fixture
def completed_order(placed_order):
    placed_order.wait_for_car()
    return placed_order


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    driver = item.funcargs.get('driver')
    if driver is not None and (report.failed or hasattr(report, 'wasxfail')):
        try:
            allure.attach(BasePage(driver).screenshot(), 'Страница при проверке', allure.attachment_type.PNG)
        except WebDriverException:
            allure.attach('Браузер недоступен для снимка.', 'Диагностика', allure.attachment_type.TEXT)
