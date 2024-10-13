import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.base_page import BasePage


class BaseTest(BasePage):

    @pytest.fixture()
    def driver(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        yield driver
        driver.close()
        driver.quit()

    def base_test(self):
        pass

