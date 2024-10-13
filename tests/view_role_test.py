import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.view_role_page import ViewRolePage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_view_role(driver):
    view_page_page = ViewRolePage(driver)
    view_page_page.click_button_view_role()
    time.sleep(1)
    view_page_page.open_page("https://jobs.lever.co/useinsider/")
    time.sleep(1)
    view_page_page.check_view_role_redirect()
    time.sleep(1)
    view_page_page.check_lever_logo()

