import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader
from utils.api_actions import ApiActions
import allure
import requests

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(ConfigReader.get_base_url()) 
        request.cls.driver = driver

        session = requests.Session()
        for cookie in driver.get_cookies():
            session.cookies.set(cookie['name'], cookie['value'])
        
        request.cls.api_actions = ApiActions(session, driver)

        username = ConfigReader.get_username()
        password = ConfigReader.get_password()
        
        print("\nĐang thực hiện đăng nhập API trong fixture setup để xác thực session...")
        login_response = request.cls.api_actions.login_api(username, password)
        
        if not login_response or login_response.status_code != 200 or "/web/index.php/dashboard/index" not in login_response.url:
            pytest.fail(f"Đăng nhập API không thành công trong fixture setup. "
                        f"Mã trạng thái: {login_response.status_code if login_response else 'None'}, "
                        f"URL hiện tại: {login_response.url if login_response else 'None'}. "
                        f"Nội dung phản hồi: {login_response.text if login_response else 'None'}")

        print(f"Đăng nhập API thành công trong fixture setup. URL: {login_response.url}")

        yield driver, session
       
        print("\nĐóng Selenium driver và requests session...")
        driver.quit()
        session.close()

    def allure_screenshot(self, name="screenshot"):
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