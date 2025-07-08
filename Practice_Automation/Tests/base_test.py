import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Utils.config_reader import ConfigReader
import allure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "re_call", rep)

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(ConfigReader.get_base_url())
        request.cls.driver = driver
        yield
        
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"failure_{request.node.name}",
                attachment_type=allure.attachment_type.PNG
            )   

        driver.quit()