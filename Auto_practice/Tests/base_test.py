
import pytest
from selenium import webdriver
import json

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        with open("testsetting.json", "r") as ts:
            setting = json.load(ts)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(setting["test_url"])
        request.cls.driver = self.driver
        yield
        self.driver.quit()