from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username: str):
        username_textbox = self.wait_for_element_visible(self.username_field)
        username_textbox.send_keys(username)

    def enter_password(self, password: str):
        password_textbox = self.wait_for_element_visible(self.password_field)
        password_textbox.send_keys(password)

    def click_login(self):
        self.click(self.login_button)       

    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()