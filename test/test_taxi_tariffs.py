import allure
import pytest

from data import ORDER_FIELDS, TARIFF_CASES, TARIFF_DESCRIPTIONS


@allure.feature('Заказ тарифа Такси')
class TestTaxiTariffs:
    @allure.title('Форма содержит шесть тарифов и ровно один активный')
    def test_six_tariffs_and_one_active(self, taxi_page):
        assert taxi_page.tariff_names() == list(TARIFF_DESCRIPTIONS)
        assert len(taxi_page.active_tariffs()) == 1
        assert taxi_page.active_tariffs()[0] in TARIFF_DESCRIPTIONS

    @allure.title('Описание тарифа «{tariff}» соответствует ТЗ')
    @pytest.mark.parametrize('tariff,description', TARIFF_CASES)
    def test_tariff_tooltip(self, taxi_page, tariff, description):
        taxi_page.select_tariff(tariff)

        assert taxi_page.tariff_description() == description

    @allure.title('Под тарифами отображаются поля заказа')
    def test_order_fields_under_tariffs(self, taxi_page):
        assert taxi_page.field_labels() == ORDER_FIELDS
