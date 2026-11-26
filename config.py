import os


BASE_URL = os.getenv('BASE_URL', 'https://qa-routes.education-services.ru/').rstrip('/')
WAIT_TIMEOUT = 20
MAP_TIMEOUT = 40
ORDER_TIMEOUT = 70
