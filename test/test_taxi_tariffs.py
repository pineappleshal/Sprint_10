import allure
import pytest

from data import ORDER_FIELDS, TARIFF_CASES, TARIFF_DESCRIPTIONS


@allure.feature('Заказ тарифа Такси')
class TestTaxiTariffs:
    @allure.title('Форма содержит шесть тарифов и ровно один активный')
    def test_six_tariffs_and_one_active(self, taxi_page):
        tariffs = taxi_page.tariff_names()
        active = taxi_page.active_tariffs()

        assert tariffs == list(TARIFF_DESCRIPTIONS)
        assert len(active) == 1
        assert active[0] in TARIFF_DESCRIPTIONS

    @allure.title('Описание тарифа «{tariff}» соответствует ТЗ')
    @pytest.mark.parametrize('tariff,description', TARIFF_CASES)
    def test_tariff_tooltip(self, taxi_page, tariff, description):
        taxi_page.select_tariff(tariff)
        actual_description = taxi_page.tariff_description()

        assert actual_description == description

    @allure.title('Под тарифами отображаются поля заказа')
    def test_order_fields_under_tariffs(self, taxi_page):
        labels = taxi_page.field_labels()

        assert labels == ORDER_FIELDS

    @allure.title('В рабочем тарифе можно включить столик для ноутбука')
    def test_laptop_table_can_be_enabled(self, work_tariff):
        is_selected = work_tariff.laptop_table_is_selected()

        assert is_selected
