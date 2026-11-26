import allure

from locators.taxi_locators import TaxiLocators
from pages.base_page import BasePage


class TaxiPage(BasePage):
    @allure.step('Получить список тарифов в форме заказа')
    def tariff_names(self):
        return self.texts(TaxiLocators.TITLES)

    def active_tariffs(self):
        return self.texts(TaxiLocators.ACTIVE_TITLE)

    @allure.step('Выбрать тариф «{tariff}»')
    def select_tariff(self, tariff):
        self.click(self.format_locator(TaxiLocators.CARD, tariff))
        self.wait_until(lambda: self.active_tariffs() == [tariff])

    @allure.step('Навести курсор на значок информации и прочитать описание')
    def tariff_description(self):
        self.hover(TaxiLocators.INFO)
        self.visible(TaxiLocators.TOOLTIP)
        return self.text(TaxiLocators.DESCRIPTION)

    @allure.step('Получить поля под тарифами')
    def field_labels(self):
        return tuple(self.text(locator) for locator in (
            TaxiLocators.PHONE, TaxiLocators.PAYMENT_LABEL,
            TaxiLocators.COMMENT_LABEL, TaxiLocators.REQUIREMENTS,
        ))

    @allure.step('Включить столик для ноутбука')
    def enable_laptop_table(self):
        self.click(TaxiLocators.REQUIREMENTS)
        self.click(TaxiLocators.LAPTOP_SWITCH)

    def laptop_table_is_selected(self):
        return self.is_selected(TaxiLocators.LAPTOP_INPUT)

    def price(self):
        return int(self.text(TaxiLocators.ACTIVE_PRICE).split()[0])

    def tariff_image(self):
        return self.attribute(TaxiLocators.ACTIVE_IMAGE, 'src')

    def payment(self):
        return self.text(TaxiLocators.PAYMENT_VALUE)

    @allure.step('Нажать «Ввести номер и заказать»')
    def order(self):
        self.click(TaxiLocators.ORDER)
