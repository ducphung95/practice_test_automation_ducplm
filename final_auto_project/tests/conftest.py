import pytest
import allure
import os
from utils.config_reader import ConfigReader

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if hasattr(item.instance, "driver") and item.instance.driver:
            driver = item.instance.driver
            screenshot_name = f"{item.name}_failure.png"
             
            screenshot_dir = os.path.join(ConfigReader.load_config_path(), "reports")
            os.makedirs(screenshot_dir, exist_ok=True)
             
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)

            try:
                driver.save_screenshot(screenshot_path)
                print(f"\nẢnh chụp màn hình đã lưu: {screenshot_path}")
                allure.attach.file(
                    screenshot_path,
                    name=f"Lỗi: {screenshot_name}",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Không thể chụp màn hình: {e}")