from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.XPATH, "//input[@id='user-name']")
        self.password_field = (By.XPATH, "//input[@id='password']")
        self.login_button = (By.XPATH, "//input[@id='login-button']")

    def enter_username(self, username: str):
        self.enter_text(self.username_field, username)

    def enter_password(self, password: str):
        self.enter_text(self.password_field, password)

    def click_login(self):
        self.click(self.login_button)           

    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def verify_login_button_display(self):
        return self.verify_element_present(self.login_button)