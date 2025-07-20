from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
import allure

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    @allure.step("Thực hiện đăng nhập UI với người dùng '{username}'")
    def do_login(self, username, password):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.username_field)
            ).send_keys(username)
            allure.attach(self.driver.get_screenshot_as_png(), name="Ảnh chụp màn hình sau khi nhập tên người dùng", attachment_type=allure.attachment_type.PNG)

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.password_field)
            ).send_keys(password)
            allure.attach(self.driver.get_screenshot_as_png(), name="Ảnh chụp màn hình sau khi nhập mật khẩu", attachment_type=allure.attachment_type.PNG)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.login_button)
            ).click()
            allure.attach(self.driver.get_screenshot_as_png(), name="Ảnh chụp màn hình sau khi nhấp nút đăng nhập", attachment_type=allure.attachment_type.PNG)

            WebDriverWait(self.driver, 15).until(
                EC.url_contains("dashboard")
            )
            allure.step(f"Đăng nhập UI hoàn tất. URL hiện tại: {self.driver.current_url}")

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Ảnh chụp màn hình khi đăng nhập UI thất bại trong do_login", attachment_type=allure.attachment_type.PNG)
            allure.step(f"Lỗi trong quá trình đăng nhập UI: {e}")
            pass   

    # def enter_username(self, username: str):
    #     self.enter_text(self.username_field, username)

    # def enter_password(self, password: str):
    #     self.enter_text(self.password_field, password)

    # def click_login(self):
    #     self.click(self.login_button)       

    # def do_login(self, username, password):
    #     self.enter_username(username)
    #     self.enter_password(password)
    #     self.click_login()