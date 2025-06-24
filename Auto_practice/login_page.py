from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def enter_username(self, username):
        username_textbox = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        username_textbox.send_keys(username)

    def enter_password(self, password):
        password_textbox = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        password_textbox.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()