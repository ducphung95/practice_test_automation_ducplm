import pytest
from Tests.base_test import BaseTest
from Pages.login_page import LoginPage
# from selenium.webdriver.support.ui import WebDriverWait
from Utils.config_reader import ConfigReader
from time import sleep
import allure

@pytest.mark.usefixtures("setup")
class TestLoginWeb(BaseTest):
    @allure.story("Valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_valid(self):
        login_pg = LoginPage(self.driver)
        login_pg.do_login(ConfigReader.get_username(), ConfigReader.get_password())
        sleep(5)
        print("\n\nLogin successful!")