import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_home_page(driver):
    home_page = HomePage(driver)
    home_page.open_page("https://useinsider.com/")
    home_page.check_page_loaded()
    time.sleep(1)
