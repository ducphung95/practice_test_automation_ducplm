import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
import allure
from selenium import webdriver
from utils.config_reader import ConfigReader

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.config = ConfigReader()
        driver.get(self.config.get_base_url())
        request.cls.driver = driver
        request.cls.config = self.config

        yield
        
        driver.quit()

    def allure_screenshot(self, name="screenshot"):
        driver = self.driver 
        screenshot_dir = os.path.join(ConfigReader.load_config_path(), "reports")
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{name}_{ConfigReader.get_timestamp()}.png")
        try:
            self.driver.save_screenshot(screenshot_path)
            allure.attach.file(
                source=screenshot_path,
                name=name,
                attachment_type=allure.attachment_type.PNG
            )
            print(f"Ảnh chụp màn hình đã lưu vào: {screenshot_path}")
        except Exception as e:
            print(f"Không thể chụp màn hình: {e}")