from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import WAIT_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def open_url(self, url):
        self._driver.get(url)

    def screenshot(self):
        return self._driver.get_screenshot_as_png()

    def wait_until(self, condition, timeout=WAIT_TIMEOUT):
        return WebDriverWait(self._driver, timeout).until(lambda _: condition())

    @staticmethod
    def format_locator(locator, value):
        return locator[0], locator[1].format(value)

    def visible(self, locator, timeout=WAIT_TIMEOUT):
        return WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located(locator))

    def visible_elements(self, locator, count=None, timeout=WAIT_TIMEOUT):
        def find_visible(driver):
            elements = [element for element in driver.find_elements(*locator) if element.is_displayed()]
            return elements if count is None or len(elements) == count else False

        return WebDriverWait(self._driver, timeout).until(find_visible)

    def text(self, locator):
        return self.visible(locator).text

    def texts(self, locator, count=None, timeout=WAIT_TIMEOUT):
        return [element.text for element in self.visible_elements(locator, count, timeout)]

    def attribute(self, locator, name):
        return self.visible(locator).get_attribute(name)

    def rectangle(self, locator, timeout=WAIT_TIMEOUT):
        return self.visible(locator, timeout).rect

    def is_visible(self, locator):
        return self.visible(locator).is_displayed()

    def is_hidden(self, locator):
        return bool(WebDriverWait(self._driver, WAIT_TIMEOUT).until(EC.invisibility_of_element_located(locator)))

    def is_selected(self, locator):
        element = WebDriverWait(self._driver, WAIT_TIMEOUT).until(EC.presence_of_element_located(locator))
        return element.is_selected()

    def enabled_states(self, locator, disabled_class='disabled'):
        return [element.is_enabled() and disabled_class not in element.get_attribute('class').split()
                for element in self.visible_elements(locator)]

    def wait_for_text(self, locator, text, timeout=WAIT_TIMEOUT):
        return WebDriverWait(self._driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def click(self, locator):
        WebDriverWait(self._driver, WAIT_TIMEOUT).until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator, value):
        element = self.visible(locator)
        element.clear()
        element.send_keys(value)

    def hover(self, locator):
        ActionChains(self._driver).move_to_element(self.visible(locator)).perform()

    def is_clickable(self, locator):
        element = WebDriverWait(self._driver, WAIT_TIMEOUT).until(EC.element_to_be_clickable(locator))
        return element.is_displayed() and element.is_enabled()

    def image_is_loaded(self, locator):
        image = self.visible(locator)
        return self.wait_until(lambda: image.get_property('complete') and image.get_property('naturalWidth') > 0)
