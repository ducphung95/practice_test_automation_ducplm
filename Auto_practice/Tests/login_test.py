from Tests.base_test import BaseTest
from Pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json

class TestLoginWeb(BaseTest):
    def test_login_valid(self):
        with open("testsetting.json", "r") as ts:
            setting = json.load(ts)
        login_pg = LoginPage(self.driver)
        login_pg.enter_username(setting["username"])
        login_pg.enter_password(setting["password"])
        login_pg.click_login()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
        )
        print("\n\nLogin successful!")