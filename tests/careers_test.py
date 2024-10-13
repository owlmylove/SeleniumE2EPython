import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.careers_page import CareersPage
from pages.home_page import HomePage
from pages.navigation_menu import NavigationMenu


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_careers(driver):
    careers_page = CareersPage(driver)
    careers_page.element_Locations()
    time.sleep(1)
    careers_page.element_Teams()
    time.sleep(1)
    careers_page.element_Lives()
    time.sleep(1)

