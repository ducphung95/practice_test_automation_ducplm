from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Định vị một phần tử trên Dashboard để chờ đợi (tùy chọn nhưng nên có)
        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")
        self.user_dropdown = (By.CLASS_NAME, "oxd-userdropdown-name")

    def is_dashboard_loaded(self):
        """Kiểm tra xem trang dashboard đã tải xong chưa."""
        try:
            self.wait_for_element_visible(self.dashboard_header)
            return True
        except:
            return False

    def get_cookies(self):
        """Lấy tất cả cookies từ trình duyệt."""
        return self.driver.get_cookies()

    def get_current_url(self):
        """Lấy URL hiện tại."""
        return self.driver.current_url