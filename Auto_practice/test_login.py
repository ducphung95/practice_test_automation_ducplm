from base_test import BaseTest
from login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class TestLoginWeb(BaseTest):
    def test_login_valid(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
        )
        sleep(3)
        print("\n\nLogin successful!")