import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Utils.config_reader import ConfigReader
import allure

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(ConfigReader.get_base_url())
        request.cls.driver = driver
        yield  
        driver.quit()
