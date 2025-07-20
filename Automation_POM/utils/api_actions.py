import requests
from utils.config_reader import ConfigReader
from bs4 import BeautifulSoup
import html
from selenium.webdriver.remote.webdriver import WebDriver

class ApiActions:
    def __init__(self, session: requests.Session, driver: WebDriver):
        self.session = session
        self.driver = driver
        self.base_url = ConfigReader.get_base_url()
        self.default_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en-US,en;q=0.9,vi;q=0.8",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }

    def login_api(self, username, password):
        login_page_url = f"{self.base_url}/web/index.php/auth/login"
        login_submit_url = f"{self.base_url}/web/index.php/auth/validate"

        headers = self.default_headers.copy()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["Referer"] = login_page_url

        print("Đang lấy HTML từ Selenium Driver để tìm CSRF token...")
        html_content_from_driver = self.driver.page_source
        soup = BeautifulSoup(html_content_from_driver, 'html.parser')

        auth_login_tag = soup.find('auth-login')
        csrf_token = None
        if auth_login_tag:
            raw_token_value = auth_login_tag.get(':token')
            if raw_token_value:
                csrf_token = html.unescape(raw_token_value)
                if csrf_token.startswith('"') and csrf_token.endswith('"'):
                    csrf_token = csrf_token[1:-1]

        if not csrf_token:
            print("Không tìm thấy CSRF token trong thẻ <auth-login> hoặc giá trị không hợp lệ.")
            return None

        print(f"Đã lấy CSRF Token từ thẻ <auth-login>: {csrf_token}")

        data = {
            "username": username,
            "password": password,
            "_token": csrf_token
        }

        print(f"Đang POST dữ liệu đăng nhập tới: {login_submit_url}")
        response = self.session.post(login_submit_url, data=data, headers=headers, allow_redirects=True)

        print(f"Cookies sau POST đăng nhập: {self.session.cookies.get_dict()}")
        if 'orangehrm' in self.session.cookies.get_dict():
            print("Đã tìm thấy cookie phiên 'orangehrm' trong requests session.")
        else:
            print("CẢNH BÁO: Không tìm thấy cookie phiên 'orangehrm' trong requests session sau POST đăng nhập.")

        return response

    def get_my_info_page(self):
        my_info_url = f"{self.base_url}/web/index.php/pim/viewPersonalDetails/empNumber/7"
        headers = self.default_headers.copy()
        headers["Referer"] = f"{self.base_url}/web/index.php/dashboard/index"

        return self.session.get(my_info_url, headers=headers)

    def get_user_management_page(self):
        user_mgmt_url = f"{self.base_url}/web/index.php/admin/viewSystemUsers"
        headers = self.default_headers.copy()
        headers["Referer"] = f"{self.base_url}/web/index.php/dashboard/index"

        return self.session.get(user_mgmt_url, headers=headers)