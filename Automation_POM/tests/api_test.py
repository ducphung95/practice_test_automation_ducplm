import pytest
import allure
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader
from utils.api_actions import ApiActions


@allure.epic("Bộ kiểm thử API")
@pytest.mark.usefixtures("setup")
class TestAPIs(BaseTest):
    @allure.story("Kiểm thử API Đăng nhập - Xác minh trạng thái phiên")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_api_login_valid(self):
        """
        Kiểm thử xác minh rằng phiên API hiện tại đã được xác thực
        thành công bởi fixture setup bằng cách truy cập trang dashboard.
        """
        allure.step("Xác minh trạng thái phiên API hiện tại bằng cách truy cập Dashboard")
        
        dashboard_url = f"{self.api_actions.base_url}/web/index.php/dashboard/index"
        response = self.api_actions.session.get(dashboard_url)
        
        allure.attach(response.request.url, name="URL Yêu cầu (Xác minh)", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(response.status_code), name="Mã trạng thái phản hồi (Xác minh)", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name="Nội dung phản hồi (HTML - Xác minh)", attachment_type=allure.attachment_type.HTML)
        
        assert response.status_code == 200, \
            f"Mã trạng thái dự kiến là 200 cho Dashboard, nhưng nhận được {response.status_code}"
        assert "dashboard" in response.url.lower(), \
            f"Không chuyển hướng đến trang tổng quan sau khi xác minh. URL hiện tại: {response.url}"
        assert "Time at Work" in response.text or "Dashboard" in response.text, \
            "Không tìm thấy văn bản xác nhận trên trang dashboard."
            
        allure.step("Xác minh trạng thái phiên API: Thành công")


    @allure.story("Truy cập trang thông tin của tôi qua API - Truy cập đã xác thực")
    @allure.severity(allure.severity_level.NORMAL)
    def test_api_get_my_info_page_access(self):
        """
        Kiểm thử truy cập trang web 'Thông tin của tôi' thông qua lệnh gọi API (requests).
        Bài kiểm thử này xác minh rằng trang có thể được truy xuất sau khi đăng nhập thành công trong setup,
        xác thực quyền truy cập đã được xác thực, nhưng mong đợi phản hồi HTML.
        """
        allure.step("Đang cố gắng lấy trang 'Thông tin của tôi' qua API")
        response = self.api_actions.get_my_info_page()

        allure.attach(response.request.url, name="URL yêu cầu", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(response.status_code), name="Mã trạng thái phản hồi", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name="Nội dung phản hồi (HTML)", attachment_type=allure.attachment_type.HTML)

        assert response.status_code == 200, f"Mã trạng thái dự kiến là 200 cho trang 'Thông tin của tôi', nhưng nhận được {response.status_code}"
        assert "Personal Details" in response.text, "Không tìm thấy văn bản 'Chi tiết cá nhân' trên trang."
        assert "/web/index.php/pim/viewPersonalDetails/empNumber/7" in response.url, "URL không khớp với trang 'Thông tin của tôi'."
        allure.step("Truy cập trang 'Thông tin của tôi' qua API: Thành công")


    @allure.story("Truy cập trang quản lý người dùng qua API - Truy cập đã xác thực")
    @allure.severity(allure.severity_level.NORMAL)
    def test_api_get_user_management_page_access(self):
        """
        Kiểm thử truy cập trang web 'Quản lý người dùng' thông qua lệnh gọi API (requests).
        Bài kiểm thử này xác minh rằng trang có thể được truy xuất sau khi đăng nhập thành công trong setup,
        xác thực quyền truy cập đã được xác thực, nhưng mong đợi phản hồi HTML.
        """
        allure.step("Đang cố gắng lấy trang 'Quản lý người dùng' qua API")
        response = self.api_actions.get_user_management_page()

        allure.attach(response.request.url, name="URL yêu cầu", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(response.status_code), name="Mã trạng thái phản hồi", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name="Nội dung phản hồi (HTML)", attachment_type=allure.attachment_type.HTML)

        assert response.status_code == 200, f"Mã trạng thái dự kiến là 200 cho trang 'Quản lý người dùng', nhưng nhận được {response.status_code}"
        assert "System Users" in response.text, "Không tìm thấy văn bản 'Người dùng hệ thống' trên trang."
        assert "/web/index.php/admin/viewSystemUsers" in response.url, "URL không khớp với trang 'Quản lý người dùng'."
        allure.step("Truy cập trang quản lý người dùng qua API: Thành công")