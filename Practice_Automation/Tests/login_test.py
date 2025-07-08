import pytest
from Tests.base_test import BaseTest
from Pages.login_page import LoginPage
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
        sleep(3)
        
        # Chụp màn hình
        screenshot_path = "./Results/dashboard_screenshot.png" # Đường dẫn tạm thời để lưu ảnh
        self.driver.save_screenshot(screenshot_path)
        
        # Đính kèm màn hình vào báo cáo Allure
        allure.attach.file(
            screenshot_path,
            name="Dashboard after login",
            attachment_type=allure.attachment_type.PNG
        )
        
        assert "dashboard" in self.driver.current_url.lower(), "Login failed: Not on dashboard page."