import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.open_positions_page import OpenPositionsPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_open_positions(driver):
    open_positions_page = OpenPositionsPage(driver)
    open_positions_page.click_button_find_jobs()
    time.sleep(1)
    open_positions_page.open_location_dropdown()
    time.sleep(2)
    open_positions_page.select_location_turkey()
    time.sleep(1)
    open_positions_page.open_department_dropdown()
    time.sleep(2)
    open_positions_page.select_department_quality_assurance()
    time.sleep(1)
    open_positions_page.check_jobs_list()
    time.sleep(1)
    open_positions_page.check_position_title()
    time.sleep(1)
    open_positions_page.check_position_department()
    time.sleep(1)
    open_positions_page.check_position_location()
    time.sleep(1)
