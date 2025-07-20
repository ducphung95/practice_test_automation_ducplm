from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.config_reader import ConfigReader
from selenium.common.exceptions import StaleElementReferenceException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = ConfigReader.get_timeout()

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def click(self, locator):
        element = self.wait_for_element_clickable(locator)
        try:
            element.click()
        except StaleElementReferenceException:
            element = self.wait_for_element_clickable(locator)
            element.click()

    def enter_text(self, locator, text, clear_first=True):
        element = self.wait_for_element_visible(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)
    
    def wait_for_element_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_element_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
