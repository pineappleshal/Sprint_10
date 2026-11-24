import pytest


ADDRESSES = ('Хамовнический вал, 34', 'Зубовский бульвар, 37')
ROUTES = (ADDRESSES, ADDRESSES[::-1])
MAP_LABELS = {'улица Хамовнический Вал, 34', 'Зубовский бульвар, 37'}
ROUTE_MODES = ('Оптимальный', 'Быстрый', 'Свой')
TRANSPORTS = {
    'Машина': 'car',
    'Пешком': 'walk',
    'Такси': 'taxi',
    'Велосипед': 'bike',
    'Самокат': 'scooter',
    'Драйв': 'drive',
}
TARIFF_DESCRIPTIONS = {
    'Рабочий': 'Для деловых особ, которых отвлекают',
    'Сонный': 'Для тех, кто не выспался',
    'Отпускной': 'Если пришла пора отдохнуть',
    'Разговорчивый': 'Если мысли не выходят из головы',
    'Утешительный': 'Если хочется свернуться калачиком',
    'Глянцевый': 'Если нужно блистать',
}
ORDER_FIELDS = ('Телефон', 'Способ оплаты', 'Комментарий водителю...', 'Требования к заказу')
SAME_ADDRESS_RESULT = ('Авто Бесплатно', 'В пути 0 мин.')

TARIFF_CASES = [
    pytest.param('Рабочий', TARIFF_DESCRIPTIONS['Рабочий'], id='work'),
    pytest.param('Сонный', TARIFF_DESCRIPTIONS['Сонный'], id='sleepy', marks=pytest.mark.xfail(
        reason='ROUTES-001: у Сонного отображается описание Разговорчивого', raises=AssertionError)),
    pytest.param('Отпускной', TARIFF_DESCRIPTIONS['Отпускной'], id='vacation'),
    pytest.param('Разговорчивый', TARIFF_DESCRIPTIONS['Разговорчивый'], id='talkative', marks=pytest.mark.xfail(
        reason='ROUTES-001: у Разговорчивого отображается описание Сонного', raises=AssertionError)),
    pytest.param('Утешительный', TARIFF_DESCRIPTIONS['Утешительный'], id='comforting'),
    pytest.param('Глянцевый', TARIFF_DESCRIPTIONS['Глянцевый'], id='glossy'),
]
