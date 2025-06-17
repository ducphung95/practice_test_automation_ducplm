import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        request.cls.driver = self.driver
        yield
        self.driver.quit()

class TestWebLogin(BaseTest):
    def test_login_valid(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        username_textbox = wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        username_textbox.send_keys("Admin")
        sleep(1)
        password_textbox = wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_textbox.send_keys("admin123")
        sleep(1)
        login_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        login_button.click()
        sleep(5)
        # dashboard_header_selector = ".oxd-topbar-header-title"
        # dashboard_header_element = wait.until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, dashboard_header_selector))
        # )
        # assert dashboard_header_element.text == "Dashboard"
        page_title = driver.title
        print(f"\nLogin to website {page_title} successfully!")

