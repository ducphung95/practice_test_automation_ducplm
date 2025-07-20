import pytest
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
import allure

@pytest.mark.usefixtures("setup")
class TestLoginWeb(BaseTest):
    @allure.story("Valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_valid(self):
        login_pg = LoginPage(self.driver)

        self.driver.get(ConfigReader.get_base_url())

        try:
            login_pg.do_login(ConfigReader.get_username(), ConfigReader.get_password())
            assert "dashboard" in self.driver.current_url.lower(), \
                f"Đăng nhập thất bại: Không ở trang dashboard. URL hiện tại: {self.driver.current_url}"
            allure.step("Đăng nhập UI thành công: Đã đến trang Dashboard.")

        except Exception as e:
            self.allure_screenshot(name="test_login_valid_failure_final")
            raise