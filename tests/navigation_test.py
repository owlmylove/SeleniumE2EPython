import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.navigation_menu import NavigationMenu


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_navigation_menu(driver):
    home_page = HomePage(driver)
    navigation_menu = NavigationMenu(driver)
    home_page.open_page("https://useinsider.com/")
    home_page.check_page_loaded()
    navigation_menu.check_navbar()
    time.sleep(2)
    navigation_menu.select_company()
    time.sleep(2)
    navigation_menu.select_careers()
    time.sleep(2)

