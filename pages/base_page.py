from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import WAIT_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    @staticmethod
    def format_locator(locator, value):
        return locator[0], locator[1].format(value)

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def visible_elements(self, locator):
        self.wait.until(lambda driver: any(e.is_displayed() for e in driver.find_elements(*locator)))
        return [e for e in self.driver.find_elements(*locator) if e.is_displayed()]

    def texts(self, locator):
        return [e.text for e in self.visible_elements(locator)]

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator, value):
        element = self.visible(locator)
        element.clear()
        element.send_keys(value)

    def hover(self, locator):
        ActionChains(self.driver).move_to_element(self.visible(locator)).perform()

    def is_clickable(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        return element.is_displayed() and element.is_enabled()

    def image_is_loaded(self, locator):
        image = self.visible(locator)
        return self.wait.until(lambda _: image.get_property('complete') and image.get_property('naturalWidth') > 0)
