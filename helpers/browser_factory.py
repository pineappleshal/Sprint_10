import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def create_browser(headed=False):
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1440,1100')
    if not headed:
        options.add_argument('--headless=new')
    if os.getenv('CHROME_BINARY'):
        options.binary_location = os.environ['CHROME_BINARY']
    driver = webdriver.Chrome(service=Service(executable_path=os.getenv('CHROMEDRIVER')), options=options)
    driver.set_page_load_timeout(40)
    return driver
