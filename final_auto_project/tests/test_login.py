import pytest
import allure
from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config_reader import ConfigReader

@pytest.mark.usefixtures("setup")
class TestLoginWeb(BaseTest):
    @allure.story("Valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_valid(self):
        login_page = LoginPage(self.driver)
        # user_creds = self.config.get_user_credentials("standard_user")
        # login_page.do_login(user_creds['username'], user_creds['password'])
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())
        inventory_page = InventoryPage(self.driver)
        assert "inventory" in self.driver.current_url, \
            f"Validation Failed: URL does not contain 'inventory'. Current URL: {self.driver.current_url}"
        print(f"Page title after login: {inventory_page.get_web_title()}")